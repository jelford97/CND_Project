#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import math
from scipy import ndimage
from scipy import integrate
from astropy import units as u
import pandas as pd
from astropy.convolution import interpolate_replace_nans


# In[2]:


def get_info(hdu,distance,beamtable):
    hdr=hdu[0].header
    if beamtable=='Yes':
        beamtab=hdu[1].data
        bmajas=np.median(beamtab['BMAJ'])
        bminas=np.median(beamtab['BMIN'])
        bmaj=bmajas/3600
        bmin=bminas/3600
    else:
        bmaj=hdr['BMAJ']
        bmin=hdr['BMIN']
    xcellsize=hdr['CDELT1']
    deltx_arcsec=np.abs(xcellsize)*3600
    deltx_pc=4.84*distance*deltx_arcsec
    return deltx_pc,bmaj,bmin,xcellsize


# In[3]:


def get_ratio(radius,inclination):
    major_axis=radius
    if inclination>85:
        minor_axis=major_axis
    else:
        minor_axis=radius*np.cos(np.deg2rad(inclination))
    ratio=major_axis/minor_axis
    return ratio


# In[4]:


def distance_ellipse(shape, center, ratio, angle):

    """
    :return:
    """

    return dist_ellipse(shape, center.x, center.y, ratio, angle.to("deg").value)

def dist_ellipse(deltx_pc, my_apertute_size,n1,n2,xc, yc, ratio, pa=0): 
    ang = np.radians(pa + 90.)
    cosang = np.cos(ang)
    sinang = np.sin(ang)
    nx = n1
    ny = n2
    x = np.arange(-xc,nx-xc)
    y = np.arange(-yc,ny-yc)

    im = np.empty([n1,n2])
    xcosang = x*cosang
    xsinang = x*sinang

    for i in range(0, ny):

        xtemp = xcosang + y[i]*sinang
        ytemp = -xsinang + y[i]*cosang
        im[i,:] = np.sqrt((xtemp*ratio)**2 + ytemp**2)
    return im*deltx_pc<my_apertute_size 


# In[5]:


def error_calc(cube,im,bmaj,bmin,xcellsize,Nchannels,dims,channelwidth,channel,rms):
    data=im*cube
    inv_beam=(math.pi*(bmaj/np.abs(xcellsize))*(bmin/np.abs(xcellsize)))/(4*math.log(2))
    spectrum=np.nansum((np.nansum((inv_beam**(-1)*data),axis=1)),axis=1)
    sumspectrum=np.nansum(spectrum)*channelwidth
    #chnint=np.int(channel)
    #if dims==0:
       #data0=data[chnint]
    #else:
        #datasq=np.squeeze(data)
        #data0=datasq[chnint]
    rmsj=rms*1e-3
    err=(np.sqrt(Nchannels)*rmsj*(inv_beam)**(-1))*channelwidth
    pererr=(err/sumspectrum)*100
    return pererr, err, sumspectrum


# In[6]:


parameters=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Parameters.csv')
dist=parameters['Distance']
inc=parameters['Inclination']
PA=parameters['Position angle']
freq=parameters['Frequency']
beamwidth=parameters['Beam width']
channelwidth=parameters['Channel width']
xcentre=parameters['X centre']
ycentre=parameters['Y centre']
N1=parameters['N1']
N2=parameters['N2']
R=parameters['Ratio']
filepath=parameters['File Path']
beamtable=parameters['Beam Table']
havecube=parameters['Cube']
assize=parameters['Total Size']
dims=parameters['Dims']
jupper=parameters['Jupper']
Nchn=parameters['Nchannels']
chn=parameters['Channel']
rms=parameters['RMS (mJy/beam)']

def total_size(distance,sizeas):
    totsize=4.84*distance*sizeas
    return totsize

totsize=total_size(dist,assize)
# In[25]:


err=[]
errJy=[]
Jy=[]
for i in range(len(havecube)):
	if havecube[i]=='No':
		pererr=np.NaN
		err.append(pererr)
		Jyerr=np.NaN
		errJy.append(Jyerr)
		Spec=np.NaN
		Jy.append(Spec)
       #print(pererr)
	else:
		hdu=fits.open(filepath[i])
		cube=hdu[0].data
		info=get_info(hdu,dist[i],beamtable[i])
		deltx_pc=info[0]
		bmaj=info[1]
		bmin=info[2]
		xcellsize=info[3]
		ratio=get_ratio(200,inc[i])
		if beamwidth[i]>200:
			pererr=np.NaN
			err.append(pererr)
			Jyerr=np.NaN
			errJy.append(Jyerr)
			Spec=np.NaN
			Jy.append(Spec)
		else:
        	im=dist_ellipse(deltx_pc,200,N1[i],N2[i],xcentre[i],ycentre[i],ratio,PA[i])
        	pererr=error_calc(cube,im,bmaj,bmin,xcellsize,Nchn[i],dims[i],channelwidth[i],chn[i],rms[i])
        	err.append(pererr[0])
        	errJy.append(pererr[1])
        	Jy.append(pererr[2])
        #print(pererr)


# In[26]:


errnew=np.array(err)
errJynew=np.array(errJy)
Jynew=np.array(Jy)

# In[27]:


totalerr=np.sqrt(errnew**2+10**2)
#print(totalerr)
Jyerrtot=np.sqrt(errJynew**2+(0.1*Jynew)**2)

# In[46]:


data=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')


# In[47]:


masserr=data['Mass 200pc']*(totalerr/100)
#masserrround=np.around(np.array(masserr),decimals=0)
#print(masserr)

# In[48]:


#data['Mass 200pc Error']=masserrround
data['200pc CO Int Error']=Jyerrtot
data.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv',index=False)


# In[ ]:




