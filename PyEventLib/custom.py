from PyEventLib.core import Event


class CustomEvent(Event):
    _logger = Event._logger.getChild("Custom")

    """Custom event object initalizable by the devloper."""
    def __init__(self, name="Unnamed"):
        super().__init__(name)

    def __call__(self, *args, **kwargs):
        self._disptach(*args, **kwargs)
