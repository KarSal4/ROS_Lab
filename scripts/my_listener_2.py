#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(msg.data)

rospy.init_node('listener')
rospy.Subscriber('my_chat_topic_2', String, callback, queue_size=10)
rospy.spin()