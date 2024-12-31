from runner_and_tournament import Runner, Tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        biden = Runner('joe')
        for i in range(10):
            biden.walk()
        self.assertEqual(biden.distance,50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        scholz = Runner('olaf')
        for i in range(10):
            scholz.run()
        self.assertEqual(scholz.distance,100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        blinken = Runner('antony')
        rice = Runner('condoleezza')
        for k in range(10):
            blinken.run()
            rice.walk()
        self.assertNotEqual(blinken.distance,rice.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    def setUp(self):
        self.usn = Runner('Usain',10)
        self.anr = Runner('Andrey', 9)
        self.nik = Runner('Nick',3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for elm in cls.all_results:
            print(*elm)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_Tournament1(self):
        cmptsh1 = Tournament(90,self.usn,self.nik)
        my_dict = cmptsh1.start()
        self.assertEqual(my_dict[2].name, self.nik.name)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_Tournament2(self):
        cmptsh2 = Tournament(90, self.anr, self.nik)
        my_dict = cmptsh2.start()
        self.assertEqual(my_dict[2].name, self.nik.name)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_Tournament3(self):
        cmptsh3 = Tournament(90, self.usn, self.anr, self.nik)
        my_dict = cmptsh3.start()
        self.assertEqual(my_dict[3].name, self.nik.name)

if __name__ == "__main__":
    unittest.main()
