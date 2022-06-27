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
                       block0_reference_frame="world",
                       block1_pose=Pose(position=Point(x=0.38, y=0.9, z=0.813)),
                       block1_reference_frame="world",
                       block2_pose=Pose(position=Point(x=-0.258, y=1.2, z=0.815)),
                       block2_reference_frame="world",
                       block0_1_pose=Pose(position=Point(x=0.38, y=1.2, z=0.813)),
                       block0_1_reference_frame="world",
                       block1_1_pose=Pose(position=Point(x=-0.225, y=1.8, z=0.813)),
                       block1_1_reference_frame="world",
                       block2_1_pose=Pose(position=Point(x=0.355, y=1.5, z=0.815)),
                       block2_1_reference_frame="world",
                       block0_2_pose=Pose(position=Point(x=-0.225, y=1.5, z=0.813)),
                       block0_2_reference_frame="world",
                       block1_2_pose=Pose(position=Point(x=0.38, y=2.1, z=0.813)),
                       block1_2_reference_frame="world",
                       block0_3_pose=Pose(position=Point(x=0.38, y=1.8, z=0.815)),
                       block0_3_reference_frame="world"):
    # Get Models' Path
    model_path = rospkg.RosPack().get_path('baxter_sim_examples')+"/models/"
    
    # Load Block0 URDF
    block0_xml = ''
    with open (model_path + "block_red/model.urdf", "r") as block0_file:
        block0_xml=block0_file.read().replace('\n', '')

    # Load Block0_1 URDF
    block0_1_xml = ''
    with open (model_path + "block_red/model.urdf", "r") as block0_1_file:
        block0_1_xml=block0_1_file.read().replace('\n', '')

    # Load Block0_2 URDF
    block0_2_xml = ''
    with open (model_path + "block_red/model.urdf", "r") as block0_2_file:
        block0_2_xml=block0_2_file.read().replace('\n', '')

    # Load Block0_3 URDF
    block0_3_xml = ''
    with open (model_path + "block_red/model.urdf", "r") as block0_3_file:
        block0_3_xml=block0_3_file.read().replace('\n', '')

    # Load Block1 URDF
    block1_xml = ''
    with open (model_path + "block_blue/model.urdf", "r") as block1_file:
        block1_xml=block1_file.read().replace('\n', '')

    # Load Block1_1 URDF
    block1_1_xml = ''
    with open (model_path + "block_blue/model.urdf", "r") as block1_1_file:
        block1_1_xml=block1_1_file.read().replace('\n', '')

    # Load Block1_2 URDF
    block1_2_xml = ''
    with open (model_path + "block_blue/model.urdf", "r") as block1_2_file:
        block1_2_xml=block1_2_file.read().replace('\n', '')

    # Load sphere1 URDF
    block2_xml = ''
    with open (model_path + "ball/model.urdf", "r") as block2_file:
        block2_xml=block2_file.read().replace('\n', '')

    # Load sphere2 URDF
    block2_1_xml = ''
    with open (model_path + "ball/model.urdf", "r") as block2_1_file:
        block2_1_xml=block2_1_file.read().replace('\n', '')
    
    # Spawn Block0 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_red", block0_xml, "/",
                               block0_pose, block0_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block0_1 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_red_1", block0_1_xml, "/",
                               block0_1_pose, block0_1_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block0_2 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_red_2", block0_2_xml, "/",
                               block0_2_pose, block0_2_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block0_3 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_red_3", block0_3_xml, "/",
                               block0_3_pose, block0_3_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block1 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_blue", block1_xml, "/",
                               block1_pose, block1_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block1_1 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_blue_1", block1_1_xml, "/",
                               block1_1_pose, block1_1_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block1_2 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("block_blue_2", block1_2_xml, "/",
                               block1_2_pose, block1_2_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block2 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("ball", block2_xml, "/",
                               block2_pose, block2_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    # Spawn Block2_1 URDF
    rospy.wait_for_service('/gazebo/spawn_urdf_model')
    try:
        spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        resp_urdf = spawn_urdf("ball_1", block2_1_xml, "/",
                               block2_1_pose, block2_1_reference_frame)
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
        resp_delete = delete_model("block_red_1")
        resp_delete = delete_model("block_red_2")
        resp_delete = delete_model("block_red_3")
        resp_delete = delete_model("block_blue")
        resp_delete = delete_model("block_blue_1")
        resp_delete = delete_model("block_blue_2")
	resp_delete = delete_model("ball")
	resp_delete = delete_model("ball_1")
    except rospy.ServiceException, e:
        rospy.loginfo("Delete Model service call failed: {0}".format(e))

def main():
    rospy.init_node("Objetos")
    # Load Gazebo Models via Spawning Services
    # Note that the models reference is the /world frame
    # and the IK operates with respect to the /base frame
    load_gazebo_models()
    # Remove models from the scene on shutdown
    rospy.on_shutdown(delete_gazebo_models)

    # Wait for the All Clear from emulator startup
    rospy.wait_for_message("/robot/sim/started", Empty)

    while not rospy.is_shutdown():
        print("Objetos en escena...")
    #    #pnp.pick(block_poses[idx])
    #    print("\nPlacing...")
    #    #idx = (idx+1) % len(block_poses)
    #    #pnp.place(block_poses[idx])
    return 0

if __name__ == '__main__':
    sys.exit(main())
