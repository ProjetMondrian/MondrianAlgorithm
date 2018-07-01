# MondrianAlgorithm

Here is the algorithm to generate a painting in the style of Mondrian. The algorithm is implemented in Python. 

The program isn't finished yet. 

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/test9.jpg)


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

![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/from%20far%20away.JPG)
![alt text](https://github.com/ProjetMondrian/MondrianAlgorithm/blob/master/superpositionImageEtLignes.JPG)

However the algorithm is not optimized and a great amout of noise is still visible on the painting. The strait lines pattern does not match the style of Mondrian. A new algorithm to create those strait lines has to be implemented, as well as a new method to remove the noise in the painting.

- Guillaume Comte
