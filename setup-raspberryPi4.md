
# Setup steps for RespberryPi4
The steps should be the same for other Raspberry Pi versions too.

- Install imager from [here](https://www.raspberrypi.com/software/) in your laptop
- Make sure you have attached a MicroSD card (which you will be using in RaspberryPi device later)
- After installing the imager
- - Select Device as RaspberryPi4
  - Select OS as the recommended option
  - Select the storage ( the option will show the SD card you attached to your laptop)
- Now click ***'Edit settings'***
- - Set username, and password. Wifi username and password. enable SSH, set country, timezone
<img width="534" alt="image" src="https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/e08926a7-af5d-48c9-ab8e-a22727054085">

<img width="531" alt="image" src="https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/6d729349-902d-4297-b2d2-e7e841c2d14d">

- Save all settings

<img width="679" alt="image" src="https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/e3fb2689-697e-425d-bb39-be9ee562b75d">

Select 'Yes'


- Click Next to start writing in your attached SD card.

![image](https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/b8d11502-e4ad-463e-b6c7-5d70b9e72913)

<img width="678" alt="image" src="https://github.com/e2eSolutionArchitect/RaspberryPi/assets/62712515/7213da9a-a2b1-43bf-8ac8-87fc50b1df35">



- After completing the write it will ask to take the SD card out
- Now put the SD card into the RaspberyPi SD card slot and simply PowerUp the device
- At this time only the power cord is added to the Raspberry Pi device. No other cable is.
- It usually takes ~10 mins to boot the device and connect to your wifi automatically. Don't power off the device.
- To check if it has connected to the WiFi, check your mobile's Wifi available network. You will find the Rasberry Pi there. Take the IP address from there. Getting the IP is important

# Connect RasberryPi using Putty and Enable VNC settings

- Download PuTTY from [here](https://www.putty.org/)
- Add the IP address of the RasberryPi as hostname and port 22 ( you had enabled SSH already )
- click connect to PuTTY
- It should open a command window and ask for a username and password
- Add the username and password that you had set during setup
- It will connect to the RaspberryPi if the IP, username and password are correct

```
login as: myusername
rasbpisom@10.0.0.145's password:
Linux raspberrypi 6.1.0-rpi7-rpi-v8 #1 SMP PREEMPT Debian 1:6.1.63-1+rpt1 (2023-11-24) aarch64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Dec  5 00:05:38 2023
myusername@raspberrypi:~ $

```
## Enable Static IP for RaspberryPi [click here](https://github.com/e2eSolutionArchitect/RaspberryPi/blob/main/setup-raspberryPi4-staticIP.md)

# Enable VNC 
Run sudo raspi-config > select Interface setting > Enable VNC > Enable Yes > Finish

```
myusername@raspberrypi:~ $ sudo raspi-config
Generating key...
Done
Generating RSA key...
Done
myusername@raspberrypi:~ $
```
Again run sudo raspi-config and this time select Display settings.
Select the VNC display and select the max display. Finish > Reboot

# Connect VNC viewer

- [Download](https://www.realvnc.com/en/connect/download/viewer/) Open VNC viewer
- Add the IP address of your Raspberry Pi and click connect
- Enter username and password of Raspberry Pi
- Click Continue
- It should open the Window of Raspberry Pi

# Update Raspberry Pi before start using
- After the VNC viewer connects to RaspberryPi the top right first icon ( install updates) . Get the latest updates of Raspberry Pi. It might take few minutes to download and install all updates

# Awesome. That's it. Now start experimenting with your new toy!
