Freshwater Toolbox 
===================
*Compute thermodynamic properties of lake water*

|Build Status|

The freshwater toolbox is a python package for estimating thermodynamic properties of water in freshwater bodies. Given temperature, salinity, and pressure, the freshwater toolbox enables the user to estimate the density, thermal expansion coefficient, specific heat capacity, speed of sound, temperature of maximum density, and freezing point of a parcel of lake water. The equation of state described in Chen and Millero (1986) [1]_ is implemented, which is suited for lake waters over the range of temperature, salinity, and pressure of 0--30 °C, 0--0.6 g/kg, and 0--180 bar, respectively.

Links
-----

-  Documentation: https://danielrobb.github.io/freshwater
-  Source code: https://github.com/danielrobb/freshwater

Installation
------------

The easiest way to install the freshwater toolbox is using pip::

    pip install freshwater

You can also clone the source code from the `github repository <https://github.com/danielrobb/freshwater>`_ and install it with the following commands::

    git clone https://github.com/danielrobb/freshwater
    cd freshwater/
    pip install .

Quick Start
------------

Say you have a sample of lake water with temperature 10 °C, salinity 0.5 g/kg, and pressure 0 bar, and you would like to compute its density 𝜌 and thermal expansion coefficient 𝛼. This can be done with the following commands.

First, import the equation of state (Eos) class::

   >>> from freshwater.eos import Eos

Second, ``Eos`` takes arguments of temperature, salinity and pressure::

   >>> e = Eos(t=10, s=0.5, p=0)
   >>> e.rho
   1000.091963
   >>> e.alpha
   8.94332e-05

Please consult the `online documentation <https://danielrobb.github.io/freshwater>`_ for more details.

.. |Build Status| image:: https://travis-ci.org/danielrobb/freshwater.svg?branch=master
   :target: https://travis-ci.org/github/danielrobb/freshwater
   :alt: travis-ci build status

.. [1] Chen, C. T. A., & Millero, F. J. (1986). Thermodynamic properties for natural waters covering only the limnological range. *Limnology and Oceanography*, 31(3), 657-662. `doi  <https://doi.org/10.4319/lo.1986.31.3.0657>`_


