
def hello(name: str):
    return "Hello " + name + "!!! How old are you?"


def test_hello():
    name = "Dima"
    expected = "Hello Dima! How are you?"
    result = hello(name)
    assert expected == result
    print("Всё хорошо!")


def test2():
    pass


if __name__ == "__main__":
    test_hello()