import tkinter as tk
from tkinter import ttk
from usuario.Usuario import Usuario

class FrmRegUser(tk.Frame):
    def __init__(self, master, volver_login):
        super().__init__(master)
        self.volver_login = volver_login

        tk.Label(self, text="Registro de Usuario", font=("Arial", 14, "bold")).pack(pady=10)

        
        self.entry_nombre = self._crear_entry("Nombre")
        self.entry_apellidos = self._crear_entry("Apellidos")
        self.entry_email = self._crear_entry("Email")
        self.entry_nickname = self._crear_entry("Nickname")
        self.entry_clave = self._crear_entry("Clave", show="*")

        
        ttk.Button(self, text="Guardar", command=self.guardar_usuario).pack(pady=5)
        ttk.Button(self, text="Volver", command=self.volver_login).pack()

    def _crear_entry(self, texto, show=None):
        tk.Label(self, text=texto).pack()
        entry = tk.Entry(self, show=show) if show else tk.Entry(self)
        entry.pack()
        return entry

    def guardar_usuario(self):
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellidos.get()
        email = self.entry_email.get()
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()

        if nombre and apellidos and email and nickname and clave:
            Usuario.guardarUsuario(nombre, apellidos, email, nickname, clave)
            tk.Label(self, text="Usuario registrado con éxito ✅", fg="green").pack()
        else:
            tk.Label(self, text="Complete todos los campos ❌", fg="red").pack()
