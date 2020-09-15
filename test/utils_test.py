import unittest
from quizc.utils.class_loader import get_class_instance_by_name


class UtilsTest(unittest.TestCase):

    def test_class_loader(self):
        class_sample_instance = get_class_instance_by_name("test.class_sample", "ClassSample")
        self.assertEqual("MyClass", class_sample_instance.name)


if __name__ == '__main__':
    unittest.main()
