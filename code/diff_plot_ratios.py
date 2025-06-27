import numpy as np
import matplotlib.pyplot as plt

target, prediction = np.loadtxt("/home/talias/trisep2025/AdvancedTutorial/code/data/training_output/output.csv", skiprows=1, delimiter=",", unpack = True)


ratio = []
for i in range(len(target)):
    ratio.append(prediction[i]-target[i])

plt.hist(ratio, histtype = "step", bins = np.linspace(-200,200,30), color = "#339934")
plt.title("Prediction Z - Target Z")
plt.xlabel("Prediction Z - Target Z [mm]")
plt.ylabel("Counts")
plt.savefig("plots/diff.pdf")

