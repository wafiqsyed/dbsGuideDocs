# -*- coding: utf-8 -*-
""" 
**Module for post-operative electrode localization.**

This module allows the user to define the location of the implanted electrodes
using post-operative images (CT or MRI).

"""
import qt
import ctk
import slicer
import os
import json
import numpy as np
import shutil
from dbsGuideWidgets.wig_12_notesWidget import notesWidget

from .helper_functions import confirmationButton, fiducialPoint, plot_models, rotation_matrix, vtkModelBuilder, model_color

class postopElectrodeWidget(ctk.ctkCollapsibleGroupBox):
    def __init__(self, parameters):
        """
        **Constructor - Main postopElectrodeWidget object**

        Initiates the ``Postoperative Info`` widget

        :param paramters: A dictionary of several important directory paths.
        :type parameters: Dictionary 

        """
        pass
    #-------------------------------------------------------------------------#
    #                         POSTOP ELECTRODE SETUP                          #
    #-------------------------------------------------------------------------#
    def postop_setup(self):
        """
        Sets up the ``Postoperative Info`` widget display configuration.
    
        """
        
        pass
    
    
    #-------------------------------------------------------------------------#
    #                POSTOPERATIVE ELECTRODE: SLOT DEFINITIONS                #
    #-------------------------------------------------------------------------#
    def onLeftActualElectrodeExpand(self, collapsed):
        """
        Slot for ``Left Side`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
            
    def onRightActualElectrodeExpand(self, collapsed):
        """
        Slot for ``Right Side`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
    
    def onNotesWidgetExpand(self, collapsed):
        """
        Slot for ``Postoperative Notes`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
            
    def onCrosshairTogglePostButton(self):

        """
        Slot for ``Turn On Crosshairs`` button
        """

        pass
    
    def onMouseMovedPost(self, observer, eventid):
        """
        Slot for when the the cross hair node has been relocated.
        :param observer: observer
        :param eventid: event ID
        """
        pass
    
    def onUpdateCrosshairPost(self):
        """
        Slot for ``Update Crosshairs`` button
        """
        pass
            
    def onFidVolumeElecBox(self):   
        """
        Slot for ``Fiducial Volume:`` combo box
        """   
        pass
                    
    def onElectrodeFidButton(self, button):
        """
        Slot for Electrode fiducial buttons

        :param button: button ID
        :type button: Integer
        """
        pass
                
    def onElecLBpointClick(self, enabled):
        """
        Slot for ``Elect Bot:`` point button clicked under ``Left Plan``

        :param enabled: status of button enabled
        :type enabled: Boolean
        """

        pass
            
    def onElecLTpointClick(self, enabled):
        """
        Slot for ``Elect Top:`` point button clicked under ``Left Plan``

        :param enabled: status of button enabled
        :type enabled: Boolean
        """
        pass
    
    def onElecRBpointClick(self, enabled):
        """
        Slot for ``Elect bot:`` point button clicked under ``Right Plan``

        :param enabled: status of button enabled
        :type enabled: Boolean
        """
        pass
            
    def onElecRTpointClick(self, enabled):
        """
        Slot for ``Elect Top:`` point button clicked under ``Right Plan``

        :param enabled: status of button enabled
        :type enabled: Boolean
        """
        pass
                       
    def onLeftActualElecButtonGroupClicked(self, button):
        """
        Slot for ``Plot Actual Lead:`` button group under ``Left Plan``

        :param button: id of the button clicked
        :type button: Integer
        """
        pass
    
    def onLeftActualMERTracksButtonGroupClicked(self, button):
        """
        Slot for ``Plot MER Tracks:`` button group under ``Left Plan``

        :param button: id of the button clicked
        :type button: Integer
        """
        pass
            
    def onRightActualElecButtonGroupClicked(self, button):
        """
        Slot for ``Plot Actual Lead:`` button group under ``Right Plan``

        :param button: id of the button clicked
        :type button: Integer
        """
        pass
    
    def onRightActualMERTracksButtonGroupClicked(self, button):
        """
        Slot for ``Plot MER Tracks:`` button group under ``Right Plan``

        :param button: id of the button clicked
        :type button: Integer
        """
        pass
                                
    def onActualElecPlotButton(self, button):
        """
        Slot for ``Update Activity`` button 

        :param button: id of the button clicked (left/right side)
        :type button: Integer
        """
        pass
    
            
    def onPostopMERConfirmButton(self, button):
        """
        Slot for ``Confirm Electrode`` button 

        :param button: id of the button clicked (right or left side)
        :type button: Integer
        """
        pass




