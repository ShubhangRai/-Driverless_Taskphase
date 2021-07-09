import rospy
from Tutorials.msg import Candidate
rospy.shubh_node('input')
pub = rospy.Publisher('candidate',Candidate,queue_size= 10)
msg = Candidate()


while not rospy.is_shutdown():
    msg.name = input("Input Candidate's name (in the format 'name'): ")
    msg.age = input("Input Candidate's age: ")
    pub.publish(msg)
