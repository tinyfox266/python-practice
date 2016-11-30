#!/usr/bin/python

import kNN

from numpy import *

dataSet, labels = kNN.createDataSet()

testX = array([1.2, 1.0])

k = 3

outputLabel = kNN.kNNClassify(testX, dataSet, labels, k)

print "Your input is:", testX, "and classified to class: ", outputLabel  
