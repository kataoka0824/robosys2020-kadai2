#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String


rospy.init_node('pub_key')
pub = rospy.Publisher('pub_key',String,queue_size = 1)
pub2 = rospy.Publisher('pub_dist',Int32,queue_size = 1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    key_inp=String()
    key_inp.data,n=input("key[x,y,z] distance;").split()
    n=int(n)
    pub.publish(key_inp)
    pub2.publish(n)
    rate.sleep()

