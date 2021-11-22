import numpy as np
def mriscan(arr3D):
  axis1 = np.size(arr3D, 0)
  axis2 = np.size(arr3D, 1)
  axis3 = np.size(arr3D, 2)
  l=[]
  for i in range(0,axis1):
    for j in range(0,axis2):
      for k in range (0,axis3):
        if arr3D[i][j][k]==0:
          l.append((i,j,k))

  for p in l:
    print("voxel at")
    print("x = ",p[0]," y = ",p[1], " z = ",p[2],"\n")
    
