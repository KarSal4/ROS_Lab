#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Int32



rospy.init_node('polinominal')
pub = rospy.Publisher('topic2', String, queue_size=1)

def callback(numbers):
       
      nums = numbers.data
      sp_nums = nums.split(',')
      
      a = int(sp_nums[0])**3
      b = int(sp_nums[1])**2
      c = int(sp_nums[2])
      
      NumsInDegree = str(a) + ',' + str(b) + ',' + str(c)
      
      rospy.loginfo(NumsInDegree)
      pub.publish(NumsInDegree)

             


def start_my_talker():
    
    	
    rospy.Subscriber('topic1', String, callback, queue_size=1)
    
    rospy.spin()
    
    

try:
    start_my_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
    
