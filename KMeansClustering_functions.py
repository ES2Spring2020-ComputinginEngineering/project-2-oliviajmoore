# Liv Moore

import numpy as np
import matplotlib.pyplot as plt
import random


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def norm(glucose, hemoglobin):
    norm_gluc = (glucose-min(glucose))/(max(glucose)-min(glucose))
    norm_hemo = (hemoglobin-min(hemoglobin))/(max(hemoglobin)-min(hemoglobin))
    return norm_hemo, norm_gluc

def select(K):
    centroid = np.random.rand(K, 2) #column 0 = hemo, column 1 = gluc
    return centroid

def assign(hemo, gluc, centroids, K):
    # takes hemoglobin and glucose arrays
    # returns assignment, an array where each value is the number of the closest centroid
    distancearray = np.zeros((len(gluc), K))
    for k in range(K):
        centroid_gluc = centroids[k, 1]
        centroid_hemo = centroids[k, 0]
        distancearray[:, k] =  np.sqrt((gluc-centroid_gluc)**2 + (hemo-centroid_hemo)**2)
    assignment = np.argmin(distancearray, axis = 1)
    return assignment

    
def update(hemo, gluc, assignment, K):
    # takes the glucose, hemoglobin, and assignment arrays
    # calculates the mean of each cluster and creates a new centroid array in which 
    # centroid are centered in the cluster
    # returns an array
    newcentroids = np.zeros((K, 2))
    for k in range(K):
        mean_hemo = np.mean(hemo[assignment == k])
        mean_gluc = np.mean(gluc[assignment == k])
        newcentroids[k,1] = mean_gluc
        newcentroids[k,0] = mean_hemo
    return newcentroids
    
    
def iterate(hemo, gluc, K, count):
    centroid = select(K)
    for i in range(count):
        assign1 = assign(hemo_scale, gluc_scale, centroid, K)
        centroid = update(assign1, hemo_scale, gluc_scale, K)
    return assign1, centroid

def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()