# CIFAR10 Example
import sensor, image, time, os, nn

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_contrast(3)
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((128, 128))       # Set 128x128 window.
sensor.skip_frames(time=100)
sensor.set_auto_gain(True)
sensor.set_auto_exposure(True)

# Load cifar10 network
#cwd = os.getcwd()
#dirs = os.listdir(cwd)
#print(dirs)

#net = nn.load('cifar10.network')
# Faster, smaller and less accurate.
net = nn.load('/cifar10_fast.network')
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

clock = time.clock()                # Create a clock object to track the FPS.
while(True):
    clock.tick()                    # Update the FPS clock.
    img = sensor.snapshot()         # Take a picture and return the image.
    out = net.forward(img)
    max_idx = out.index(max(out))
    score = int(out[max_idx]*100)
    print("%s:%d%% "%(labels[max_idx], score))
    #if (score < 70):
        #score_str = "??:??%"
    #else:
        #score_str = "%s:%d%% "%(labels[max_idx], score)
    #img.draw_string(0, 0, score_str, color=(255, 0, 0))

    #print(clock.fps())             # Note: OpenMV Cam runs about half as fast when connected
                                   # to the IDE. The FPS should increase once disconnected.
