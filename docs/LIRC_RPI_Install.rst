Getting LIRC on Raspberry Pi
============================


Installation
------------

.. code:: bash

  sudo apt-get install lirc

Configuration
-------------

Make sure you have these lines in your /etc/lirc/hardware.conf file:

::

    DRIVER="default"
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"

Check the kernel version in a terminal:

.. code:: bash

  uname -r

For kernel versions >= 3.18, add this line to /boot/config.txt:

::

    dtoverlay=lirc_rpi

For kernel versions < 3.18, add these lines to /etc/modules:

::

    lirc_dev
    lirc_rpi


Reboot, or restart `lircd` for these changes to take effect:

.. code:: bash

    /etc/init.d/lirc restart

OR

.. code:: bash

    sudo /etc/init.d/lirc stop && /etc/init.d/lirc start


Customization
-------------

Default settings can be overridden as follows:

::

    dtoverlay=lirc-rpi,gpio_in_pin=17,gpio_out_pin=13

Or, for kernels older than 3.18:

::

    lirc_rpi gpi_in_pin=17 gpio_out_pin=13


References
----------

- `Raspberry Pi Firmware Overlays`_
- `Setting Up LIRC on the Raspberry Pi`_

.. _Raspberry Pi Firmware Overlays: https://github.com/raspberrypi/firmware/blob/master/boot/overlays/README#L504
.. _Setting Up LIRC on the Raspberry Pi: http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/
