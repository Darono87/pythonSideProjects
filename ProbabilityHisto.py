import matplotlib.pyplot as plt
import numpy as np


tossCount = int(input("Please give me the number of tosses to perform:"))
experimentsCount = [30,100,250,1000,5000]

randomTab = np.array([])
for x in range(experimentsCount[4]):
    randomTab = np.append(randomTab,np.random.randint(0, 2, tossCount))

randomTab = randomTab.reshape((-1, tossCount))
randomTab = np.sum(randomTab,axis=1)
print(randomTab)

firstExperimentTab = randomTab[:experimentsCount[0]]
secondExperimentTab = randomTab[:experimentsCount[1]]
thirdExperimentTab = randomTab[:experimentsCount[2]]
fourthExperimentTab = randomTab[:experimentsCount[3]]
fifthExperimentTab = randomTab

bins = np.arange(tossCount+1)
plt.figure(1)
plt.subplot(221)
plt.hist(firstExperimentTab,bins=bins, histtype='bar')
plt.subplot(222)
plt.hist(secondExperimentTab,bins=bins, histtype='bar')
plt.subplot(223)
plt.hist(thirdExperimentTab,bins=bins, histtype='bar')
plt.subplot(224)
plt.hist(fourthExperimentTab,bins=bins, histtype='bar')
plt.figure(2)
plt.xlabel("Ile reszek w " + str(tossCount) + " rzutach.")
plt.ylabel("Liczba eksperymentów")
plt.hist(fifthExperimentTab,bins=bins, histtype='bar')
plt.show()