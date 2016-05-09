LEGO Power Functions LIRC
=========================

**Linux Infrared Remote Control configuration files for LEGO Power Functions RC v1.20.**

----

Setup
-----

- Copy the included configuration files into the an appropriate folder (likely /etc/lirc/lircd.conf.d/lego).
- Add include directives to /etc/lirc/lircd.conf for each configuration file you wish to use, for example:

.. code:: bash

  echo "include /etc/lirc/lircd.conf.d/lego/Combo_PWM" >> /etc/lirc/lircd.conf

- includes the necessary steps to get LIRC up and running on a Raspberry Pi.
- Jorge Pereira's blog post, `Infrared Remote Control`_, demonstrates how to use LEGO LIRC with a headphone jack.

Known Issues
------------

- The Extended Mode generation code is included, however, it has not yet been tested.
- Of Single Output Mode's two sub-modes, PWM is implemented while Clear/Set/Toggle/Inc/Dec is not.

References
----------

| **Included:**
- LEGO_Power_Functions_RC_v120_ is a copy of LEGO's official documentation for their protocol.
- LPF_RC_Protocol_ contains a summarized protocol definition and encoding/decoding timing parameters.
- LPF_RC_Modes_ contains summarized mode-specific data and deviations from the standard protocol.
- LIRC_Remote_ contains common LIRC lircd.conf-style configuration file settings for the LEGO RC protocol.

| **Compatible Hardware:** `8884 IR Receiver`_ | `8885 IR Remote Control`_ | `8879 IR Speed Remote Control`_
| **Referenced Documentation:** `LIRC Configuration File Format`_ | `LEGO Power Functions RC v1.20`_

----

Released under the `MIT License`_.

.. _Infrared Remote Control: http://ofalcao.pt/blog/en/2014/infrared-remote-control

.. _8884 IR Receiver: http://powerfunctions.lego.com/en-us/ElementSpecs/8884.aspx
.. _8885 IR Remote Control: http://powerfunctions.lego.com/en-us/ElementSpecs/8885.aspx
.. _8879 IR Speed Remote Control: http://powerfunctions.lego.com/en-us/ElementSpecs/8879.aspx

.. _LIRC Configuration File Format: http://www.lirc.org/html/lircd.conf.html
.. _LEGO Power Functions RC v1.20: http://cache.lego.com/Media/Download/PowerfunctionsElementSpecsDownloads/otherfiles/download9FC026117C091015E81EC28101DACD4E/8884RemoteControlIRReceiver_Download.pdf

.. _LEGO_Power_Functions_RC_v120: https://github.com/iConor/lego-lirc/blob/master/docs/LEGO_Power_Functions_RC_v120.pdf
.. _LPF_RC_Protocol: https://github.com/iConor/lego-lirc/blob/master/docs/LPF_RC_Protocol.rst
.. _LPF_RC_Modes: https://github.com/iConor/lego-lirc/blob/master/docs/LPF_RC_Modes.rst
.. _LIRC_Remote: https://github.com/iConor/lego-lirc/blob/master/docs/LIRC_Remote.rst
.. _LIRC_RPI_Install: https://github.com/iConor/lego-lirc/blob/master/docs/LIRC_RPI_Install.md

.. _MIT License: http://github.com/iConor/lego-lirc/blob/master/LICENSE
