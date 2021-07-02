import rospy
from Tutorials.msg import Age
def callback(data):
    a= data.age1 + data.age2
    print "The addition of the Ages is " + str(a)

rospy.shubh_node('Sub')
sub=rospy.Subscriber('Ages',Age, callback)
rospy.spin()
