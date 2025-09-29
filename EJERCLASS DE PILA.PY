import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

class PilaApp:
    def __init__(self, root):
        self.pila = Pila()
        self.root = root
        self.root.title("Simulación de Pila")

        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        
        tk.Button(root, text="Apilar", command=self.apilar).pack(pady=2)
        tk.Button(root, text="Desapilar", command=self.desapilar).pack(pady=2)

       
        self.canvas = tk.Canvas(root, width=200, height=300, bg="white")
        self.canvas.pack(pady=10)

       
        self.dibujar_pila()

    def apilar(self):
        dato = self.entry.get()
        if dato:
            self.pila.apilar(dato)
            self.entry.delete(0, tk.END)
            self.dibujar_pila()
        else:
            messagebox.showwarning("Atención", "Ingresa un dato para apilar.")

    def desapilar(self):
        if not self.pila.esta_vacia():
            self.pila.desapilar()
            self.dibujar_pila()
        else:
            messagebox.showinfo("Aviso", "La pila está vacía.")

    def dibujar_pila(self):
        self.canvas.delete("all")  
        x1, y1 = 50, 250
        x2, y2 = 150, 280

        
        for dato in reversed(self.pila.items):
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue")
            self.canvas.create_text((x1+x2)//2, (y1+y2)//2, text=str(dato))
            y1 -= 35
            y2 -= 35

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaApp(root)
    root.mainloop()
