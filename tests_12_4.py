
import unittest
from rt_with_exceptions import Runner,Tournament
import logging

logging.basicConfig(level='INFO', filemode='w', filename='runner_tests.log',encoding='UTF-8',format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            biden = Runner('joe',-5)
            logging.INFO('"test_walk" выполнен успешно')
        except:
            logging.WARNING("Неверная скорость для Runner")
        for i in range(10):
            biden.walk()
        self.assertEqual(biden.distance,50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            scholz = Runner(0)
            logging.INFO('"test_run" выполнен успешно')
        except:
            logging.WARNING("Неверный тип данных для объекта Runner")
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

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second)

print(t.start())
