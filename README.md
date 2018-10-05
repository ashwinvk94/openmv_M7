# Overview

The OpenMV M7 is a board containing an cortex M7 processor. I runs the MicroPython OS and you can program the OpenMV Cam in high level MicroPython scripts. The OpenMV IDE(based on the QtCreator) can be used to edit and run python scripts on the M7 board.

Other details pertaining to IO use and hardware setup is found in the below link:
http://docs.openmv.io/openmvcam/tutorial/index.html

## Installing the IDE
http://docs.openmv.io/openmvcam/tutorial/software_setup.html

## Example scripts
Once you have the IDE installed, you can run example scripts, which be found in the File/Examples menu in the IDE itself. The examples cover the boards I/O interfaces and basic applications such as Face Detection and Machine Learning.

At the PRG lab, the following examples were tested on the M7:

 - helloworld
 - main
 - text_drawing
 - face_detection (Using haar features)
 - automatic_rg565_color_tracking
 - iris_detection
 - find_line_segments
 - on_disk_basic_frame_differencing
 - absolute_translation (optical_flow)(bad results)
 - image_patches_differential_translation
 - nn_cifar10 (modified example file is available in this repo)
 - nn_haar_smile_detection
 - find_apriltags
 
Note: Could only load the cifar10_fast net, not the cifar10 or Let net. Out of Heap memory Issue shows up when Loading these files. This issue has been added to openmv forum. Waiting for feedback.

