# test.py
import unittest
from random import choice, randint
from app import Figure  # Файл app.py має містити клас Figure

class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Виконується лише раз на початку тестування."""
        pass
    
    def setUp(self) -> None:
        """Виконується перед кожним тестом."""
        self.figure = choice(Figure.FIGURES)
        self.length = randint(1, 10)
        self.obj = Figure(self.figure, self.length)
        return super().setUp()

    def tearDown(self) -> None:
        del self.obj
        return super().tearDown()

    def test_figure_type(self):
        print(f"Тестуємо вивід: {self.figure} == {self.obj.get_figure_type}")
        self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")

    def test_figure_lengh(self):
        # Очікується, що це тест провалиться через навмисну помилку в методі get_figure_length
        self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")

    def test_obj(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)  # Створення фігури з недозволеними параметрами має викликати помилку.

if __name__ == '__main__':
    unittest.main(verbosity=2)
