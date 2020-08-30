import numpy as np
from .constants import Constants

class Eos():

    def __init__(self, t, s=0, p=0):
        self.t = t
        self.s = s
        self.p = p
        self.c = Constants()
        self.compute()

    def compute_rho(self):
        c = self.c
        rho = polyval_r(c.a, self.t) + polyval_r(c.b, self.t)*self.s
        if self.p != 0:
            K = (polyval_r(c.c, self.t)
                 + polyval_r(c.d, self.t) * self.p
                 + (c.e[0] + c.e[1]*self.t + c.e[2]*self.p) * self.s)
            rho = rho / (1 - self.p/K)
        self.rho = rho * 1000.

    def compute_alpha(self):
        c = self.c
        self.alpha = ((polyval_r(c.f, self.t)
                      + polyval_r(c.g, self.t) * self.s
                      + (polyval_r(c.h[:3], self.t) + c.h[3]*self.s) * self.p)
                      * 1e-6)

    def compute_tmd(self):
        c = self.c
        self.tmd = (c.i[0] + c.i[1]*self.p + c.i[2]*self.p**2
                    - (c.i[3]+c.i[4]*self.p)*self.s)

    def compute_sound_speed(self):
        c = self.c
        self.sound_speed = (polyval_r(c.j, self.t)
                            + polyval_r(c.k, self.t) * self.s
                            + ((polyval_r(c.l[:3], self.t) + c.l[3] * self.s)
                               * self.p)
                            + c.m[0]*self.p**2)

    def compute(self):
        self.compute_rho()
        self.compute_alpha()
        self.compute_tmd()
        self.compute_sound_speed()


def polyval_r(p, x):
    return np.polyval(np.flipud(p), x)
