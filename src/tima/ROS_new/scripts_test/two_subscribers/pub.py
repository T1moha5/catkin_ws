#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('topic1', String, queue_size=10) 
pub1 = rospy.Publisher('topic2', String, queue_size=10) 
rate1 = rospy.Rate(1)  


def start_talker():
    msg = String()
    msg1 = String()
    while not rospy.is_shutdown():
        for1 = "%s" % rospy.get_time()
        for2 = "time "+"%s" % rospy.get_time()
        


        rospy.loginfo(for2)
        i = 0
        msg1.data = for2
        pub1.publish(msg1)



        rospy.loginfo(for1)
        msg.data = for1
        pub.publish(msg)

        rate1.sleep()


try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
