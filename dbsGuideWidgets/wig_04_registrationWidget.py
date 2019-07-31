#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

**Module for running registration of nifti files.**

This module runs FSL flirt registration.
"""
import qt
import ctk
import slicer
import os
import stat
import shutil

from .helper_functions import confirmationButton, warningBox
 
class registrationWidget(ctk.ctkCollapsibleGroupBox):
	"""
	**Constructor - Main registrationWidget object**

	Initializes the registration widget. 

	:param regLogic: Registration logic
	:param paramters: A dictionary of several important directory paths.
	:type parameters: Dictionary 

	"""
	def __init__(self, regLogic, parameters):
		
		pass
		
	#-------------------------------------------------------------------------#
	#                            REGISTRATION SETUP                           #
	#-------------------------------------------------------------------------#
	def linear_registration_setup(self):
		"""Class setup function for widget.
		
		This function sets up the registration widget.
	
		"""
		
		#
		#---------------------- Select Reference Volume -----------------------
		#
		
		pass
 
	#-------------------------------------------------------------------------#
	#                      REGISTRATION: SLOT DEFINITIONS                     #
	#-------------------------------------------------------------------------#             
	def onDeleteVolume(self):
		"""
		Slot for ``Delete Highlighted Volumes`` button
	
		"""
		pass
		
	def onReferenceVolCBox(self):
		"""
		Slot for ``Reference Volume:`` combo box
	
		"""           
		pass
			
	def onCTFrameVolCBox(self):      
		"""
		Slot for ``CT Frame Volume:`` combo box
	
		"""    
		pass
				
	def onRunRegistrationButton(self):
		"""
		Slot for ``Run Registration`` button
	
		"""  
		pass
			 
