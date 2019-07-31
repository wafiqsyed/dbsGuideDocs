#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
**Module for placing anatomical fiducials.**

This module allows the user to define several anatomical fiducial points. These
points include `AC`, `PC`, and midline points.

"""
import qt
import ctk
import slicer
import os

from .helper_functions import confirmationButton, fiducialPoint

class anatomicalFiducialsWidget(ctk.ctkCollapsibleGroupBox):
    """
    **Constructor - Main anatomicalFiducialsWidget object**
    
    Initializes the Anatomical Fiducials widget.

    :param paramters: A dictionary of several important directory paths.
    :type parameters: Dictionary 
    """
    def __init__(self, parameters):
        
        pass
  
    #-------------------------------------------------------------------------#
    #                                ACPC SETUP                               #
    #-------------------------------------------------------------------------#
    def acpc_point_setup(self):
        """
        *Sets up the** ``Anatomical Fiducials`` **widget.**
    
        """
        
        #
        #------------------- Volume For Anatomical Fiducials ------------------
        #
        
        pass
                
    #-------------------------------------------------------------------------#
    #                  ANATOMICAL FIDUCIALS: SLOT DEFINITIONS                 #
    #-------------------------------------------------------------------------#
    def onFidVolumeCBox(self):
        """
        Slot for ``Fiducial Volume:`` combo box.
        """
        pass
            
    def onCrosshairToggleButton(self):
        """
        Slot for ``Turn On Crosshairs`` button.
        """
        pass
            
    def onMidlineFidButtonGroup(self, button):
        """
        Slots for buttons in the midline fiducial button group
        
        :param button: button that was clicked
        :type button: Integer
        """
        pass

    def onAddMidlineButton(self):
        """
        Slot for ``Add Midline`` button.
        """
        pass
    
    def onRemoveMidlineButton(self):
        
        """
        Slot for ``Remove Midline`` button.
        """

        pass
        
               
    def onFidConfirmButton(self):
        
        """
        Slot for ``Confirm Fiducials`` button.
        """

        pass
              
    def getFidCoords(self, fids):    
        """
        Gets the coordinates for fiducials.

        :param fids: fiducials to get coordinates for
        :type fids: array
        :return rasCoord: The coordinates
        """      
        pass
                
    def onACPointClick(self, enabled):
        """
        Slot for AC point clicked.

        :param enabled: if the  AC point is clicked
        :type enabled: boolean
        """
        pass
            
    def onPCPointClick(self, enabled):
        """
        Slot for PC point clicked.

        :param enabled: if the  PC point is clicked
        :type enabled: boolean
        """
        pass
            
    def onMid1PointClick(self, enabled):
        """
        Slot for Mid1 point clicked.

        :param enabled: if the  Mid1 point is clicked
        :type enabled: boolean
        """
        pass
    
    def onMid2PointClick(self, enabled):

        """
        Slot for Mid2 point clicked.

        :param enabled: if the  Mid2 point is clicked
        :type enabled: boolean
        """

        pass
    
    def onAcpcTransformButton(self):
        """
        Slot for ``Run ACPC Transform`` button
        """
        pass
        
    def onACPCTransformCBox(self):
        """
        Slot for ``Select Transform:`` combo box
        """
        pass