# app.py - Calculadora com interface gráfica BONITA
import customtkinter as ctk
from calculadora import *

ctk.set_appearance_mode("dark")  # ou "light"
ctk.set_default_color_theme("blue")

class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Python Turbo 3000")
        self.geometry("400x600")
        self.resizable(False, False)

        # Display
        self.display = ctk.CTkEntry(self, font=("Arial", 24), justify="right")
        self.display.pack(fill="x", padx=20, pady=20, ipady=20)
        self.display.insert(0, "0")

        # Botões
        botoes = [
            ['C', '±', '%', '÷'],
            ['√', 'x²', '^', '←'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['9', '0', '.', '=']
        ]

        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)

        for linha in botoes:
            row = ctk.CTkFrame(frame)
            row.pack(fill="x", padx=20, pady=5)
            for texto in linha:
                if texto in "0123456789.":
                    btn = ctk.CTkButton(row, text=texto, width=70, height=60,
                                        font=("Arial", 20), command=lambda t=texto: self.digitar(t))
                elif texto == "=":
                    btn = ctk.CTkButton(row, text=texto, width=70, height=60,
                                        fg_color="orange", font=("Arial", 20), command=self.calcular)
                elif texto == "C":
                    btn = ctk.CTkButton(row, text=texto, width=70, height=60,
                                        fg_color="red", font=("Arial", 18), command=self.limpar)
                else:
                    btn = ctk.CTkButton(row, text=texto, width=70, height=60,
                                        font=("Arial", 20), command=lambda t=texto: self.operacao(t))
                btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        # Easter egg
        ctk.CTkLabel(self, text="Eu odeio carro elétrico", font=("Arial", 10), text_color="gray").pack(side="bottom", pady=10)

    def digitar(self, valor):
        if self.display.get() == "0":
            self.display.delete(0, "end")
        self.display.insert("end", valor)

    def limpar(self):
        self.display.delete(0, "end")
        self.display.insert(0, "0")

    def operacao(self, op):
        # Futuro: implementar calculadora com múltiplas operações
        # Por enquanto só faz uma operação por vez (simples)
        self.primeiro = float(self.display.get())
        self.operador = op
        self.display.delete(0, "end")

    def calcular(self):
        try:
            segundo = float(self.display.get())
            if self.operador == "+": result = somar(self.primeiro, segundo)
            elif self.operador == "-": result = subtrair(self.primeiro, segundo)
            elif self.operador == "×": result = multiplicar(self.primeiro, segundo)
            elif self.operador == "÷": result = dividir(self.primeiro, segundo)
            elif self.operador == "^": result = potencia(self.primeiro, segundo)
            elif self.operador == "x²": result = potencia(self.primeiro, 2)
            elif self.operador == "√": result = raiz_quadrada(self.primeiro)
            else: result = segundo

            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Erro")

app = CalculadoraApp()
app.mainloop()