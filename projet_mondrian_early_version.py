from PIL import Image
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import random

image_name = "test9.jpg"
scale = 20

## We define here the number of lines that we want
number_of_lines = 20
#the number of lines must be even

## Selection of the image
img = Image.open(image_name)
owidth, oheight = img.size

## We define the height and the width so that the algorithme doesnt have
## too many pixels to work with
width = owidth/scale
height = oheight/scale
img.resize((width,height)).save("20.jpg")

imgblank = np.zeros([width,height,3],dtype=np.uint8)
imgblank.fill(255)
cv.imwrite("blank.jpg",imgblank)

## We use the image with less pixels
img = Image.open("20.jpg")

## We get the RGB decomposition of each pixels into an array
pixels = list(img.getdata())

## We remove black pixels to not get errors with contour
for i in range (0,len(pixels)):
    if pixels[i][0] < 20 and pixels[i][1] < 20 and pixels[2] < 20:
        pixels[i] = (20,20,20)

img.putdata(pixels)
img.save("20.jpg")

img = Image.open("20.jpg")
pixels = list(img.getdata())

## Since all RGB values are in an array, we will put them inside a matrix
## so that it will be easier to manipulate them
a = [[]] * width
for i in range(width):
    a[i] = [[]] * height

k = 0
for i in range(0,width):
    for j in range(0,height):
        a[i][j] = pixels[k]
        k = k +1

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
imgingray = cv.imread("20.jpg",0)
img = cv.imread("20.jpg")
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

## Function to floodfill 
def floodfill(matrix, x, y, color):
    if matrix[x][y] == (255,255,255):  
        matrix[x][y] = color
        if x > 0:
            floodfill(matrix,x-1,y, color)
        if x < len(matrix[y]) - 1:
            floodfill(matrix,x+1,y, color)
        if y > 0:
            floodfill(matrix,x,y-1, color)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1, color)

    
##lower = np.array([1, 1, 1])
##upper = np.array([255,255,255])
##shapeMask = cv.inRange(img, lower, upper)
##
##__ ,contours, hierarchy = cv.findContours(shapeMask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
##
##
##for contour in contours:
##    cv.drawContours(img, contour, -1, (255, 255, 255), -1)
##
##cv.imwrite("shape.jpg",shapeMask)
            
cv.imwrite("20.jpg",img)
cv.imwrite("blank.jpg",imgblank)

cv.imread("shape.jpg")


        
cv.imwrite("shape.jpg",img)

           
img = Image.open("20.jpg")
img.resize((owidth,oheight)).save("20.jpg")

img = Image.open("blank.jpg")
img.resize((owidth,oheight)).save("blank.jpg")


