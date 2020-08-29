import unittest
from freshwater.equation_of_state import EquationOfState

class TestEquationOfState(unittest.TestCase):

    def setUp(self):
        self.eos = EquationOfState()

    def test_density(self):
        density = self.eos.density(t=10, s=0.5, p=0)
        self.assertAlmostEqual(density, 1000.0920, places=4)

    def test_alpha(self):
        alpha = self.eos.alpha(t=0, s=0, p=50)*1e6
        self.assertAlmostEqual(alpha, -49.59, places=2)

    def test_alpha2(self):
        alpha = self.eos.alpha(t=25, s=0, p=10)*1e6
        self.assertAlmostEqual(alpha, 258.25, places=2)

    def test_tmd(self):
        tmd = self.eos.tmd(t=10, s=0.5, p=100)
        self.assertAlmostEqual(tmd, 1.8181, places=4)

    def test_sound_speed(self):
        sound_speed = self.eos.sound_speed(t=10, s=0.5, p=100)
        self.assertAlmostEqual(sound_speed, 1464.016, places=3)

if __name__ == "__main__":
    unittest.main()
