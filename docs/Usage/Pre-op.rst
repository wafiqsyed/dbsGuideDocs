.. _Preop:

Pre-op
=======

.. note::
	To install DBS Guide. Visit our :ref:`installation tutorial <Installation>`


Two to three weeks prior to the surgery, the patient gets an MRI Scan along with several sequences. Among the sequences is a **3D Volumetric Stealth MRI**. Using the ``Registration Widget``, we can **co-register** the MRI scans with the 3D Volumetric Stealth MRI.

1. **Load the patient's directory.** 
	Click ``Browse`` to find your folder with the scans. Notice, we only select the folder and not the files inside the folder. This folder contains folders in the .nii.gz format which means each folder is a gzipped folder of NIFTI (Neuroinformatics Technology Initiative) files. NIFTI files are files of MRI scans.

.. image:: ../Images/Preop/loadDir.gif
	:align: center

2. **Rename volumes [optional].** 
	If you would like to rename volumes you may do so. 

.. image:: ../Images/Preop/renameVolume.gif
	:align: center


.. note::
	``Frame Detection`` is going to be skipped because the CT frame scan is performed on the day of the surgery. ``Frame Detection`` will be explored in the next phase, ``intra-op``.

3. **Co-register the 3D Volumetric Stealth MRI with the other MRI scans.**
	Using ``Registration``, select the appropraite reference volume, which in our case is ``3D Stealt``. Leave ``CT Frame Volume`` as ``None`` because the frame CT has not been obtained yet. Choose the algorithm of your preference. Then ``Run Registration.`` Note, this may take a while (upto 10 minutes). If your computer freezes, just wait, the program is still running. 

.. image:: ../Images/Preop/registration.png
	:align: center

