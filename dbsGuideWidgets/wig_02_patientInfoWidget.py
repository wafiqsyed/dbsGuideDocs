#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" **Module for providing information about the patient.**

This module provides information about the date, the specific patient that is 
loaded, and the surgeon.

"""
import qt
import os
import ctk
import json

from .helper_functions import warningBox

class patientInfoWidget(ctk.ctkCollapsibleGroupBox):
	"""
	**Constructor - Main patientInfoWidget**

	Initializes the patient info widget. 

	:param parameters: A dictionary of several important directory paths.
	:type parameters: Dictionary
		
	"""
	def __init__(self, parameters):
		pass
		
	#-------------------------------------------------------------------------#
	#                            PATIENT INFO SETUP                           #
	#-------------------------------------------------------------------------#
	def patient_info_setup(self):
		"""
		**Patient info widget setup.**
	
		"""
		
		#
		#---------------------------- Patient Name ----------------------------
		#
		
		pass
		
		#
		#---------------------------- Surgery Date ----------------------------
		#
		
		
	#-------------------------------------------------------------------------#
	#                      PATIENT INFO: SLOT DEFINITIONS                     #
	#-------------------------------------------------------------------------#
	def selectedDateChanged(self):
		"""
		**Slot for date widget.**
		
		Updates the date widget and writes to file the date that has been 
		selected by the user.

		"""
		pass
		
	def onPatientNameChanged(self):
		pass
		
		
	def updateSurgeonName(self):
		"""
		**Slot for surgeon name widget.**
		
		Updates the surgeon name widget and writes to file the surgeon name 
		that has been selected by the user.
		
		"""
		pass
	
	
	def onImplantedSidesButtonGroupClicked(self, button):
		"""
		**Slot for** ``Implanted sides`` **button.**

		:param button: The number that refers to the button clicked
		:type button: Macro - Integer

		"""
		pass
	
	def onSurgicalTarget(self):
		pass
	
	def onSurgicalTargetOtherChanged(self):
		pass