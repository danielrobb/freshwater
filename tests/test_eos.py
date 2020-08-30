import unittest
from freshwater.eos import Eos

class TestEos(unittest.TestCase):

    def test_rho(self):
        self.eos = Eos(t=10, s=0.5, p=00)
        rho = self.eos.rho
        self.assertAlmostEqual(rho, 1000.0920, places=4)

    def test_alpha(self):
        self.eos = Eos(t=15, s=0, p=50)
        alpha = self.eos.alpha
        self.assertAlmostEqual(alpha*1e6, 160.05, places=2)

    def test_tmd(self):
        self.eos = Eos(t=10, s=0.5, p=100)
        tmd = self.eos.tmd
        self.assertAlmostEqual(tmd, 1.8181, places=4)

    def test_u(self):
        self.eos = Eos(t=10, s=0.5, p=100)
        u = self.eos.u
        self.assertAlmostEqual(u, 1464.016, places=3)

    def test_cp(self):
        self.eos = Eos(t=10, s=0.5, p=100)
        cp = self.eos.cp 
        self.assertAlmostEqual(cp, 4155.55, places=2)

    def test_tf(self):
        self.eos = Eos(t=10, s=0.5, p=100)
        tf = self.eos.tf
        self.assertAlmostEqual(tf, -0.7877, places=4)

if __name__ == "__main__":
    unittest.main()
