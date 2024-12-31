import unittest
from unittest import TextTestRunner

import runner_and_tournament
import tests_12_3


run_turnST = unittest.TestSuite()
# run_turnST.addTest(unittest.makeSuite(tests_12_3.TournamentTest))
run_turnST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
run_turnST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

check1 = TextTestRunner(verbosity=2)

check1.run(run_turnST)