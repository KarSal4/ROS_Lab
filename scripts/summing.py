#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int32



rospy.init_node('summing')
pub = rospy.Publisher('topic3', String, queue_size=1)

def callback(NumsInDegree):

      nums = NumsInDegree.data
      sp_nums = nums.split(',')
      
      a = int(sp_nums[0])
      b = int(sp_nums[1])
      c = int(sp_nums[2])
      
      result = str(a+b+c)
      
      rospy.loginfo(result)
      pub.publish(result)

             


def start_my_talker():
    
    	
    rospy.Subscriber('topic2', String, callback, queue_size=1)
    
    rospy.spin()
    
    

try:
    start_my_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
    
