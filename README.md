# MondrianAlgorithm

Here is the algorithm to generate a painting in the style of Mondrian. The algorithm is implemented in Python. It chooses the color by calculating the mean of the RGB components of each pixel inside a region. 

Choosing the color based on the pixel that appears more frequently inside a region will be implemented. 

The program isn't finished yet. 

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/test9.jpg)



## The first algorithm

Based on this picture with the following parameters we get with the algorithm :  

- scale = 40

- resizevalue = 1

- cleanvalue = 20

- marge = 60

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/Result1.jpg)


By lowering the scale we get a picture which looks a little bit more like the original picture : 

- scale = 20

- resizevalue = 1  

- cleanvalue = 20

- marge = 60

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/Result2.jpg)


From far away we can almost guess the original picture from the painting

<p align="center">
  <img width="200" height="200" src="https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/from%20far%20away.JPG">
</p>



However the algorithm is not optimized and a great amount of noise is still visible on the painting. The noise could be removed by the function called "cleanUpPainting" inside of the python program, unfortunately this function works recursively and for pictures with a fair amount of pixels (1960x1960) it is impossible for the function to work without taking several minutes.

Furthermore the straight lines pattern on the painting generated does not match the style of Mondrian. A new algorithm to create those strait lines has to be implemented, as well as a new method to remove the noise in the painting.

## The second algorithm
The noise problem can be corrected by changing the values of the parameters in the procedure ```img.resize``` from the PIL library

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/FinalResult_noNoise.jpg)


## The third algorithm

With a better algorithm to generate the staight lines we get a very promising result: 

- scale = 20

- outputSize = (1000,1000)

- number_of_lines = 50

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/betterAlgorithm.jpg)

by choosing the color with the most numerous pixels we get : 

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/Algo4.jpg)

No facial recognition is used inside the program, it might be a good idea to add it. 


- Guillaume Comte
