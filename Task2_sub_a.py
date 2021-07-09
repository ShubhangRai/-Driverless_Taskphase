#!/usr/bin/env python
import rospy
from Tutorials.msg import Candidate
def callback(data):
    a = data.age
    if a >=30:
        print("Candidate can stand for the election")
    if a<30:
        print("Candidate cannot stand for the election")

rospy.shubh_node('Candidature Eligibility')
sub = rospy.Subscriber('candidate',Candidate,callback)
rospy.spin()
