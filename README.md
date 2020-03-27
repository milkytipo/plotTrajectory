# plotTrajectory

---
### Directly Read sensor_msgs from rosbag and save them in .txt. Then plot it. This tool is very convenient to plot the SLAM/GPS or other trajectories from rosbag.
---

The usage is very simple, you just need to use rosbag record node to record the /SLAM/pose or /GPS sensor_msgs, then :

> 1. rosbag record /slam/pose /gps/fix 
> 2. set the file path in the loadtxt("/path") in extract_topics_from_rosbag.py
> 3. python extract_topics_from_rosbag.py
> 4. python plotTrajectory.py

Then, you can see the trajectory like this:
<div align = center><img width = "600" height ="400" src ="https://github.com/milkytipo/MSF_developed/blob/master/images/MSF-SLAM-GPS.png" /></div>

I also add the calcuateError function in [plotTrajectory](https://github.com/milkytipo/plotTrajectory). If you do not change the output filename in extract_topics_from_rosbag.py, you just directly run:
```
python calculateError.py
```
**Note:** As we all know, KITTI didn't provide the groudtruth about the trajectory, so **I suppose the original fixed GPS as the groudtruth and use the GPS-noised as the GPS input**. Then, through comparing the GPS-noised and MSF_developed results, you can value the effect about the framework.
### RMSE excel

| Type        | MSF_developed   |  GPS-noised  |
| --------   | -----:  | :----:  |
| RMSE     | 26.036 |   36.993   |
| MAE       |  None    |  None   |

