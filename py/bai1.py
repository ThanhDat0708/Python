class MyError(Exception):
    """My own exception class

    Attributes:
        msg -- explanation of the error
    """

    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


error = MyError("Có gì đó sai sai!")
print(error)