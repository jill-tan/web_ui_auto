class UICheckException(Exception):
    """
    Raised when a UI click fails to navigate to a specific location.
    """

    def __init__(self, function_name):
        message = (
            f"UICheckException: {function_name} navigate to a specific location Fail."
        )
        super().__init__(message)
