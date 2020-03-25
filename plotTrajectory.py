# coding:utf-8
#!/usr/bin/python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import geo 
import warnings

with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    SLAM_data = np.loadtxt("./SLAM_data_raw.txt")
with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    GPS_data = np.loadtxt("./GPS_data_raw.txt")
with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    MSF_data = np.loadtxt("./MSF_data_raw.txt")
with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    IMU_data = np.loadtxt("./imu_data_raw.txt")

if SLAM_data[:,1] is not None:
    SLAM_data_x = SLAM_data[:,1]
    SLAM_data_y = SLAM_data[:,2]
    SLAM_data_z = SLAM_data[:,3]

if GPS_data[:,1] is not None:
    GPS_data_x = GPS_data[:,1]
    GPS_data_y = GPS_data[:,2]
    GPS_data_z = GPS_data[:,3]

if MSF_data[:,1] is not None:
    MSF_data_x = MSF_data[:,1]
    MSF_data_y = MSF_data[:,2]
    MSF_data_z = MSF_data[:,3]

#if IMU_data[:,1] is not None:
 #   IMU_data_time = IMU_data[:,0]
 #   IMU_data_x = IMU_data[:,1]
 #   IMU_data_y = IMU_data[:,2]
 #   IMU_data_z = IMU_data[:,3]

#for i in range(len(IMU_data_time)-1):
 #   if IMU_data_time[i]>IMU_data_time[i+1]:
 #       print("fatal error!!!!!!")
 #       print i

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
#aimu= fig.gca(projection = '2d')

# set figure information
ax.set_title("3D_Curve")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure = ax.plot(SLAM_data_x, SLAM_data_y, SLAM_data_z, c='r',label = 'SLAM')
figure = ax.plot(GPS_data_x, GPS_data_y, GPS_data_z, c='b',label = 'GPS')
figure = ax.plot(MSF_data_x, MSF_data_y, MSF_data_z, c='g',label = 'MSF')
ax.legend()
plt.show()
