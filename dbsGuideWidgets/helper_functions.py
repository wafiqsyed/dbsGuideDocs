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

from .variables import electrodeModels

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

class warningBox(qt.QMessageBox):
    """Class for wanring message box. 

    This class displays a wanring message box to the user. 

    Parameters
    ----------
    text: str
        Text to appear in the error box.
    """
    def __init__(self, text):
        super(warningBox,self).__init__()
        self.setIcon(qt.QMessageBox.Critical)
        self.setText(text)
        self.setWindowTitle("Error")
        self.exec_()
        
if platform.system() in {'Darwin','Windows'}:
    install_and_import('scipy')
else:
    try:
        import scipy
    except:
        warningBox("Please run pip_install('scipy') within the interactor first.")
        
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
        
        #### Confirmation Button
        self.confirmButton = qt.QToolButton()
        self.confirmButton.setText(text)
        self.confirmButton.enabled = True
        self.confirmButton.setStyleSheet("font-weight: normal;font-size: 12px;")
        
        self.confirmationButtonGB = qt.QGroupBox()
        self.confirmationButtonGB.setMaximumWidth(500)
        if customStyle == None:
            self.confirmationButtonGB.setStyleSheet("QGroupBox{margin-top:0px;\
                                                    padding-top:5px;\
                                                    margin-bottom:5px;\
                                                    padding-bottom:5px;\
                                                    margin-left:128px;\
                                                    margin-right:128px;\
                                                    border: 0px solid gray;}")
        else:
            self.confirmationButtonGB.setStyleSheet(customStyle)
        self.confirmationButtonQVBox = qt.QGridLayout(self.confirmationButtonGB)
        self.confirmationButtonQVBox.addWidget(self.confirmButton,0,0,qt.Qt.AlignHCenter)

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
        
        #### Label
        sText = qt.QLabel(text)
        sText.setFixedWidth(60)
        coordWigWidth = 240
            
        sText.setContentsMargins(0,0,0,0)
        sText.setAlignment(qt.Qt.AlignRight | qt.Qt.AlignVCenter)
        sText.setStyleSheet("font-weight: bold;font-size: 12px;")
        
        #### Slicer fiducial widget
        self.Point = slicer.qSlicerMarkupsPlaceWidget()
        self.Point.setMRMLScene(slicer.mrmlScene)
        if not node == None:
            self.Point.setCurrentNode(node)
        self.Point.placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
        self.Point.buttonsVisible = False
        self.Point.placeButton().show()
        self.Point.deleteButton().show()
        
        #### Unlock/Lock button
        self.lockButton = qt.QToolButton()
        self.lockButton.setText("Unlock/Lock")
        self.lockButton.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:3px;margin-left:3px;")
        self.lockButton.setFixedWidth(90)
        self.lockButton.enabled = True
                
        #### Coordinate widget
        self.coords = ctk.ctkCoordinatesWidget()
        self.coords.minimum = -1000
        self.coords.setStyleSheet("font-weight: normal;font-size: 12px")
        self.coords.setFixedWidth(coordWigWidth)
        
        #### Coordinate row layout
        self.pointWig = qt.QWidget()
        self.pointWig.setVisible(visible)
        self.pointWig.setContentsMargins(20,0,0,0)
        
        self.pointHBox = qt.QHBoxLayout(self.pointWig)
        self.pointHBox.addWidget(sText)
        self.pointHBox.addSpacing(10)
        self.pointHBox.addWidget(self.Point)
        self.pointHBox.addWidget(self.lockButton)
        self.pointHBox.addWidget(self.coords)
        self.pointHBox.addStretch()
        self.pointHBox.setSpacing(0)
        self.pointHBox.setMargin(0)

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
        #### Label
        self.coordText = qt.QLabel(text + ':')
        self.coordText.setMaximumWidth(480)
        self.coordText.setContentsMargins(0,10,0,10)
        self.coordText.setStyleSheet("font-weight: normal;font-size: 12px;text-decoration: underline")
        
        #### Slicer fiducial widget
        self.Point = slicer.qSlicerMarkupsPlaceWidget()
        self.Point.setMRMLScene(slicer.mrmlScene)
        self.Point.setCurrentNode(node)
        self.Point.placeMultipleMarkups = slicer.qSlicerMarkupsPlaceWidget.ForcePlaceSingleMarkup
        self.Point.buttonsVisible = False
        self.Point.placeButton().show()
        self.Point.deleteButton().show()
        
        #### Unlock/Lock button
        self.lockButton = qt.QToolButton()
        self.lockButton.setText("Unlock/Lock")
        self.lockButton.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:0px;margin-left:3px")
        self.lockButton.setFixedWidth(100)
        self.lockButton.enabled = True
        
        #### Confirm Coords button
        self.coordConfirmButton = qt.QToolButton()
        self.coordConfirmButton.setFixedWidth(100)
        self.coordConfirmButton.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:0px;margin-left:3px")
        self.coordConfirmButton.setText('Set ' + text)
        self.coordConfirmButton.enabled = True
        
        #### Jump To button
        self.jumpButton = qt.QToolButton()
        self.jumpButton.setFixedWidth(100)
        self.jumpButton.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:0px;margin-left:3px")
        self.jumpButton.setText("Jump to...")
        self.jumpButton.enabled = True
        
        #### Button Vertical Layout
        self.pointButtonWig = qt.QWidget()
        self.pointButtonWig.setMaximumWidth(110)
        self.pointButtonVBox = qt.QGridLayout(self.pointButtonWig)
        self.pointButtonVBox.addWidget(self.lockButton,0,0,qt.Qt.AlignHCenter)
        self.pointButtonVBox.addWidget(self.coordConfirmButton,1,0,qt.Qt.AlignHCenter)
        self.pointButtonVBox.addWidget(self.jumpButton,2,0,qt.Qt.AlignHCenter)
        
        #### Coordinate widget
        self.coords = ctk.ctkCoordinatesWidget()
        self.coords.setMaximumWidth(240)
        self.coords.minimum = -1000
        self.coords.setStyleSheet("font-weight: normal;font-size: 12px;")
        
        #### Coordinate Widget Header
        self.tableCaption = ["X", "Y", "Z"]
        self.captionFrameWig = qt.QGroupBox()
        self.captionFrameWig.setContentsMargins(0,0,0,0)
        self.captionFrameWig.setMaximumWidth(240)
        self.captionFrameWig.setStyleSheet("QGroupBox{margin-top:9px;padding-top:0px;\
                                            margin-bottom:0px;\
                                            margin-left:0px;\
                                            border: 0px solid gray;\
                                            border-top: 1px solid black;\
                                            border-radius: 0px;}")
        self.captionFrameBL = qt.QHBoxLayout(self.captionFrameWig)
        self.captionFrameBL.setContentsMargins(0,0,0,0)
        self.captionFrameBL.setSpacing(0)
            
        for i in (range(len(self.tableCaption))):
            a = qt.QLabel(self.tableCaption[i])
            a.setMinimumWidth(80)
            a.setMaximumWidth(80)
            a.setStyleSheet("qproperty-alignment: AlignCenter;font-weight: bold;font-size: 12px;")
            self.captionFrameBL.addWidget(a)
          
        self.captionFrameBL.addStretch()
        
        self.horizontalBotLine = qt.QFrame()
        self.horizontalBotLine.setFrameShape(qt.QFrame().HLine)
        self.horizontalBotLine.setLineWidth(1)
        self.horizontalBotLine.setContentsMargins(0,0,0,0)
        self.horizontalBotLine.setStyleSheet("margin-bottom:-10px;")
        self.horizontalBotLine.setMaximumWidth(240)
        
        self.captionUnderlineWig = qt.QWidget()
        self.captionUnderlineWig.setMaximumWidth(240)
        self.captionUnderlineQVBox = qt.QVBoxLayout(self.captionUnderlineWig)
        self.captionUnderlineQVBox.addWidget(self.captionFrameWig)
        self.captionUnderlineQVBox.addWidget(self.horizontalBotLine)
        self.captionUnderlineQVBox.addWidget(self.coords)
        self.captionUnderlineQVBox.setMargin(0)
        self.captionUnderlineQVBox.setSpacing(0)
        self.captionUnderlineQVBox.addStretch()
        
        #### Coordinate text row
        self.pointTextHBox = qt.QHBoxLayout()
        self.pointTextHBox.setContentsMargins(20,0,0,0)
        self.pointTextHBox.addWidget(self.coordText)
        
        #### Coordinate Widget Layout
        self.pointHBox = qt.QHBoxLayout()
        self.pointHBox.setContentsMargins(40,0,0,10)
        self.pointHBox.addWidget(self.Point)
        self.pointHBox.addWidget(self.pointButtonWig)
        self.pointHBox.addWidget(self.captionUnderlineWig)
        self.pointHBox.addStretch()

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
        
        #### Label
        label = qt.QLabel(text)
        label.setContentsMargins(0,0,0,0)
        label.setFixedWidth(75)
        label.setStyleSheet("font-weight: bold;font-size: 12px;")
        
        #### Slider Widget
        self.slider = ctk.ctkRangeWidget()
        self.slider.setStyleSheet("font-weight: normal;font-size: 12px;")
        self.slider.minimum = -10
        self.slider.maximum = 10
        self.slider.minimumValue = -1
        self.slider.maximumValue = 1
        self.slider.singleStep = 0.5
        self.slider.setFixedWidth(285)
        
        #### No MER Activity Button
        self.noActivityButton = qt.QRadioButton("No activity")
        self.noActivityButton.checked = False
        self.noActivityButton.setFixedWidth(85)
        self.noActivityButton.setStyleSheet("font-weight: normal;font-size: 12px;")
        
        #### Layout
        self.merHBox = qt.QHBoxLayout()
        self.merHBox.setContentsMargins(20,0,0,0)
        self.merHBox.addWidget(label)
        self.merHBox.addWidget(self.slider)
        self.merHBox.addWidget(self.noActivityButton)

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
        
        self.buttonGroup = qt.QButtonGroup()
        self.buttonGroup.setExclusive(False)
                
        #### Label
        label = qt.QLabel(text)
        label.setFixedWidth(70)
        label.setStyleSheet("font-weight: normal;font-size: 12px;")
        
        #### Left Side Data
        self.left = qt.QCheckBox('Left')
        self.left.checked = True
        self.left.setFixedWidth(55)
        self.left.setStyleSheet("qproperty-alignment: AlignCenter;font-weight: normal;font-size: 12px;")
        self.buttonGroup.addButton(self.left)
        
        #### Right Side Data
        self.right = qt.QCheckBox('Right')
        self.right.checked = True
        self.right.setFixedWidth(55)
        self.right.setStyleSheet("qproperty-alignment: AlignCenter;font-weight: normal;font-size: 12px;")
        self.buttonGroup.addButton(self.right)
        
        #### Slice View Data
        self.slice = qt.QCheckBox('2D Slice Visibility')
        self.slice.checked = sliceVis
        self.slice.setFixedWidth(130)
        self.slice.setStyleSheet("qproperty-alignment: AlignCenter;font-weight: normal;font-size: 12px;")
        self.buttonGroup.addButton(self.slice)
        
        #### Color selector
        self.colorSelector = ctk.ctkColorPickerButton()
        self.colorSelector.displayColorName = False
        
        #### Layout
        self.HBox = qt.QHBoxLayout()
        self.HBox.setContentsMargins(40,0,0,0)
        self.HBox.addWidget(label)
        self.HBox.addWidget(self.left)
        self.HBox.addWidget(self.right)
        self.HBox.addWidget(self.slice)
        self.HBox.addWidget(self.colorSelector)
        self.HBox.addStretch()

class frameDetect:
    def __init__(self, node, z_coord, dataFolder, side_thres, ant_thres):
        
        self.dataFolder = dataFolder
        self.voxelArray = slicer.util.arrayFromVolume(node)
        self.frame_detect(node, z_coord, side_thres, ant_thres)
        
    def convert_ijk(self, point, node):
        ijkToRas = vtk.vtkMatrix4x4()
        node.GetIJKToRASMatrix(ijkToRas)
        position_Ijk = point+[1]
        # point_VolumeRas = [0, 0, 0, 1]
        point_Ras = ijkToRas.MultiplyPoint(position_Ijk)
        
        # transformMatrix = vtk.vtkMatrix4x4()
        # slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(None, node.GetParentTransformNode(), transformMatrix)
        # # point_Ras = transformVolumeRasToRas.TransformPoint(point_VolumeRas[0:3])
        
        return point_Ras
    
    def calc_frame_fids_X(self, P1,P2,P3):
        aTop = np.array([P1[0], P1[1], P1[2]-(P1[1] - P2[1])])   
        aBot = np.array([aTop[0], aTop[1], aTop[2] - 120])
        cTop = np.array([P3[0], P3[1], P3[2]-(P1[1] - P2[1])])   
        cBot = np.array([cTop[0], cTop[1], cTop[2] - 120])

        return aTop, aBot, cTop, cBot

    def calc_frame_fids_Y(self, P1, P2, P3):
        aTop = np.array([P3[0], P3[1], P3[2]+(P3[0] - P2[0])])   
        aBot = np.array([aTop[0], aTop[1], aTop[2] - 120])
        cTop = np.array([P1[0], P1[1], P1[2] + (P3[0] - P2[0])])   
        cBot = np.array([cTop[0], cTop[1], cTop[2] - 120])

        return aTop, aBot, cTop, cBot

    def lineModel(self, scene, point1, point2, name, color, outDir):
        #Line mode source
        line = vtk.vtkLineSource()
        line.SetPoint1(point1)
        line.SetPoint2(point2)

        # Create model node
        lineModel = slicer.vtkMRMLModelNode()
        lineModel.SetScene(scene)
        lineModel.SetName(name)
        lineModel.SetAndObservePolyData(line.GetOutput())
        
        # Create display node
        lineModelDisplay = slicer.vtkMRMLModelDisplayNode()
        lineModelDisplay.SetColor(color)
        lineModelDisplay.SetLineWidth(2)
        lineModelDisplay.SetScene(scene)
        scene.AddNode(lineModelDisplay)
        lineModel.SetAndObserveDisplayNodeID(lineModelDisplay.GetID())

        #Add to scene
        lineModelDisplay.SetInputPolyDataConnection(line.GetOutputPort())
        scene.AddNode(lineModel)
        
        fileN = os.path.join(outDir, name + '.vtk')
        slicer.util.saveNode(lineModel, fileN)
            
    def frame_detect(self, node, z_coord, side_thres, ant_thres):
        # Left side
        voxel_slice = self.voxelArray[z_coord,:,:]
        indices = np.where(voxel_slice>500)
        threshold = int(max(indices[1])-side_thres)
        voxel_slice = self.voxelArray[z_coord,:, threshold:]
        indices = np.where(voxel_slice>500)
        numberOfVoxels = len(indices[0])
        i = []
        j = []
        k = []
        tempj = []
        tempk = []
        lastj = indices[0][0]
        for pointIndex in range(numberOfVoxels):
            if pointIndex == (numberOfVoxels-1):
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))
            elif lastj - indices[0][pointIndex] > 0:
                continue
            elif indices[0][pointIndex] - lastj < 8:
                tempj.append(indices[0][pointIndex])
                tempk.append(indices[1][pointIndex]+(threshold))
                lastj = indices[0][pointIndex]
            else:
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))
                tempj = []
                tempk = []
                lastj = indices[0][pointIndex]

        num_poles = len(k)
        position_left = []
        for ipole in range(num_poles):
            position_left.append(self.convert_ijk([k[ipole],j[ipole],i[ipole]], node))
    
        # Anterior side
        voxel_slice = self.voxelArray[z_coord, :, :]
        indices = np.where(voxel_slice>500)
        threshold = int(max(indices[0])-ant_thres)
        voxel_slice = self.voxelArray[z_coord,threshold:,:]
        indices = np.where(voxel_slice>500)
        numberOfVoxels = len(indices[0])
        i = []
        j = []
        k = []
        tempj = []
        tempk = []
        last = indices[1][0]
        for pointIndex in range(numberOfVoxels):
            if pointIndex == (numberOfVoxels-1):
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))
            elif last - indices[1][pointIndex] > 0:
                continue
            elif indices[1][pointIndex] - last < 6:
                tempj.append(indices[0][pointIndex]+(threshold))
                tempk.append(indices[1][pointIndex])
                last = indices[1][pointIndex]
            else:
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))
                tempj = []
                tempk = []
                last = indices[1][pointIndex]

        num_poles = len(k)
        position_ant = []
        for ipole in range(num_poles):
            position_ant.append(self.convert_ijk([k[ipole],j[ipole],i[ipole]], node))
    
        # Right Side
        voxel_slice = self.voxelArray[z_coord,:,:]
        indices = np.where(voxel_slice>500)
        threshold = int(min(indices[1])+side_thres)
        voxel_slice = self.voxelArray[z_coord,:,:threshold]
        indices = np.where(voxel_slice>500)
        numberOfVoxels = len(indices[0])
        i = []
        j = []
        k = []
        tempj = []
        tempk = []
        last = indices[0][0]
        for pointIndex in range(numberOfVoxels):
            if pointIndex == (numberOfVoxels-1):
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))   
            elif last - indices[0][pointIndex] > 0:
                continue
            elif indices[0][pointIndex] - last < 8:
                tempj.append(indices[0][pointIndex])
                tempk.append(indices[1][pointIndex])
                last = indices[0][pointIndex]
            else:
                i.append(z_coord)
                j.append(np.median(tempj))
                k.append(np.median(tempk))
                tempj = []
                tempk = []
                last = indices[0][pointIndex]
        
        num_poles = len(k)
        position_right = []
        for ipole in range(num_poles):
            position_right.append(self.convert_ijk([k[ipole],j[ipole],i[ipole]], node))
    
        self.combined_ras = np.concatenate((position_left, position_ant[::-1], position_right[::-1]), axis=0)

        models = slicer.util.getNodesByClass('vtkMRMLMarkupsFiducialNode')
        for i in models:
            if i.GetName() == 'frame_fids':
                slicer.mrmlScene.RemoveNode(slicer.util.getNode(i.GetName()))

        models = slicer.util.getNodesByClass('vtkMRMLModelNode')
        currentModelNames = {'Frame_Pole_A1', 'Frame_Pole_B1', 'Frame_Pole_C1',
                              'Frame_Pole_A2', 'Frame_Pole_B2', 'Frame_Pole_C2',
                              'Frame_Pole_A3', 'Frame_Pole_B3', 'Frame_Pole_C3'
        }
        for imodel in models:
            if imodel.GetName() in currentModelNames:
                slicer.mrmlScene.RemoveNode(slicer.util.getNode(imodel.GetID()))
                
        fidNodeFrame = slicer.vtkMRMLMarkupsFiducialNode()
        fidNodeFrame.SetName('frame_fids')
        slicer.mrmlScene.AddNode(fidNodeFrame)
        fidNodeFrame.GetDisplayNode().SetGlyphScale(0.8)
        fidNodeFrame.GetDisplayNode().SetTextScale(2.5)
        for ipoint in range(len(self.combined_ras)):
            n = fidNodeFrame.AddFiducial(self.combined_ras[ipoint][0], self.combined_ras[ipoint][1], self.combined_ras[ipoint][2])
            fidNodeFrame.SetNthFiducialLabel(n, "P" + str(ipoint+1))

        slicer.util.saveNode(fidNodeFrame, os.path.join(self.dataFolder, 'markups','frame_fids.fcsv'))
        
        [aT1, aB1, cT1, cB1] = self.calc_frame_fids_X(self.combined_ras[0], self.combined_ras[1],self.combined_ras[2])
        [aT2, aB2, cT2, cB2] = self.calc_frame_fids_Y(self.combined_ras[3], self.combined_ras[4],self.combined_ras[5])
        [aT3, aB3, cT3, cB3] = self.calc_frame_fids_X(self.combined_ras[8], self.combined_ras[7],self.combined_ras[6])
        
        self.frame_center = [(cT3[0] + aT1[0])/2, (cT3[1] + aT1[1])/2, (aT1[2] + cB3[2])/2]
        
        outDir = os.path.join(self.dataFolder, 'Frame_poles')
        if not os.path.exists(outDir):
            os.mkdir(outDir)
            
        self.lineModel(slicer.mrmlScene, aB1, aT1, 'Frame_Pole_A1', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB1, aT1, 'Frame_Pole_B1', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB1, cT1, 'Frame_Pole_C1', (1,0,0), outDir)

        self.lineModel(slicer.mrmlScene, aB2, aT2, 'Frame_Pole_A2', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB2, aT2, 'Frame_Pole_B2', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB2, cT2, 'Frame_Pole_C2', (1,0,0), outDir)

        self.lineModel(slicer.mrmlScene, aB3, aT3, 'Frame_Pole_A3', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB3, aT3, 'Frame_Pole_B3', (1,0,0), outDir)
        self.lineModel(slicer.mrmlScene, cB3, cT3, 'Frame_Pole_C3', (1,0,0), outDir)        

def calc_frame_fids_X(P1,P2,P3):
    aTop = np.array([P1[0], P1[1], P1[2]-(P1[1] - P2[1])])   
    aBot = np.array([aTop[0], aTop[1], aTop[2] - 120])
    cTop = np.array([P3[0], P3[1], P3[2]-(P1[1] - P2[1])])   
    cBot = np.array([cTop[0], cTop[1], cTop[2] - 120])

    return aTop, aBot, cTop, cBot

def calc_frame_fids_Y(P1, P2, P3):
    aTop = np.array([P3[0], P3[1], P3[2]+(P3[0] - P2[0])])   
    aBot = np.array([aTop[0], aTop[1], aTop[2] - 120])
    cTop = np.array([P1[0], P1[1], P1[2] + (P3[0] - P2[0])])   
    cBot = np.array([cTop[0], cTop[1], cTop[2] - 120])

    return aTop, aBot, cTop, cBot
        
class vtkModelBuilder:
    def __init__(self, coords, TubeR, thick, filename, electrode=False, plane = [], trans = False, electrodeLen = 0):
        
        self.buildModel(coords, TubeR, thick, filename, electrode)
        
    def compute_transform(self, start, end, rotate):
        normalized_x = [0]*3
        normalized_y = [0]*3
        normalized_z = [0]*3
    
        # The X axis is a vector from start to end
        vtk.vtkMath.Subtract(end, start, normalized_x)
        vtk.vtkMath.Normalize(normalized_x)
        
        # The Z axis is an arbitrary vector cross X
        rng = vtk.vtkMinimalStandardRandomSequence()
        rng.SetSeed(8775070)  # For testing.
        arbitrary = [0]*3
        for i in range(0, 3):
            rng.Next()
            arbitrary[i] = rng.GetRangeValue(-10, 10)
            
        vtk.vtkMath.Cross(normalized_x, arbitrary, normalized_z)
        vtk.vtkMath.Normalize(normalized_z)
        
        # The Y axis is Z cross X
        vtk.vtkMath.Cross(normalized_z, normalized_x, normalized_y)
        matrix = vtk.vtkMatrix4x4()
        
        # Create the direction cosine matrix
        matrix.Identity()
        for i in range(3):
            matrix.SetElement(i, 0, normalized_x[i])
            matrix.SetElement(i, 1, normalized_y[i])
            matrix.SetElement(i, 2, normalized_z[i])
    
        transform = vtk.vtkTransform()
        transform.Translate(start)          
        transform.Concatenate(matrix)       
        if rotate:
            transform.RotateY(90.0)             
    
        return transform
    
    def transform_item(self, item, transform):
        transformed = vtk.vtkTransformPolyDataFilter()
        transformed.SetInputConnection(item.GetOutputPort())
        transformed.SetTransform(transform)
        transformed.Update()
        return transformed
    
    def create_sphere(self, radius):
        sphere = vtk.vtkSphereSource()
        sphere.SetThetaResolution(128)
        sphere.SetPhiResolution(128)
        sphere.SetRadius(radius)
        
        plane = vtk.vtkPlane()
        plane.SetOrigin(0,0,0)
        plane.SetNormal(0, 0, -1.0)
        
        clipper = vtk.vtkClipPolyData()
        clipper.SetInputConnection(sphere.GetOutputPort())
        clipper.SetClipFunction(plane)
        clipper.SetValue(0)
        clipper.Update()
        
        return clipper
        
    def create_pipe(self, radius, thickness, height):
        disk = vtk.vtkDiskSource()
        disk.SetCircumferentialResolution(128)
        disk.SetRadialResolution(1)
        disk.SetOuterRadius(radius)
        disk.SetInnerRadius(radius - thickness)
        
        pipe = vtk.vtkLinearExtrusionFilter()
        pipe.SetInputConnection(disk.GetOutputPort())
        pipe.SetExtrusionTypeToNormalExtrusion()
        pipe.SetVector(0, 0, 1)
        pipe.SetScaleFactor(height)
        pipe.Update()
        
        return pipe

    def combine_polydata(self, source1, source2):
        if source2 is None:
            return source1
        if source1 is None:
            return source2
        combo = vtk.vtkAppendPolyData()
        combo.AddInputData(source1.GetOutput())
        combo.AddInputData(source2.GetOutput())
        combo.Update()
        
        return self.clean_mesh(combo)
    
    def clean_mesh(self, source):
        clean = vtk.vtkCleanPolyData()
        #clean.ConvertPolysToLinesOff()
        clean.SetInputData(source.GetOutput())
        clean.Update()
        
        return clean
    
    def buildModel(self, coords, TubeR, thick, filename, electrode):
        if electrode:
            normVec = norm_vec(coords[0:3],coords[3:])
            
            start_point_pipe = np.array(coords[0:3].astype(float)+(normVec*TubeR))
            start_point_sphere = np.array(coords[0:3].astype(float)+(normVec*TubeR))
            end_point_pipe = coords[3:]
            end_point_sphere = coords[3:]
            
            transform = self.compute_transform(start_point_sphere, end_point_sphere, True)
            sphere = self.create_sphere(TubeR)
            sphere = self.transform_item(sphere, transform)
            sphere.Update()
        else:
            start_point_pipe = coords[0:3]
            start_point_sphere = coords[0:3]
            end_point_pipe = coords[3:]
            end_point_sphere = coords[3:]
        
        length_pipe = np.linalg.norm(start_point_pipe-end_point_pipe)    
        transform = self.compute_transform(start_point_pipe, end_point_pipe, True)
        pipe = self.create_pipe(radius=TubeR, thickness=thick, height=length_pipe)
        pipe = self.transform_item(pipe, transform)
        pipe.Update()
        
        if electrode:
            final = self.combine_polydata(pipe, sphere)
        else:
            final = pipe
            
        writer = vtk.vtkPolyDataWriter()
        writer.SetInputData(final.GetOutput())
        writer.SetFileName(filename)
        writer.Update()
        writer.Write()

    def bsci_dir_bottomContact(self, coords, radius, thick, electrodeLen, filename):
        normVecTemp = norm_vec(coords[0:3], coords[3:])
        start_point = np.array(coords[0:3].astype(float)+(normVecTemp*radius))
#        start_point = np.array(coords[0:3].astype(float))
        transform = self.compute_transform(start_point,  coords[3:], True)
        sphere = self.create_sphere(radius)
        sphere = self.transform_item(sphere, transform)
        sphere.Update()
        
        end_point = np.array(start_point+(normVecTemp*(electrodeLen-radius)))
        length_pipe = np.linalg.norm(start_point-end_point)    
        transform = self.compute_transform(start_point, end_point, True)
        pipe = self.create_pipe(radius=radius, thickness=thick, height=length_pipe)
        pipe = self.transform_item(pipe, transform)
        pipe.Update()
        final = self.combine_polydata(pipe, sphere)
        
        writer = vtk.vtkPolyDataWriter()
        writer.SetInputData(final.GetOutput())
        writer.SetFileName(filename)
        writer.Update()
        writer.Write()
    
    def seg_contact(self, coords, plane, TubeR, thick, trans, filename):
        start_point_pipe = coords[0:3]
        end_point_pipe = coords[3:]
        length_pipe = np.linalg.norm(start_point_pipe - end_point_pipe) 
        transform = self.compute_transform(start_point_pipe, end_point_pipe, True)
        
        disk = vtk.vtkDiskSource()
        disk.SetCircumferentialResolution(128)
        disk.SetRadialResolution(1)
        disk.SetOuterRadius(TubeR)
        disk.SetInnerRadius(TubeR - thick)
        
        pipe = vtk.vtkLinearExtrusionFilter()
        pipe.SetInputConnection(disk.GetOutputPort())
        pipe.SetExtrusionTypeToNormalExtrusion()
        pipe.SetVector(0, 0, 1)
        pipe.SetScaleFactor(length_pipe)
        pipe.SetCapping(1)
        pipe.Update()
        trian = vtk.vtkTriangleFilter()
        trian.SetInputConnection(pipe.GetOutputPort())
        trian.Update()
    
        cent = [0,0,0]
        planes = vtk.vtkPlaneCollection()
        
        plane1 = vtk.vtkPlane()
        plane1.SetOrigin(cent[0], cent[1], cent[2])
        plane1.SetNormal(plane[0,:])
        planes.AddItem(plane1)
        
        plane2 = vtk.vtkPlane()
        plane2.SetOrigin(cent[0], cent[1], cent[2])
        plane2.SetNormal(plane[1,:])
        planes.AddItem(plane2)
        
        plane3 = vtk.vtkPlane()
        plane3.SetOrigin(cent[0], cent[1], cent[2])
        plane3.SetNormal(plane[2,:])
        planes.AddItem(plane3)
        
        clipper = vtk.vtkClipClosedSurface()
        clipper.SetInputData(trian.GetOutput())
        clipper.SetClippingPlanes(planes)
        clipper.SetScalarModeToColors()
        clipper.SetClipColor(0.8900, 0.8100, 0.3400)
        clipper.SetBaseColor(1.0000, 0.3882, 0.2784)
        clipper.SetActivePlaneColor(0.6400, 0.5800, 0.5000)
        clipper.Update()
        
        if trans:
            clipper = self.transform_item(clipper, transform)
            clipper.Update() 
        
        writer = vtk.vtkPolyDataWriter()
        writer.SetInputData(clipper.GetOutput())
        writer.SetFileName(filename)
        writer.Update()
        writer.Write()
        
    
def norm_vec(P1, P2):
    DirVec = [P2[0]-P1[0], P2[1]-P1[1], P2[2]-P1[2]]
    MagVec = np.sqrt([np.square(DirVec[0]) + np.square(DirVec[1]) + np.square(DirVec[2])])
    NormVec = np.array([float(DirVec[0]/MagVec), float(DirVec[1]/MagVec), float(DirVec[2]/MagVec)])
    
    return NormVec

def mag_vec(P1, P2):
    DirVec = [P2[0]-P1[0], P2[1]-P1[1], P2[2]-P1[2]]
    MagVec = np.sqrt([np.square(DirVec[0]) + np.square(DirVec[1]) + np.square(DirVec[2])])
    
    return MagVec
        
def frame_target(frame_center, target, side):
    frame_target_X = frame_center[0]-target[0]
    frame_target_Y = np.diff((frame_center[1],target[1]))
    frame_target_Z = np.diff((frame_center[2],target[2]))
    
    frame_target =[]
    if 'left' in side:
        frame_target.append(100+abs(frame_target_X))
            
    elif 'right' in side:
        frame_target.append(100-abs(frame_target_X))
            
    if frame_target_Y > 0:
        frame_target.append(100+abs(frame_target_Y))
    else:
        frame_target.append(100-abs(frame_target_Y))
        
    if frame_target_Z > 0:
        frame_target.append(100-abs(frame_target_Z))
    else:
        frame_target.append(100+abs(frame_target_Z))        

    return frame_target

class model_color:
    def __init__(self, fileName, color, sliceVisible):
        
        self.fileName = fileName
        self.volumeColor = color
        self.volumeVisibility = sliceVisible
        
        self.setAttributes()
        
    def setAttributes(self):
        [success, self.node] = slicer.util.loadModel(self.fileName, returnNode = True)
        self.node.GetModelDisplayNode().SetColor(self.volumeColor)
        self.node.GetModelDisplayNode().SetSelectedColor(self.volumeColor) 
        self.node.GetModelDisplayNode().SetSliceIntersectionVisibility(self.volumeVisibility)
        if self.volumeVisibility:
            self.node.GetModelDisplayNode().SetSliceIntersectionOpacity(1)
            
        if [x for x in {'entry_target','electrode','midline'} if x in self.node.GetName()]:
            self.node.GetDisplayNode().SetTextScale(0)
            self.node.GetDisplayNode().VisibilityOff()
        
        if '_lead' in self.node.GetName():
            self.node.SetAttribute('ProbeEye', '1')
            
        if 'mer_activity' in self.fileName:
            self.node.GetDisplayNode().BackfaceCullingOff()
            
        slicer.util.saveNode(self.node, self.fileName)
    

def rotation_matrix(pitch, roll, yaw):
    pitch,roll,yaw = np.array([pitch, roll, yaw])*np.pi/180
    matrix_pitch = np.array([
                        [np.cos(pitch), 0, np.sin(pitch)],
                        [0, 1, 0],
                        [-np.sin(pitch), 0, np.cos(pitch)]
                    ])
    matrix_roll = np.array([
                        [1,0,0],
                        [0, np.cos(roll), -np.sin(roll)],
                        [0, np.sin(roll), np.cos(roll)]
                    ])
    matrix_yaw = np.array([
                        [np.cos(yaw),-np.sin(yaw),0],
                        [np.sin(yaw), np.cos(yaw), 0],
                        [0, 0,1]
                    ])

    return np.dot(matrix_pitch, np.dot(matrix_roll,matrix_yaw))
 
def plot_models(side, dataFolder, model_parameters):
    DirVec = [side['entry'][0]-side['target'][0], side['entry'][1]-side['target'][1], side['entry'][2]-side['target'][2]]
    MagVec = np.sqrt([np.square(DirVec[0]) + np.square(DirVec[1]) + np.square(DirVec[2])])
    NormVec = np.array([float(DirVec[0]/MagVec), float(DirVec[1]/MagVec), float(DirVec[2]/MagVec)])
    
    alpha = np.round(float((np.arccos(DirVec[0]/MagVec))*180/np.pi),2)
    beta = np.round(float((np.arccos(DirVec[1]/MagVec))*180/np.pi),2)
    
    #
    ### Add entry and target to combined fiducial list
    #
    entry_name = side['side'] + '_entry_' + side['type']
    target_name = side['side'] + '_target_' + side['type']
    
    nodes = slicer.util.getNodesByClass('vtkMRMLMarkupsFiducialNode')
    for inodes in nodes:
        if entry_name in inodes.GetName():
            slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
        if target_name in inodes.GetName():
            slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
            
    entry_fid_Node = slicer.vtkMRMLMarkupsFiducialNode()
    entry_fid_Node.SetName(entry_name)
    slicer.mrmlScene.AddNode(entry_fid_Node)
    entry_fid_Node.GetDisplayNode().SetVisibility(0)
    n = entry_fid_Node.AddFiducial(side['entry'][0], side['entry'][1], side['entry'][2])
    entry_fid_Node.SetNthFiducialLabel(n, entry_name)
    entry_fid_Node.SetNthMarkupLocked(n,1)
    
    slicer.util.saveNode(entry_fid_Node, os.path.join(dataFolder, 'markups', entry_name + '.fcsv'))
    
    target_fid_Node = slicer.vtkMRMLMarkupsFiducialNode()
    target_fid_Node.SetName(target_name)
    slicer.mrmlScene.AddNode(target_fid_Node)
    target_fid_Node.GetDisplayNode().SetVisibility(0)
    n = target_fid_Node.AddFiducial(side['target'][0], side['target'][1], side['target'][2])
    target_fid_Node.SetNthFiducialLabel(n, target_name)
    target_fid_Node.SetNthMarkupLocked(n,1)
        
    slicer.util.saveNode(target_fid_Node, os.path.join(dataFolder, 'markups', target_name + '.fcsv'))
    
    coordsFile = []
    csvfile = os.path.join(os.path.split(dataFolder)[0], 'summaries', 'lead_coordinates.csv')
    if not os.path.exists(csvfile):
        coordsFile.append(['side', 'type' , 'point', 'X', 'Y', 'Z'])
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(coordsFile)
            
    else:
        coordsFile.append([side['side'], side['type'], 'entry', side['entry'][0]-side['MCP'][0], side['entry'][1]-side['MCP'][1], side['entry'][2]-side['MCP'][2]])
        coordsFile.append([side['side'], side['type'], 'target', side['target'][0]-side['MCP'][0], side['target'][1]-side['MCP'][1], side['target'][2]-side['MCP'][2]])
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(coordsFile)

    jsonfile = os.path.join(os.path.split(dataFolder)[0], 'summaries', side['side'] + '_surgical_data.json')
    with open(jsonfile) as side_file:
        ch_info_json_orig = json.load(side_file)
    
    if 'planned_update' in side['type']:
        ch_info_json_orig['lead_traj_chosen'] = side['implantTraj'] if not ch_info_json_orig['lead_traj_chosen'] or \
                                    ch_info_json_orig['lead_traj_chosen'] != side['implantTraj'] else ch_info_json_orig['lead_traj_chosen']
        
        ch_info_json_orig['lead_depth'] = side['depth'] if not ch_info_json_orig['lead_depth'] or \
                                    ch_info_json_orig['lead_depth'] != side['depth'] else ch_info_json_orig['lead_depth']
    elif 'planned' in side['type']:                                
        if not ch_info_json_orig['mer_tracks']:
            ch_info = {}
            for ichan in side['chansUsed']:
                ch_info[ichan] = {
                    'mer_top': [],
                    'mer_bot': [],
                    'acpc_enter(x,y,z)': [],
                    'acpc_target(x,y,z)': []
                    }
            ch_info_json_orig['mer_tracks'] = ch_info
            
        ch_info_json_orig['traj_len'] = float(np.round(MagVec, decimals = 2)) if not ch_info_json_orig['traj_len'] or \
                                        ch_info_json_orig['traj_len'] != float(np.round(MagVec, decimals = 2)) else ch_info_json_orig['traj_len']
        
        ch_info_json_orig['axial_ang'] = beta if not ch_info_json_orig['axial_ang'] or \
                                        ch_info_json_orig['axial_ang'] != beta else ch_info_json_orig['axial_ang']
    
        ch_info_json_orig['sag_ang'] = abs(alpha) if not ch_info_json_orig['sag_ang'] or \
                                        ch_info_json_orig['sag_ang'] != abs(alpha) else ch_info_json_orig['sag_ang']
        
        entry_temp = [side['entry'][0]-side['MCP'][0], side['entry'][1]-side['MCP'][1], side['entry'][2]-side['MCP'][2]]
        ch_info_json_orig['entry'] = entry_temp if not ch_info_json_orig['entry'] or \
                                        ch_info_json_orig['entry'] != entry_temp else ch_info_json_orig['entry']
        
        target_temp = [side['target'][0]-side['MCP'][0], side['target'][1]-side['MCP'][1], side['target'][2]-side['MCP'][2]]
        ch_info_json_orig['target'] = target_temp if not ch_info_json_orig['target'] or \
                                        ch_info_json_orig['target'] != target_temp else ch_info_json_orig['target']           
         
        ch_info_json_orig['elecUsed'] = side['elecUsed'] if not ch_info_json_orig['elecUsed'] or \
                                        ch_info_json_orig['elecUsed'] != side['elecUsed'] else ch_info_json_orig['elecUsed']
   
    os.remove(jsonfile)
    json_output = json.dumps(ch_info_json_orig, indent=4)
    with open(jsonfile, 'w') as fid:
        fid.write(json_output)
        fid.write('\n')

    if not os.path.exists(model_parameters['lead_dir']):
        os.makedirs(model_parameters['lead_dir'])
    else:
        shutil.rmtree(model_parameters['lead_dir'])
        os.makedirs(model_parameters['lead_dir'])
    
    nodes = slicer.util.getNodesByClass('vtkMRMLModelNode')
    for inodes in nodes:
        if os.path.split(model_parameters['fileN'])[-1].split('.vtk')[0] in inodes.GetName():
            slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
            
    vtkModelBuilder(np.hstack((side['target'], side['entry'])), 1.1, 0.2, model_parameters['fileN'], electrode=True) 
    
    if side['plot_model']:
        model_color(model_parameters['fileN'], model_parameters['model_col'], model_parameters['model_vis'])
    
    index = [i for i, x in enumerate(electrodeModels.keys()) if side['elecUsed'] == x][0]
    e_specs = electrodeModels[list(electrodeModels)[index]]
    bottomTop = np.empty([0,6])
    start = e_specs['encapsultation']
    conSize = e_specs['contact_size']
    conSpace = e_specs['contact_spacing']
    
    contactFile = []
    contact_col = model_parameters['contact_col']
    contact_vis = model_parameters['contact_vis']
    for iContact in range(0, e_specs['num_contacts']):
        bottomTop = np.append(bottomTop, np.hstack((
                np.array([[side['target'][0]+(NormVec[0]*(start))],[side['target'][1]+(NormVec[1]*(start))],[side['target'][2]+(NormVec[2]*(start))]]).T,
                np.array(([side['target'][0]+(NormVec[0]*(start + conSize))],[side['target'][1]+(NormVec[1]*(start + conSize))],[side['target'][2]+(NormVec[2]*(start + conSize))])).T)), axis=0)
        
        filen = "_".join([model_parameters['contact_fileN'], str(iContact+1) + '.vtk'])
        nodes = slicer.util.getNodesByClass('vtkMRMLModelNode')
        for inodes in nodes:
            if os.path.split(filen)[-1].split('.vtk')[0] in inodes.GetName():
                slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
            
        midContact = bottomTop[iContact,:3] + ((bottomTop[iContact,3:]-bottomTop[iContact,:3]))/2
        
        contactFile.append([side['side'], side['type'], str(iContact+1), midContact[0]-side['MCP'][0], midContact[1]-side['MCP'][1], midContact[2]-side['MCP'][2]])
        
        if side['elecUsed'] in ('Directional','directional', 'bsci_directional'):
            if iContact == 0:
                vtkModelBuilder.bsci_dir_bottomContact(bottomTop[iContact,:], 1.2, 0.2, 1.4, filen)
                if side['plot_model']:
                    model_color(model_parameters['contact_fileN'], contact_col, contact_vis)
                    
            elif iContact == 1 or iContact == 2:
                
                filena = '_'.join([filen.split('.')[0],'01']) + '.vtk'
                plane = np.vstack(([0.7, 1.0, 0.0], 
                                   [1.0, -0.4, 0.0],
                                   [1.0, -0.4, 0.0]))
                
                nodes = slicer.util.getNodesByClass('vtkMRMLModelNode')
                for inodes in nodes:
                    if os.path.split(filena)[-1].split('.vtk')[0] in inodes.GetName():
                        slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
                
                vtkModelBuilder.seg_contact(bottomTop[iContact,:], plane, 1.2, 0.2, True, filena)
                
                if side['plot_model']:
                    model_color(filena, contact_col, contact_vis)
        
                filena = '_'.join([filen.split('.')[0],'02']) + '.vtk'
                plane = np.vstack(([-1.0, -0.7, 0.0], 
                                   [0.4, -1.0, 0.0],
                                   [0.4, -1.0, 0.0]))
                
                nodes = slicer.util.getNodesByClass('vtkMRMLModelNode')
                for inodes in nodes:
                    if os.path.split(filena)[-1].split('.vtk')[0] in inodes.GetName():
                        slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
                        
                vtkModelBuilder.seg_contact(bottomTop[iContact,:], plane, 1.2, 0.2, True, filena)
                
                if side['plot_model']:
                    model_color(filena, contact_col, contact_vis)
        
                filena = '_'.join([filen.split('.')[0],'03']) + '.vtk'
                plane = np.vstack(([-0.1, 1.0, 0.0], 
                                   [-1.0, 0.1, 0.0],
                                   [-1.0, 0.1, 0.0]))
                
                nodes = slicer.util.getNodesByClass('vtkMRMLModelNode')
                for inodes in nodes:
                    if os.path.split(filena)[-1].split('.vtk')[0] in inodes.GetName():
                        slicer.mrmlScene.RemoveNode(slicer.util.getNode(inodes.GetID()))
                        
                vtkModelBuilder.seg_contact(bottomTop[iContact,:], plane, 1.2, 0.2, True, filena)
                
                if side['plot_model']:
                    model_color(filena, contact_col, contact_vis)
                    
            else:
                vtkModelBuilder(bottomTop[iContact,:], 1.2, 0.2, filen)
                if side['plot_model']:
                    model_color(filen, contact_col, contact_vis)

        else:
            vtkModelBuilder(bottomTop[iContact,:], 1.2, 0.2, filen)
            if side['plot_model']:
                model_color(filen, contact_col, contact_vis)

        start += conSize
        start += conSpace
    
    csvfile = os.path.join(os.path.split(dataFolder)[0], 'summaries', 'contact_coordinates.csv')
    if not os.path.exists(csvfile):
        contactFileHeader = []
        contactFileHeader.append(['side', 'type', 'contact', 'X', 'Y', 'Z'])
        with open(csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerows(contactFile)
                
    with open(csvfile, "a") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(contactFile)
    
    if 'planned_update' not in side['type']:
        alpha = np.round(float((np.arccos(DirVec[0]/MagVec))*180/np.pi),2)
        alpha = np.round(float(90-alpha),2)
        beta = np.round(float((np.arccos(DirVec[1]/MagVec))*180/np.pi),2) - 90
        
        R = rotation_matrix(alpha, beta, 0)
        t = 2*np.pi*np.arange(0,1,0.25)
        coords_norm = 2*np.c_[np.cos(t), np.sin(t), np.zeros_like(t)].T
        new_coords_P1 = ((np.dot(R,coords_norm)).T + side['target']).T
        
        if 'actual' in side['type']:
            if 'Center' in side['implantTraj']:
                new_coords_final = new_coords_P1
            else:
                chanIdx = side['chanNewCent'].get(list(side['chanIndex'].keys())[[i for i, x in enumerate(side['chanIndex'].values()) if x ==side['implantTraj']][0]])[0]
                t = 2*np.pi*np.arange(0,1,0.25)
                coords_shift = 2*(np.c_[np.cos(t), np.sin(t), np.zeros_like(t)]).T
                R = rotation_matrix(alpha, beta, 0)
                new_coords_final = ((np.dot(R,coords_shift)).T + list(new_coords_P1.T[chanIdx])).T
        else:
            new_coords_final = new_coords_P1
            
        if not os.path.exists(model_parameters['mer_dir']):
            os.makedirs(model_parameters['mer_dir'])
        else:
            shutil.rmtree(model_parameters['mer_dir'])
            os.makedirs(model_parameters['mer_dir'])
        
        for ichan in side['chansUsed']: 
            mer_fileName = os.path.join(model_parameters['mer_dir'], side['side'] + '_' + ichan + model_parameters['mer_fileN'] + '.vtk')
            
            models = slicer.util.getNodesByClass('vtkMRMLModelNode')
            currentModelName = side['side'] + '_' + ichan + model_parameters['mer_fileN']
            for imodel in models:
                if currentModelName in imodel.GetName():
                    slicer.mrmlScene.RemoveNode(slicer.util.getNode(imodel.GetID()))
            
            if 'Center' in ichan:
                P1_shift = new_coords_final.T[2]-(new_coords_final.T[2] - new_coords_final.T[0])/2
                coords = np.hstack((P1_shift, P1_shift + (NormVec.T*MagVec)))
                if 'planned' in side['type']:
                    ch_info_json_orig['mer_tracks'][ichan]['acpc_enter(x,y,z)'] = list(P1_shift + (NormVec.T*MagVec))
                    ch_info_json_orig['mer_tracks'][ichan]['acpc_target(x,y,z)'] = list(P1_shift)
    
            else:
                for idx, chan in side['chanIndex'].items():
                    if ichan == chan:
                        coords = np.hstack((new_coords_final.T[idx], new_coords_final.T[idx] + (NormVec.T*MagVec)))
                        if 'planned' in side['type']:
                            ch_info_json_orig['mer_tracks'][ichan]['acpc_enter(x,y,z)'] = list(new_coords_final.T[idx] + (NormVec.T*MagVec))
                            ch_info_json_orig['mer_tracks'][ichan]['acpc_target(x,y,z)'] = list(new_coords_final.T[idx])
            
            vtkModelBuilder(coords, 0.1, 0.1, mer_fileName, electrode=False)   
            if side['plot_mer_tracks']:
                model_color(mer_fileName, model_parameters['mer_col'], model_parameters['mer_vis'])

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
        
        #### Label
        self.sText = qt.QLabel()
        self.sText.setText(text)
        self.sText.setFixedWidth(60)
        self.sText.setContentsMargins(0,0,10,0)
        self.sText.setStyleSheet("font-weight: bold;font-size: 12px;qproperty-alignment: AlignCenter")
        
        #### Polarity buttons
        self.contactNegative = qt.QCheckBox('Neg')
        self.contactNegative.setChecked(False)
        self.contactNegative.setFixedWidth(47)
        self.contactNegative.setStyleSheet("font-weight: normal;\
                                                font-size: 12px;")
        self.contactPositive = qt.QCheckBox('Pos')
        self.contactPositive.setChecked(False)
        self.contactPositive.setFixedWidth(47)
        self.contactPositive.setStyleSheet("font-weight: normal;\
                                                font-size: 12px;")
        self.polarityButtonGroup = qt.QButtonGroup()
        self.polarityButtonGroup.setExclusive(False)
        self.polarityButtonGroup.addButton(self.contactNegative)
        self.polarityButtonGroup.addButton(self.contactPositive)
        self.polarityButtonGroup.setExclusive(True)
		
        #### Amplitude box
        self.stimAmp = qt.QDoubleSpinBox()
        self.stimAmp.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:6px")
        self.stimAmp.setFixedWidth(70)
        self.stimAmp.setMinimum(-1000)
        self.stimAmp.setMaximum(1000)
        self.stimAmp.value = 0
        
        #### Frequency box
        self.stimFreq = qt.QDoubleSpinBox()
        self.stimFreq.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:6px")
        self.stimFreq.setFixedWidth(70)
        self.stimFreq.setMinimum(-1000)
        self.stimFreq.setMaximum(1000)
        self.stimFreq.value = 0
        
        #### Pulse width box
        self.stimPW = qt.QDoubleSpinBox()
        self.stimPW.setStyleSheet("font-weight: normal;font-size: 12px;margin-right:6px")
        self.stimPW.setFixedWidth(70)
        self.stimPW.setMinimum(-1000)
        self.stimPW.setMaximum(1000)
        self.stimPW.value = 0
        
        #### Impedance box
        self.stimImp = qt.QDoubleSpinBox()
        self.stimImp.setStyleSheet("font-weight: normal;font-size: 12px;")
        self.stimImp.setFixedWidth(90)
        self.stimImp.setMinimum(-1000)
        self.stimImp.setMaximum(1000)
        self.stimImp.value = 0
        
        #### Contact settings row layout
        self.contactWig = qt.QWidget()
        self.contactWig.setVisible(visible)
        self.contactWig.setContentsMargins(20,0,0,0)
        
        self.contactHBox = qt.QHBoxLayout(self.contactWig)
        self.contactHBox.addWidget(self.sText)
        self.contactHBox.addWidget(self.contactNegative)
        self.contactHBox.addWidget(self.contactPositive)
        self.contactHBox.addWidget(self.stimAmp)
        self.contactHBox.addWidget(self.stimFreq)
        self.contactHBox.addWidget(self.stimPW)
        self.contactHBox.addWidget(self.stimImp)
        self.contactHBox.addStretch()
        self.contactHBox.setSpacing(0)
        self.contactHBox.setMargin(0)
        
class VTAModelBuilder:
    def __init__(self, elspec, stimulation, contactSettings, VATMethod, coords, options, vatsettings=None):
        """
        
        """
        self.elspec = elspec
        self.stimulation = stimulation
        self.VATMethod = VATMethod
        self.coords = coords
        self.contactSettings = contactSettings
        self.options = options
        self.vatsettings = vatsettings
        
        self.main()
        
    def main(self):
        if 'R' in self.options['side']:
            sidec='R'
            cnts=['k0','k1','k2','k3']
        elif 'L' in self.options['side']:
            sidec='L'
            cnts=['k8','k9','k10','k11']
    
        xx,yy,zz,_ = self.psphere(1000)

        radius = np.kron(np.ones((self.elspec['num_contacts'], 1)), self.elspec['contact_size'])
        sources = [int(x) for x in np.linspace(0, len(self.stimulation)-1, len(self.stimulation))]
        volume = np.zeros(len(radius))
        VAT = []
        K = []
        ivx = self.three_d_array(0, [len(sources), 3, 2])
        for source in sources:
            U = []
            Im = []
            stimsource=self.stimulation[sidec+'s'+str(source)]
            for cnt in range(len(cnts)):
                U.append(stimsource[cnts[cnt]]['perc'])
                Im.append(stimsource[cnts[cnt]]['imp'])
        
            Acnt = [x for i,x in enumerate(U) if x > 0]
            Aidx = [i for i,x in enumerate(U) if x > 0]
            if len(Acnt)>1:
                print('In the Dembek model, only one active contact can be selected in each source');
            else:
                Im = Im[Aidx[0]]
                Im = Im # kohm -> ohm
                U = stimsource['amp']
                
                if self.VATMethod == 1:
                    if self.vatsettings == None:
                        # Define the stimulation settings
                        self.vatsettings = {}
                        self.vatsettings['ethresh'] = 0.20
                        self.vatsettings['ethresh_pw'] = 60
                        self.vatsettings['pw'] = 60
                    
                    radius[source] = self.dembek17_radius(U, Im, self.vatsettings['ethresh'], self.vatsettings['pw'], self.vatsettings['ethresh_pw'])
                if self.VATMethod == 2:
                    radius[source] = self.maedler12_eq3(U, Im)
                if self.VATMethod == 3:
                    radius[source] = self.kuncel(U, Im)
                    
                volume[source] = (4/3)*np.pi*radius[source]**3
                
                VAT.append(np.vstack((xx*radius[source] + self.coords[Aidx[0]][0],
                                        yy*radius[source] + self.coords[Aidx[0]][1],
                                        zz*radius[source] + self.coords[Aidx[0]][2])))
                
                CH = scipy.spatial.ConvexHull(VAT[source].T + np.random.rand(VAT[source].shape[1], VAT[source].shape[0])*0.000001)
                vid = np.sort(CH.vertices)
                mask = np.zeros(len(CH.points), dtype=np.int64)
                mask[vid] = np.arange(len(vid))
                K.append(mask[CH.simplices]) # create triangulation
        
                for dim in range(3):
                    ivx[source][dim][:]=[min(VAT[source][dim]),max(VAT[source][dim])]
      
    def dembek17_radius(self, U, Im, ethresh, pw, ethresh_pw):
        # This function radius of Volume of Activated Tissue for stimulation settings U and Ohm. See Maedler 2012 for details.
        # Clinical measurements of DBS electrode impedance typically range from
        # 500?1500 Ohm (Butson 2006).
        r = 0
        if U: #(U>0)
            r = ((pw/ethresh_pw)**0.3) * np.sqrt((0.72 * (U/Im)) / (ethresh * 1000))
            r = r * 1000 # from m to mm
            return r
        else:
            return None
    
    def kuncel(self, U):
        """
        This function radius of Volume of Activated Tissue for stimulation settings 
        U. See Kuncel 2008 for details. Clinical measurements of DBS electrode 
        impedance typically range from 500-1500 Ohm (Butson 2006).
        """
        r=0
        if U:
            k=0.22
            Uo=0.1
            r=np.sqrt((U-Uo)/k)
            return r
        else:
            return None
    
    def maedler12_eq3(self, U, Im):
        """
        This function radius of Volume of Activated Tissue for stimulation settings 
        U and Ohm. See Maedler 2012 for details. Clinical measurements of DBS 
        electrode impedance typically range from 500-1500 Ohm (Butson 2006).
        """
        r=0
        if U:
            k1=-1.0473
            k3=0.2786
            k4=0.0009856
            r = -((k4*Im) - np.sqrt(((k4**2)*(Im**2)) + (2*k1*k4*Im) + (k1**2) + (4*k3*U)) + k1)/(2*k3)
            return r
        else:
            return None
        
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
        x = np.random.uniform(0,1,n) - 0.5
        y = np.random.uniform(0,1,n) - 0.5
        z = np.random.uniform(0,1,n) - 0.5
        
        # Make the matrix R matrices for comparison.
        rm_new = np.ones((n,n))
        rm_old = np.zeros((n,n))
        
        # Scale the coordinates so that their distance from the origin is 1.
        r = np.sqrt(x**2 + y**2 + z**2)
        
        x = np.divide(x,r)
        y = np.divide(y,r)
        z = np.divide(z,r)
        
        not_done = True
        s = 1
        np.seterr(divide='ignore', invalid='ignore')
        while not_done:
            for i in range(n):
                # Calculate the i,j,k vectors for the direction of the repulsive forces.
                ii = x[i] - x
                jj = y[i] - y
                kk = z[i] - z
                
                rm_new[i,:] = np.sqrt(ii**2 + jj**2 + kk**2)
                
                ii = np.divide(ii, rm_new[i,:])
                jj = np.divide(jj, rm_new[i,:])
                kk = np.divide(kk, rm_new[i,:])
                
                #Take care of the self terms.
                ii[i] = 0
                jj[i] = 0
                kk[i] = 0
                
                # Use a 1/r^2 repulsive force, but add 0.01 to the denominator to avoid a 0 * Inf below. The self term automatically disappears since the ii,jj,kk vectors were set to zero for self terms.
                f = np.divide(1, (0.01 + rm_new[i,:]**2))
                
                # Sum the forces
                fi = sum(np.multiply(f,ii))
                fj = sum(np.multiply(f,jj))
                fk = sum(np.multiply(f,kk))
                
                # Find magnitude
                fn = np.sqrt(fi**2 + fj**2 + fk**2)
                
                #Find the unit direction of repulsion.
                fi = fi/fn
                fj = fj/fn
                fk = fk/fn
                
                # Step a distance s in the direciton of repulsion
                x[i] = x[i] + np.multiply(s,fi)
                y[i] = y[i] + np.multiply(s,fj)
                z[i] = z[i] + np.multiply(s,fk)
                
                # Scale the coordinates back down to the unit sphere.
                r = np.sqrt(x[i]**2 + y[i]**2 + z[i]**2)
                
                x[i] = x[i]/r
                y[i] = y[i]/r
                z[i] = z[i]/r
                
            #Check convergence
            diff = abs(rm_new - rm_old)
            not_done = diff.any() > 0.01
            rm_old = rm_new
            
        #Find the smallest distance between neighboring points. To do this exclude the self terms which are 0.
        tmp = rm_new[:]
        avgr = min(tmp[tmp != 0])
        
        return x,y,z,avgr
    
    def three_d_array(self, value, dim):
        """
        Create 3D-array
        :param dim: a tuple of dimensions - (x, y, z)
        :param value: value with which 3D-array is to be filled
        :return: 3D-array
        """
    
        return [[[value for _ in range(dim[2])] for _ in range(dim[1])] for _ in range(dim[0])]


        