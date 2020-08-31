import numpy as np
from .constants import Constants

class Eos():
    """Equation of state for freshwater from Chen and Millero (1986).

    Attributes
    ----------
    t : array_like
        temperature (:math:`\mathrm{^{\circ} C}`)
    s : array_like
        salinity (g/kg) grams of dissolved salt in 1 kg of lake water
    p : array_like
        pressure (bar) applied pressure
    rho : array_like
        density of lake water (:math:`\mathrm{kg \, m^{-3}}`)
    alpha : array_like
        Coefficient of thermal expansion :math:`\mathrm{(^{\circ} C)^{-1}}`
    tmd : array_like
        Temperature of maximum density (:math:`\mathrm{^{\circ} C}`)
    u : array_like
        Speed of sound (:math:`\mathrm{m \, s^{-1}}`)
    cp : array_like
        Specific heat capacity (:math:`\mathrm{J \, kg^{-1} \, ^{\circ} C^{-1}}`)
    tf : array_like
        Freezing point of lake water (:math:`\mathrm{^{\circ} C}`)

    References
    ----------
    .. [1] Chen, C. T. A., & Millero, F. J. (1986). Thermodynamic properties 
        for natural waters covering only the limnological range 1. Limnology and
        Oceanography, 31(3), 657-662.

    Examples
    --------
    Import the class Eos (Equation of state) from the freshwater module

    >>> from freshwater.eos import Eos

    Compute properties of lake water with a temperature of 10 deg C,
    a salinity of 0.5 g/kg and a pressure of 0 bar (gauge pressure).

    >>> e = Eos(t=10, s=0.5, p=0)
    >>> e.rho
    1000.091963
    >>> e.alpha
    8.9433231e-05
    >>> e.tmd
    3.87295
    """

    def __init__(self, t, s=0, p=0):
        self.t = t
        self.s = s
        self.p = p
        self.c = Constants()
        self._compute()

    def _compute_rho(self):
        c = self.c
        rho = polyval_r(c.a, self.t) + polyval_r(c.b, self.t)*self.s
        if np.any(self.p) != 0:
            K = (polyval_r(c.c, self.t)
                 + polyval_r(c.d, self.t) * self.p
                 + (c.e[0] + c.e[1]*self.t + c.e[2]*self.p) * self.s)
            rho = rho / (1 - self.p/K)
        self.rho = rho * 1000.

    def _compute_alpha(self):
        c = self.c
        self.alpha = ((polyval_r(c.f, self.t)
                      + polyval_r(c.g, self.t) * self.s
                      + (polyval_r(c.h[:3], self.t) + c.h[3]*self.s) * self.p)
                      * 1e-6)

    def _compute_tmd(self):
        c = self.c
        self.tmd = (c.i[0] + c.i[1]*self.p + c.i[2]*self.p**2
                    - (c.i[3]+c.i[4]*self.p)*self.s)

    def _compute_u(self):
        c = self.c
        self.u = (polyval_r(c.j, self.t)
                  + polyval_r(c.k, self.t) * self.s
                  + ((polyval_r(c.l[:3], self.t) + c.l[3] * self.s)
                     * self.p)
                  + c.m[0]*self.p**2)

    def _compute_cp(self):
        c = self.c
        self.cp = (polyval_r(c.n, self.t)
                            + polyval_r(c.o, self.t) * self.s
                            + ((polyval_r(c.p[:3], self.t) + c.p[3] * self.s)
                               * self.p)
                            + c.q[0]*self.p**2) * 1000.

    def _compute_tf(self):
        c = self.c
        self.tf = c.r[0] + c.r[1]*self.s + c.r[2]*self.p

    def _compute(self):
        self._compute_rho()
        self._compute_alpha()
        self._compute_tmd()
        self._compute_u()
        self._compute_cp()
        self._compute_tf()

def polyval_r(p, x):
    """Identical to numpy.polyval except p is an array of coefficients 
       of increasing order instead of decreasing order.
    """
    return np.polyval(np.flipud(p), x)
