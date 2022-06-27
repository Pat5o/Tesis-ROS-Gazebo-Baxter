#!/usr/bin/env python
# coding=utf-8

from __future__ import print_function

import roslib

import sys
import rospy
import rospkg
import cv2  # openCV for image processing
import numpy as np

# messeges for subscribing and publishing
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError  # cv_bridge bridges the gap between ros msgs and openCV
from enum import Enum
#from scipy import ndimage  # import scipy library for center of mass calculation
from gazebo_msgs.srv import SpawnModel, DeleteModel
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

# ---------------------------------------IMAGE PROCESSING---------------------------------------------

class image_to_initial_state:
    received_image = [None]

    class Color(Enum):
        Red = 0
        Blue = 1
        Green = 2
        Yellow = 3

    ## @brief initialize the class artifacts
    def __init__(self):
        self.initial_state_pub = rospy.Publisher("initial_state_from_cameras", Image, queue_size=1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/cameras/head_camera/image", Image, self.callback)
	#rospy.Rate(10) # 10hz
        self.received_image = [None]
        # dictionary for colors' lower and upper HSV values
        self.ColorDict = {self.Color.Red: {'LowerHSV': (0, 52, 115), 'UpperHSV': (0, 255, 255)},
                          self.Color.Blue: {'LowerHSV': (110, 50, 50), 'UpperHSV': (130, 255, 255)},
                          self.Color.Green: {'LowerHSV': (50, 100, 50), 'UpperHSV': (70, 255, 255)},
                          self.Color.Yellow: {'LowerHSV': (20, 100, 90), 'UpperHSV': (50, 255, 255)}}
        self.Cubes_center_of_mass = [0, 0, 0, 0]

    ## @brief ROS saves images as ros messages, therefore we need to convert it
    ##        using CvBridge to cv2 format in order to do image processing
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print("Error! image converting to cv2 format failed")
        self.received_image[0] = cv_image

    ## @brief creates the masked image for each cube specific color
    ## @param Color an Enum of the used colors
    ## @return mask a masked image
    def image_processing(self, Color):
        original = self.received_image[0]
	#cv2.imshow('Original',original)
	#cv2.waitKey(0)
	self.resut = [0]
        # converts the image to HSV
        hsv = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
        # a different image processing routine for red due to Baxter's red body
        if Color == self.Color.Red:
            # splits the image to h, s, v where v is a gray scale image
            (h, s, v) = cv2.split(hsv)
            # turns all the pixels that greater than 600 in y axis to black (WORK FOR HEAD CAMERA!!!)
            v[700:][:] = 1
            # filters according to the HSV values
	    #cv2.imshow('Filtro',v)
	    #cv2.waitKey(0)
            # merges the three matrices back to hsv format
            hsv_no_red = cv2.merge((h, s, v))
            # filters according to the HSV values
	    #cv2.imshow('Filtro',hsv_no_red)
	    #cv2.waitKey(0)	
            mask = cv2.inRange(hsv_no_red, self.ColorDict.get(Color).get('LowerHSV'),
                               self.ColorDict.get(Color).get('UpperHSV'))
        else:
            # filters according to the HSV values
            mask = cv2.inRange(hsv, self.ColorDict.get(Color).get('LowerHSV'),
                               self.ColorDict.get(Color).get('UpperHSV'))
        # erode and dilate the mask in order to clean noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
	#cv2.imshow('Mascara',mask)
	#cv2.waitKey(100)
        return mask

    ## @brief calculates the center of mass of the cubes using a masked image of each cube
    def masked_image(self):
        red_mask = self.image_processing(self.Color.Red)
	self.contorno_red = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        blue_mask = self.image_processing(self.Color.Blue)
	self.contorno_blue = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        #cv2.imshow('Mascara',blue_mask)
	#cv2.waitKey()
	green_mask = self.image_processing(self.Color.Green)
	self.contorno_green = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        yellow_mask = self.image_processing(self.Color.Yellow)
        self.contorno_yellow = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	#cv2.imshow('Mascara',self.contorno_blue)
	#cv2.waitKey()

    ## @brief calculate the initial state from the center of mass and publish it
    def initial_color(self):
	Flag = 0	
	while Flag == 0:
            # deduct the initial state using the center of mass x values 
            self.masked_image()
            if len(self.contorno_red): 
	   	self.color = 'Rojo'
	    	#cont = self.contorno_red
	    	namefig = 'Cubo Rectangular'
	    	print ('Forma:',namefig)
	    	#return namefig,self.color

            elif len(self.contorno_blue): 
	    	self.color = 'Azul'
	    	#cont = self.contorno_blue
	    	namefig = 'Cubo Rectangular'
	    	print ('Forma:',namefig)
	    	#return namefig,self.color

            elif len(self.contorno_green): 
	    	self.color = 'Verde'
    	    	#cont = self.contorno_green
	    	namefig = 'Esfera'
	    	print ('Forma:',namefig)
	    	#return namefig,self.color
            # turn the list into a string in order to publish
            rate = rospy.Rate(1)
	    if self.color != 0:
	    	print ('Color:',self.color)
	    	Flag = 1
	    else:
	    	print ("COLOR NO DETECTADO")
	    	Flag = 0
	return self.color,namefig
        
	while not rospy.is_shutdown():
            rospy.loginfo(str_to_publish) # publish info in the terminal
            self.initial_state_pub.publish(str_to_publish)
            rate.sleep()

    def initial_form(self):
        red_mask = self.image_processing(self.Color.Red)
	self.contorno_red = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        blue_mask = self.image_processing(self.Color.Blue)
	self.contorno_blue = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	green_mask = self.image_processing(self.Color.Green)
	self.contorno_green = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
	
	namefig = 0
        if len(self.contorno_red): 
	    self.color = 'Rojo'
	    #cont = self.contorno_red
	    namefig = 'Rectangulo'
	    print ('Forma: ',namefig)
	    return namefig

        elif len(self.contorno_blue): 
	    self.color = 'Azul'
	    #cont = self.contorno_blue
	    namefig = 'Rectangulo'
	    print ('Forma: ',namefig)
	    return namefig

        elif len(self.contorno_green): 
	    self.color = 'Verde'
    	    #cont = self.contorno_green
	    namefig = 'Circulo'
	    print ('Forma: ',namefig)
	    return namefig

	#namefig = 0
	#print(cnts)
	#for c in cont:
	#    x, y, w, h = cv2.boundingRect(c)
	#    epsilon = 0.01*cv2.arcLength(c,True)
    	#    approx = cv2.approxPolyDP(c,epsilon,True)
	    #print(approx)
    	#    if len(approx) == 3:
        #    	namefig = 'Triangulo'
    	#    if len(approx) == 4:
        #    	aspect_ratio = float(w)/h
        #    	if aspect_ratio == 1:
        #    	    namefig = 'Cuadrado'
        #    	else:
        #    	    namefig = 'Rectangulo'
    	#    if len(approx) == 5:
        #    	namefig = 'Pentagono'
    	#    if len(approx) == 6:
        #    	namefig = 'Hexagono'
    	#    if len(approx) > 5:
        #        namefig = 'Circulo'
    	#
        #print (namefig)
	#print (len(approx))
	#return namefig

# -------------------------------------------- MAIN --------------------------------------------

def main(args):
    #load_gazebo_models()
    rospy.sleep(4) # sleep untill all models have been loaded 
    i2initialState = image_to_initial_state()
    # we use "disable_signals" because ROS and OpenCV  try to control the same signals,
    # so it's necessary to disable it on ROS to avoid conflicts.
    rospy.init_node("image_to_initial_state", disable_signals=True, anonymous=True)

    global objeto_color, objeto_form

    [objeto_color,objeto_form]=i2initialState.initial_color()

    #objeto_form=i2initialState.initial_form()
    
    __all__ = [ 'objeto_color', 'objeto_form' ]

if __name__ == '__main__':
    main(sys.argv)
