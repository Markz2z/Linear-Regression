from numpy import *

def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine);
    return dataMat

#compute euclidean metric
def disEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)));

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

#disMeans:compute means
#createCent:generate k initial point
def kMeans(dataSet, k, distMeans=disEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
                if clusterAssment[i:0] != minIndex:
                    clusterChanged = True
                clusterAssment[i,:] = minIndex, minDist**2
        print centroids
    print clusterAssment[:,0]
    for cent in range(k):
        #calculate the new cluster core(middle point) for those which belong to the same cluster
		ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
        centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

def bitKmeans(dataSet, k, distMeans = disEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j, 1] = distMeans(mat(centroid0), dataSet[j,:] ** 2)
    while (len(centList) < k):
        lowerstSSE = inf
        for i in range(len(centList)):
            ptsInCurrentCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0], :]
            centroidMat, splitClustAss = kMeans(ptsInCurrentCluster, 2, distMeans)
            sseSplit = sum(splitClustAss[:, 1])
            









