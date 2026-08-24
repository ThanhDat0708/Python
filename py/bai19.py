class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


error = MyError("Có gì đó sai sai!")

print(error.msg)