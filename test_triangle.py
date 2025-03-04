import unittest
import triangle


class TriangleTest(unittest.TestCase):
    ''' модуль UNITTEST, проверяющий корректность вычислений функции вычисления площади треугольника'''
    def test_area_1(self):
        res = triangle.area(2, 3)
        self.assertEqual(res, 3)

    def test_area_2(self):
        res = triangle.area(0, 4)
        self.assertEqual(res, "The figure doesn't exist")

    def test_area_3(self):
        res = triangle.area(-1, 3)
        self.assertEqual(res, "Invalid input")

    def test_area_4(self):
        res = triangle.area(2, 'b')
        self.assertEqual(res, "Invalid input")

    def test_area_5(self):
        res = triangle.area(3, True)
        self.assertEqual(res, "Invalid input")

    ''' модуль UNITTEST, проверяющий корректность вычислений функции вычисления периметра треугольника'''
    def test_perimeter_1(self):
        res = triangle.perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_perimeter_2(self):
        res = triangle.perimeter(0, 2, 3)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_3(self):
        res = triangle.perimeter(-1, 2, 3)
        self.assertEqual(res, "Invalid input")

    def test_perimeter_4(self):
        res = triangle.perimeter(-1, 'N', 3)
        self.assertEqual(res, "Invalid input")

    def test_perimeter_5(self):
        res = triangle.perimeter(2, 13, 56)
        self.assertEqual(res, "The figure doesn't exist")

    def test_perimeter_6(self):
        res = triangle.perimeter(False, 3, 5)
        self.assertEqual(res, "Invalid input")


if __name__ == '__main__':
    unittest.main()
