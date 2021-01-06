#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

position=[0,0,0]
axis="n"
pos_x=[0]
pos_y=[0]
pos_z=[0]
#x,y,zの文字の取得
def cb_key(message):
    global axis
    rospy.loginfo(message.data)
    axis=message.data
    print(axis)
    plt.close()
#距離データの取得、座標の加工、表示
def cb_dist(message):
    rospy.sleep(0.02)
    global axis,position
    plt.ion()
    fig=plt.figure("subscriber")
    ax=fig.add_subplot(111,projection='3d')
    rospy.loginfo(message.data)
    print(message.data)
    if (axis=="x"):
        position[0]+=message.data
    elif(axis=="y"):
        position[1]+=message.data
    elif(axis=="z"):
        position[2]+=message.data
    pos_x.append(position[0])
    pos_y.append(position[1])
    pos_z.append(position[2])
    print(position)
    print(axis)
    ax.plot(pos_x,pos_y,pos_z,marker="o")
    ax.plot(pos_x[0:1],pos_y[0:1],pos_z[0:1],color="r",marker="o")
    ax.plot(pos_x[-1:],pos_y[-1:],pos_z[-1:],color="c",marker="o")
    plt.draw()
    plt.pause(5)
#サブスクライバーの設定
if __name__ == '__main__':
    rospy.init_node('sub_key')
    sub = rospy.Subscriber('pub_key',String,cb_key)
    sub2 = rospy.Subscriber('pub_dist',Int32,cb_dist)
    rospy.spin()

