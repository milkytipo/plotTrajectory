# coding:utf-8
#!/usr/bin/python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import geo 

SLAM_data = np.loadtxt("./SLAM_data_raw.txt")
GPS_data = np.loadtxt("./GPS_data_raw.txt")
IMU_data = np.loadtxt("./SLAM_data_raw.txt")

SLAM_data_x = SLAM_data[:,1]
SLAM_data_y = SLAM_data[:,2]
SLAM_data_z = SLAM_data[:,3]

GPS_data_x = GPS_data[:,1]
GPS_data_y = GPS_data[:,2]
GPS_data_z = GPS_data[:,3]

#TODO:implement the LS to get Rotaion matrix
"""
Mat_GPS = np.hstack((np.mat(GPS_data_x).T,np.mat(GPS_data_y).T,np.mat(GPS_data_z).T))
Mat_SLAM = np.hstack((np.mat(SLAM_data_x).T,np.mat(SLAM_data_y).T,np.mat(SLAM_data_z).T))

R = (np.linalg.inv((Mat_GPS.T*Mat_GPS)))*Mat_GPS.T*Mat_SLAM[:len(GPS_data_x),:]

print (Mat_GPS*R).shape
GPS_data_x = (Mat_GPS*R[:,0]).A
GPS_data_y = (Mat_GPS*R[:,1]).A
GPS_data_z = (Mat_GPS*R[:,2]).A
	
print (GPS_data_x)
"""
GPS_data_x_ref = GPS_data_x[0]
GPS_data_y_ref = GPS_data_y[0]
GPS_data_z_ref = GPS_data_z[0]
for i in range(len(GPS_data_x)):
    GPS_data_x[i],GPS_data_y[i],GPS_data_z[i] = geo.geodetic_to_enu(GPS_data_x[i], GPS_data_y[i], GPS_data_z[i], GPS_data_x_ref, GPS_data_y_ref, GPS_data_z_ref)

# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure = ax.plot(SLAM_data_x, SLAM_data_y, SLAM_data_z, c='r')
figure = ax.plot(GPS_data_x, GPS_data_y, GPS_data_z, c='b')

plt.show()
