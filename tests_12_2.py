from runner_and_tournament import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):

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

    def test_Tournament1(self):
        cmptsh1 = Tournament(90,self.usn,self.nik)
        my_dict = cmptsh1.start()
        print(my_dict[1].name, my_dict[2].name)
        self.assertEqual(my_dict[2].name, self.nik.name)

    def test_Tournament2(self):
        cmptsh2 = Tournament(90, self.anr, self.nik)
        my_dict = cmptsh2.start()
        print(my_dict[1].name, my_dict[2].name)
        self.assertEqual(my_dict[2].name, self.nik.name)

    def test_Tournament3(self):
        cmptsh3 = Tournament(90, self.usn, self.anr, self.nik)
        my_dict = cmptsh3.start()
        print(my_dict[1].name,my_dict[2].name,my_dict[3])
        self.assertEqual(my_dict[3].name, self.nik.name)

if __name__ == "__main__":
    unittest.main()
