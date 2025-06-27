import numpy as np
import matplotlib.pyplot as plt

target, prediction = np.loadtxt("/home/talias/trisep2025/AdvancedTutorial/code/data/training_output/output.csv", skiprows=1, delimiter=",", unpack = True)


ratio = []
for i in range(len(target)):
    ratio.append(prediction[i]-target[i])

plt.scatter(target , ratio, s = 5, color = "#cc32cc")
plt.title("(Prediction Z - Target Z) vs Target Z")
plt.ylabel("Prediction Z - Target Z [mm]")
plt.xlabel("Target Z [mm]")
plt.savefig("plots/diffvsTarget.pdf")

