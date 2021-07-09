##!/usr/bin/env python
import rospy
from Tutorials.msg
import Age
rospy.shubh_node('Pub')
pub=rospy.Publisher('Ages',Age,queue_size=10)
msg=Age()

while not rospy.is_shutdown():
     msg.age1=input("Input 1st Age:")
     msg.age2=input("Input 2nd Age:")
     pub.publish(msg)
