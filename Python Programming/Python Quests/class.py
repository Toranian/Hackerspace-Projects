class Dog:

    amount = 0

    def __init__(self, name):
        self.name = name
        amount += 1


fido = Dog("Fido")
walter = Dog("Walter")

print(fido.amount, walter.amount)
