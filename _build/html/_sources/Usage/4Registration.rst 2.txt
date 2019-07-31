Registration
============

.. image:: ../Images/widget04.png
   :align: center

1. Select ``Reference Volume`` as ``3D T1 Weighted``. This ``Reference Volume`` 
   will be the scan that DBS Guide will co-register the other scans to as a reference. 
2. Select ``CT Frame Volume`` as ``CT Frame``
3. Select ``Registration Algorithm`` as ``NiftyReg``
   
   .. image:: ../Images/widget04selected.png

4. Click ``Run Registration``. You can watch the progess on the ``Registration Process`` bar.
   Once ``Registration is completed`` is printed on the ``Registration Progress`` bar, you will see 
   the results under ``Co-registered Volumes``.
5. We need to confirm that the registration was successful. 
   Link the views shown on the right by pressing the "link" icon located at the top of the scans as shown here:

   This will ensure that the views are all linked together so when you zoom in one view, you zoom in on the others too. 
6. Click the ``Pin`` icon on the top left corner of the red menu bar to open Slicer's viewer menu. Then click the
   "Viewer" icon shown as two arrows ``<<`` and select ``T1 Weighted`` on the bottom selection. This sets 
   ``T1 Weighted`` as the reference scan. 
7. Compare the ``T1 Weighted`` scan with our co-registered volumes. See the following video:

8. Select all the scans in ``Co-registered Volumes`` and click ``Delete Highlighted Volumes``. This will leave us 
   with just the co-registered volumes. 
9. Registration is now complete.