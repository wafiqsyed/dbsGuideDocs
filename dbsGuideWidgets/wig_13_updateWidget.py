#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" **Module for progress update**

This module informs the user of the latest action that has been performed by 
the graphic user interface by updating the status bar at the top of the user 
interface.

"""
import qt

class updateWidget(qt.QWidget):
    """
    **Main updateWidget object**
    
    Sets up the status bar with the desired text.
    
    :param text: Text to be shown as the most recent update. 
    :type text: String
    
    """	
    def __init__(self, text):
        pass
    
    def updateStatus(self, text):
        """
        **Updates the status bar with text**
        
        :param text: Text to be shown as the most recent update.
        :type text: String
        
        """
        pass