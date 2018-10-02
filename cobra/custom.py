from cobra.core import Event


class CustomEvent(Event):
    """Custom event object initalizable by the devloper."""
    def __init__(self):
        super().__init__()

    def __call__(self):
        self._disptach()