
def hello(name: str):
    print("Hello " + name + "! How old are you?")


if __name__ == "__main__":
    name = input("Введите имя: ")
    hello(name)