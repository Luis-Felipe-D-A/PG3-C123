import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import util.generic as utl
from clases.clientes import Clientes
from formularios.FrmDashboard import Dashboard

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("INGRESO AL SISTEMA - UNITECNAR")
        self.root.resizable(False, False)
        utl.centrar_ventana(self.root, 800, 500)
        self.logo = utl.leer_imagen("image/logo.png", (300, 100))       
        self.icon_user = utl.leer_imagen("image/login.png", (64, 64))   

        self.frame = tk.Frame(self.root, bd=0, relief=tk.SOLID)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.frame_logo = tk.Frame(self.frame, bd=0, width=300, relief=tk.SOLID)
        self.frame_logo.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
        self.llogo = tk.Label(self.frame_logo, image=self.logo)
        self.llogo.pack(padx=5, pady=150)

        self.frame_form = tk.Frame(self.frame, bd=0, relief=tk.SOLID)
        self.frame_form.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)

        self.texto = tk.Label(self.frame_form, text="INGRESO AL SISTEMA", font=('Times', 20))
        self.texto.pack(padx=10, pady=10)

        self.imglogin = tk.Label(self.frame_form, image=self.icon_user)
        self.imglogin.pack(padx=10, pady=10)

        self.lusuario = tk.Label(self.frame_form, text="Usuario:", font=('Times', 14))
        self.lusuario.pack(padx=10, pady=5)

        self.txt_user = tk.Entry(self.frame_form, width=30, font=('Times', 12))
        self.txt_user.pack(fill=tk.X, padx=10, pady=10)
        self.txt_user.focus()

        self.lclave = tk.Label(self.frame_form, text="Clave:", font=('Times', 14))
        self.lclave.pack(fill=tk.X, padx=10, pady=5)

        self.txt_pass = tk.Entry(self.frame_form, width=30, font=('Times', 12), show="*")
        self.txt_pass.pack(fill=tk.X, padx=10, pady=10)

        self.bregistrar = tk.Button(self.frame_form, text="Iniciar sesión", font=('Times', 16), command=self.ingresar)
        self.bregistrar.pack(fill=tk.X, padx=10, pady=10)

        self.root.mainloop()

    def ingresar(self):
        username = self.txt_user.get()
        clave = self.txt_pass.get()

        if not username or not clave:
            messagebox.showwarning("Campos vacíos", "ingrese usuario y clave")
            return

        clientes = Clientes()  
        cliente = clientes.validar_cliente(username, clave) 

        if cliente:
            nombre_completo = f"{cliente[1]} {cliente[2]}"
            email = cliente[3]
            rol = cliente[6]
            self.root.destroy()
            Dashboard(nombre_completo, email, rol)
        else:
            messagebox.showerror("ERROR", "Usuario o clave incorrectos")
