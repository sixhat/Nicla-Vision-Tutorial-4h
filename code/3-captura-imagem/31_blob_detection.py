## Exemplo inspirado no tutorial disponível online em:
# https://docs.arduino.cc/tutorials/nicla-vision/blob-detection/
#
# Colocar os histogramas em modo LAB
# Seleccionar areas de intresse na janela do OpenMV
# criar blobX com os parametros que enquadrem os histogramas

import pyb # Import module for board related functions
import sensor # Import the module for sensor related functions
import time # Import module for tracking elapsed time

sensor.reset() # Resets the sensor
sensor.set_pixformat(sensor.RGB565) # Sets the sensor to RGB
sensor.set_framesize(sensor.QVGA) # Sets the resolution to 320x240 px
sensor.set_vflip(False) # Flips the image vertically
sensor.set_hmirror(False) # Mirrors the image horizontally
sensor.skip_frames(time = 2000) # Skip some frames to let the image stabilize

# Define the min/max LAB values we're looking for
# Configue OpenMV IDE to use LAB Colors.
# Draw squares on the Frame Buffer to define areas of interest
# Copy aproximate treshold values and define as many blobs as needed.
blob1 = (30, 40, -10, 4, 0, 10)

blob2 = (65, 75, 10, 17, 2, 10)

blob_color = [(255,0,0),(0,255,0),(0,0,255)]

ledRed = pyb.LED(1) # Initiates the red led
ledGreen = pyb.LED(2) # Initiates the green led

clock = time.clock() # Instantiates a clock object

while(True):
    clock.tick() # Advances the clock
    img = sensor.snapshot() # Takes a snapshot and saves it in memory

    # Find blobs with a minimal area of 50x50 = 2500 px
    # Overlapping blobs will be merged
    blobs = img.find_blobs([blob1, blob2], area_threshold=2500, merge=True)

    # Draw blobs
    for i,blob in enumerate(blobs):
        # Draw a rectangle where the blob was found
        img.draw_rectangle(blob.rect(), color=blob_color[i%3])
        # Draw a cross in the middle of the blob
        img.draw_cross(blob.cx(), blob.cy(), color=blob_color[i%3])

    # Turn on green LED if a blob was found
    if len(blobs) > 0:
        ledGreen.on()
        ledRed.off()
    else:
    # Turn the red LED on if no blob was found
        ledGreen.off()
        ledRed.on()

    pyb.delay(50) # Pauses the execution for 50ms
    print(clock.fps()) # Prints the framerate to the serial console
