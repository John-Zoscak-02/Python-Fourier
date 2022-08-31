# Python-Fourier

Over my winter break, I worked with two friends to create a program in Python for producing a Fourier series given an svg file https://github.com/DanielTolbert/Python-Fourier. This involved significant studying of the relevant mathematics, as well as investigation on how to implement scientific functions in python. 
-Notes, due to the use of svg readers in python, we encountered an issue where the svg reader will incorrectly read the line element of the svg file exactly once. Running window.py will produce a visualization of the svg as created by the fourier series, but will exhibit a sharp inconsistency in the graph. Solutions include producing our own svg line reader. (This shouldn't be too hard, simply look at the keys of the element of the line, for curves, we will assume the slope at the midpoint will equal to the average slope of the element)
