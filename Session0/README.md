# Session 0: Getting Set up (Pre-Work)

This session is intended to be completed before attending the first face-to-face session and covers installing python, setting up an interactive development environment and solving a few simple problems.

Follow this guide to get setup. It is not a difficult process but follow the instructions carefully. This way everyone is configured the same way.

## Step 1: Get set up with Slack

Head on over and install [Slack](https://slack.com/get).

Once Slack is installed, you'll be prompted to answer a few questions:

1. You'll be asked to enter your team's Slack URL. Type `arupconsulting` into the text box and select `Continue`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SlackInstallImages/Step1.png)

2. You'll be asked to enter your Arup email. Type your Arup email into the text box and select `Continue`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SlackInstallImages/Step2.png)

3. You should have received a confirmation email - click the link in the email to continue. You'll need to select the team (Click on the `Arup` team with a picture of Ove Arup). You'll be asked to enter a few details about yourself, and pick a username. Enter in your details and continue on to the next step.

4. On the left you will see a purple navigation pane. Click on `Channels`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SlackInstallImages/Step3.png)

5. Into the search box type `python` and click on the channel `# python`. Make sure you go down to the bottom of the screen and click `Join`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/SlackInstallImages/Step4.png)

6. You're good to go! This will be your first port of call for anything related to the course materials.

## Step 2: Introduction to Automate the Boring Stuff

A great teacher, Al Sweigart, created an open source beginners guide to python programming called [Automate the Boring Stuff](https://automatetheboringstuff.com/). It is a great resource with an online text book and youtube videos. Since it aligns so closely to our course and goals that we will rely on it throughout the course.

Please watch this [short video](https://youtu.be/1F_OgqRuSdI) to get started. Ignore the download instructions, we will get to that.

## Step 3: Proxy Settings

Arup IT have set up a proxy to manage (and secure) internet traffic. We will need to add  the proxy settings to your system variables in order to use Visual Studio Code and Python.

Here is a [script](https://github.com/ArupAus/lunchtimepython/blob/2017/Session0/Resources/set_proxy.cmd),  `set_proxy.cmd` will set the proxy for you. Right click on the page and save as set_proxy.cmd. Double click to run the script. If you have admin rights on you computer it should add the proxy settings to your system variables.

**NOTE:** *Setting this proxy will cause all sort of problems when trying to work from home. You will have to work on the vpn or unset the proxy settings if you want to work from home. If this confuses you, skip this step and we will do it in Session 1.*

## Step 4: Install Python

You may have heard us say python is a programming language. So why do we need to install anything? We need to install the 'interpreter' that understands our python code and tells the computer what to do. That is the first step.

We have downloaded python from the python website for you and placed it on the Arup network drive. This way we can minimise our number of downloads from Rackspace - the genorous company that hosts python for everyone... for free!

1. Copy the `python-3.6.1-amd64.exe` file from the Arup Programs folder (P:\Program Files\Python) to your desktop.
2. Double click the file.
3. Select `Run` if a security warning appears.
4. Tick the box `Add Python 3.6 to PATH` and then select `Install Now`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/PythonInstallImages/Step1.PNG)

5. If everything goes well a success message will appear. Select `Close`.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/PythonInstallImages/Step2.PNG)

6. Go to your start menu and look for `IDLE (Python 3.6 64-bit)`. Once selected the python command prompt should appear.

![](https://raw.githubusercontent.com/ArupAus/lunchtimepython/2017/Session0/Resources/PythonInstallImages/Step3.PNG)

Please get in touch if you get stuck.

## Step 5: Install Visual Studio Code

In the videos you have been watching from Automate the Boring Stuff, Al uses a text editor called IDLE that comes standard with python. You can use this if you want. However, we suggests using a more advanced editor called Visual Studio Code (we use it on a daily basis). Follow these instructions to install it on your computer.

1. Copy the `VSCodeSetup-1.11.2.exe` file from the Arup Programs folder (P:\Program Files\Visual Studio Code) to your desktop.
2. Double click the file and follow the instructions in this [video](https://youtu.be/8tkuu0Rugg4?t=1m34s).
3. Install python extension for Visual Studio Code. Instructions can be found [here](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python). (skip this step if you have not set up the proxy in Step 3.)

## Step 6: Your First Problem Set

In each session we will provide a README.md (this file), a problem set and solutions. As part of this pre work, watch the [next video](https://youtu.be/7qHMXu99d88) from automate the boring stuff and try to solve problems in **Session 0**.

Use slack to ask questions if you get stuck.

See you in the first session!
 
