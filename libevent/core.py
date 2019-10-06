class Event(object):
    """The base class that all Events inherit from."""

    def __init__(self):
        """Initializes a new instance of the Event class."""
        self._listeners = set()

    def _dispatch(self, *args, **kwargs):
        """Dispatches this event."""
        for func in self._listeners:
            func()

    def subscribe(self, *args):
        """Adds the handler(s) in args to this event."""
        self._listeners.update(args)

    def unsubscribe(self, *args):
        """Removes the handler(s) in args from this event."""
        for func in args:
            self._listeners.discard(func)

    def clear(self):
        """Removes all handlers from this event."""
        self._listeners = set()


class EventError(Exception):
    """Base class of Exceptions rasied by Events. Includes a refernce to
       the underlying exception that was thrown by handlers."""

    def __init__(self, message: string):
        pass


class HandlerRaisedError(EventError):
    """A wrapper class that is thrown when an event handler throws an
       exception."""

    def __init__(self, handlerError: Exception):
        errorType = type(handlerError)
        super().__init__("An exception of type {exceptionType} was thrown"
                         " when dispatching an event.")
