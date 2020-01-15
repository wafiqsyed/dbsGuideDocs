#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:40:00 2019

@author: ggilmore
"""
import qt
import ctk
import slicer
import vtk
import numpy as np
import os
import shutil
import csv
import json
import sys
import subprocess
import platform


def install_and_import(package):
    pass


class warningBox(qt.QMessageBox):
    """Class for wanring message box. 

    This class displays a wanring message box to the user. 

    Parameters
    ----------
    text: str
        Text to appear in the error box.
    """

    def __init__(self, text):
        pass


class confirmationButton:
    """Class for confirmation buttons.

    This class provides a generic confirmation button.
    img = nib.load('/media/veracrypt1/projects/stealthMRI/MRIdatabase/bids/derivatives/sub_study/sub-P057/scene/data/anat/sub-P057_ctFrame_coreg.nii.gz')

    Parameters
    ----------
    text: str
        Text to appear beside the button groups.
    customStyle: dict
        Dictionary containing a custom style sheet.

    """

    def __init__(self, text, customStyle=None):

        pass


class fiducialPoint:
    """Class for placing fiducial points.

    This class provides a generic template for fiducial point widgets.

    Parameters
    ----------
    text: str
        Text to appear beside the button groups.
    node: vtkMRMLMarkupsFiducialNode
        Slicer node used for the fiducial point
    visible: Bool
        Boolean for the visibility of the widget.
    customStyle: dict
        Dictionary containing a custom style sheet.

    """

    def __init__(self, text, node, visible, customStyle=None):

        # Label
        pass


class planingFiducialPoint:
    """Class for planning fiducial points.

    This class provides a generic template for planning fiducial point widgets.

    Parameters
    ----------
    text: str
        Text to appear above the button groups.
    node: vtkMRMLMarkupsFiducialNode
        Slicer node used for the fiducial point

    """

    def __init__(self, text, node):
        pass


class merSlider:
    """Class for MER slider widgets.

    This class provides a generic template used for defining MER recording 
    depths.

    Parameters
    ----------
    text: str
        Text to appear beside the button groups.

    """

    def __init__(self, text):

        # Label
        pass


class dataVisGroup:
    """Class for selecting what data to shown in the slice views.

    This class provides a generic template used for turning specific model
    data views ON/OFF in the 3D and slice views.

    Parameters
    ----------
    text: str
        Text to appear beside the button groups.
    sliceVis: bool
        Boolean to indicate if the button is checked.

    """

    def __init__(self, text, sliceVis):

        pass


class frameDetect:
    def __init__(self, node, z_coord, dataFolder, side_thres, ant_thres):

        pass

    def convert_ijk(self, point, node):
        pass

        # transformMatrix = vtk.vtkMatrix4x4()
        # slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, node.GetParentTransformNode(), transformMatrix)
        # # point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])

    def calc_frame_fids_X(self, P1, P2, P3):
        pass

    def calc_frame_fids_Y(self, P1, P2, P3):
        pass

    def lineModel(self, scene, point1, point2, name, color, outDir):
        pass

    def frame_detect(self, node, z_coord, side_thres, ant_thres):
        pass

    def calc_frame_fids_X(P1, P2, P3):
        pass

    def calc_frame_fids_Y(P1, P2, P3):
        pass


class vtkModelBuilder:
    def __init__(self, coords, TubeR, thick, filename, electrode=False, plane=[], trans=False, electrodeLen=0):

        pass

    def compute_transform(self, start, end, rotate):
        pass

    def transform_item(self, item, transform):
        pass

    def create_sphere(self, radius):
        pass

    def create_pipe(self, radius, thickness, height):
        pass

    def combine_polydata(self, source1, source2):
        pass

    def clean_mesh(self, source):
        pass

    def buildModel(self, coords, TubeR, thick, filename, electrode):
        pass

    def bsci_dir_bottomContact(self, coords, radius, thick, electrodeLen, filename):
        pass

    def seg_contact(self, coords, plane, TubeR, thick, trans, filename):
        pass


def norm_vec(P1, P2):
    pass


def mag_vec(P1, P2):
    pass


def frame_target(frame_center, target, side):
    pass


class model_color:
    def __init__(self, fileName, color, sliceVisible):

        pass

    def setAttributes(self):
        pass


def rotation_matrix(pitch, roll, yaw):
    pass


def plot_models(side, dataFolder, model_parameters):
    pass


class contactSettings:
    """Class for defining contact settings.

    This class provides a generic template for contact settings.

    Parameters
    ----------
    text: str
        Text to appear beside the button groups.
    visible: Bool
        Boolean for the visibility of the widget.
    customStyle: dict
        Dictionary containing a custom style sheet.

    """

    def __init__(self, text, visible):

        pass


class VTAModelBuilder:
    def __init__(self, elspec, stimulation, contactSettings, VATMethod, coords, options, vatsettings=None):
        pass

    def main(self):
        pass

    def dembek17_radius(self, U, Im, ethresh, pw, ethresh_pw):
        # This function radius of Volume of Activated Tissue for stimulation settings U and Ohm. See Maedler 2012 for details.
        # Clinical measurements of DBS electrode impedance typically range from
        # 500?1500 Ohm (Butson 2006).
        pass

    def kuncel(self, U):
        """
        This function radius of Volume of Activated Tissue for stimulation settings 
        U. See Kuncel 2008 for details. Clinical measurements of DBS electrode 
        impedance typically range from 500-1500 Ohm (Butson 2006).
        """
        pass

    def maedler12_eq3(self, U, Im):
        """
        This function radius of Volume of Activated Tissue for stimulation settings 
        U and Ohm. See Maedler 2012 for details. Clinical measurements of DBS 
        electrode impedance typically range from 500-1500 Ohm (Butson 2006).
        """
        pass

    def psphere(self, n):
        """
        Distributes n points "equally" about a unit sphere.

        Parameters
        ----------
            n: int
                The number of points to distribute.

        Returns
        -------
            x,y,z: 2D vector 
                Each is 1 x N vector
            r: float
                The smallest linear distance between two neighboring points. If the 
                function is run several times for the same n, r should not change 
                by more than the convergence criteria, which is +-0.01 on a unit 
                sphere.

        """
        # Since rand produces number from 0 to 1, subtract off -0.5 so that the points are centered about (0,0,0).
        pass

    def three_d_array(self, value, dim):
        """
        Create 3D-array
        :param dim: a tuple of dimensions - (x, y, z)
        :param value: value with which 3D-array is to be filled
        :return: 3D-array
        """

        pass
