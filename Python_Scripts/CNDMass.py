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


# In[3]:


def total_size(distance,sizeas):
    totsize=4.84*distance*sizeas
    return totsize


# In[4]:


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


# In[5]:


def get_ratio(radius,inclination):
    major_axis=radius
    if inclination>85:
        minor_axis=major_axis
    else:
        minor_axis=radius*np.cos(np.deg2rad(inclination))
    ratio=major_axis/minor_axis
    return ratio


# In[6]:


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


# In[7]:


#def get_radius(radius,deltx_pc):
    #radius_pixel=radius/deltx_pc
    #radius_pix=round(radius_pixel)
    #return radius_pix


# In[8]:


#radius_pix,xcentre,ycentre
def hydrogen_mass(cube,im,distance,bmaj,bmin,xcellsize,channel_width,R,Jup):
    #mh=1.67e-27*u.kg
    #kb=1.38e-23*u.J/u.Kelvin
    Xco=3e20#*u.s/(u.Kelvin*u.km*(u.cm)**2)
    Xco20=3e20/2e20
    Rref=1/R
    Dl=distance
    #wavelength=(3e8/frequency)*u.meter
    #x_max=xcentre+radius_pix
    #x_min=xcentre-radius_pix
    #y_max=ycentre+radius_pix
    #y_min=ycentre-radius_pix
    data=im*cube
    inv_beam=(math.pi*(bmaj/np.abs(xcellsize))*(bmin/np.abs(xcellsize)))/(4*math.log(2))
    #spectrum=(inv_beam**(-1)*(cube[:,int(x_min):int(x_max),int(y_min):int(y_max)])).sum(axis=1).sum(axis=1)
    spectrum=np.nansum((np.nansum((inv_beam**(-1)*data),axis=1)),axis=1)
    #sum_spectrum=(integrate.trapz(spectrum))*u.Jy*u.km/u.s
    sum_spectrum=(np.nansum(spectrum)*channel_width)#*u.Jy*u.km/u.s
    #mass_hydrogen=np.abs((2*mh*(wavelength**2/(2*kb))*Xco*Dl**2*R*sum_spectrum).decompose())
    #mass_hydrogen_lsolar=(mass_hydrogen/(2e30*u.kg)).decompose()
    mass_hydrogen_lsolar=7847*(1/(Jup**2))*Xco20*Rref*Dl**2*sum_spectrum
    return sum_spectrum, mass_hydrogen_lsolar


# In[9]:


totsize=total_size(dist,assize)


# In[10]:


mass=[]
CO_Int=[]
for i in range(len(havecube)):
    app=totsize[i]
    #print(i)
    if havecube[i]=='No':
        hmass=np.NaN
        mass.append(hmass)
        sum_spectrum=np.NaN
        CO_Int.append(sum_spectrum)
    else:
        hdu=fits.open(filepath[i])
        cube=hdu[0].data
        if dims[i]==4:
            cuben=np.squeeze(cube)
        else:
            cuben=cube
        if beamwidth[i]>app:
            hmass=np.NaN
            mass.append(hmass)
            sum_spectrum=np.NaN
            CO_Int.append(sum_spectrum)
        else:
            info=get_info(hdu,dist[i],beamtable[i])
            deltx_pc=info[0]
            bmaj=info[1]
            bmin=info[2]
            xcellsize=info[3]
            #mask=smooth_mask(dimensions[i],cube,bmaj/np.abs(xcellsize),[1,20],rmsfac=3)
            #cubem=mask*cube

            ratio=get_ratio(app,inc[i])
    
            im=dist_ellipse(deltx_pc,app,N1[i],N2[i],xcentre[i],ycentre[i],ratio,PA[i])
    
            hmass=hydrogen_mass(cuben,im,dist[i],bmaj,bmin,xcellsize,channelwidth[i],R[i],jupper[i])
    
            mass.append(hmass[1])
            CO_Int.append(hmass[0])
        hdu.close()
#print(CO_Int)
python=pd.read_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv')
massround=np.around(np.array(mass),decimals=0)
#python['Mass beam width']=massround
#python['200pc CO Intensity (Jy km/s)']=CO_Int
print(massround)
python['Total Mass New']=massround
python.to_csv('/Users/jelford/Documents/PhD_Work/CND_Project/CSV_Files/Python.csv', index=False)




