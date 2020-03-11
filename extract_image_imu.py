# coding:utf-8
#!/usr/bin/python
 
# Extract images from a bag file.

import os
import sys
import roslib
import rosbag
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError

 
rgb_path = '/home/wuzida/plotTrajectory/'
IMU_Data = open("imu_data_raw.txt",'w')
GPS_Data = open("GPS_data_raw.txt",'w')
SLAM_Data = open("SLAM_data_raw.txt",'w')
class ImageCreator():
    def __init__(self):
        self.bridge = CvBridge()
        with rosbag.Bag('/home/wuzida/data/MSF/KITTI_2019-05-14-15-34-59.bag', 'r') as bag:  #要读取的bag文件；
            for topic,msg,t in bag.read_messages():
                if topic == "/zr300_node/color/image_raw": #图像的topic；
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print e
                        # timestr = "%.9f" %  msg.header.stamp.to_sec()
                        timestr_ns = "%d" %  msg.header.stamp.to_nsec()
                        #%.6f表示小数点后带有6位，可根据精确度需要修改；
                        image_name = timestr_ns+ ".png" #图像命名：时间戳.png
                        cv2.imwrite(rgb_path + image_name, cv_image)  #保存；
                elif topic == "/imu":   #imu的topic；
                        
                        timestr = "%d" %  msg.header.stamp.to_nsec()

                        dx = msg.linear_acceleration.x
                        dy = msg.linear_acceleration.y
                        dz = msg.linear_acceleration.z

                        rx = msg.angular_velocity.x
                        ry = msg.angular_velocity.y
                        rz = msg.angular_velocity.z

                        IMU_Data.writelines([timestr, " ", str(dx), " ",str(dy)," ",str(dz)," ",str(rx)," ",str(ry)," ",str(rz), "\r\n"])
                elif topic == "/gps/fix": # gps topic

                        timestr = "%d" %  msg.header.stamp.to_sec()

                        lattitude = msg.latitude 
                        longitude = msg.longitude
                        altitude = msg.altitude

                        GPS_Data.writelines([timestr, " ", str(lattitude), " ",str(longitude)," ",str(altitude)," " "\r\n"])

                elif topic == "/slam/tf": #slam topic

                        timestr = "%d" %  msg.header.stamp.to_sec()
                        px = msg.transform.translation.x 
                        py = msg.transform.translation.y
                        pz = msg.transform.translation.z
                        qx = msg.transform.rotation.x
                        qy = msg.transform.rotation.y
                        qz = msg.transform.rotation.z
                        qw = msg.transform.rotation.w

                        SLAM_Data.writelines([timestr, " ", str(px), " ",str(py)," ",str(pz)," ",str(qx)," ",str(qy)," ",str(qz)," ",str(qw),"\r\n"])
 
if __name__ == '__main__':
    try:
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
