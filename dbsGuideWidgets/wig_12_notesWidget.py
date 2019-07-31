#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" **Module for notes box**

This module creates a notes box for the user interface and saves any typed 
notes to the patient data directory as a .txt file.

"""
import qt
import ctk
import os

class notesWidget(ctk.ctkCollapsibleGroupBox):
    """
    **Main NotesWidget object.**
    Initializes the notes box with the desired title of the notes in the notes 
    box. The notes box is closed/collapsed by default. If the user needs to 
    enter notes, the user can expand the notes box and start typing. 
    
    :param parameters: A dictionary of several important directory paths.`
    :type parameters: Dictionary
    :param plainText: Text to be included inside text box by defualt.
    :type planText: String
    :param title: Title of notes box collapsible button
    :type title: String
    :param extension: Text for file to be saved as.
    :type extension: String
    
    """
    def __init__(self, parameters, plainText, title, extension):
        pass
    
    #-------------------------------------------------------------------------#
    #                              NOTES SETUP                                #
    #-------------------------------------------------------------------------#
    def notes_setup(self):
        """
        **Sets up the notes widget**
        
        Connects the 'save button' with onSaveNotesButton.
        
        """
        pass
        
    def onSaveNotesButton(self, button):
        """
        **Slot for save button**
        
        Saves notes once ``Save`` button is clicked.
        
        :param button: The status of the button.
        :type button: Boolean
        
        """
        pass


