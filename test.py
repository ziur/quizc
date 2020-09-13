import unittest
from quizc import quiz


class TestQuizc(unittest.TestCase):

    def test_form(self):
        form = quiz.run("My Form")

        self.assertEqual("My Form", form.title)


if __name__ == '__main__':
    unittest.main()
