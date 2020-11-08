#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:48:31 2020

@author: felix
"""


#we need to import different modules to be able to do different tasks 
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
import numpy as np 
from scipy.signal import find_peaks
import mplcursors

#creating a function that is finding the peaks of emission
def emission_lines(height,intensity,distance) :   #what you need to give to the funtion
    
    peaks_emission=find_peaks(intensity,height=height,distance=distance)  
    
    return peaks_emission #returns where are the aemissions lines are 

#function that is finding the peaks of absorption 
def absorption_lines(height,intensity,distance) : 
    
    peaks_absorption=find_peaks(-intensity,height=height,distance=distance) #minus intensity so the minimums become maximums

    return peaks_absorption #returns where are the absorptions lines are 


#initiating the parameters that we will use later to find the maximum and the minimum 
height_minimum_peaks,distance_peaks=20,10000 #you can modify those parameters 


#import data from files 
url1='https://www.cfht.hawaii.edu/~manset/Hackathon2020/1835518in.s'  #we want data from the website
url2='https://www.cfht.hawaii.edu/~manset/Hackathon2020/2107396pn.s'
urlretrieve(url1,'1835518in.s')  #telling wich file do we want the data from
urlretrieve(url2,'2107396pn.s')

wavelenght_PN,intensity_PN=np.loadtxt('1835518in.s',skiprows=2,usecols=(0,1),unpack=True) #we put the date into variables and we want only the the first two columns 
wavelenght_GAM,intensity_GAM=np.loadtxt('2107396pn.s',skiprows=2,usecols=(0,1),unpack=True) #we put the date into variables and we want only the the first two columns 
wavelenght_PN,wavelenght_GAM=wavelenght_PN*10,wavelenght_GAM*10 #we want the date in Angstroms

wavelenght_PN.sort()   #sorting the dat in increasing order
wavelenght_GAM.sort()

#using our functions to find the peaks for both data sets
peaks_emission_wavelenght_PN,peaks_emission_PN=emission_lines(height_minimum_peaks,intensity_PN,distance_peaks)
peaks_absorption_wavelenght_PN,peaks_absorption_PN=absorption_lines(height_minimum_peaks,intensity_PN,distance_peaks)

peaks_emission_wavelenght_GAM,peaks_emission_PN=emission_lines(height_minimum_peaks,intensity_GAM,distance_peaks)
peaks_absorption_wavelenght_GAM,peaks_absorption_PN=absorption_lines(height_minimum_peaks,intensity_GAM,distance_peaks)


#here we are plotting the graphs of the wavelenght and relative itensity
plt.figure(1,figsize=(11,11))

plt.subplot(2,1,1) #doing two graphs in the same figure 
plt.plot(wavelenght_PN,intensity_PN)  #plotting everything including noise 
for i in peaks_emission_wavelenght_PN : 
    plt.axvline(wavelenght_PN[i],color='r',linestyle=':',label='Emission peaks') #plotting where are the peaks 
for i in peaks_absorption_wavelenght_PN : 
    plt.axvline(wavelenght_PN[i],color='g',linestyle=':',label='Absorption peaks')
plt.title('Intensity spectrum of PN M1-46') #title
plt.xlabel('Wavelenght (Å)')               #axis names
plt.ylabel('Relative intensity')
plt.axhline(1,color='k',linestyle=':',label='Continuum') #plotting a line at x=1
plt.legend() #legend on the graph


plt.subplot(2,1,2)
plt.plot(wavelenght_GAM,intensity_GAM) #same thing as the first one
for i in peaks_emission_wavelenght_GAM : 
    plt.axvline(wavelenght_GAM[i],color='r',linestyle=':',label='Emission peaks')
for i in peaks_absorption_wavelenght_GAM : 
    plt.axvline(wavelenght_GAM[i],color='g',linestyle=':',label='Absorption peaks')
plt.title('Intensity spectrum of gam CrA A')
plt.xlabel('Wavelenght (Å)')
plt.ylabel('Relative intensity')
plt.axhline(1,color='k',linestyle=':')
plt.legend()

plt.subplots_adjust(hspace=0.35)  #more space between the two graphs
plt.savefig('CFHTchallenge.pdf')  #saving the figure
mplcursors.cursor(hover=True)
plt.show()  #you can show it 


with open('peaks_PM-M1 46',mode='w') as fic :  #creating a fichier and writing where are the peaks of 
                                                #absorption and emission in it for PM-M1 46
    fic.write('#these are the absorption and emission peaks of PM-M1 46\n')
    fic.write('#wavelenght (Å), intensity\n')
    fic.write('#emission : \n')
    
    for i in peaks_emission_wavelenght_PN : 
        fic.write(str(wavelenght_PN[i])+'\t'+str(intensity_PN[i])+'\n')  #writing every 

    fic.write('#absorption : \n')
    for i in peaks_absorption_wavelenght_PN : 
        fic.write(str(wavelenght_PN[i])+'\t'+str(intensity_PN[i])+'\n')

with open('peaks_gam CrA A',mode='w') as fic : 
    
    fic.write('#these are the absorption and emission peaks of PM-M1 46\n')
    fic.write('#wavelenght (Å), intensity\n')
    fic.write('#emission : \n')
    
    for i in peaks_emission_wavelenght_GAM : 
        fic.write(str(wavelenght_GAM[i])+'\t'+str(intensity_GAM[i])+'\n')

    fic.write('#absorption : \n')
    for i in peaks_absorption_wavelenght_GAM : 
        fic.write(str(wavelenght_GAM[i])+'\t'+str(intensity_GAM[i])+'\n')
    











