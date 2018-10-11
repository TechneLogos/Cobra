import unittest
import PyEventLib


def test_handler():
    pass


def another_handler():
    pass


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.test_event = PyEventLib.CustomEvent()

    def test_add_listeners(self):
        """Checks that listeners are correctly added."""
        self.test_event.bind(test_handler, another_handler)

    def test_remove_listener(self):
        self.test_event.bind(test_handler)
        self.test_event.unbind(test_handler)

    def test_clear_listeners(self):
        self.test_event.clear()


class TestCustomEvents(TestEvents):
    def setUp(self):
        self.test_event = PyEventLib.CustomEvent()

    def test_dispatch(self):
        self.test_event()


if __name__ == "__main__":
    unittest.main()
