import rospy
from Tutorials.msg import Candidate

def callback(data):
    a = str(data.age)
    b = data.name
    print ("Candidate's name is " + b)
    print ("Candidate's age is " + a)
rospy.shubh_node('output')
sub = rospy.Subscriber('candidate',Candidate,callback)
rospy.spin()
