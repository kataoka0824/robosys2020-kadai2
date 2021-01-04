#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

position=[0,0,0]
axis="n"

def cb_key(message):
    rospy.loginfo(message.data)
    axis=message.data
    if(message.data!="x" or message.data!="y" or message.data!="z"){
        axis="n"
    }
def cb_dist(message):
    rospy.loginfo(message.data)
    print(message.data)
    if (axis="x"){
        position[0]+=message.data
    }elif(axis="y"){
        position[1]+=message.data
    }elif(axis="z"){
        position[2]+=message.data
    }
    print(position)
if __name__ == '__main__':
    rospy.init_node('sub_key')
    sub = rospy.Subscriber('pub_key',String,cb_key)
    sub2 = rospy.Subscriber('pub_dist',Int32,cb_dist)
    rospy.spin()
