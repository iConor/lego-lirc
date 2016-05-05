LEGO Power Functions LIRC
=========================

***Linux Infrared Remote Control configuration files for LEGO Power Functions RC v1.20.***    

Setup
-----

LIRC_RPI_install.md includes the necessary steps to get LIRC up and running on a Raspberry Pi.

Jorge Pereira's blog post, [Infrared Remote Control](http://ofalcao.pt/blog/en/2014/infrared-remote-control), demonstrates how to use LEGO LIRC with a headphone jack.

References
----------

- LPF_RC_Protocol.rst contains the protocol definition and encoding/decoding timing parameters.
- LPF_RC_Modes.rst contains mode-specific data and deviations from the standard protocol.



Known Issues
------------
- The Extended Mode generation code is included, however, it has not yet been tested.
- Of Single Output Mode's two sub-modes, PWM is implemented while Clear/Set/Toggle/Inc/Dec is not.

---

**Compatible Hardware:** *[8884 IR Receiver](http://powerfunctions.lego.com/en-us/ElementSpecs/8884.aspx) | [8885 IR Remote Control](http://powerfunctions.lego.com/en-us/ElementSpecs/8885.aspx) | [8879 IR Speed Remote Control](http://powerfunctions.lego.com/en-us/ElementSpecs/8879.aspx)*  
**Reference Documentation:** *[LIRC Configuration File Format](http://www.lirc.org/html/lircd.conf.html) | [LEGO Power Functions RC v1.20](http://cache.lego.com/Media/Download/PowerfunctionsElementSpecsDownloads/otherfiles/download9FC026117C091015E81EC28101DACD4E/8884RemoteControlIRReceiver_Download.pdf)*  

---
[MIT License](http://github.com/iConor/lego-lirc/blob/master/LICENSE)
