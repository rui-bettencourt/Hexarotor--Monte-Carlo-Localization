import rospy
from nav_msgs.msg import Odometry

def callback(msg):
    print (msg.pose.pose)

rospy.init_node('check_odometry')
# print in console that the node is running
rospy.loginfo('started check_odometry node !')

odom_sub = rospy.Subscriber('/odom',Odometry,callback)

rospy.spin()