class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0


class Platea(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 80.0


class Galeria(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 50.0
