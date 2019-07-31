#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" **Module for detecting the stereotactic frame.**

This module allows the user to define the frame fiducials on the CT image.

"""
import qt
import ctk
import slicer
import os
import shutil
import numpy as np
import vtk

from .helper_functions import confirmationButton, fiducialPoint, frameDetect

class frameDetectionWidget(ctk.ctkCollapsibleGroupBox):
	"""
	**Constructor - Main frameDetectionWidget object**

	Initializes the frame detection widget.
	
	:param parameters: A dictionary of several important directory paths.
	:type parameters: Dictionary

	"""

	def __init__(self, parameters):
		
		pass
		
	#-------------------------------------------------------------------------#
	#                            FRAME DETECT SETUP                           #
	#-------------------------------------------------------------------------#
	def frame_detect_setup(self):
		"""
		**Setup function for frameDetectionWidget**
		
		This function sets up the frame detection widget with all the appropriate
		forms.
	
		"""
		
		#
		#-------------- Select Frame Volume Containing fiducials --------------
		#
		
		pass
				
	#-------------------------------------------------------------------------#
	#                    FRAME DETECTION: SLOT DEFINITIONS                    #
	#-------------------------------------------------------------------------#
	def onShowFrameLegendButton(self):               
		"""
		**Slot for** ``Show Frame Fiducial Legend`` **button.**

		Displays frame fiducial legend. 

		"""
		pass
	
	def onWindowVolButton(self):
		pass
			
	def onRerunAutodetectButton(self):
		pass        
	def onFrameFidVolumeCBox(self, rerun=False):
		"""
		**Slot for** ``Fiducial Volume`` **box.**
		
		Displays the brain scan of the patient corresponding to the 
		fiducial volume selected. 

		The list of available volumes:
			- 3D T1 weighted (3D-T1W)
			- Fast spin echo T2 weighted coronal view (FSEcor_T2w)
			- Fast spin echo T2 weighted transverse view (FSEtra_T2W)
			- 3D electodes T1 weighted (3DELECTRODE_T1w)
			- Fast spin echo T2 weighted saggital view (FSEsag_T2w)
			- CT scan with frame (ctFrame)

		"""
		pass
				 
	def onCrosshairToggleFrameButton(self):
		"""
		**Slot for** ``Turn On Crosshairs`` **button.**

		Toggles crosshairs ON/OFF.

		"""
		pass
	
	def onP1pointClick(self, enabled):
		"""
		**Slot for Point 1 fiducial placement click.**

		Locks the point and records its coordinates.

		:param enabled: whether the point has been clicked onto the scan or not
		:type enabled: Boolean

		"""
		pass
			
	def onP2pointClick(self, enabled):
		pass          
				
	def onP3pointClick(self, enabled):
		pass
	
	def onP4pointClick(self, enabled):
		pass
	
	def onP5pointClick(self, enabled):
		pass
	
	def onP6pointClick(self, enabled):
		pass
	
	def onP7pointClick(self, enabled):
		pass
	
	def onP8pointClick(self, enabled):
		pass
	
	def onP9pointClick(self, enabled):
		pass
	
	def getFidCoords(self, fids):
		"""
		**Gets fiucial world coordinates.**
		
		Gets the world coordinates of the fiducial by looping through all 
		fiducials in provided markups list node. 

		:param fids: markups list node 
		:type fids: vtkMRMLMarkupsFiducialNode
		
		:return: fiducial coordinates
		:rtype: list array
		
		"""

		pass
		
	def onFrameFidButtonGroup(self, button):
		"""
		**Slot for buttons within the frame fiducial button group.**
		
		
		"""
		pass
	
	def calc_frame_fids_X(self, P1, P2, P3):
		"""
		**Calculates frame fiducial x-coordinates**

		:param P1: Point 1
		:type P1: float
		:param P2: Point 2
		:type P2: float
		:param P3: Point 3
		:type P3: float

		:return: arrays of the top and bottom fiducials
		:rtype: Numpy array
		"""
		pass

	def calc_frame_fids_Y(self, P1, P2, P3):
		"""
		**Calculates frame fiducial y-coordinates**

		:param P1: Point 1
		:type P1: float
		:param P2: Point 2
		:type P2: float
		:param P3: Point 3
		:type P3: float

		:return: arrays of the top and bottom fiducials
		:rtype: Numpy array
		"""
		pass

		
	
	def lineModel(self, scene, point1, point2, name, color):
		"""
		**Creates line model between two points**
		
		Creates a line model between two points and displays it.

		:param scene: MRML scene
		:type scene: Nodes
		:param point1: point 1 of the line
		:type point1: array
		:param point2: point 2 of the line
		:type point2: array
		:param name: name of the line model
		:type name: String
		:param color: color of the line model
		:type color: Tuple

		"""
		#Line mode source
		pass
		
	def onFrameFidConfirmButton(self):
		"""
		**Slot for** ``Confirm Frame Fiducials`` **button.**

		Saves frame fiducials as 3D Slicer nodes and writes to patient 
		directory as .vtk files. Finally, the frame .vtk files are displayed. 

		"""
		pass
