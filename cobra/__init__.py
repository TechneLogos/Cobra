import logging
import threading


class Event(object):
    def __init__(self, name=None, *args):
        """Initializes a new instance of the Event class.
        Name attribute is for logging and identification purposes."""
        self.name = name if name is not None else "Unnamed"
        self.__logger = logging.getLogger("EventSystem").getChild(self.name)
        self.__listeners = set()
        self.__listeners.update(args)
        self.__logger.info("{0} event initialized")

    def __call__(self):
        """Dispatches this event."""
        for func in self.__listeners:
            func()
        self.__logger.info("{0} event dispatched successfully.".format(name))

    def add_listener(self, *args):
        """Adds the function(s) in args to the event's listeners set."""
        if not args:
            self.__logger.warning("No argument passed to Event.add_listener()"
                                  ", no listener was added.")
        for func in args:
            if not callable(func):
                self.__logger.error("{0} is not a callable object."
                                    "Was not added to {1} event.".format(
                                        str(func), self.name))
                raise TypeError
        self.__listeners.update(args)
        self.__logger.info("Listeners successfuly subsrcibed to {0}".
                           format(self.name))

    def get_listeners(self):
        return list(self.__listeners)

    def remove_listener(self, *args):
        """Removes a listener from this event."""
        for func in args:
            self.__listeners.discard(func)

    def clear_listeners(self):
        """Removes all listeners from this event."""
        self.__listeners = set()
        self.__logger.info("{0}'s listeners cleared.".format(self.name))


class EventError(Exception):
    """Base class of Exceptions rasied by cobra."""
    def __init__(self):
        """"""
