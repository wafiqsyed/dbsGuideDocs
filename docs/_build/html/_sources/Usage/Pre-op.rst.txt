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

	|
		
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


	|
		
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

5. **Plot the anatomical fiducials.**
   	There are four points that need to be marked. 
   		- Anterior Comissure (AC)
   		- Posterior Comissure (PC)
   		- Two midline points (Mid1 and Mid2)

   	Select ``3D Stealth`` as your fiducial volume. 

	.. note:: 
		To adjust the the brightness of the window and level of volume of the scan, click on the window tool. Then drag your crusor across the scan until you reach the level of brightness desired. A helpful shortcut is to hold control (or command) and drag a square across the brain (exclude the skull). This will give you a good baseline. 

	
		.. image:: ../Images/Preop/windowTool.gif

		|
		
		**TIP** 
			Hold Control/Command and make a square across brain tissue

		.. image:: ../Images/Preop/windowTool2.gif


	**Anterior Commissure**

		The anterior commissure is **the white matter tract connecting the two temporal lobes across the midline, and is placed in front of the columns of the fornix.**

		.. image:: ../Images/Preop/ACDiagram.jpeg
			:align: center

		.. image:: ../Images/Preop/ACDiagramCoronal.png
			:align: center

		|
		
		Click ``Turn On Crosshairs``. Hold ``shift`` while moving your crusor to position your crosshair on the anterior commissure. As long as you mark the AC fiducial on one view, the it'll be marked on the other views as well. 

		.. image:: ../Images/Preop/ACFiducials.png

		Now add the AC point to our list of ``Anatomical Fiducials``.

		.. image:: ../Images/Preop/ACMarkup.gif
			:align: center


		Repeat these steps for PC, Mid1, and Mid2.

	**Posterior Commissure**

		.. image:: ../Images/Preop/PCMarkup.png
			:align: center


	**Mid1**

		We can use the fourth ventricle.

		.. image:: ../Images/Preop/Mid1Markup.png
			:align: center

	**Mid2**

		.. image:: ../Images/Preop/Mid2Markup.png
			:align: center

	.. Note::
		You may add more midlines (upto 5) if you would like to. Click ``Add Midline`` to add another one.

	Once done, click ``Confirm Fiducials.`` A new fiducial ``MCP (Mid Commissure Point)`` will be added automatically based on your ``AC`` and ``PC`` fiducials.

	.. image:: ../Images/Preop/confirmFiducials.gif
		:align: center

	|
		
	6. Plan target trajectory.
		Using the ``Target Planning`` widget, we will plan the trajectory of the micoelectrodes. 

		.. note::
			To center and zoom out of the scans, click on the square with four lines on the top left of each view's menu bar. 

		.. image:: ../Images/Preop/adjustView.png
			:align: center

		|
		
		Click ``Turn On Crosshairs``. Below this button are ``X, Y, and Z`` coordinates, relative to ``MCP``. As you click on the scan the values update. If you have the planned coordinates from before, you can input them into these coordinates. In this example, the coordinates were already provided, so we input them into the appropriate boxes. 

		.. image:: ../Images/Preop/leftPlan.png
			:align: center

		|

		Click ``Confirm Left Plan``, and you will see an electrode plotted in 3D space. 

		.. image:: ../Images/Preop/leftPLanConfirmed.png
			:align: center

		|
		
		``Left Plan`` is complete. We do not have any frame settings as the CT frame scan is taken on the day of surgery.
		Repeat these steps for ``Right Plan``.

		.. image:: ../Images/Preop/rightPlan.png
			:align: center

		|
		
		.. image:: ../Images/Preop/rightPLanConfirmed.png
			:align: center
		
		|

		View the scan on the 3D view with the electrodes:
		
		.. image:: ../Images/Preop/plan3DView.gif
				:align: center

		|

		Target planning is now complete! To look down the electrode and ensure you're not hitting any unwanted tissue, use the ``Probes Eye``. After selecting the left or right planned lead as your ``Probe Eye Model``, slide the ``Entry`` slider. 

		.. image:: ../Images/Preop/probeEyeModel.png
				:align: center

**The preoperative phase of DBS Guide is complete! Moving onto the day of the surgery, visit** :ref:`Intraoperative Phase <Intraop>`.
