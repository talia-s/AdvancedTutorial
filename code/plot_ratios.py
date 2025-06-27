import numpy as np
import matplotlib.pyplot as plt

target, prediction = np.loadtxt("/home/talias/trisep2025/AdvancedTutorial/code/data/training_output/output.csv", skiprows=1, delimiter=",", unpack = True)


ratio = []
for i in range(len(target)):
    ratio.append(prediction[i]/target[i])

plt.hist(ratio, histtype = "step", bins = np.linspace(-1,3,60))
plt.title("Prediction Z / Target Z")
plt.xlabel("Prediction Z / Target Z")
plt.ylabel("Counts")
plt.savefig("plots/ratio.pdf")

