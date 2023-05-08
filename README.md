ModbusTCP/IP and OpenCV handTracking
===============
In this procjet data about relative finger poses is made available through modbus TCP/IP protocol. For data capture The System Management Console (allows you to monitor the application in real-time so that problems can be acted upon immediately) it was used. Below show example configuration.

## Dependencies
Tested on python 3.10.4  
Required modules:
```bash
    pip install opencv-python==4.5.5.64
    pip install mediapipe==0.8.7
    pip install pycaw
```
## SMC Configuration
![SMC_configuration](https://github.com/NavierMillennium/modbusTCP_hand_tracking/blob/master/screeenshots/smc_view.png?raw=true)

![SMC_configuration-device](https://github.com/NavierMillennium/modbusTCP_hand_tracking/blob/master/screenshots/smc_device_group.png?raw=true)

![SMC_configuration-items](https://github.com/NavierMillennium/modbusTCP_hand_tracking/blob/master/screenshots/smc_items.png?raw=true)

## Examples
* **Output image** 

![Image with markers](https://github.com/NavierMillennium/modbusTCP_hand_tracking/blob/master/screenshots/hand_tracking.png?raw=true)

## Links
* [Venv – creation of virtual environment ][1]
* [OpenCV – tutorial ][2]
* [Gesture Volume Control][3]


[1]:https://docs.python.org/3/library/venv.html
[2]:https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html
[3]:https://www.youtube.com/watch?v=9iEPzbG-xLE