#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("%s", msg.data)

rospy.init_node('listener')
rospy.Subscriber('topic1', String, callback, queue_size=10)
rospy.spin()
