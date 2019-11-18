import unittest


class TestSetProperties(unittest.TestCase):
    def test_unique(self):
        test_set = {1, 1, 1, 1, 2, 3}
        self.assertEqual(test_set, {1, 2, 3})

    def test_different_sets(self):
        first_set = {1, 2, 3}
        second_set = {3, 2, 1}
        self.assertEqual(first_set, second_set)

    def test_copy(self):
        first_set = {1, 2, 3}
        second_set = first_set.copy()
        self.assertEqual(first_set, second_set)

    def test_add_the_same(self):
        test_set = {1, 2, 3}
        test_set.add(3)
        self.assertEqual(test_set, {1, 2, 3})

    def test_add_not_the_same(self):
        test_set = {1, 2}
        test_set.add(3)
        self.assertEqual(test_set, {1, 2, 3})

    def test_different_sets_differ(self):
        first_set = {1, 2, 3, 4}
        second_set = {1, 2, 3}
        self.assertNotEqual(first_set, second_set)

    def test_delete(self):
        test_set = {1, 2, 3}
        test_set.remove(3)
        self.assertNotIn(3, test_set)

    def test_contains_element(self):
        test_set = {1, 2, 3}
        self.assertIn(1, test_set)

    def test_contains_notNone(self):
        test_set = {1}
        self.assertIsNotNone(test_set)

    def test_not_contains_element(self):
        test_set = {1, 2, 3}
        self.assertNotIn(4, test_set)


if __name__ == '__main__':
    unittest.main()
