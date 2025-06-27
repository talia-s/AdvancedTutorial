import numpy as np
import matplotlib.pyplot as plt

epoch, training_loss, validation_loss, mean, std = np.loadtxt("/home/talias/trisep2025/AdvancedTutorial/code/data/training_output/training_log.csv", skiprows=1, delimiter=",", unpack = True)

plt.plot(epoch, training_loss, color = "blue", label = "Training Loss", linewidth = 1)
plt.plot(epoch, validation_loss, color = "red", label = "Validation Loss", linewidth = 1)
plt.legend()
plt.title("Training and Validation Loss vs Epoch")
plt.xlabel("Number of Epochs")
plt.ylabel("Loss Function")
plt.savefig("plots/train_val_loss.pdf")

