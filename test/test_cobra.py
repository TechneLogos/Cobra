import unittest
import logging
import cobra


def handler_func():
    print("hnadler")


def listener_func1():
    print("listener 1")


def listener_func2():
    print("listener 2")


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.event_system = cobra.EventSystem("TestSystem")
        self.test_event = cobra.Event()

    def test_event_init(self):
        self.assertIsInstance(cobra.Event(), cobra.Event)

    def test_set_handler(self):
        self.test_event.set_handler(handler_func)

    def test_add_listeners(self):
        error_msg = "Listeners were not correctly added."
        self.test_event.add_listener(listener_func1, listener_func2)
        self.assertIn(listener_func1, self.test_event.get_listeners(),
                      error_msg)
        self.assertIn(listener_func1, self.test_event.get_listeners(),
                      error_msg)

    def test_remove_listener(self):
        error_msg = "Listeners were not correctly removed."
        self.test_event.remove_listener(listener_func1)
        self.assertNotIn(listener_func1, self.test_event.get_listeners(),
                         error_msg)

    def test_clear_listeners(self):
        self.test_event.clear_listeners()

    def test_invalid_listener(self):
        self.assertRaises(TypeError, self.test_event.add_listener(), None)


class TestEventSystem(unittest.TestCase):
    def setUp(self):
        self.event_system = cobra.EventSystem("TestSystem")

    def test_loggers(self):
        """checks that the EventSysstem logs correctly."""
        self.assertLogs(logging.getLogger("EventSystem"))
        self.assertLogs(logging.getLogger("EventSystem").
                        getChild(self.event_system.name))
        self.assertLogs(logging.getLogger("EventSystem").
                        getChild(self.event_system.name).getChild("test"))


if __name__ == "__main__":
    unittest.main()
