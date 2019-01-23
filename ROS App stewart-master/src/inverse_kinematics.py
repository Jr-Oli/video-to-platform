#!/usr/bin/env python
import rospy #library for ROS
import numpy as np #library for multidimensional arrays
from numpy import cos, sin
from std_msgs.msg import Float32MultiArray #msgs for multidimensional arrays
from geometry_msgs.msg import Twist #allows for expressing velocity with linear->movement along x,y, and z axes and angular->rotations around x,y, and z axes

h = 2.0 #Height of platform above base when legs are completely unextended

b = np.array([[-0.101, 0.8, 0.25],
              [0.101, 0.8, 0.25],
              [0.743, -0.313, 0.25],
              [0.642, -0.487, 0.25],
              [-0.643, -0.486, 0.25],
              [-0.744, -0.311, 0.25]])

p = np.array([[-0.642, 0.487, -0.05],
              [0.642, 0.487, -0.05],
              [0.743, 0.313, -0.05],
              [0.101, -0.8, -0.05],
              [-0.101, -0.8, -0.05],
              [-0.743, 0.313, -0.05]])

def twist_callback(twist_msg): #unsure if the following sets speeds, coordinates, or something else
                               #assumption based on usage in the for loop: it refers to coordinates
    x = twist_msg.linear.x #x axis (forwards or backwards)
    y = twist_msg.linear.y #y axis(left or right)
    z = twist_msg.linear.z #z axis(up or down)
    roll = twist_msg.angular.x #rotation along x axis
    pitch = twist_msg.angular.y #rotation along y axis
    yaw = twist_msg.angular.z #rotation along z axis 
    #note function np.dot(a,b) is for dot product between arrays a and b
    for i in range(n_pistons) 
        l = (np.array([x, y, z + h]) + 
             np.dot(rotation_matrix(roll, pitch, yaw), p[i]) -
             b[i])
        #l = np.array([x, y, z + h]) + np.dot(rotation_matrix(roll, pitch, yaw), p[i]) - b[i] #original code on a single line
        piston_lengths.data[i] = np.sqrt(l[0]**2 + l[1]**2 + l[2]**2)-h

    piston_pub.publish(piston_lengths)

def rotation_matrix(rho, theta, psi):
    return np.array([[cos(psi)*cos(theta), -sin(psi)*cos(rho)+cos(psi)*sin(theta)*sin(rho), sin(psi)*sin(rho)+cos(psi)*sin(theta)*cos(rho)],
                     [sin(psi)*cos(theta), cos(psi)*cos(rho)+sin(psi)*sin(theta)*sin(rho), -cos(psi)*sin(rho)+sin(psi)*sin(theta)*cos(rho)],
                     [-sin(theta), cos(theta)*sin(rho), cos(theta)*cos(psi)]])
  
#register client node with the master under the specified name 'ik'
rospy.init_node('ik')
#register twist_sub as a subscriber to the topic '/stewart/platform_twist' where the messages are of type Twist, 
#and when new messages are received, twist_callback is invoked with the message as the first argument
twist_sub = rospy.Subscriber('/stewart/platform_twist', Twist, twist_callback)
#declare piston_pub node is publishing to the 'stewart/piston_cmd' topic using the message type Float32MultiArray
#and allow a queue size of ten messages if the subscriber is not receiving the messages fast enough
piston_pub = rospy.Publisher('/stewart/piston_cmd', Float32MultiArray, queue_size=10)
piston_lengths = Float32MultiArray() #assumption: this creates a multidemensional array (multiarray)
piston_lengths.data = [0, 0, 0, 0, 0, 0] #initialize data in the multiarray to 0 for each piston
n_pistons = len(piston_lengths.data) #assumption: set the number of pistons (in this particular case 6)
length_components = [0, 0, 0] #initializing another array- yet i cannot find where this is used.
rospy.spin() #keep the node from exiting until the node has been shutdown
