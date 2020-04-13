# plotTrajectory

---
### Directly Read sensor_msgs from rosbag and save them in .txt. Then plot it. This tool is very convenient to plot the SLAM, GPS or other trajectories from rosbag.
---

The usage is very simple, you just need to use rosbag record node to record the /SLAM/pose or /GPS sensor_msgs, then :

> 1. rosbag record /slam/pose /gps/fix 
> 2. set the file path in the loadtxt("/path") in extract_topics_from_rosbag.py
> 3. python extract_topics_from_rosbag.py
> 4. python plotTrajectory.py

Then, you can see the trajectory like this:
<div align = center><img width = "600" height ="400" src ="https://github.com/milkytipo/MSF_developed/blob/master/images/MSF-SLAM-GPS.png" /></div>
<div align = center><img width = "600" height ="400" src ="https://github.com/milkytipo/MSF_developed/blob/master/MSF_noised_results/noised03-GPS-MSF-Front.png" /></div>

P.S. If you want to obtain the RMSE, STD, MAE and other error items, I recommend you the [evo](https://github.com/MichaelGrupp/evo) tool. In addition, I have transfered the KITTI groudtruth file into a general format for MSF error evaluation, namely [kitti_00_groudtruth.tum](https://github.com/milkytipo/MSF_developed/blob/master/MSF_noised_results/kitti_00_groudtruth.tum). **Note:** I recommed you use this groudtruth file, in case you spend lots of time to do the same work as I have done.

