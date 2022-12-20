import unittest
import try_it_yourself_11


class TestFramework(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = try_it_yourself_11.Employee("Garry", "Garryson")

    def test_E11_1_1(self):
        self.assertEqual(
            "Wellington, New Zealand",
            try_it_yourself_11.city_name_E11_1("wellington", "new zealand"),
        )

    def test_E11_1_2(self):
        self.assertNotEqual(
            "Wellington, New Zealand",
            try_it_yourself_11.city_name_E11_1("new zealand", "new zealand"),
        )

    def test_E11_2_1(self):
        self.assertEqual(
            "Wellington, New Zealand",
            try_it_yourself_11.city_name_E11_2("wellington", "new zealand"),
        )

    def test_E11_2_2(self):
        self.assertNotEqual(
            "Wellington, New Zealand",
            try_it_yourself_11.city_name_E11_2("new zealand", "new zealand"),
        )

    def test_E11_3_1(self):
        self.assertEqual(self.employee.salary, 45000)
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 50000)
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 60000)


if __name__ == "__main__":
    unittest.main()
