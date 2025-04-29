# archivo: teatro_gui.py

import tkinter as tk
from tkinter import messagebox
from boletos import Palco, Platea, Galeria

class TeatroMunicipalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")

        titulo = tk.Label(root, text="Teatro Municipal", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=10)

        marco = tk.LabelFrame(root, text="Datos del Boleto", padx=10, pady=10)
        marco.pack(padx=10, pady=5)

        self.tipo_boleto = tk.StringVar(value="Palco")
        tk.Radiobutton(marco, text="Palco", variable=self.tipo_boleto, value="Palco").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(marco, text="Platea", variable=self.tipo_boleto, value="Platea").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(marco, text="Galería", variable=self.tipo_boleto, value="Galeria").grid(row=0, column=2, sticky="w")

        tk.Label(marco, text="Número:").grid(row=1, column=0, sticky="e")
        self.entrada_numero = tk.Entry(marco)
        self.entrada_numero.grid(row=1, column=1, padx=5, pady=5)

       
        tk.Label(marco, text="Cant. Días para el Evento:").grid(row=2, column=0, columnspan=2, sticky="w")
        self.entrada_dias = tk.Entry(marco)
        self.entrada_dias.grid(row=2, column=2, padx=5)

        tk.Button(marco, text="Vende", command=self.vender_boleto).grid(row=3, column=1, pady=10)
        tk.Button(marco, text="Salir", command=root.quit).grid(row=3, column=2)

        self.informacion = tk.Label(root, text="", font=("Helvetica", 12), fg="blue")
        self.informacion.pack(pady=10)

    def vender_boleto(self):
        tipo = self.tipo_boleto.get()
        numero = self.entrada_numero.get()

        if not numero.isdigit():
            messagebox.showerror("Error", "Ingrese un número válido.")
            return

        numero = int(numero)

        if tipo == "Palco":
            boleto = Palco(numero)
        elif tipo == "Platea":
            boleto = Platea(numero)
        elif tipo == "Galeria":
            boleto = Galeria(numero)

        self.informacion.config(text=str(boleto))

if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalGUI(root)
    root.mainloop()
