from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        biden = Runner('joe')
        for i in range(10):
            biden.walk()
        self.assertEqual(biden.distance,50)
    def test_run(self):
        scholz = Runner('olaf')
        for i in range(10):
            scholz.run()
        self.assertEqual(scholz.distance,100)
    def test_challenge(self):
        blinken = Runner('antony')
        rice = Runner('condoleezza')
        for k in range(10):
            blinken.run()
            rice.walk()
        self.assertNotEqual(blinken.distance,rice.distance)

if __name__ == "__main__":
    unittest.main()
