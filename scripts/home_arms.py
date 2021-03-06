#!/usr/bin/env python

"""
Script to return Baxter's arms to a "home" position
"""

# rospy - ROS Python API
import rospy

# baxter_interface - Baxter Python API
import baxter_interface

# initialize our ROS node, registering it with the Master
rospy.init_node('Home_Arms')

# create instances of baxter_interface's Limb class
limb_right = baxter_interface.Limb('right')
limb_left = baxter_interface.Limb('left')

# store the home position of the arms
home_right = {'right_s0': 0.08, 'right_s1': -1.00, 'right_w0': -0.67, 'right_w1': 1.03, 'right_w2': 0.50, 'right_e0': 1.18, 'right_e1': 1.94}
home_left = {'right_s0': -1.05, 'right_s1': -0.502, 'right_w0': 2.94, 'right_w1': -1.1, 'right_w2': 1.14, 'right_e0': 0.27, 'right_e1': 1.32}

# move both arms to home position
limb_right.move_to_joint_positions(home_right)
limb_left.move_to_joint_positions(home_left)
print ("hola mundo")

quit()



