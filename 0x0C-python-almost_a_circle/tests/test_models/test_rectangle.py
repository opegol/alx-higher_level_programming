#!/usr/bin/python3

"""Definition for rectangle.py unit tests.
Unittest classes:
    TestRectangle_init
    TestRectangle_width
    TestRectangle_height
    TestRectangle_x
    TestRectangle_area 
    
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    """Unittests for Rectangle class initialization."""

    def test_a1(self):
        self.assertIsInstance(Rectangle(2, 3), Base)

    def test_a2(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_a3(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_a4(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a5(self):
        r1 = Rectangle(1, 2, 4)
        r2 = Rectangle(5, 6, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a6(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a7(self):
        self.assertEqual(9, Rectangle(10, 2, 0, 0, 9).id)

    def test_a8(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_a9(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 0, 1, 1).__width)

    def test_a10(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 0, 1, 1).__height)

    def test_a11(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 0, 1, 1).__x)

    def test_a12(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 4, 0, 1, 1).__y)

    def test_width_getter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        self.assertEqual(7, r.width)

    def test_width_setter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        r.width = 12
        self.assertEqual(12, r.width)

    def test_height_getter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        self.assertEqual(6, r.height)

    def test_height_setter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        self.assertEqual(8, r.x)

    def test_x_setter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        r.x = 11
        self.assertEqual(11, r.x)

    def test_y_getter(self):
        r = Rectangle(7, 6, 8, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 9
        self.assertEqual(9, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""
    
    def test_b1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_b2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 4)

    def test_b3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(8.1, 1)

    def test_b4(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_b5(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_b6(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)
    
    def test_b7(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 11)

    def test_b8(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_b9(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_c1(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_c2(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "inv")

    def test_c3(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 8.1)

    def test_c4(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_c5(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -2)

    def test_c6(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests forRectangle x attribute."""

    def test_d1(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, None)

    def test_d2(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "inv", 2)

    def test_d3(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 8.1, 9)

class TestRectangle_area(unittest.TestCase):
    """Unittests for area method of the Rectangle class."""

    def test_e1(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_e2(self):
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 6
        r.height = 10
        self.assertEqual(60, r.area())


if __name__ == "__main__":
    unittest.main()

