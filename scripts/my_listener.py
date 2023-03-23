#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(i):
    rospy.loginfo(i)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic', Int32, callback, queue_size=10)
rospy.spin()
