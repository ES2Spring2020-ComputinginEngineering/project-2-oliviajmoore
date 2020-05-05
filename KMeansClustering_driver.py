# Liv Moore


import numpy as np
import matplotlib.pyplot as plt
import random
import KMeansClustering_functions as kmc #Use kmc to call your functions


K = 2
count = 100

g, h, c = openckdfile()
hemo_scale, gluc_scale = norm(g, h)

assign1, centroid = iterate(hemo_scale, gluc_scale, K, count)
graphingKMeans(gluc_scale, hemo_scale, assign1, centroid)

truepos = np.sum(np.logical_and(assign1 == 1, c == 1))
trueneg = np.sum(np.logical_and(assign1 == 0, c == 0))
falsepos = np.sum(np.logical_and(assign1 == 1, c == 0))
falseneg = np.sum(np.logical_and(assign1 == 0, c == 1))


trueposrate = truepos/(truepos+falseneg)
truenegrate = trueneg/(trueneg+falsepos)

if trueposrate < 0.5:
    trueposrate = 1 - trueposrate
    truenegrate = 1 - truenegrate
    
print(trueposrate*100)
print(truenegrate*100)
