
# To look at the RPi's camera 
libcamera-jpeg --qt-preview on -o test.jpg

# To Take a photo without displaying the preview:
libcamera-jpeg -n -o test2.jpg

# To copy all jpg images from the home drive of one linux machine to the home drive of another:
scp cyberneticbilby@rpi.local:~/*.jpg ~/

# Take a high quality photo every 30 seconds for 2 minutes:
libcamera-still -n -t 120000 --timelapse 30000 --datetime --hdr