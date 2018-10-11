import logging


class Event(object):
    _logger = logging.getLogger("Event")

    def __init__(self, name="Unnamed"):
        """Initializes a new instance of the Event class.
        Name attribute is for logging and identification purposes."""
        self._handlers = set()
        self._logger = Event._logger.getChild(name)
        self._name = name

    def _dispatch(self, *args, **kwargs):
        """Dispatches this event."""
        for handler in self._handlers:
            handler(*args, **kwargs)
        self._logger.info("Successfully dispatched event")

    def bind(self, *args):
        """Adds the function(s) in args to the event's listeners set."""
        self._handlers.update(args)
        self._logger.info("Handler {0} was bound to event.".format(str(args)))

    def unbind(self, *args):
        """Removes a listener from this event."""
        for func in args:
            self._handlers.discard(func)
        self._logger.info("Unbound {0} from event.".format(args))

    def clear(self):
        """Removes all listeners from this event."""
        self._handlers = set()
        self._logger.info("All handlers removed from event.")


class EventError(Exception):
    """Base class of Exceptions rasied by cobra."""
    def __init__(self):
        """"""
        pass
