#! /usr/bin/env python

import rospy
import argparse
import struct
import sys
import copy

import rospy
import rospkg

from gazebo_msgs.msg import ModelState

from gazebo_msgs.srv import (
    GetModelState,
    SetModelState,
    SpawnModel,
    DeleteModel,
)

from geometry_msgs.msg import (
    PoseStamped,
    Pose,
    Point,
    Quaternion,
)
from std_msgs.msg import (
    Header,
    Empty,
)

from control_msgs.msg import JointControllerState



class lector:
    senal = [0]
    def __init__(self):

    	sub= rospy.Subscriber("/robot/left_joint_position_controller/joints/left_s0_controller/state/process_value", JointControllerState, self.callback_process_value)
    	#rospy.sleep(0.05)

    def callback_process_value(self, msg):
    
        rospy.info('hola')
        

def main():
    #global senal, inter1, inter2
    rospy.init_node('reading_controller')
    while not rospy.is_shutdown():
    	ok = lector()
    	#ok.mover_objetos()
    #sub= rospy.Subscriber("/robot/laser1/scan", LaserScan, callback_laser)
    #rospy.sleep(0.1)
    #rospy.spin()
    return 0

if __name__ == '__main__':
  main()
