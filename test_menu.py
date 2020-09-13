import unittest
from quizc.menu import Menu


class TestMenu(unittest.TestCase):

    def test_menu(self):
        menu = Menu()
        menu.show_main_menu()
        #self.assertEqual("My Form", form.title)


if __name__ == '__main__':
    unittest.main()
