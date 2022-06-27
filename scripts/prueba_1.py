#!/usr/bin/env python

import rospy

from smach import State,StateMachine

from time import sleep
from MoveControl import Baxter_Arms


import baxter_interface
import subprocess
import sense_p
import detector
import cv2  # openCV for image processing
from std_msgs.msg import String

class pose_1(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_y = {
            'letter': {
                      'left':  [0.0, -0.5, 0.0, 1.5, 0.0, -1.5,  0.0],
                      'right':  [0.0, -0.5,  0.0, 1.5, 0.0, -1.5,  0.0]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_y)
        sleep(5)
        return 'success'

class pose_2(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [-0.08, -1.0, -1.19, 1.94,  0.67, 1.03, -0.50],
                      'right':  [0.08, -1.0,  1.19, 1.94, -0.67, 1.03,  0.50]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(5)
        return 'success'
        
class pose_3(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_m = {
            'letter': {
                      'left':  [1.18, -0.71, 0.087, 1.3, 3.04, -0.97,  2.11],
                      'right':  [0.08, -1.0,  1.19, 1.94, -0.67, 1.03,  0.50]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_m)
        sleep(0.3)
        return 'success'

class pose_4(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_c = {
            'letter': {
                      'left':  [0.88, -0.89, -1.24, 1.59,  2.4, -1.11, 0.72],
                      'right':  [-0.30, 0.0017, 1.60, 1.55,  0.025, 0.95, 2.34]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_c)
        sleep(0.3)
        return 'success'

class pose_5(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.135, -0.10, -1.52, 1.44,  3.052, -1.06, -0.78],
                      'right':  [-0.30, 0.021, 1.66, 1.44,  -0.078, 1.063, 2.58]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_6(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_y = {
            'letter': {
                      'left':  [0.72, -0.71, 0.08, 1.27,  3.04, -1.02, -1.11],
                       'right':  [0.08, -1.0,  1.19, 1.94, -0.67, 1.03,  0.50]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_y)
        sleep(0.3)
        return 'success'
        
class pose_7(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.21, -0.77, 0.27, 1.21,  2.89, -1.17, 1.30],
                      'right':  [0.08, -1.0,  1.19, 1.94, -0.67, 1.03,  0.50]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_8(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_y = {
            'letter': {
                      'left':  [0.14, -0.82, 0.27, 1.32,  2.94, -1.1, 1.14],
                      'right':  [-1.22, -1.25,  1.69, 1.72, -0.40, 1.45,  1.97]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_y)
        sleep(0.3)
        return 'success'

class pose_9(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_m = {
            'letter': {
                      'left':  [0.22, -0.10, -1.53, 1.44,  3.056, -1.10, 0.75],
                      'right':  [-0.56, -0.77,  1.69, 1.64, 0.21, 1.19,  2.17]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_m)
        sleep(0.3)
        return 'success'

class pose_10(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.72, -0.71, 0.08, 1.27,  3.04, -1.02, -1.11],
                      'right':  [-1.67, -1.5,  1.15, 1.87, -0.12, 1.22,  0.50]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_11(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.21, -0.77, 0.27, 1.21,  2.89, -1.17, 1.30],
                      'right':  [-1.69, -1.078,  0.46, 1.40, -0.21, 1.28,  2.68]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_12(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.21, -0.77, 0.27, 1.21,  2.89, -1.17, 1.30],
                      'right':  [-1.43, -1.30,  0.68, 1.75, -0.18, 1.18,  3.05]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_13(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.21, -0.77, 0.27, 1.21,  2.89, -1.17, 1.30],
                      'right':  [-1.36, -0.902,  1.52, 1.83, -0.66, 1.30,  -0.65]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_14(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.letter_m = {
            'letter': {
                      'left':  [0.22, -0.10, -1.53, 1.44,  3.056, -1.10, 0.75],
                      'right':  [-0.56, -0.77,  1.69, 1.64, 0.21, 1.19,  2.17]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.letter_m)
        sleep(0.3)
        return 'success'

class pose_15(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [0.72, -0.71, 0.08, 1.27,  3.04, -1.02, -1.11],
                      'right':  [-1.67, -1.5,  1.15, 1.87, -0.12, 1.22,  0.50]
                       } }
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_16(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [1.18, -0.71, 0.087, 1.3, 3.04, -0.97,  2.11],
                      'right':  [-1.69, -1.078,  0.46, 1.40, -0.21, 1.28,  2.68]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_17(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [1.18, -0.71, 0.087, 1.3, 3.04, -0.97,  2.11],
                      'right':  [-1.43, -1.30,  0.68, 1.75, -0.18, 1.18,  3.05]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

class pose_18(State):
    def __init__(self):
        State.__init__(self, outcomes=['success'])

        self.zero = {
            'letter': {
                      'left':  [1.18, -0.71, 0.087, 1.3, 3.04, -0.97,  2.11],
                      'right':  [-1.36, -0.902,  1.52, 1.83, -0.66, 1.30,  -0.65]
                       } } 
                         #DoF Key [s0,s1,e0,e1,w0,w1,w2]

    def execute(self, userdata):
        barms.supervised_move(self.zero)
        sleep(0.3)
        return 'success'

def pose_pick_1():

    pose = {'left_e0': 0.070,
            'left_e1': 1.19,
            'left_s0': 1.22,
            'left_s1': -0.465,
            'left_w0': 3.03,
            'left_w1': -0.86,
            'left_w2': 2.11}

    barms.move_to_pose(pose,'left')

def pose_pick_2():

    pose = {'left_e0': 0.23,
            'left_e1': 1.22,
            'left_s0': 0.22,
            'left_s1': -0.46,
            'left_w0': 2.88,
            'left_w1':-0.87,
            'left_w2': 1.27}

    barms.move_to_pose(pose,'left')


def class_1():

    pose = {'left_e0': -1.52,
            'left_e1': 1.44,
            'left_s0': 0.135,
            'left_s1': -0.10,
            'left_w0': 3.052,
            'left_w1': -1.06,
            'left_w2': 0.607}

    barms.move_to_pose(pose,'left')

    pose = {'right_e0': 1.67,
	    'right_e1': 1.24, 
	    'right_s0':0.015,
	    'right_s1':0.001, 
	    'right_w0':-0.11, 
	    'right_w1':1.13, 
	    'right_w2': 2.65}

    barms.move_to_pose(pose,'right')
    barms.close_gripper('right')
    barms.open_gripper('left')

    pose = {'left_e0': -1.50,
            'left_e1': 1.40,
            'left_s0': 0.24,
            'left_s1': -0.0087,
            'left_w0': 3.054,
            'left_w1': -1.20,
            'left_w2': 0.6092}

    barms.move_to_pose(pose,'left')

def class_2():

    pose = {'right_e0': 1.63,
	    'right_e1': 1.57, 
	    'right_s0':-0.10,
    	    'right_s1':-0.017, 
	    'right_w0':-0.15, 
	    'right_w1':0.80, 
	    'right_w2': 2.61}

    barms.move_to_pose(pose,'right')
    barms.close_gripper('right')
    barms.open_gripper('left')

    pose = {'left_e0': -1.50,
            'left_e1': 1.40,
            'left_s0': 0.24,
            'left_s1': -0.0087,
            'left_w0': 3.054,
            'left_w1': -1.20,
            'left_w2': 0.6092}

    barms.move_to_pose(pose,'left')

def clasificacion_1(objeto_form,objeto_color):
    if objeto_form == 'Rectangulo':
	if objeto_color == 'Rojo':
	    class_1()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_9', pose_9(), transitions={'success':'pose_10'})
                StateMachine.add('pose_10', pose_10(), transitions={'success':'pose_11'})
                StateMachine.add('pose_11', pose_11(), transitions={'success':'success'})  
            sm.execute()
	    
	if objeto_color == 'Azul':
	    class_1()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_9', pose_9(), transitions={'success':'pose_10'})
                StateMachine.add('pose_10', pose_10(), transitions={'success':'pose_12'})
                StateMachine.add('pose_12', pose_12(), transitions={'success':'success'})  
            sm.execute()

    else:
	if objeto_color == 'Verde':
	    class_2()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_9', pose_9(), transitions={'success':'pose_10'})
                StateMachine.add('pose_10', pose_10(), transitions={'success':'pose_13'})
                StateMachine.add('pose_13', pose_13(), transitions={'success':'success'})  
            sm.execute()

    barms.open_gripper('right')
    
def clasificacion_2(objeto_form,objeto_color):
    if objeto_form == 'Rectangulo':
	if objeto_color == 'Rojo':
	    class_1()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_14', pose_14(), transitions={'success':'pose_15'})
                StateMachine.add('pose_15', pose_15(), transitions={'success':'pose_16'})
                StateMachine.add('pose_16', pose_16(), transitions={'success':'success'})  
            sm.execute()

	if objeto_color == 'Azul':
	    class_1()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_14', pose_14(), transitions={'success':'pose_15'})
                StateMachine.add('pose_15', pose_15(), transitions={'success':'pose_17'})
                StateMachine.add('pose_17', pose_17(), transitions={'success':'success'})  
            sm.execute()

    else:
	if objeto_color == 'Verde':
	    class_2()

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_14', pose_14(), transitions={'success':'pose_15'})
                StateMachine.add('pose_15', pose_15(), transitions={'success':'pose_18'})
                StateMachine.add('pose_18', pose_18(), transitions={'success':'success'})  
            sm.execute()

    barms.open_gripper('right')

if __name__ == '__main__':
    
    #cam = CameraController()
    #cam.open()
    #subprocess.call(["rosrun","image_view","image_view", "image:=/cameras/left_hand_camera/image"])

    barms = Baxter_Arms()
    rospy.on_shutdown(barms.clean_shutdown)

    sm = StateMachine(outcomes=['success'])
    with sm:
        StateMachine.add('pose_1', pose_1(), transitions={'success':'pose_2'})
    	StateMachine.add('pose_2', pose_2(), transitions={'success':'success'}) 
    sm.execute()
    #barms.open_gripper('left')
    #rospy.sleep(5)
    #barms.close_gripper('left')
'''
    barms.open_gripper('right')
    barms.open_gripper('left')

    while not rospy.is_shutdown():
    	find_obj = detector.image_to_initial_state()
    	rospy.sleep(0.5)
    	find_obj_1 = find_obj.find_obj()

   	if find_obj_1 == 'Yes':
	   
	    pose_pick_1()
	    barms.close_gripper('left')

	    sm = StateMachine(outcomes=['success'])
            with sm:
                
                StateMachine.add('pose_3', pose_3(), transitions={'success':'pose_4'})
                StateMachine.add('pose_4', pose_4(), transitions={'success':'pose_5'})
                StateMachine.add('pose_5', pose_5(), transitions={'success':'success'})  
            sm.execute()

            objeto_color = sense_p.image_to_initial_state()
            rospy.sleep(0.5)
            [objeto_color,objeto_form] = objeto_color.initial_color()
            clasificacion_1(objeto_form,objeto_color)
    	
	else:

            sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_6', pose_6(), transitions={'success':'pose_7'})
	        StateMachine.add('pose_7', pose_7(), transitions={'success':'success'}) 
            sm.execute()
	
	find_obj = detector.image_to_initial_state()
        rospy.sleep(0.5)
        find_obj_2 = find_obj.find_obj()

	if find_obj_2 == 'Yes':

	    pose_pick_2()
	    barms.close_gripper('left')

            sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_8', pose_8(), transitions={'success':'pose_4'})
                StateMachine.add('pose_4', pose_4(), transitions={'success':'pose_5'})
                StateMachine.add('pose_5', pose_5(), transitions={'success':'success'})  
            sm.execute()

            objeto_color = sense_p.image_to_initial_state()
            rospy.sleep(0.5)
            [objeto_color,objeto_form] = objeto_color.initial_color()
            clasificacion_2(objeto_form,objeto_color)
    
    	else:

	    sm = StateMachine(outcomes=['success'])
            with sm:
                StateMachine.add('pose_1', pose_1(), transitions={'success':'pose_2'})
	        StateMachine.add('pose_2', pose_2(), transitions={'success':'success'})
            sm.execute()
'''
 

