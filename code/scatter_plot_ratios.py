import numpy as np
import matplotlib.pyplot as plt

target, prediction = np.loadtxt("/home/talias/trisep2025/AdvancedTutorial/code/data/training_output/output.csv", skiprows=1, delimiter=",", unpack = True)

plt.scatter(prediction, target, s=5, color = "#9933ff")
plt.title("Prediction Z vs Target Z")
plt.xlabel("Prediction Z [mm]")
plt.ylabel("Target Z [mm]")
plt.savefig("plots/ratios.pdf")

