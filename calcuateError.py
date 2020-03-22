# coding:utf-8
#!/usr/bin/python
 
# -*- coding: utf-8 -*-
# @Author: wuzida
# @Date:   2020-3-21 15:20:54
# @Last Modified by:   wuzida
# @Last Modified time: 2020-3-21 15:50:54

import matplotlib.pyplot as plt
import numpy as np
import geo 
import warnings
import math

#msf_synchronize2gps
#integrate the frame values in one second into one frame. namely, 100 frame -> 1 frame
def time_syn(MSF_time,msfArray):
   #     time = [[0 for col in range (int(MSF_time[-1] - MSF_time[0] + 1))] for row in range(2)]
    time = []
    p_mean = []
    n = 1 
    p_mean_persecond = 0
    flag = 1
    for i in range(len(msfArray)):
        if i <len(MSF_time)-1 and MSF_time[i] == MSF_time[i+1] :
            n = n+1
        else:
            for m in range(n):
                p_mean_persecond = p_mean_persecond + msfArray[flag+m-1]/(n)
            time.append(MSF_time[i])
            p_mean.append(p_mean_persecond - msfArray[0])
            n = 1
            flag = i+1
            p_mean_persecond = 0
    return time,p_mean

def calculateMAE(refTime, dataTime,refArray,dataArray):
    error = []
    j = 0
    for i in range(len(refTime)):
        if refTime[i] == dataTime[j]:
           error.append(refArray[i] - dataArray[j])
           j = j + 1
        else:
           i = i + 1
    return error

def calculateRMSE(refTime, dataTime,refArray_x,refArray_y,refArray_z,dataArray_x,dataArray_y,dataArray_z) :    
    error = []
    j = 0
    for i in range(len(refTime)):
        if refTime[i] == dataTime[j]:
           error.append( (refArray_x[i] - dataArray_x[j])*(refArray_x[i] - dataArray_x[j]) + (refArray_y[i] - dataArray_y[j])*(refArray_y[i] - dataArray_y[j]) + (refArray_z[i] - dataArray_z[j])*(refArray_z[i] - dataArray_z[j]) ) 
           j = j + 1
        else:
           i = i + 1
    RMSE = math.sqrt(sum(error))/i

    return RMSE

with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    GPS_raw = np.loadtxt("./GPS_raw.txt")
    if GPS_raw[:,1] is not None:
        GPS_time= GPS_raw[:,0]
        GPS_raw_x = GPS_raw[:,1]
        GPS_raw_y = GPS_raw[:,2]
        GPS_raw_z = GPS_raw[:,3]
        GPS_data_x_ref = GPS_raw_x[0]
        GPS_data_y_ref = GPS_raw_y[0]
        GPS_data_z_ref = GPS_raw_z[0]
    for i in range(len(GPS_raw_x)):
        GPS_raw_x[i],GPS_raw_y[i],GPS_raw_z[i] = geo.geodetic_to_enu(GPS_raw_x[i], GPS_raw_y[i], GPS_raw_z[i], GPS_data_x_ref, GPS_data_y_ref, GPS_data_z_ref)

with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    GPS_noised = np.loadtxt("./GPS_noised-03.txt")
    if GPS_noised[:,1] is not None:
        GPS_noised_time = GPS_noised[:,0]
        GPS_noised_x = GPS_noised[:,1]
        GPS_noised_y = GPS_noised[:,2]
        GPS_noised_z = GPS_noised[:,3]
        GPS_data_x_ref = GPS_noised_x[0]
        GPS_data_y_ref = GPS_noised_y[0]
        GPS_data_z_ref = GPS_noised_z[0]
    for i in range(len(GPS_raw_x)):
        GPS_noised_x[i],GPS_noised_y[i],GPS_noised_z[i] = geo.geodetic_to_enu(GPS_noised_x[i], GPS_noised_y[i], GPS_noised_z[i], GPS_data_x_ref, GPS_data_y_ref, GPS_data_z_ref)

with warnings.catch_warnings():
   # warnings.simplefilter("ignore")
    MSF_noised = np.loadtxt("./MSF_noised-03.txt")
    if MSF_noised[:,1] is not None:
        MSF_time= MSF_noised[:,0]
        MSF_noised_x = MSF_noised[:,1]
        MSF_noised_y = MSF_noised[:,2]
        MSF_noised_z = MSF_noised[:,3]

msf_sysn_time,msf_sysn_x = time_syn(MSF_time,MSF_noised_x)
msf_sysn_time,msf_sysn_y = time_syn(MSF_time,MSF_noised_y)
msf_sysn_time,msf_sysn_z = time_syn(MSF_time,MSF_noised_z)


MAE_x_msf2GPS = calculateMAE(msf_sysn_time,GPS_time,msf_sysn_x,GPS_raw_x)
MAE_y_msf2GPS = calculateMAE(msf_sysn_time,GPS_time,msf_sysn_y,GPS_raw_y)
MAE_z_msf2GPS = calculateMAE(msf_sysn_time,GPS_time,msf_sysn_z,GPS_raw_z)

RMSE_msf = calculateRMSE(msf_sysn_time, GPS_time,msf_sysn_x,msf_sysn_y,msf_sysn_z,GPS_raw_x,GPS_raw_y,GPS_raw_z)
RMSE_GPS_noised = calculateRMSE(GPS_noised_time, GPS_time,GPS_noised_x,GPS_noised_y,GPS_noised_z,GPS_raw_x,GPS_raw_y,GPS_raw_z)
RMSE_GPS = calculateRMSE(GPS_time, GPS_time,GPS_raw_x,GPS_raw_y,GPS_raw_z,GPS_raw_x,GPS_raw_y,GPS_raw_z)
print("MSF RMSE = ", RMSE_msf,"GPS-noised RMSE",RMSE_GPS_noised)

