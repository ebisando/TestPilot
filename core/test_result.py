class TestResult:

    def __init__(
        self,
        name,
        status,
        error=None,
        duration=0
    ):

        self.name = name
        self.status = status
        self.error = error
        self.duration = duration