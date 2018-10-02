import unittest
import cobra


def func1():
    pass


def func2():
    pass


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.test_event = cobra.CustomEvent()

    def test_add_listeners(self):
        """Checks that listeners are correctly added."""
        self.test_event.bind(func1, func2)

    def test_remove_listener(self):
        self.test_event.unbind(func1)

    def test_clear_listeners(self):
        self.test_event.clear()


if __name__ == "__main__":
    unittest.main()
