.. sample project documentation master file, created by
   sphinx-quickstart on Sun Jul  7 01:30:14 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**DBS Guide**
==========================================
Visualization Software for Deep Brain Stimulation Neurosurgery
----------------------------------------------------------------

.. image:: Images/DBSLaunch.png
   :align: center

What is DBS Guide?
^^^^^^^^^^^^^^^^^^
**DBS Guide** is a surgical planning, visuazliation, and postoperative assessment tool used for deep brain stimulation. It is an extension that can be used with 3D Slicer (a well-known MRI Visualization software). DBS Guide provides capabilities across the entire surgical spectrum:

- :ref:`Pre-operative <Preop>`
   - Co-registration of MRI scans with 3D volumetric stealth MRI
   
   .. image:: Images/Preop/coregConfirmSlide.gif
      :align: center

   - Planning DBS lead trajectory 
- :ref:`Intra-operative <Intraop>`
   - Co-restration of frame CT with MRI 
   - Confirmation of frame fiducials using automated frame detection (DBS Guide identifies the frame fiducials using image recognition)
   - Determining accuracy of (x,y,z) coordinates, arc and ring angles
   - Mapping of microelectrode (MER) recordings and plotting them in patient brain anatomy
   - Saving information regarding the trajectory used (medial, lateral, etc.) and other lead implant specs (e.g. depth)
- :ref:`Post-operative <Postop>`
   - Co-registration of post-op CT with pre-op MRI 
   - Visualization of implanted electrodes with high accuracy
   - Manipulation of stimulation settings 
   - Volume tissue activation model based on stimulation settings

To get a walk-through of DBS Guide and its capabilities in each phase of surgery (pre/intra/post-op), visit :ref:`How to Use DBS Guide <usage>`.

To get started with installation, visit :ref:`Installation Tutorial <Installation>`.


.. toctree::
   :maxdepth: 2
   :caption: User Guide

   Home <self>
   about
   install
   usage
   contact
   
.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation

   mainScript
   widgetsAPI

