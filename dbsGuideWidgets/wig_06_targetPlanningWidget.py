#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
**Module for target planning.**

This module provides target planning capabilities for the surgeon.

"""
import qt
import ctk
import slicer
import numpy as np
import vtk
import os
import json

from .helper_functions import confirmationButton, planingFiducialPoint, norm_vec, mag_vec, frame_target, plot_models, warningBox

class targetPlanningWidget(ctk.ctkCollapsibleGroupBox):
	"""
	**Constructor - Main targetPlanningWidget object**

	Initiates the targetPlanningWidget

	:param paramters: A dictionary of several important directory paths.
	:type parameters: Dictionary 

	"""
	def __init__(self, parameters):
		
		pass
		
	#-------------------------------------------------------------------------#
	#                          TARGET PLANNING SETUP                          #
	#-------------------------------------------------------------------------#
	def target_planning_setup(self):
		"""
		Sets up the ``Target Planning`` widget.
	
		"""
		
		#
		#--------------------- Select Volume For Planning ---------------------
		#
		
		pass
		
		#
		#----------------------- Toggle Crosshair Button ----------------------
		#
		
		
	#-------------------------------------------------------------------------#
	#                    TARGET PLANNING: SLOT DEFINITIONS                    #
	#-------------------------------------------------------------------------#
	def onLeftTargetPlanningExpand(self, collapsed):
		"""
		Slot for when ``Left Plan`` collapsible button is expanded.

		:param collapsed: the state of the button (collapsed or not)
		:type collapsed: Boolean
		"""
		pass
	def onRightTargetPlanningExpand(self, collapsed):
		"""
		Slot for when ``Right Plan`` collapsible button is expanded.

		:param collapsed: the state of the button (collapsed or not)
		:type collapsed: Boolean
		"""
		pass
			
	def onPlanningVolumeCBox(self):
		"""
		Slot for ``Planning Volume`` combo box.
		"""
		pass
	
	def onProbeEyeCBox(self):
		"""
		Slot for ``Probe Eye Model`` combo box.
		"""
		pass
			
	def onProbeEyeClose(self):
		"""
		Slot for ``Close Probe's Eye`` button.
		"""
		pass
			
	def onFrameSliderValueChanged(self, newValue):
		"""
		Slot for ``Entry`` to ``Target`` slider

		:param newValue: the new value tha the slider is set to
		:type newValue: Integer

		"""
		pass
	
	def reslice_on_path(self, p0, pN, orientation=0): 
		"""
		Modifies the slice node to be resliced on a specific path

		:param p0: point 0
		:type p0: array - coordinates

		:param pN: point N
		:type pN: array - coordinates

		:param orientation: the orientation, default set to 0
		:type orientation: Integer
		"""
		pass
		
	def onCrosshairTogglePlanningButton(self):

		"""
		Slot for ``Turn On Crosshairs`` button
		"""
		pass
	
	def onMouseMovedPlanning(self, observer, eventid):
		"""
		Slot for when the the cross hair node has been relocated.
		
		:param observer: observer
		:param eventid: event ID
		"""
		pass
	
	def onUpdateCrosshairPlanning(self):
		"""
		Slot for ``Update Crosshairs`` button
		"""
		pass

	def onLeftEntryPointClick(self, enabled):
		"""
		Slot for ``Left Plan - Entry:`` point button clicked

		:param enabled: status of button enabled
		:type enabled: Boolean
		"""
		pass
			
	def onLeftTargetPointClick(self, enabled):
		"""
		Slot for ``Left Plan - Target:`` point button clicked

		:param enabled: status of button enabled
		:type enabled: Boolean
		"""
		pass
	
	def onRightEntryPointClick(self, enabled):
		"""
		Slot for ``Right Plan - Entry:`` point button clicked

		:param enabled: status of button enabled
		:type enabled: Boolean
		"""
		pass
	
	def onRightTargetPointClick(self, enabled):
		"""
		Slot for ``Right Plan - Target:`` point button clicked

		:param enabled: status of button enabled
		:type enabled: Boolean
		"""

		pass
	
	def onLeftEntryMoveButton(self):
		"""
		Slot for when the ``Left Plan - Entry button`` is moved.
		"""
		pass
	def onLeftTargetMoveButton(self):
		"""
		Slot for when the ``Left Plan - Target button`` is moved.
		"""
		pass
	
	def onRightEntryMoveButton(self):
		"""
		Slot for when the ``Right Plan - Entry button`` is moved.
		"""
		pass
			
	def onRightTargetMoveButton(self):
		"""
		Slot for when the ``Right Plan - Target button`` is moved.
		"""
		pass
	
	def onLeftButtonGroupClicked(self, button):
		"""
		Slot for ``Left Plan - Plot Planned Lead`` button group.

		:param button: id of the button clicked
		:type button: Integer
		"""

		pass
	
	def onLeftMERTracksButton(self, button):
		"""
		Slot for ``Left Plan - Plot MER Tracks`` button group.

		:param button: id of the button clicked
		:type button: Integer
		"""
		
		pass
			
	def onRightButtonGroupClicked(self, button):
		"""
		Slot for ``Right Plan - Plot Planned Lead`` button group.

		:param button: id of the button clicked
		:type button: Integer
		"""

		pass
	
	def onRightMERTracksButton(self, button):
		"""
		Slot for ``Right Plan - Plot MER Tracks`` button group.

		:param button: id of the button clicked
		:type button: Integer
		"""

		pass
	
	def onSelectAllLeftMERClicked(self, button):
		"""
		Slot for ``All`` button in ``Left Plan - MER Tracks``

		:param button: status of button being clicked
		:type button: Boolean
		"""

		pass
				
	def onSelectAllRightMERClicked(self, button):
		"""
		Slot for ``All`` button in ``Right Plan - MER Tracks``

		:param button: status of button being clicked
		:type button: Boolean
		"""
		pass
				
	def onLeftElecModelButtonGroup(self):
		"""
		Slot for electrode type in ``Left Plan - Electrode:``

		"""
		pass
				
	def onRightElecModelButtonGroup(self):
		"""
		Slot for electrode type in ``Right Plan - Electrode:``

		"""
		pass
				
	def onLeftEntryCoordConfirmButton(self):
		"""
		Slot for confirming left entry coordinates
		"""
		pass
		
	def onLeftTargetCoordConfirmButton(self):
		"""
		Slot for ``Confirm Left Plan`` button under ``Left Plan``
		"""
		pass
	
	def onRightEntryCoordConfirmButton(self):
		"""
		Slot for confirming right entry coordinates
		"""
		pass
		
	def onRightTargetCoordConfirmButton(self):
		"""
		Slot for ``Confirm Left Plan`` button under ``Left Plan``
		"""
		pass
	
	def onLeftEntryJumpButton(self):
		"""
		Slot for ``Jump to...`` button under ``Left Plan - Entry:``
		"""
		pass
	
	def onLeftTargetJumpButton(self):
		"""
		Slot for ``Jump to...`` button under ``Left Plan - Target:``
		"""
		pass
	
	def onRightEntryJumpButton(self):
		"""
		Slot for ``Jump to...`` button under ``Right Plan - Entry:``
		"""
		pass
	
	def onRightTargetJumpButton(self):
		"""
		Slot for ``Jump to...`` button under ``Right Plan - Target:``
		"""
		pass
	
	def get_model_point(self, node):
		"""
		Gets model point. 

		:param node: the node for which the model point is requested
		:return point_Ras: the model point
		"""
		pass
	
	def norm_vec(self, P1, P2):

		"""
		Creates a normal vector between two points.

		:param P1: Point 1
		:type P1: Array - coordinates

		:param P2: Point 2
		:type P2: Array - coordinates

		:return NormVec: The normal vector
		"""
		pass
	
	def onPlannedPreopConfirmButton(self, button):

		"""
		Slot for Planned Preop Confirm button

		:param button: ID of button
		:type button: Integer
		"""
		pass
