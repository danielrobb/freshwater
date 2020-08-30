class Constants():
    """Constants from Chen and Millero (1986)."""

    def __init__(self):
        self._init_constants()

    def _init_constants(self):
        # Density (Eqs. 1--3)
        self.a = [0.9998395, 6.7914e-5, -9.0894e-6, 1.0171e-7, -1.2846e-9,
                  1.1592e-11, -5.0125e-14]
        self.b = [8.181e-4, -3.85e-6, 4.98e-8]
        self.c = [19652.17, 148.113, -2.293, 1.256e-2, -4.18e-5]
        self.d = [3.2726, -2.147e-4, 1.128e-4]
        self.e = [53.238, -0.313, 5.728e-3]

        # Thermal expansivity (Eq. 5)
        self.f = [-68.00, 18.2091, -0.30866, 5.3445e-3, -6.0721e-5, 3.1441e-7]
        self.g = [4.599, -0.1999, 2.790e-3]
        self.h = [0.3682, -1.520e-2, 1.91e-4, -4.613e-3]

        # Temperature of maximum density (Eq. 7)
        self.i = [3.9839, -1.9911e-2, -5.822e-6, 0.2219, 1.106e-4]

        # Speed of sound (Eq. 15)
        self.j = [1402.388, 5.0371, -5.8085e-2, 3.342e-4, -1.478e-6, 3.146e-9]
        self.k = [1.322, -7.01e-3, 4.9e-5]
        self.l = [0.15564, 4.046e-4, -8.15e-7, -5.58e-5]
        self.m = [1.593e-5]

        # Heat capacity (Eq. 12)
        self.n = [4.2174, -3.6608e-3, 1.3129e-4, -2.210e-6, 1.508e-8]
        self.o = [-6.616e-5, 9.28e-6, -2.39e-8]
        self.p = [-4.917e-4, 1.335e-5, -2.177e-7, 3.441e-6]
        self.q = [1.50e-7]

        # Freezing temperature (Eq. 18)
        self.r = [-0.0137, -0.052, -7.48e-3]
