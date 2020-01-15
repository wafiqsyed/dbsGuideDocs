#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""**Module for defining patient directory.**

This module allows the user to define the patient data directory.

"""
import qt
import ctk

from .helper_functions import confirmationButton


class patientDirectoryWidget(ctk.ctkCollapsibleGroupBox):
    """
    **Constructor - Main patientDirectoryWidget object**

    Initializes the patient directory widget.

    :param parameters: A dictionary of several important directory paths.
    :type parameters: Dictionary

    """

    def __init__(self, parameters):
        pass

    #-------------------------------------------------------------------------#
    #                         PATIENT DIRECTORY SETUP                         #
    #-------------------------------------------------------------------------#
    def patient_directory_setup(self):
        """
        Confiugres patient directory widget's form. 

        """

        #
        #-------------------- Patient Directory Selection ---------------------
        #

        pass

    #-------------------------------------------------------------------------#
    #                   PATIENT DIRECTORY: SLOT DEFINITIONS                   #
    #-------------------------------------------------------------------------#
    def onRenameScansButtonGroupClicked(self, button):
        """
        **Slot for** ``Rename Scans`` **button.**

        :param button: The number that refers to the button that's clicked
        :type button: Macro - Integer

        """
        pass

    def onUsePreviousValuesClicked(self, button):
        """
        **Slot for** ``Use Previous Values`` **button.**

        :param button: The number that refers to the button that's clicked
        :type button: Macro - Integer

        """
        pass
