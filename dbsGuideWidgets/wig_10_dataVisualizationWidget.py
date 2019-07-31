#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
**Module for manipulating what data models are shown.**

This module provides the user the capability of turning model data OFF/ON 
within the 3D view and slice view.

"""
import qt
import ctk
import slicer
import os
import json

from .helper_functions import confirmationButton, dataVisGroup

class dataVisualizationWidget(ctk.ctkCollapsibleGroupBox):
    """
    **Constructor - Main dataVisualizationWidget object**

    Initiates the ``Data View`` widget
    
    :param dataVisibility: Data visibility
    :param paramters: A dictionary of several important directory paths.
    :type parameters: Dictionary 

    """
    def __init__(self,dataVisibility, parameters):
        
        pass
    #-------------------------------------------------------------------------#
    #                             DATA VIEW SETUP                             #
    #-------------------------------------------------------------------------#
    def data_view_setup(self):
        """
        Sets up the ``Data View`` widget display configuration
    
        """
        
        #
        #-------------------------- Save Scene Button -------------------------
        #
        
        pass
    #-------------------------------------------------------------------------#
    #                       DATA VIEW: SLOT DEFINITIONS                       #
    #-------------------------------------------------------------------------#
    def rgbToHex(self, color):
        """
        Changes colour mode from RGB to HEX

        :param color: color in RGB
        :type color: tuple
        :return rgb2hex: the HEX equivalent of the given RGB
        :return type: String
        """
        pass
    
    def hex2rgb(self, hx):
        """
        Changes colour mode from HEX to RGB

        :param color: color in RGB
        :type color: string
        :return rgb: the RGB equivalent of the given HEX
        :return type: Tuple
        """
        pass
        
    def onPlannedLeadColorChange(self, color):
        """
        Slot for change in colour of ``Electrode Leads - Planned:``

        :param color: the new color that was selected
        """
        pass
    
    def onActualLeadColorChange(self, color):
        """
        Slot for change in colour of ``Electrode Leads - Actual:``

        :param color: the new color that was selected
        """
        pass
    
    def onPlannedContactColorChange(self, color):
        """
        Slot for change in colour of ``Electrode Contacts - Planned:``

        :param color: the new color that was selected
        """
        pass
    def onActualContactColorChange(self, color):
        """
        Slot for change in colour of ``Electrode Contacts - Actual:``

        :param color: the new color that was selected
        """
        pass
            
    def onPlannedMERTrackColorChange(self, color):
        """
        Slot for change in colour of ``MER Trajectory - Planned:``

        :param color: the new color that was selected
        """
        pass
    
    def onActualMERTrackColorChange(self, color):
        """
        Slot for change in colour of ``MER Trajectory - Actual:``

        :param color: the new color that was selected
        """
        pass
    
    def onPlannedMERActivityColorChange(self, color):
        """
        Slot for change in colour of ``MER Activity - Planned:``

        :param color: the new color that was selected
        """
        pass
    
    def onActualMERActivityColorChange(self, color):
        """
        Slot for change in colour of ``MER Activity - Actual:``

        :param color: the new color that was selected
        """
        pass
            
    def onSaveSceneButton(self):
        """

        Slot for ``Save Slicer Scene`` button.

        """
        ### Create Subject Hierchy
        pass
    def onPlannedLeadButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``Electrode Leads - Planned:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
                    
    def onActualLeadButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``Electrode Leads - Actual:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
    
    def onPlannedContactButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``Electrode Contacts - Planned:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
    
    def onActualContactButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``Electrode Contacts - Actual:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
                    
    def onPlannedMERTracksButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``MER Trajectory - Planned:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
                    
    def onActualMERTracksButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``MER Trajectory - Actual:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
                    
    def onPlannedMERSTNButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``MER Activity - Planned:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
                    
    def onActualMERSTNButtonGroupClicked(self, button):
        """
        Slot for button group belonging to ``MER Activity - Planned:``

        :param button: ID of the button selected
        :type button: Integer
        """
        pass
    
    
