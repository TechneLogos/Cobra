import logging
import threading


class Event(object):
    def __init__(self, name=None, system=None, *args):
        """Initializes a new instance of the Event class.

        The name attribute is for logging purposes."""
        if system is not None:
            self.name = "{0}.{1}".format(system.name, name)
        elif name is not None:
            self.name = name
        else:
            self.name = "Unnamed"
        self.__logger = logging.getLogger(self.name)
        self.__handler = None
        self.__listeners = set()
        for func in args:
            self.__listeners.add(func)
        self.__logger.info("{0} event initialized")

    def __call__(self):
        """Dispatches this event."""
        if self.__handler is not None:
            self.__handler()
        self.__logger.info("{0} event dispatched successfully.".format(name))

    def set_handler(self, handler):
        """Sets the handler to be invoked when this Event is dispatched."""
        if not callable(handler):
            raise ValueError
        self.__handler = handler
        self.__logger.info("{0} set as {1}'s handler.".format(str(handler),
                                                              self.name))

    def add_listener(self, *args):
        """Adds the function(s) in args to the event's listeners set."""
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
        return self.__listeners

    def remove_listener(self, *args):
        """Removes a listener from this event."""
        for func in args:
            self.__listeners.discard(func)

    def clear_listeners(self):
        """Removes all listeners from this event."""
        self.__listeners = set()
        self.__logger.info("{0}'s listeners cleared.".format(self.name))


class EventSystem(object):
    """An event system that allows for easier handling of cobra.
    The name parameter is for logging purposes."""
    def __init__(self, name=None, **kwargs):
        self.name = name if name is not None else "Unnamed"
        self.__events = dict(kwargs)
        self.__events.setdefault(Event(name, self))
        self.__logger = logging.getLogger("EventSystem").getChild(name)

    def get_event(self, name):
        """Returns the event with the given name."""
        return self.__events.get[name]

    def get_events(self):
        """Returns all event names in this EventSystem"""
        return list()


class EventError(Exception):
    """Base class of Exceptions rasied by cobra."""
    def __init__(self):
        """"""


class EventSystemError(Exception):
    def __init__(self):
        """"""
