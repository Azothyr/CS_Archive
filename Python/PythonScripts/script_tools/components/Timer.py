import time


class Timer:
    """
    A simple timing context manager.

    Used to measure the execution time of code blocks. When used in a `with` statement,
    the timer starts upon entering the block and stops upon exiting.

    Attributes:
        start_time (float): The time the timer starts.
        end_time (float): The time the timer ends.
        interval (float): The duration the timer ran for.

    Example:
        with Timer() as timer:
            # Your time-consuming code here
            ...
        timer.print_duration()
    """

    def __enter__(self):
        """
        Start the timer when entering the `with` block.
        """
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Stop the timer upon exiting the `with` block.
        """
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time

    def get_duration(self):
        """
        Retrieve the duration for which the timer ran.

        Returns:
            float: The duration in seconds.
        """
        return self.interval

    def print_duration(self):
        """
        Print the elapsed time in a formatted string.
        """
        if hasattr(self, 'interval'):
            print(f"Elapsed time: {self.interval:.4f} seconds")
        else:
            print("Timer has not yet completed.")
