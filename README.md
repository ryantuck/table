## Code for hacking the table

**osc-pi.py**

test script from [instructables tutorial](http://www.instructables.com/id/R-Pi-control-Android-iPhone-via-OSC/step3/Making-the-python-script-more-like-transferring-it/) for hooking TouchOSC up to Raspberry Pi.

IP address of the Pi needs to be set here.

**osc-fadecandy.py**

combines TouchOSC with Fadecandy python script.

Currently works with the `.touchosc` file in the iphone-osc folder.

### Notes

Need to have Fadecandy server running on the pi, and then crack open the python script through another terminal window.

On Pi, navigate to `/usr/local/bin` and run:

`sudo fcserver fcserver.json`

On laptop, 

`ssh pi@[ip address]`

enter password and navigate to folder containing script. the folder should also contain the file `opc.py` from [open pixel control](https://github.com/zestyping/openpixelcontrol). 

Fire up the touchOSC app. If you're doing it on Android, you'll have to make your own, but make sure your faders are named appropriately so the python script knows how to interpret them. 

