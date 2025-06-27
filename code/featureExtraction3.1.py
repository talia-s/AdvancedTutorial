import torch
import torch.nn as nn

def batchNorm(x, avg, std):
    y = (x-avg)/(np.sqrt(std**2))


output = torch.randn(2, 3, 4)

x = torch.randn(2, 3, 4)
print(x)
feature1 = torch.flatten(x[:,0,:]).tolist()
avg1 = sum(feature1)/8
std1 = 0
for element in feature1:
    std1+=(element-avg)**2
std1 = (std1/8)**0.5


feature2 = torch.flatten(x[:,1,:]).tolist()
avg2 = sum(feature2)/8
std2 = 0
for element in feature2:
    std2+=(element-avg)**2
std2 = (std2/8)**0.5


feature3 = torch.flatten(x[:,2,:]).tolist()
avg3 = sum(feature3)/8
std3 = 0
for element in feature3:
    std3+=(element-avg)**2
std3 = (std3/8)**0.5

for i in range(2):
    for j in range(3):
        for k in range(4):
            if(j==0):
                avg = avg1
                std = std1
            elif(j==1):
                avg = avg2
                std = std2
            else:

            output[i,j,k] = batchNorm(x[i,j,k], ) 
print("Input shape:", x.shape)

net = nn.Conv1d(3, 5, 1)
x = net(x)
print("Output shape:", x.shape)

