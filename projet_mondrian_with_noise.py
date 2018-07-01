from PIL import Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random
from operator import add
import sys
sys.setrecursionlimit(1500)


image_name = "test7.jpg"
scale = 40
resizevalue = 1        
cleanvalue = 20
marge = 60


## We define here the number of lines that we want
number_of_lines = 20
#the number of lines must be even


'''
all the values above must be between 1 and 100, the bigger the value, the more pixelated it will be
resize = final size of picture
scale = the scale of the mondrian painting
cleanvalue = scale to cleanup ... doesnt really work
marge = how to compare colors for the cleanup, the bigger the better
'''


''' USEFUL FUNCTIONS '''

def listToMatrix(alist,width,height):
    a = [[]] * height
    for i in range(height):
        a[i] = [[]] * width
    k = 0
    for i in range(0,height):
        for j in range(0,width):
            a[i][j] = alist[k]
            k = k +1
    return a




''' FUNCTIONS TO COLOR THE PAINTING '''

def removeBlackWhiteImperfection(matrix,width,height):
    for i in range (0,height):
        for j in range (0, width):
            if matrix[i][j] > (100,100,100):
                matrix[i][j] = (255,255,255)
            else:
                matrix[i][j] = (0,0,0)
    return matrix

def getLengthY(length,a,firstPoint):
    numrows = len(a)   
    if firstPoint[0] < numrows:
        if a[firstPoint[0]][firstPoint[1]] == (255,255,255):
            firstPoint[0] = firstPoint[0] + 1
            length = getLengthY(length + 1,a,firstPoint)
    return length

def getLengthX(length,a,firstPoint):
    numcols = len(a[0])
    if firstPoint[1] < numcols:
        if a[firstPoint[0]][firstPoint[1]] == (255,255,255):
            firstPoint[1] = firstPoint[1] + 1
            length = getLengthX(length + 1,a, firstPoint)
    return length

def fillBlanks(NoColorImage, ColorImage, width, height):
    imgToFill = Image.open(NoColorImage)
    imgOrigin = Image.open(ColorImage)
    pixelsNotColored = list(imgToFill.getdata())
    pixelsColored = list(imgOrigin.getdata())
    a = listToMatrix(pixelsColored,width,height)
    b = listToMatrix(pixelsNotColored,width,height)
    b = removeBlackWhiteImperfection(b,width,height)
    for i in range (0,(height)):
        for j in range (0,(width)):
            if b[i][j] == (255,255,255):
                firstPoint = [i,j]
                firstXPoint = [i,j]
                firstYPoint = [i,j]
                surfaceW = getLengthX(0,b,firstXPoint)
                surfaceH = getLengthY(0,b,firstYPoint)
                b = fillColor(a,b,firstPoint,surfaceH,surfaceW)            
    c = [0] * (width*height)
    index = 0 
    for i in range (0,height):
        for j in range (0, width):
            c[index] = b[i][j]
            index = index + 1           
    return c

def fillColor(a,b,firstPoint,h,w):
    R = 0
    G = 0
    B = 0
    for i in range (firstPoint[0],h + firstPoint[0]):
        for j in range (firstPoint[1],w + firstPoint[1]):
            listToAdd = a[i][j]
            R = R + listToAdd[0]
            G = G + listToAdd[1]
            B = B + listToAdd[2]
    RGB = [R,G,B]
    RGB = np.array(RGB)
    newColor = RGB/(h*w)
    newColor = (newColor[0],newColor[1],newColor[2])

    for i in range (firstPoint[0],h + firstPoint[0]):
        for j in range (firstPoint[1],w + firstPoint[1]):
            b[i][j] = newColor
    return b




''' FUNCTIONS TO CLEAN UP THE PAINTING '''

def getCleanLengthY(length,a,firstPoint):
    numrows = len(a)   
    if firstPoint[0] < numrows:
        if a[firstPoint[0]][firstPoint[1]] > (marge,marge,marge):
            firstPoint[0] = firstPoint[0] + 1
            length = getCleanLengthY(length + 1,a,firstPoint)
    return length

def getCleanLengthX(length,a,firstPoint):
    numcols = len(a[0])
    if firstPoint[1] < numcols:
        if a[firstPoint[0]][firstPoint[1]] > (marge,marge,marge):
            firstPoint[1] = firstPoint[1] + 1
            length = getCleanLengthX(length + 1,a, firstPoint)
    return length

def cleanUpPainting(painting,w,h):
    imgToClean = Image.open(painting)
    pixelsToClean = list(imgToClean.getdata())
    b = listToMatrix(pixelsToClean,w,h)
    for i in range (0,h):
        for j in range (0,w):
            if b[i][j] > (marge,marge,marge):
                firstPoint = [i,j]
                firstXPoint = [i,j]
                firstYPoint = [i,j]
                surfaceW = getCleanLengthX(0,b,firstXPoint)
                surfaceH = getCleanLengthY(0,b,firstYPoint)
                b = fillColorClean(b,firstPoint,surfaceH,surfaceW)
    c = [0] * (w*h)
    index = 0 
    for i in range (0,h):
        for j in range (0, w):
            c[index] = b[i][j]
            index = index + 1           
    return c

def fillColorClean(b,firstPoint,h,w):
    color = b[firstPoint[0]][firstPoint[1]]
    for i in range (firstPoint[0],h + firstPoint[0]):
        for j in range (firstPoint[1],w + firstPoint[1]):
            b[i][j] = color
    return b







## Selection of the image
img = Image.open(image_name)
owidth, oheight = img.size


## We define the height and the width so that the algorithme doesnt have
## too many pixels to work with
width = owidth/scale
height = oheight/scale
img.resize((width,height)).save("LessPixelsImage.jpg")


imgblank = np.zeros([width,height,3],dtype=np.uint8)
imgblank.fill(255)
cv.imwrite("blank.jpg",imgblank)



## We use the image with less pixels
img = Image.open("LessPixelsImage.jpg")



## We get the RGB decomposition of each pixels into an array
pixels = list(img.getdata())



## We remove black pixels to not get errors with contour
for i in range (0,len(pixels)):
    if pixels[i][0] < 20 and pixels[i][1] < 20 and pixels[2] < 20:
        pixels[i] = (20,20,20)
img.putdata(pixels)
img.save("LessPixelsImageWithoutBlack.jpg")
img = Image.open("LessPixelsImageWithoutBlack.jpg")
pixels = list(img.getdata())



## Since all RGB values are in an array, we will put them inside a matrix
## so that it will be easier to manipulate them

a = listToMatrix(pixels,width,height)


"""
Some examples to verify the indexes
print(a[0][0])
print(pixels[0])
print(a[1][0])
print(pixels[50])
print(a[49][49])
print(pixels[2499])
"""


## We extract inside an array the edges of the image
imgingray = cv.imread("LessPixelsImageWithoutBlack.jpg",0)
img = cv.imread("LessPixelsImageWithoutBlack.jpg")
edges = cv.Canny(imgingray,100,200)



## For each line of pixels, we look where are the principals edges
line_ed = [0] * (height)
for i in range(0,height-1):
    line_ed[i] = np.sum(edges[i])



## For each column of pixels, we look where are the principals edges
column_ed = [0] * (width)
for i in range(0,width-1):
    somme = 0
    for j in range(0,height-1):
        somme = somme + edges[j][i]
    column_ed[i] = somme
ycoor = [height]
xcoor = [width]
line_ed[0] = 0
line_ed[1] = 0
line_ed[height-1] = 0
line_ed[height-2] = 0
column_ed[0] = 0
column_ed[1] = 0
column_ed[width-1] = 0
column_ed[width-2] = 0



## Function that plots one horizontal and one vertical line
def plot_line(edges,line_ed,column_ed,ycoor,xcoor,imgs,img2):
    rn = 0 
    xlen = len(xcoor)
    #rn = random.randint(0, xlen-1)
    le = np.argmax(line_ed)
    cv.line(img,(0,le),(xcoor[rn],le),(0,0,0),1)
    cv.line(img2,(0,le),(xcoor[rn],le),(0,0,0),1)
    line_ed[le] = 0
    line_ed[le + 1] = 0
    line_ed[le - 1] = 0
    line_ed[le + 2] = 0
    line_ed[le - 2] = 0 
    ycoor.append(le)
    ylen = len(ycoor)
    rn = ylen-1
    #rn = 0
    k = rn%2
    ce = np.argmax(column_ed)
    #cv.line(img,(ce,0),(ce,ycoor[rn]),(0,0,0),1)
    if k ==1:
        cv.line(img,(ce,0),(ce,ycoor[rn]),(0,0,0),1)
        cv.line(img2,(ce,0),(ce,ycoor[rn]),(0,0,0),1)
    else:
        cv.line(img,(ce,ycoor[rn]),(ce,height),(0,0,0),1)
        cv.line(img2,(ce,ycoor[rn]),(ce,height),(0,0,0),1)
    column_ed[ce] = 0
    column_ed[ce + 1] = 0
    column_ed[ce - 1] = 0
    column_ed[ce + 2] = 0
    column_ed[ce - 2] = 0 
    xcoor.append(ce)
    return [edges,line_ed,column_ed,ycoor,xcoor,img,img2]


j = 0
while j <= number_of_lines:
    edges,line_ed,column_ed,ycoor,xcoor,img,imgblank = plot_line(edges,line_ed,column_ed,ycoor,xcoor,img,imgblank)
    j = j + 1





          
cv.imwrite("TemporaryResult.jpg",img)
cv.imwrite("blank.jpg",imgblank)

cv.imread("superposition.jpg")       
cv.imwrite("superposition.jpg",img)

resultatList = fillBlanks("blank.jpg", "LessPixelsImageWithoutBlack.jpg", width, height)
img = Image.open("TemporaryResult.jpg")
img.putdata(resultatList)
img.save("TemporaryResult.jpg")

resizewidth = owidth/resizevalue
resizeheight = oheight/resizevalue

cleanWidth = owidth/cleanvalue
cleanHeight = oheight/cleanvalue

img = Image.open("TemporaryResult.jpg")
img.resize((cleanWidth,cleanHeight)).save("resultWithoutCleaning.jpg")

img = Image.open("resultWithoutCleaning.jpg")
cleanPixels = cleanUpPainting("resultWithoutCleaning.jpg",cleanWidth, cleanHeight)
img.putdata(cleanPixels)
img.save("FinalResult.jpg")



img = Image.open("FinalResult.jpg")
img.resize((resizewidth,resizeheight)).save("FinalResult.jpg")

img = Image.open("blank.jpg")
img.resize((resizewidth,resizeheight)).save("blank.jpg")


