from libevent.core import Event


class CustomEvent(Event):
    """Custom event object initalizable by the devloper."""

    def __init__(self):
        super().__init__()

    def dispatch(self, *args, **kwargs):
        """Allow users to dispatch this instance a CustomEvent"""
        self._dispatch(*args, **kwargs)
