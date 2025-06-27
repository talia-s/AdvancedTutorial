from data.dataset import PointCloudDataset
import matplotlib.pyplot as plt

config = {"cloud_size": 140}
dataset = PointCloudDataset(
    "/fast_scratch_1/TRISEP_data/AdvancedTutorial/small_dataset.parquet", config
)

index = 0  # First event
point_cloud, target = dataset[index]
print(point_cloud)


fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.scatter(point_cloud[0], point_cloud[1], point_cloud[2])
ax.scatter(0, 0, target.item(), color="red")
plt.savefig("plots/first10Events.pdf")
