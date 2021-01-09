#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import tkinter as tk
import sys

#データの送信
def pub_data():
    key_inp=String()
    key_inp.data=entry_axis.get()
    dist=entry_dist.get()
    try:
        dist=int(dist)
    except:
        dist=0
    pub.publish(key_inp)
    pub2.publish(dist)
    entry_axis.delete(0,tk.END)
    entry_dist.delete(0,tk.END)
#ウィンドウを閉じる
def exit_window():
    sys.exit()
#パブリッシャーの設定
rospy.init_node('pub_node')
pub = rospy.Publisher('pub_key',String,queue_size = 1)
pub2 = rospy.Publisher('pub_dist',Int32,queue_size = 1)
rate = rospy.Rate(10)
#入力用GUI
root=tk.Tk()
root.title("publisher")
root.geometry("400x100")
text_axis=tk.Label(root,text="軸x,y,z:")
text_axis.grid(row=0,column=0)
entry_axis=tk.Entry(root,width=3)
entry_axis.grid(row=0,column=1)
text_dist=tk.Label(root,text="移動距離:")
text_dist.grid(row=0,column=2)
entry_dist=tk.Entry(root,width=10)
entry_dist.grid(row=0,column=3)
button_pub=tk.Button(root,text="送信",command=pub_data)
button_pub.grid(row=0,column=4)
button_exit=tk.Button(root,text="閉じる",command=exit_window)
button_exit.grid(row=1,column=2)
root.mainloop()
