import tkinter as tk
from usuario.Usuario import Usuario

class FrmLogin(tk.Frame):
    def __init__(self, master, go_register, go_dashboard):
        super().__init__(master)
        self.go_register = go_register
        self.go_dashboard = go_dashboard

        tk.Label(self, text="Iniciar Sesión", font=("Arial", 14, "bold")).pack(pady=10)

        self.entry_nick = self._crear_entry("Usuario")
        self.entry_pass = self._crear_entry("Clave", show="*")

        tk.Button(self, text="Ingresar", command=self.login).pack(pady=5)
        tk.Button(self, text="Registrarse", command=self.go_register).pack()

    def _crear_entry(self, texto, show=None):
        tk.Label(self, text=texto).pack()
        entry = tk.Entry(self, show=show) if show else tk.Entry(self)
        entry.pack()
        return entry

    def login(self):
        nickname = self.entry_nick.get()
        clave = self.entry_pass.get()
        usuario = Usuario.validarUsuario(nickname, clave)
        if usuario:
            self.go_dashboard(usuario)
        else:
            tk.Label(self, text="Usuario o clave incorrectos ❌", fg="red").pack()
