#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String


rospy.init_node('my_talker')
pub = rospy.Publisher('my_chat_topic', Int32, queue_size=10)
pub2 = rospy.Publisher('my_chat_topic_2', String, queue_size=10)
rate = rospy.Rate(10)

def start_my_talker():
    i = 0
    msg = String()
    while not rospy.is_shutdown():
       
        rospy.loginfo(i)
        pub.publish(i)
        i+=2
        
        if i == 102:
        	i = 0
        	msg.data = "it's 100!"
        	rospy.loginfo(msg)
        	pub2.publish(msg)
        rate.sleep()

try:
    start_my_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
