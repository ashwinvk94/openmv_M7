# Overview

The OpenMV M7 is a board containing an cortex M7 processor. I runs the MicroPython OS and you can program the OpenMV Cam in high level MicroPython scripts. The OpenMV IDE(based on the QtCreator) can be used to edit and run python scripts on the M7 board.

Other details pertaining to IO use and hardware setup is found in the below link:
http://docs.openmv.io/openmvcam/tutorial/index.html

## Installing the IDE
http://docs.openmv.io/openmvcam/tutorial/software_setup.html

## Example scripts
Once you have the IDE installed, you can run example scripts, which be found in the File/Examples menu in the IDE itself. The examples cover the boards I/O interfaces and basic applications such as Face Detection and Machine Learning.

At the PRG lab, the following examples were tested on the M7. Please note that all the examples oncludes live streaming of images to the IDE:

 - helloworld (35 fps)
 - main
 - text_drawing (35 fps)
 - face_detection (Using haar features) (8 fps)
 - automatic_rg565_color_tracking (20 fps)
 - iris_detection (7 fps)
 - find_lines (23 fps)
 - on_disk_basic_frame_differencing (8 fps)
 - absolute_translation (optical_flow)(bad results) (28 fps)
 - image_patches_differential_translation (14 fps)
 - nn_cifar10 (modified example file is available in this repo) (12 fps)
 - nn_haar_smile_detection (3 fps)
 - find_apriltags (9 fps)
 
Note: Could only load the cifar10_fast net, not the cifar10 or Let net. Out of Heap memory Issue shows up when Loading these files. This issue has been added to openmv forum. Waiting for feedback.

