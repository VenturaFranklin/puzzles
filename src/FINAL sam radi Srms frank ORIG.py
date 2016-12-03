from scipy import misc
from PIL import Image
import numpy as np
import scipy.ndimage
import itertools
import scipy.misc
from skimage import data, io, filter
from scipy.misc.pilutil import Image
import numpy as np
import matplotlib.pyplot as pl
from scipy import ndimage
from scipy import misc
from skimage import data
from skimage import filter
import cPickle
import tables
from scipy import ndimage, interpolate
import numpy as np
import pylab as pl
from scipy import ndimage
import sys
import matplotlib
import numpy as np
import cPickle
import os
import itertools
import math as m
from matplotlib import cm


import matplotlib
import matplotlib.pyplot as plt

from skimage import data
from skimage.morphology import disk
from skimage.filter import threshold_otsu, rank
from skimage.util import img_as_ubyte


matplotlib.rcParams['font.size'] = 9
from PIL import Image

import matplotlib
import matplotlib.pyplot as plt
from skimage import filters
from skimage import data
from skimage.morphology import disk
from skimage.filter import threshold_otsu
from skimage.util import img_as_ubyte

from skimage import data
from skimage import filter
import os


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


def sector_mask(shape,centre,radius,angle_range):
    """
    Return a boolean mask for a circular sector. The start/stop angles in  
    `angle_range` should be given in clockwise order.
    """

    x,y = np.ogrid[:shape[0],:shape[1]]
    cx,cy = centre
    tmin,tmax = np.deg2rad(angle_range)

    # ensure stop angle > start angle
    if tmax < tmin:
            tmax += 2*np.pi

    # convert cartesian --> polar coordinates
    r2 = (x-cx)*(x-cx) + (y-cy)*(y-cy)
    theta = np.arctan2(x-cx,y-cy) - tmin

    # wrap angles between 0 and 2*pi
    theta %= (2*np.pi)

    # circular mask
    circmask = r2 <= radius*radius

    # angular mask
    anglemask = theta <= (tmax-tmin)

    return circmask*anglemask

    return circmask*anglemask


    
    

fileStub =  '/Users/sangart/Desktop/MICAST project/MICAST7G/Srms M7G-2L'



#/Users/sangart/Desktop/MICAST project/MICAST7/Optical Images/Srmsimages
#Unimportant counter
counter = 0

list = os.listdir(fileStub)
sliced = list[:]

#os.listdir() returns a list of the file names in the provided folder
for name in sliced:
    counter += 1
    
    fileName = fileStub + '/' + name
    
    img = Image.open(fileName)
    img = misc.fromimage(img)
    

    
    # Gamma Correction
    # Higher value yields darker/more contrasted images
    
    gamma = 3
    new_image = img.astype(float)
    maxi = np.max(new_image)
        
    normalized_image = new_image / maxi
    normalized_image = np.log(normalized_image) * gamma
        
    final = np.exp(normalized_image) * 255.0
    final = final.astype(int)
    final = scipy.misc.toimage(final)
    img = misc.fromimage(final)
    #final.show()
        

    img = filters.gaussian_filter(img, 4.5)
    
    final = scipy.misc.toimage(img)
    img = misc.fromimage(final)
    #final.show()
    r = 12
    selem = disk(r)
        
    
    local_otsu = rank.otsu(img, selem)
    threshold_global_otsu = threshold_otsu(img)
    global_otsu = img >= threshold_global_otsu

            
    #plt.imshow(img >= local_otsu, cmap=plt.cm.gray)
    #plt.title('MICAST7 Tranverse Seed Crystal without Median Filter')



    #plt.show()
    
    img2 = img >= local_otsu
        
    final = np.array(img2) + 1
    
    
    maskt= sector_mask(final.shape,ndimage.measurements.center_of_mass(final), 805,(0,360))
    totalaverage = final[np.nonzero(maskt)]
    totala = []
    for t in totalaverage:
        totala.append(t)
    size = float(len(totala)) 
    white = float(listsum(totala))  - totala.count(1)
    Fe_average = 1 - white/(2*size)  
    
    
    
    radius_step = 115
    list_1 = range(0, 805, radius_step)
    list_2 = range(radius_step, 920 , radius_step)
    
    
    Num_theta = []
    for r in list_2:
        t = (((m.pi*(radius_step)**2)*(360)/(m.pi*r**2))) 
        Num_theta.append(t)
        
    list_a = []
    list_b = []
    
    for x in Num_theta:
        a = np.arange(0,360, x)
        b = np.arange(x,(360 +x), x)
        list_a.append(a)
        list_b.append(b)

    
    circle1a_theta = list_a[0].tolist()
    circle1b_theta = list_b[0].tolist()
    
    circle2a_theta = list_a[1].tolist()
    circle2b_theta = list_b[1].tolist()
    
    circle3a_theta = list_a[2].tolist()
    circle3b_theta = list_b[2].tolist()
    
    circle4a_theta = list_a[3].tolist()
    circle4b_theta = list_b[3].tolist()
    
    circle5a_theta = list_a[4].tolist()
    circle5b_theta = list_b[4].tolist()
    
    circle6a_theta = list_a[5].tolist()
    circle6b_theta = list_b[5].tolist()
    
    circle7a_theta = list_a[6].tolist()
    circle7b_theta = list_b[6].tolist()
    
    #breaking up into a grid circle1
    circle_1 = [] 

    mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,115,(0,360))
    totalc= final[np.nonzero(mask)] 
    total = [] 
    for line in totalc:
        total.append(line)
    size = float(len(total))
    white = listsum(total) - total.count(1)
    one = 1 - (white/(2.0*size))
    circle_1.append(one)
         
            

            
           
    #breaking up into a grid circle
    circle_2 = [] 



    for y, z in itertools.izip(circle2a_theta, circle2b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,115,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),230,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_2.append(Fe)
            

    circle_3 = []              

    for y, z in itertools.izip(circle3a_theta, circle3b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,230,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),345 ,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_3.append(Fe)
            


    circle_4 = []              

    for y, z in itertools.izip(circle4a_theta, circle4b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,345,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),460,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_4.append(Fe)
        
    circle_5 = []              

    for y, z in itertools.izip(circle4a_theta, circle4b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,460,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),575,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_5.append(Fe)
        
    circle_6 = []              

    for y, z in itertools.izip(circle4a_theta, circle4b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,575,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),690,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_6.append(Fe)
        
    circle_7 = []              

    for y, z in itertools.izip(circle4a_theta, circle4b_theta):
        mask = sector_mask(final.shape,ndimage.measurements.center_of_mass(final) ,690,(y,z))
        mask2 = sector_mask(final.shape,ndimage.measurements.center_of_mass(final),805,(y,z))
        total= mask2-mask
        totalc= final[np.nonzero(total)] 
        total = []
        for t in totalc:
            total.append(t)
        size = float(len(total))
        white = listsum(total) - total.count(1)
        Fe = 1 - (white/(2.0*size))
        circle_7.append(Fe)
        

   
   
   
    allcircles = circle_1 + circle_2 + circle_3 + circle_4  + circle_5 + circle_6 +circle_7 
    
    
    
    dA = m.pi*115**2
    area = m.pi*805**2
    sum = []
    for m1 in allcircles:
        s = ((m1/(Fe_average))-1)**2*dA
        sum.append(s)
        
    Srms = (listsum(sum)/area)**0.5
    
    stdev = []
    for p in allcircles:
        d = ((p/(Fe_average))-1)**2
        stdev.append(d)
    
    stdev = np.asarray(stdev)
    
    

    
    print name
    print Srms
    print np.std(stdev)
    print Fe_average
  
    


            