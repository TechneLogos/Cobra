class Event(object):
    def __init__(self, *args):
        """Initializes a new instance of the Event class.
        Name attribute is for logging and identification purposes."""
        self.__listeners = set()
        self.__listeners.update(args)

    def _dispatch(self):
        """Dispatches this event."""
        for func in self.__listeners:
            func()

    def bind(self, *args):
        """Adds the function(s) in args to the event's listeners set."""
        self.__listeners.update(args)

    def unbind(self, *args):
        """Removes a listener from this event."""
        for func in args:
            self.__listeners.discard(func)

    def clear(self):
        """Removes all listeners from this event."""
        self.__listeners = set()


class EventError(Exception):
    """Base class of Exceptions rasied by cobra."""
    def __init__(self):
        """"""
        pass
