import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class FrmDashboard(tk.Frame):
    def __init__(self, master, usuario, volver_login):
        super().__init__(master)

        self.usuario = usuario
        self.volver_login = volver_login

        tk.Label(self, text="Bienvenido al SIstema", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Label(self, text=f"Hola, {self.usuario.nombre} {self.usuario.apellidos}", font=("Arial", 20)).pack(pady=5)

   
        ruta_imagen = os.path.join("assets", "Fotoperfil.png")

 
        img = Image.open(ruta_imagen)
        img = img.resize((120, 120))
        self.img_tk = ImageTk.PhotoImage(img)

        tk.Label(self, image=self.img_tk).pack(pady=10)

        ttk.Button(self, text="Cerrar Sesión", command=self.logout).pack(pady=20)

    def logout(self):
        """Cerrar sesión y volver al login"""
        self.pack_forget()
        self.volver_login()
