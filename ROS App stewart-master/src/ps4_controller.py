#!/usr/bin/env python

#get mathematical pi 3.1415
from math import pi 
#Python client library for ROS
import rospy        
#allows for reporting the state of a joysticks axes and buttons.
from sensor_msgs.msg import Joy 
#allows for expressing velocity with linear->movement along x,y, and z axes and angular->rotations around x,y, and z axes
from geometry_msgs.msg import Twist 

platform_twist = Twist()

def joy_callback(msg):
	# msg for linear.x moves it forward, -msg moves it backwards
	platform_twist.linear.x = -msg.axes[0]
	# assumption: msg for linear.y moves it right
	platform_twist.linear.y = msg.axes[1]
	# -msg for linear.x moves it backwards
	platform_twist.angular.x = -msg.axes[4]
	# assumption: -msg for linear.y moves it left
	platform_twist.angular.y = -msg.axes[3]
	# assumption: z axis is movement up and down,  positive is up and negative is down.
	#assumption: <1 and >0 conditions are too keep the arms from over extending
	if msg.buttons[7] and platform_twist.linear.z < 1:
		platform_twist.linear.z += 0.01
	elif msg.buttons[6] and platform_twist.linear.z > 0:
		platform_twist.linear.z -= 0.01

	#angular.z is used for rotation along the z axis
	#-msg is clockwise, msg is counter clockwise
	#assumption: < and > pi/2 conditions are too keep the arms from over extending
	if msg.buttons[5] and platform_twist.angular.z < pi/2:	
		platform_twist.angular.z += 0.01
	elif msg.buttons[4] and platform_twist.angular.z > -pi/2:
		platform_twist.angular.z -= 0.01	

	twist_pub.publish(platform_twist)

#register client node with the master under the specified name 'ps4_controller'
rospy.init_node('ps4_controller') 

#register '/joy' as a subscriber to the topic '/joy' where the messages are of type Joy, 
#and when new messages are received, joy_callback is invoked with the message as the first argument
joy_sub = rospy.Subscriber('/joy', Joy, joy_callback) 

#declare twist_pub node is publishing to the 'stewart/platform_twist' topic using the message type Twist
#and allow a queue size of ten messages if the subscriber is not receiving the messages fast enough
twist_pub = rospy.Publisher('stewart/platform_twist', Twist, queue_size=10) #

#keep the node from exiting until the node has been shutdown
rospy.spin()
