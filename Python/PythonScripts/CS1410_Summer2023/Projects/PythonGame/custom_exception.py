class CustomException(Exception):
    """Used to modify how an exception is handled."""
    def __init__(self, *args, **kwargs):
        self.error = None
        if self.error:
            print(self.error)
    pass
