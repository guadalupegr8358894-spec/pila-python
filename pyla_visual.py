import tkinter as tk
from tkinter import messagebox

class PilaVisualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Pila (Stack)")
        self.root.geometry("550x550")
        self.root.config(bg="#f4f6f9")

        # Estructura de datos de la Pila (máximo 7 elementos para que luzca bien gráficamente)
        self.pila = []
        self.limite = 7

        # --- TÍTULO ---
        titulo = tk.Label(root, text="Simulador Gráfico de una Pila (LIFO)", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#333333")
        titulo.pack(pady=15)

        # --- PANEL DE CONTROL ---
        frame_controles = tk.Frame(root, bg="#f4f6f9")
        frame_controles.pack(pady=10)

        lbl_valor = tk.Label(frame_controles, text="Valor:", font=("Arial", 11), bg="#f4f6f9")
        lbl_valor.grid(row=0, column=0, padx=5)

        self.entry_valor = tk.Entry(frame_controles, font=("Arial", 12), width=12)
        self.entry_valor.grid(row=0, column=1, padx=5)
        self.entry_valor.focus()
        self.entry_valor.bind("<Return>", lambda event: self.push()) # Permite presionar Enter

        btn_push = tk.Button(frame_controles, text="PUSH (Apilar)", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=12, command=self.push)
        btn_push.grid(row=0, column=2, padx=5)

        btn_pop = tk.Button(frame_controles, text="POP (Desapilar)", font=("Arial", 10, "bold"), bg="#F44336", fg="white", width=12, command=self.pop)
        btn_pop.grid(row=1, column=2, padx=5, pady=5)

        btn_peek = tk.Button(frame_controles, text="PEEK (Ver Tope)", font=("Arial", 10, "bold"), bg="#FF9800", fg="white", width=12, command=self.peek)
        btn_peek.grid(row=2, column=2, padx=5)

        btn_limpiar = tk.Button(frame_controles, text="Limpiar Pila", font=("Arial", 10), bg="#9E9E9E", fg="white", width=12, command=self.limpiar)
        btn_limpiar.grid(row=3, column=2, padx=5, pady=5)

        # --- LIENZO GRÁFICO (CANVAS) PARA LA PILA ---
        self.canvas = tk.Canvas(root, width=250, height=320, bg="white", highlightthickness=2, highlightbackground="#cccccc")
        self.canvas.pack(side=tk.LEFT, padx=30, pady=10)

        # --- ETIQUETA DE ESTADO / INFORMACIÓN ---
        self.lbl_estado = tk.Label(root, text="Estado: Pila Vacía", font=("Arial", 11, "italic"), bg="#f4f6f9", fg="#555555", justify=tk.LEFT)
        self.lbl_estado.pack(side=tk.RIGHT, anchor="n", padx=20, pady=20)

        self.dibujar_pila()

    def push(self):
        valor = self.entry_valor.get().strip()
        if not valor:
            messagebox.showwarning("Advertencia", "Por favor ingresa un valor.")
            return
        
        if len(self.pila) >= self.limite:
            messagebox.showerror("Error", f"¡La pila está llena! (Límite: {self.limite} elementos)")
            return

        self.pila.append(valor)
        self.entry_valor.delete(0, tk.END)
        self.lbl_estado.config(text=f"Estado: Elemento '{valor}' agregado (PUSH).")
        self.dibujar_pila()

    def pop(self):
        if not self.pila:
            messagebox.showerror("Error", "¡La pila está vacía! (Underflow)")
            return

        valor = self.pila.pop()
        self.lbl_estado.config(text=f"Estado: Elemento '{valor}' retirado (POP).")
        self.dibujar_pila()

    def peek(self):
        if not self.pila:
            messagebox.showwarning("Información", "La pila está vacía.")
            return
        
        tope = self.pila[-1]
        self.lbl_estado.config(text=f"Estado: El tope actual es '{tope}'.")
        self.dibujar_pila(resaltar_tope=True)

    def limpiar(self):
        self.pila.clear()
        self.lbl_estado.config(text="Estado: Pila limpiada.")
        self.dibujar_pila()

    def dibujar_pila(self, resaltar_tope=False):
        self.canvas.delete("all")

        # Dibujar la estructura base de la pila (un contenedor abierto arriba)
        # Base y paredes laterales
        self.canvas.create_line(50, 290, 200, 290, width=4, fill="#333333") # Base
        self.canvas.create_line(50, 50, 50, 290, width=4, fill="#333333")   # Pared izquierda
        self.canvas.create_line(200, 50, 200, 290, width=4, fill="#333333") # Pared derecha

        # Dibujar los elementos desde la base (abajo) hacia arriba
        ancho_caja = 130
        alto_caja = 30
        x1 = 60
        y_inicial = 255

        for i, elemento in enumerate(self.pila):
            y1 = y_inicial - (i * 35)
            y2 = y1 + alto_caja
            x2 = x1 + ancho_caja

            # Color especial si es el tope y se solicitó resaltar
            if i == len(self.pila) - 1 and resaltar_tope:
                color_fondo = "#FFCC80"  # Naranja claro para el tope
                color_borde = "#E65100"
            else:
                color_fondo = "#90CAF9"  # Azul claro para los demás
                color_borde = "#1565C0"

            # Dibujar rectángulo del elemento
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color_fondo, outline=color_borde, width=2)
            
            # Texto dentro del bloque
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(elemento), font=("Arial", 11, "bold"), fill="#000000")

            # Etiqueta de "TOPE" en el elemento superior
            if i == len(self.pila) - 1:
                self.canvas.create_text(x2 + 25, (y1 + y2) / 2, text="<-- TOPE", font=("Arial", 9, "bold"), fill="#D32F2F")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaVisualApp(root)
    root.mainloop()