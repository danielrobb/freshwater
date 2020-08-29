from numpy import empty, polyval, flipud

class EquationOfState:
    """Compute thermodynamic properties of (relatively) fresh water.

    Attributes
    ----------
    a, b, ... , m : array_like
        Coefficients from the equations in Chen and Millero (1986).

    Methods
    -------
    density(t, s=0, p=0):
        Computes the density (kg/m^3) from temperature, salinity, and pressure.
    alpha(t, s=0, p=0):
        Computes the thermal expansivity (deg C)^{-1} from t, s, and p.
    tmd(t, s=0, p=0):
        Computes the temperature of maximum density (deg C) from t, s, and p.
    sound_speed(t, s=0, p=0):
        Computes the speed of sound (m/s) from t, s, and p.
    
    References
    ----------
    .. [1] Chen and Millero (1986) Limnol. Oceanogr., 31(3), 657-662.
    """

    def __init__(self):
        self._init_coeffs()
        
    def density(self, t, s=0, p=0):
        rho = (polyval(flipud(self.a), t)
               + polyval(flipud(self.b), t) * s)
        if p != 0:
            K = (polyval(flipud(self.c), t)
                 + polyval(flipud(self.d), t) * p
                 + (self.e[0] + self.e[1]*t + self.e[2]*p) * s)
            rho = rho / (1 - p/K)
        return rho * 1000.

    def alpha(self, t, s=0, p=0):
        return (polyval(flipud(self.f), t)
                + polyval(flipud(self.g), t) * s
                + (polyval(flipud(self.h[:3]), t) + self.h[3]*s) * p) * 1e-6

    def tmd(self, t, s=0, p=0):
        return (self.i[0] + self.i[1]*p + self.i[2]*p**2
                    - (self.i[3] + self.i[4]*p) * s)

    def sound_speed(self, t, s=0, p=0):
        return (polyval(flipud(self.j), t)
                + polyval(flipud(self.k), t) * s
                + (polyval(flipud(self.l[:3]), t) + self.l[3]*s) * p
                + self.m[0] * p**2)

    def _init_coeffs(self):
        # Density (Eqs. 1--3)
        self.a = empty(7)
        self.b = empty(3)
        self.c = empty(5)
        self.d = empty(3)
        self.e = empty(3)
        self.a[0] = 0.9998395
        self.a[1] = 6.7914e-5
        self.a[2] = -9.0894e-6
        self.a[3] = 1.0171e-7
        self.a[4] = -1.2846e-9
        self.a[5] = 1.1592e-11
        self.a[6] = -5.0125e-14
        self.b[0] = 8.181e-4
        self.b[1] = -3.85e-6
        self.b[2] = 4.98e-8
        self.c[0] = 19652.17
        self.c[1] = 148.113
        self.c[2] = -2.293
        self.c[3] = 1.256e-2
        self.c[4] = -4.18e-5
        self.d[0] = 3.2726
        self.d[1] = -2.147e-4
        self.d[2] = 1.128e-4
        self.e[0] = 53.238
        self.e[1] = -0.313
        self.e[2] = 5.728e-3

        # Thermal expansivity (Eq. 5)
        self.f = empty(6)
        self.g = empty(3)
        self.h = empty(4)
        self.f[0] = -68.00 
        self.f[1] = 18.2091
        self.f[2] = -0.30866
        self.f[3] = 5.3445e-3
        self.f[4] = -6.0721e-5
        self.f[5] = 3.1441e-7
        self.g[0] = 4.599 
        self.g[1] = -0.1999
        self.g[2] = 2.790e-3
        self.h[0] = 0.3682
        self.h[1] = -1.520e-2
        self.h[2] = 1.91e-4
        self.h[3] = -4.613e-3

        # Temperature of maximum density (Eq. 7)
        self.i = empty(5)
        self.i[0] = 3.9839 
        self.i[1] = -1.9911e-2
        self.i[2] = -5.822e-6
        self.i[3] = 0.2219
        self.i[4] = 1.106e-4

        # Speed of sound (Eq. 15)
        self.j = empty(6)
        self.k = empty(3)
        self.l = empty(4)
        self.m = empty(1)
        self.j[0] = 1402.388 
        self.j[1] = 5.0371
        self.j[2] = -5.8085e-2
        self.j[3] = 3.342e-4
        self.j[4] = -1.478e-6
        self.j[5] = 3.146e-9
        self.k[0] = 1.322 
        self.k[1] = -7.01e-3
        self.k[2] = 4.9e-5
        self.l[0] = 0.15564 
        self.l[1] = 4.046e-4
        self.l[2] = -8.15e-7
        self.l[3] = -5.58e-5
        self.m[0] = 1.593e-5
