import unittest
import logging
import cobra


def listener_func1():
    print("listener 1")


def listener_func2():
    print("listener 2")


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.test_event = cobra.CustomEvent()

    def test_add_listeners(self):
        """Checks that listeners are correctly added."""
        self.test_event.add_listener(listener_func1, listener_func2)

    def test_remove_listener(self):
        self.test_event.remove_listener(listener_func1)

    def test_clear_listeners(self):
        self.test_event.clear_listeners()


if __name__ == "__main__":
    unittest.main()
