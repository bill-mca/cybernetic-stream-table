
# To look at the RPi's camera 
libcamera-jpeg --qt-preview on -o test.jpg

# To Take a photo without displaying the preview:
libcamera-jpeg -n -o test2.jpg

# To copy all jpg images from the home drive of one linux machine to the home drive of another:
scp cyberneticbilby@rpi.local:~/*.jpg ~/

# Take a high quality photo every 30 seconds for 2 minutes
# Good for building a training dataset for machine learning
libcamera-still -n -t 120000 --timelapse 30000 --datetime --hdr

# Make GIFs to embed in 

# This might be another option https://itsfoss.com/photocollage-linux/

# Make a GIF from a folder of JPGs
# You'll need to have image magick installed
convert -delay 20 -loop 0 *.jpg myimage.gif

# Get JPGs from an MP4
ffmpeg -i video.mp4  -r 5 'frames/frame-%03d.jpg'

# Run a command on a remote machine and save the output to a local file.
ssh $REMOTE_MC "digest -a md5 $TARGET_DIR/$filename" > $HOME_DIR/remote_hash_$datetag.txt

