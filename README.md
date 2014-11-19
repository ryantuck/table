# Code for hacking the table
	
### osc-fadecandy.py

**This is the script you want to run!**

combines TouchOSC with Fadecandy python script. 

Currently works with the `.touchosc` file in the iphone-osc folder.

### osc-pi.py

test script from [instructables tutorial](http://www.instructables.com/id/R-Pi-control-Android-iPhone-via-OSC/step3/Making-the-python-script-more-like-transferring-it/) for hooking TouchOSC up to Raspberry Pi.

This has a bunch of good functions etc to hold on to. 

# Notes

Need to have Fadecandy server running on the pi, and then crack open the python script through another terminal window. I believe you need to have the fadecandy plugged in via USB before starting the server. 

On Pi, navigate to `/usr/local/bin` and run:

`sudo fcserver fcserver.json`

On laptop, 

`ssh pi@[ip address]`

enter password and navigate to folder containing script. the folder should also contain the file `opc.py` from 

```
cd Documents/table
python osc-fadecandy.py`


Fire up the touchOSC app. If you're doing it on Android, you'll have to make your own, but make sure your faders are named appropriately so the python script knows how to interpret them. 

Be sure to make note of your fader names in your TouchOSC build.

### References

[open pixel control](https://github.com/zestyping/openpixelcontrol)


