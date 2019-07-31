# -*- coding: utf-8 -*-
""" 
**Module for intraoperative planning.**

This module provides manipulation of the pre-operative plan during the 
operation.

"""
import qt
import ctk
import os
import json
import numpy as np
import slicer
from dbsGuideWidgets.wig_12_notesWidget import notesWidget

from .helper_functions import confirmationButton, plot_models, rotation_matrix

class intraopPlanningWidget(ctk.ctkCollapsibleGroupBox):
    """
    **Constructor - Main intraopPlanningWidget object**

    Initializes the ``Intraoperative Planning`` widget.

    """
    def __init__(self, parameters):
        
        pass
     
    #-------------------------------------------------------------------------#
    #                         INTRAOP PLANNING SETUP                          #
    #-------------------------------------------------------------------------#
    def intraop_planning_setup(self):
        """
        Sets up the intraoperative planning widget.
    
        """
        pass
        
        #---------------------------------------------------------------------#
        #                         LEFT SIDE SUB-MENU                          #
        #---------------------------------------------------------------------#
        
        
        
    #-------------------------------------------------------------------------#
    #                INTRAOPERATIVE PLANNING: SLOT DEFINITIONS                #
    #-------------------------------------------------------------------------#
    def onLeftIntraopPlanningExpand(self, collapsed):
        """
        Slot for ``Left Plan`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
            
    def onRightIntraopPlanningExpand(self, collapsed):
        """
        Slot for ``Right Plan`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
    
    def onNotesWidgetExpand(self, collapsed):
        """
        Slot for ``Intraoperative Notes`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """
        pass
        
    def onLeftTrajUsedButtonGroup(self):
        """
        Slot for selection of ``Trajectory used`` under ``Left Plan``

        """
        pass
    
    def onRightTrajUsedButtonGroup(self):
        """
        Slot for selection of ``Trajectory used`` under ``Right Plan``

        """
        pass
                
    def onLeftButtonGroupIntraopClicked(self, button):
        """
        Slot for selection of ``Plot Planned Lead`` under ``Left Plan``

        :param button: id of button clicked
        :type button: Integer
        """
        pass
    
    def onLeftMERTracksIntraopButton(self, button):
        """
        Slot for selection of ``Plot MER Tracks`` under ``Left Plan``

        :param button: id of button clicked
        :type button: Integer
        """
        pass
            
    def onRightButtonGroupIntraopClicked(self, button):
        """
        Slot for selection of ``Plot Planned Lead`` under ``Right Plan``

        :param button: id of button clicked
        :type button: Integer
        """
        pass
    def onRightMERTracksIntraopButton(self, button):
        """
        Slot for selection of ``Plot MER Tracks`` under ``Right Plan``

        :param button: id of button clicked
        :type button: Integer
        """
        pass
            
    def onUpdatePlannedLeads(self, button):
        """
        Slot for ``Update Plan`` buttons

        :param button: id of button clicked -2 for left, -3 for right
        :type button: Integer
        """
        pass