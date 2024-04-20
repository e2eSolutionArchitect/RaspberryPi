# Setup StaticIP for RaspberryPi4

***Prerequisites***
- Please make sure you have completed the RaspberryPi setup and you can connect to your RaspberryPi using the VNC viewer. [Click here](https://github.com/e2eSolutionArchitect/RaspberryPi/blob/main/setup-raspberryPi4.md) for setup instructions.


Steps for Static IP setup
- Check the currently assigned IP. Run below command 
```
ipconfig
```
If you are connecting wirelessly ( using wifi) then check 'wlan0'. If you are connecting via ethernet cable then check 'eth0' 
- check 'inet addr: ###.###.###.###'. It is your current ip assigned. Which is the one you use in Putty to connect to your RaspberryPi device.
- 
