#!/usr/bin/env python

"""
Baxter RSDK Inverse Kinematics mundo
"""
import argparse
import struct
import sys
import copy

import rospy
import rospkg

from gazebo_msgs.srv import (
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

import baxter_interface

def load_gazebo_models(block0_pose=Pose(position=Point(x=-0.225, y=0.895, z=0.813)),
                       block0_reference_frame="world"):
    # Get Models' Path
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/"
    
    # Load Block0 URDF
    block0_xml = ''
    with open (model_path + "block_red/model.urdf", "r") as block0_file:
        block0_xml=block0_file.read().replace('\n', '')
    
    # Spawn Block0 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_red", block0_xml, "/",
                               block0_pose, block0_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

def delete_gazebo_models():
    # This will be called on ROS Exit, deleting Gazebo models
    # Do not wait for the Gazebo Delete Model service, since
    # Gazebo should already be running. If the service is not
    # available since Gazebo has been killed, it is fine to error out
    try:
        delete_model = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        resp_delete = delete_model("block_red")
    except rospy.ServiceException, e:
        rospy.loginfo("Delete Model service call failed: {0}".format(e))

def main():
    rospy.init_node("mundo")
    # Load Gazebo Models via Spawning Services
    # Note that the models reference is the /world frame
    # and the IK operates with respect to the /base frame
    load_gazebo_models()
    # Remove models from the scene on shutdown
    rospy.on_shutdown(delete_gazebo_models)

    # Wait for the All Clear from emulator startup
    rospy.wait_for_message("/robot/sim/started", Empty)

    while not rospy.is_shutdown():
        print("Objeto rojo colocado...")
    #    #pnp.pick(block_poses[idx])
    #    print("\nPlacing...")
    #    #idx = (idx+1) % len(block_poses)
    #    #pnp.place(block_poses[idx])
    return 0

if __name__ == '__main__':
    sys.exit(main())
