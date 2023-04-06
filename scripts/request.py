#!/usr/bin/env python3
import rospy

from std_msgs.msg import Int32
from std_msgs.msg import String



rospy.init_node('request')
pub = rospy.Publisher('topic1', String, queue_size=10)
rate = rospy.Rate(10)

def callback(result):
    rospy.loginfo(result)





def start_my_talker():
    
    while not rospy.is_shutdown():
        numbers = input()
        rospy.loginfo(numbers)
        pub.publish(numbers)
        rate.sleep()
        
rospy.Subscriber('topic3', String, callback, queue_size=10)
          

try:
    start_my_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
    

