import unittest
from unittest.mock import Mock
import libevent


output = []


class TestEvents(unittest.TestCase):
    def setUp(self):
        self.test_event = libevent.Event()

    def test_add_listeners(self):
        """Checks that listeners are correctly added."""
        mock_function = Mock()
        self.test_event.subscribe(mock_function)
        self.assertIn(mock_function, self.test_event._listeners, "The event handler was not added.")

    def test_add_multiple_listeners(self):
        """"""
        mock_function_1 = Mock()
        mock_function_2 = Mock()
        self.test_event.subscribe(mock_function_1, mock_function_2)
        self.assertIn(mock_function_1, self.test_event._listeners, "The first handler was not subscribed to the event.")
        self.assertIn(mock_function_2, self.test_event._listeners, "The second handler was not subscribed to the event.")

    def test_remove_listener(self):
        """Checks that listeners are correctly removed."""
        mock_function = Mock()
        self.test_event.subscribe(mock_function)
        self.test_event.unsubscribe(mock_function)
        self.assertNotIn(mock_function, self.test_event._listeners, "The event handler was not added.")

    def test_clear_listeners(self):
        mock_function = Mock()
        self.test_event.subscribe(mock_function)
        self.test_event.clear()
        self.assertTrue(not self.test_event._listeners)

    def test_dispatch_with_no_handlers(self):
        pass

    def test_handler_with_arguements(self):
        """Ensure that events correctly handle passed parameters."""
        self.test_event.subscribe
        self.test_event._dispatch(None, 5, title="Hello")


class TestCustomEvents(TestEvents):
    def setUp(self):
        self.test_event = libevent.CustomEvent()

    def test_dispatch(self):
        mock_function = Mock()
        self.test_event.subscribe(mock_function)
        self.test_event.dispatch()
        mock_function.assert_called()


if __name__ == "__main__":
    unittest.main()
