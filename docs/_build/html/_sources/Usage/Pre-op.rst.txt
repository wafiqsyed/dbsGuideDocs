.. _Preop:

Pre-op
=======

.. note::
	To install DBS Guide, visit the :ref:`installation tutorial <Installation>`.


Two to three weeks prior to the surgery, the patient gets an MRI Scan along with several sequences. Among the sequences is a **3D Volumetric Stealth MRI**. Using the ``Registration Widget``, we can **co-register** the MRI scans with the 3D Volumetric Stealth MRI.

1. **Load the patient's directory.** 
	Click ``Browse`` to find your folder with the scans. Notice, we only select the folder and not the files inside the folder. This folder contains folders in the .nii.gz format which means each folder is a gzipped folder of NIFTI (Neuroinformatics Technology Initiative) files. NIFTI files are files of MRI scans.

	.. image:: ../Images/Preop/loadDir.gif
		:align: center

	.. note::

		There are two folders now in your patient directory:
			scene 
				Contains data/scans that will be edited by DBS Guide
			source 
				Contains the original brain scans

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


	Upon completion:

	.. image:: ../Images/Preop/registrationComplete.png
		:align: center


4. **Confirm that the registration was a success.**
  	We want to make sure the the co-registered scan matches ``3D Stealth``. We will use the views on the right to do this. First link all the views so that they're in sync as you zoom in and out. 

	.. image:: ../Images/Preop/link.gif
		:align: center


	Next, we'll need to set the background view to **3D Stealth** and foreground view the **co-registered** scan. 

	.. image:: ../Images/Preop/coregConfirm1.gif
		:align: center


	.. note::
		Any scan that ends with ``coreg`` has been coregistered. 


	To confirm that coregistration is successful, use the slider to transition from background and foreground. As seen below, the scans have coregistered successfully.

	.. note::
		Quick controls for Slicer
			Slide image
				Hold Shift and drag
			Move through scan according to axis (e.g. Anterior to Posterior)
				Scroll up/down
			Increase size of image
				Hold right-click and drag

	.. image:: ../Images/Preop/coregConfirmSlide.gif
		:align: center




