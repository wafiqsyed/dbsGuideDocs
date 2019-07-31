# -*- coding: utf-8 -*-
""" 
**Module for intraoperative microelectrode recordings.**

This module allows input of recordings depths of the target nucleus using 
intraoperaive microelectrode recordings.

"""
import qt
import ctk
import os
import json
import shutil
import numpy as np
import slicer

from dbsGuideWidgets.wig_12_notesWidget import notesWidget

from .helper_functions import confirmationButton, merSlider, vtkModelBuilder, rotation_matrix, model_color

class intraopMicroelectrodeWidget(ctk.ctkCollapsibleGroupBox):
    def __init__(self, parameters):
        """
        **Constructor - Main intraopMicroelectrodeWidget object**

        Initiates the ``Microelectrode Recordings`` widget

        :param paramters: A dictionary of several important directory paths.
        :type parameters: Dictionary 

        """
        pass
   
    #-------------------------------------------------------------------------#
    #                      INTRAOP MICROELECTRODE SETUP                       #
    #-------------------------------------------------------------------------#
    def intraop_microelectrode_setup(self):
        """
        Sets up the intraoperative microelectrode recordings widget display 
        configuration.
    
        """
        
        pass
        
        
    #-------------------------------------------------------------------------#
    #               MICROELECTRODE RECORDINGS: SLOT DEFINITIONS               #
    #-------------------------------------------------------------------------#
    def onLeftMicroelectrodeExpand(self, collapsed):
        """
        Slot for ``Left Plan`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
            
    def onRightMicroelectrodeExpand(self, collapsed):
        """
        Slot for ``Right Plan`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
    
    def onNotesWidgetExpand(self, collapsed):
        """
        Slot for ``Microelctrode Recordings Notes`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
            
    def onLeftTrajNoMERButton(self, button):
        """
        Slot for trajectory used under ``Left Plan``

        :param button: id of button clicked
        :type button: Integer
        """
        pass
    
    def onRightTrajNoMERButton(self, button):
        """
        Slot for trajectory used under ``Right Plan``
        
        :param button: id of button clicked
        :type button: Integer
        """
        pass
    
    def onLeftMERActivityPlotClicked(self, button):
        """
        Slot for selection of ``Plot MER Tracks`` under ``Left Plan``

        :param button: id of button clicked
        :type button: Integer
        """

        pass
            
    def onRightMERActivityPlotClicked(self, button):
        """
        Slot for selection of ``Plot MER Tracks`` under ``Right Plan``

        :param button: id of button clicked
        :type button: Integer
        """

        pass
    def onIntraopMERConfirmButton(self, button):
        """
        Slot for ``Confirm MER`` button.

        :param button: id of button clicked
        :type button: Integer
        """

        pass