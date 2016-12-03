from scipy import misc
from PIL import Image
import numpy as np
import scipy.ndimage
import itertools
import scipy.misc
from skimage import data, io, filter
from scipy.misc.pilutil import Image
import matplotlib.pyplot as pl
import cPickle
from scipy import ndimage, interpolate
import pylab as pl
import sys
import matplotlib
import os
import math as m
from matplotlib import cm
import matplotlib.pyplot as plt

from skimage.morphology import disk
from skimage.filter import threshold_otsu, rank
from skimage.util import img_as_ubyte

matplotlib.rcParams['font.size'] = 9
from skimage import filters


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


def sector_mask(shape, centre, radius, angle_range):
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

fileStub =  '/Users/sangart/Desktop/MICAST project/MICAST7G/Srms M7G-2L'

#/Users/sangart/Desktop/MICAST project/MICAST7/Optical Images/Srmsimages
#Unimportant counter
counter = 0

this_list = os.listdir(fileStub)
sliced = this_list[:]

#os.listdir() returns a list of the file names in the provided folder
for name in sliced:
    counter += 1
    fileName = fileStub + '/' + name
    img = Image.open(fileName)
    img = misc.fromimage(img)
    misc.imread(name, flatten)
    
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
    circle_dict = {}
    for i, r in enumerate(list_2):
        t = (((m.pi*(radius_step)**2)*(360)/(m.pi*r**2))) 
        a = np.arange(0, 360, t).tolist()
        b = np.arange(x, (360 + t), x).tolist()
        circle_name = 'cirle_'+i
        circle_dict[circle_name] = [a, b, (list_1[i], list_1[i + 1]), []]

    #breaking up into a grid circle1
    for circle_name in circle_dict:
        circlea_theta = circle_dict[circle_name][0]
        circleb_theta = circle_dict[circle_name][1]
        circle_radius1, circle_radius2 = circle_dict[circle_name][2]
        for y, z in itertools.izip(circlea_theta, circleb_theta):
            total = sector_mask(final.shape,
                                ndimage.measurements.center_of_mass(final),
                                circle_radius1,
                                (y,z))
            if circle_name != 'circle_1':
                mask2 = sector_mask(final.shape,
                                    ndimage.measurements.center_of_mass(final),
                                    circle_radius2,
                                    (y,z))
                total= mask2-mask
            totalc= final[np.nonzero(total)] 
            total = []
            for t in totalc:
                total.append(t)
            size = float(len(total))
            white = listsum(total) - total.count(1)
            Fe = 1 - (white/(2.0*size))
            circle_dict[circle_name][3].append(Fe)
        
        try:
            allcircles += circle_dict[circle_name][3]
        except NameError:
            allcircles = circle_dict[circle_name][3]
    
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
  
    


            