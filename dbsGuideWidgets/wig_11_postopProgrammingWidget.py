# -*- coding: utf-8 -*-
""" **Module for Postoperative Programming widget.**

This module is used to program the visualization postoperative. 
"""
import qt
import ctk

from .helper_functions import contactSettings, warningBox


class postopProgrammingWidget(ctk.ctkCollapsibleGroupBox):

    """
    **Constructor - Main dataVisualizationWidget object**

    Initiates the ``Data View`` widget

    :param dataVisibility: Data visibility
    :param paramters: A dictionary of several important directory paths.
    :type parameters: Dictionary 

    """

    def __init__(self, parameters):

        pass

    #-------------------------------------------------------------------------#
    #                        POSTOP PROGRAMMING SETUP                         #
    #-------------------------------------------------------------------------#
    def postop_programming_setup(self):
        """

        Sets up the postoperative planning widget.

        """
        pass

    def onLeftPostopProgrammingExpand(self, collapsed):
        """
        Slot for ``Left Electrode`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """

        pass

    def onRightPostopProgrammingExpand(self, collapsed):
        """
        Slot for ``Right Electrode`` collapsible button.

        :param collapsed: status of button - expanded/collapsed
        :type collapsed: Boolean
        """

        pass

    def onLeftElecModelButtonGroup(self):
        """
        Slot for button group belonging to ``Electrode:`` under ``Left Electrode``
        """

        pass

    def onLeftElecNumberButtonGroup(self, button):
        """
        Slot for button group belonging to ``Channel:`` under ``Left Electrode``
        """
        pass

    def onRightElecModelButtonGroup(self):
        """
        Slot for button group belonging to ``Electrode:`` under ``Right Electrode``
        """
        pass

    def onRightElecNumberButtonGroup(self, button):
        """
        Slot for button group belonging to ``Channel:`` under ``Right Electrode``
        """
        pass

    def onLeftShowElectrodeDiagramButton(self):
        """
        Slot for ``Electrode Diagram`` button belonging to ``Left Electrode``
        """
        pass

    def onRightShowElectrodeDiagramButton(self):
        """
        Slot for ``Electrode Diagram`` button belonging to ``Right Electrode``
        """
        pass
