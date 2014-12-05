# The Table.

The dopest table ever.


#Files

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
python osc-fadecandy.py
```


Fire up the touchOSC app. If you're doing it on Android, you'll have to make your own, but make sure your faders are named appropriately so the python script knows how to interpret them. 

Be sure to make note of your fader names in your TouchOSC build.

# Git / GitHub Notes

Generally, we'll be using a handful of commands and a very basic workflow. Putting all these here so we can have them for easy-peasy reference. 

### Cheat Sheet

`git status` tells you what's up with your latest work. 

`git add .` adds all files to your working directory (note the period `.`). 

`git add osc-fadecandy.py` adds only the file `osc-fadecandy.py` to the working directory. 

`git commit -m 'testing something rad'` will commit all files in the working directory. 

`git push origin master` will push code from your computer up to github. 

`git pull origin master` will pull from github to your computer.

`git checkout .` will get rid of any changes you've made locally, clearing the path for a `pull`. 

### Local Setup

I believe we both have **repositories** set up on our laptops and on the pi. If not, go ahead and `clone` it to your laptop (this will create a `table` folder in whatever directory you're currently in):

```
git clone https:github.com/ryantuck/table.git
```

## Git Workflow

**0 - Before editing, pull code down to your laptop from GitHub.**

This will prevent conflicts. 

```
git pull origin master
```

**1 - Make some changes to the code on your laptop.**

**2 - Check the `status` of what we're working on:**

```
cd Documents/active/table
git status
```

Your results should look like this (I'm editing `README.md`):

```
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

**3 - add your changes**

I generally use the following syntax because I'm not too picky about what I'm committing. Otherwise, we could specify a filename instead of the period `.`

```
git add .
```
**4 - commit the changes**

We'll commit changes with a message specifying what we did. 

Note: you can make multiple `commit`s before `push`ing, if you're doing a lot of different work. 

```
git commit -m 'editing readme with git stuff'
```

**5 - Push to GitHub**

```
git push origin master
```

**6 - Check the Raspberry Pi for any changes**

We want to make sure the pi is ready to pull down code. Let's check the status:

```
cd Documents/table
git status
```

If we get a message saying everything's up to date, then gravy. Otherwise, let's clear our changes (don't forget the period):

```
git checkout .
```

This somehow saves the working directory somewhere, but basically removes any changes we had made. Kind of black magic, but generally speaking, we won't be making any serious changes to the code on the pi. 

**7 - pull code down to the pi**

On the pi,

```
git pull origin master
```

You should now be up to date.






# References

[open pixel control](https://github.com/zestyping/openpixelcontrol)


