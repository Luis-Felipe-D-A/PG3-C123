import tkinter as tk
from tkinter import messagebox
import util.generic as utl
import webbrowser
from formularios.FrmRegCliente import FrmClientes  

class Dashboard:
    def __init__(self, NombreCompleto, email, rol):
        self.root = tk.Tk()
        self.root.title("Panel Administrativo")
        self.root.geometry("1000x600")
        self.nombre_completo = NombreCompleto
        self.email = email
        self.rol = rol
        self.ancho_pantalla = 1000

        menubar = tk.Menu(self.root)

        if self.rol == "Admin":
            menu_clientes = tk.Menu(menubar, tearoff=0)
            menu_clientes.add_command(label="Administración de Clientes", command=self.main_clientes)
            menubar.add_cascade(label="Clientes", menu=menu_clientes)

        if self.rol == "Admin":
            menu_usuarios = tk.Menu(menubar, tearoff=0)
            menu_usuarios.add_command(label="Administración de Usuarios", command=self.main_usuarios )
            menubar.add_cascade(label="Usuarios", menu=menu_usuarios)

        menu_categorias = tk.Menu(menubar, tearoff=0)
        menu_categorias.add_command(label="Administración de Categorías", command=self.main_categorias)
        menubar.add_cascade(label="Categorías", menu=menu_categorias)

        menu_productos = tk.Menu(menubar, tearoff=0)
        menu_productos.add_command(label="Administración de Productos", command=self.main_productos)
        menubar.add_cascade(label="Productos", menu=menu_productos)

        menu_ventas = tk.Menu(menubar, tearoff=0)
        menu_ventas.add_command(label="Administración de Ventas", command=self.main_ventas)
        menubar.add_cascade(label="Ventas", menu=menu_ventas)

        self.root.config(menu=menubar)

        self.user_info = tk.Frame(self.root, bd=0, relief=tk.SOLID, width=200)
        self.user_info.pack(side=tk.LEFT, padx=4, pady=5, fill="y")

        tk.Label(self.user_info, text="PANEL ADMINISTRATIVO", font=('Arial', 25)).pack(padx=20, pady=4)

        self.userimg = utl.leer_imagen("image/userinfo.png", (128,128))
        self.imgfacebook = utl.leer_imagen("image/face.png", (48,48))
        self.imglinkedin = utl.leer_imagen("image/linkedin.png", (48,48))
        self.imgwebsite = utl.leer_imagen("image/website.png", (48,48))
        self.imglogout = utl.leer_imagen("image/logout.png", (48,48))

        tk.Label(self.user_info, image=self.userimg).pack(padx=30, pady=4)
        tk.Label(self.user_info, text=self.nombre_completo, font=('Arial', 15)).pack(pady=4)
        tk.Label(self.user_info, text=self.email, font=('Arial', 12)).pack(pady=2)
        tk.Label(self.user_info, text=self.rol, font=('Arial', 12, 'italic')).pack(pady=2)

        social_buttons_frame = tk.Frame(self.user_info)
        social_buttons_frame.pack(pady=10)

        tk.Button(social_buttons_frame, image=self.imgfacebook, command=self.abrirfacebook).pack(side=tk.LEFT, padx=5)
        tk.Button(social_buttons_frame, image=self.imglinkedin, command=self.abrirlinkedin).pack(side=tk.LEFT, padx=5)
        tk.Button(social_buttons_frame, image=self.imgwebsite, command=self.abrirwebsite).pack(side=tk.LEFT, padx=5)
        tk.Button(social_buttons_frame, image=self.imglogout, command=self.logout).pack(side=tk.LEFT, padx=5)

        self.frame_data = tk.Frame(self.root, bd=0, relief=tk.SOLID, width=self.ancho_pantalla - 200)
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

        tk.Label(self.frame_data, text="BIENVENIDOS AL SISTEMA", font=('Arial', 20)).pack(padx=20, pady=4)
        self.frame_dynamic = tk.Frame(self.frame_data, bd=0, relief=tk.SOLID)
        self.frame_dynamic.pack(side=tk.TOP, padx=4, pady=5, fill="both", expand=1)

        
        tk.Label(self.root, text="Desarrollado por: FRANCISCO JOSE RAMOS ESQUIVEL & Luis Felipe Diaz Arriaga", font=('Arial', 10, 'italic')).place(x=10, rely=0.97)

        self.root.mainloop()

    def main_usuarios(self):
        if self.rol != "Admin":
            messagebox.showwarning(" no permitido", "No tienes permisos para acceder a Administración de Usuarios.")
            return
        print("Se cambio a módulo de Clientes")

    def main_clientes(self):
        if self.rol != "Admin":
            messagebox.showwarning(" no permitido", "No tienes permisos para acceder a Administración de Clientes.")
            return
        
        self.limpiar_panel(self.frame_dynamic)
        FrmClientes(self.frame_dynamic, self.nombre_completo, self.email, self.rol)

    def main_categorias(self):
        print("Proximamente módulo de categorías")

    def main_productos(self):
        print("Proximamente módulo de productos")

    def main_ventas(self):
        print("Proximamente módulo de ventas")

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()

    def abrirfacebook(self):
        webbrowser.open_new_tab("https://www.facebook.com")

    def abrirlinkedin(self):
        webbrowser.open_new_tab("https://www.linkedin.com")

    def abrirwebsite(self):
        webbrowser.open_new_tab("https://www.unitecnar.edu.co")

    def logout(self):
        self.root.quit()
