import tkinter as tk


class AplicacionCuadrado:
    def __init__(self, root):
        self.root = root
        self.root.title("Dibuja un Cuadrado")

        # Etiqueta de entrada
        self.label = tk.Label(root, text="Introduce el tamaño del cuadrado:")
        self.label.pack(pady=10)

        # Entrada de texto
        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=5)

        # Botón para dibujar el cuadrado
        self.boton_dibujar = tk.Button(root, text="Dibujar Cuadrado", command=self.dibujar_cuadrado)
        self.boton_dibujar.pack(pady=10)

        # Lienzo para dibujar el cuadrado
        self.lienzo = tk.Canvas(root, width=300, height=300, bg="white")
        self.lienzo.pack(pady=10)

    def dibujar_cuadrado(self):
        self.lienzo.delete("all")  # Limpia el lienzo antes de dibujar

        try:
            tamano = int(self.entrada.get())
            if tamano <= 0:
                mensaje = "El tamaño debe ser un número positivo."
            else:
                # Calcular las coordenadas para centrar el cuadrado
                x1 = (self.lienzo.winfo_width() - tamano) / 2
                y1 = (self.lienzo.winfo_height() - tamano) / 2
                x2 = x1 + tamano
                y2 = y1 + tamano

                # Dibujar el cuadrado
                self.lienzo.create_rectangle(x1, y1, x2, y2, outline="black", fill="lightblue")
                mensaje = ""
        except ValueError:
            mensaje = "Por favor, introduce un número válido."

        if mensaje:
            self.lienzo.create_text(self.lienzo.winfo_width() / 2, self.lienzo.winfo_height() / 2, text=mensaje,
                                    fill="red")


# Crear la ventana principal
root = tk.Tk()
app = AplicacionCuadrado(root)
root.mainloop()
