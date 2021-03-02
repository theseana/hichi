def azhdar():
    print("azhdar asli")


class A:
    def __init__(self):
        azhdar()
        self.azhdar()


def azhdar(self):
    print("Azhdar")

A()