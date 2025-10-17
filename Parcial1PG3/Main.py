import tkinter as tk
from formularios.FrmLogin import FrmLogin
from formularios.FrmRegUser import FrmRegUser
from formularios.FrmDashboard import FrmDashboard
from usuario.Usuario import Usuario

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Login")

        
        self.frm_login = None
        self.frm_reg_user = None
        self.frm_dashboard = None

        
        self.show_login_form()

    def show_register_form(self):
        if self.frm_login is not None:
            self.frm_login.pack_forget()
        self.frm_reg_user = FrmRegUser(self.master, self.show_login_form)
        self.frm_reg_user.pack()

    def show_login_form(self):
        if self.frm_reg_user is not None:
            self.frm_reg_user.pack_forget()
        if self.frm_dashboard is not None:
            self.frm_dashboard.pack_forget()
        self.frm_login = FrmLogin(self.master, self.show_register_form, self.show_dashboard)
        self.frm_login.pack()

    def show_dashboard(self, usuario: Usuario):
        if self.frm_login is not None:
            self.frm_login.pack_forget()
        self.frm_dashboard = FrmDashboard(self.master, usuario, self.show_login_form)
        self.frm_dashboard.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

#FRANCISCO JOSE RAMOS ESQUIVEL & LUIS FELIPE DIAZ ARRIAGA