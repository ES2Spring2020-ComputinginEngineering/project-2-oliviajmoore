#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    norm_gluc = (glucose - min(glucose))/(max(glucose)-min(glucose))
    norm_hemo = (hemoglobin - min(hemoglobin))/(max(hemoglobin)-min(hemoglobin))
    return norm_gluc, norm_hemo, classification

def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def createTestCase():
    newhemoglobin = np.random.random(1)
    newglucose = np.random.random(1)
    return newhemoglobin, newglucose

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distance_array = np.sqrt((glucose-newglucose)**2 + (hemoglobin-newhemoglobin)**2)
    return distance_array

def nearestNeighborClassifier(newglucose,newhemoglobin,glucose,hemoglobin,classification):
    distances = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    nearest_index = np.argmin(distances)
    point_class = classification[nearest_index]
    return point_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    if nearestNeighborClassifier(newglucose,newhemoglobin,glucose,hemoglobin,classification) == 1:
        plt.plot(newhemoglobin,newglucose, "k.", label = "Class 1")
    else:
        plt.plot(newhemoglobin,newglucose, "r.", label = "Class 0")
    plt.show()
    
def KNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distances = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distances)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    k_class = np.median(k_classifications)
    return k_class

# MAIN SCRIPT
glucose, hemoglobin, classification = openckdfile()

#raphData(glucose, hemoglobin, classification)

# newhemoglobin, newglucose = createTestCase()
# graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)

k = 99

print(KNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification))