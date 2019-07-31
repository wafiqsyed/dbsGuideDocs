#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:00:43 2019

@author: ggilmore
"""

#
#------------------------ Electrode Model Information -------------------------
#
        
electrodeModels = {}
medtronic_3387 = {
        'num_contacts': 4,
        'encapsultation': 1.5,
        'contact_size': 1.5,
        'contact_spacing': 1.5,
        'electrode_1': [0,1,2,3],
        'electrode_2': [8,9,10,11]
     }
electrodeModels['3387'] = medtronic_3387

medtronic_3389 = {
        'num_contacts': 4,
        'encapsultation': 1.5,
        'contact_size': 1.5,
        'contact_spacing': 0.5,
        'electrode_1': [0,1,2,3],
        'electrode_2': [8,9,10,11]
     }
electrodeModels['3389'] = medtronic_3389

bsci_directional = {
        'num_contacts': 4,
        'encapsultation': 0,
        'contact_size': 1.5,
        'contact_spacing': 0.5,
        'electrode_1': [1,2,3,4,5,6,7,8],
        'electrode_2': [9,10,11,12,13,14,15,16],
        'contact_label':['','seg ','seg ','seg ','seg ','seg ','seg ', '']
     }
electrodeModels['Directional'] = bsci_directional

bsci_nondirectional = {
        'num_contacts': 8,
        'encapsultation': 1.1,
        'contact_size': 1.5,
        'contact_spacing': 0.5,
        'electrode_1': [1,2,3,4,5,6,7,8],
        'electrode_2': [9,10,11,12,13,14,15,16],
        'contact_label':['','','','','','','', '']
     }
electrodeModels['Non-Directional'] = bsci_nondirectional


#
#-------------------------------- JSON Files ----------------------------------
#

patient_info_json = {
    'subject': [],
    'surgery_date': [],
    'surgeon': [],
    'left_side': [],
    'right_side': [],
    'target':[]
    }
        
ch_info_json = {
    'subject': [],
    'side': [],
    'traj_len': [],
    'axial_ang': [],
    'sag_ang': [],
    'entry': [],
    'target': [],
    'elecUsed':[],
    'lead_traj_chosen': [],
    'lead_depth': [],
    'lead_type': [],
    'active_con_first': [], 
    'active_con_second': [],
    'mcp_coords': [],
    'mer_tracks':[]
    }

#
#------------------------------ Data Visibiltiy -------------------------------
#

dataVisibility= {
        'plannedLeadSliceVis': True,
        'actualLeadSliceVis': True,
        'plannedContactSliceVis': True,
        'actualContactSliceVis': True,
        'plannedMERTrackSliceVis': True,
        'actualMERTrackSliceVis': True,
        'plannedSTNMERSliceVis': True,
        'actualSTNMERSliceVis': True
     }

       