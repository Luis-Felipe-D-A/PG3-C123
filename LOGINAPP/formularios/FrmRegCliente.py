import tkinter as tk
from tkinter import ttk, messagebox
from clases.clientes import Clientes

class FrmClientes:
    def __init__(self, parent, NombreCompleto, email, rol):
        self.nombre_completo = NombreCompleto
        self.email = email
        self.rol = rol
        self.cliente_seleccionado_id = None  

        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        
        tk.Label(self.frame, text=f"Sesión activa: {self.nombre_completo}", font=('Times', 12)).place(x=500, y=30)
        tk.Label(self.frame, text=f"Email: {self.email}", font=('Times', 12)).place(x=500, y=55)
        tk.Label(self.frame, text=f"Rol: {self.rol}", font=('Times', 12)).place(x=500, y=80)

        
        tk.Label(self.frame, text="Registro de cliente", font=('Times', 16)).place(x=70, y=30)

        tk.Label(self.frame, text="Nombre", font=('Times', 14)).place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        tk.Label(self.frame, text="Apellido", font=('Times', 14)).place(x=70, y=160)
        self.capellido = tk.Entry(self.frame, width=40)
        self.capellido.place(x=220, y=160)

        tk.Label(self.frame, text="Username", font=('Times', 14)).place(x=70, y=190)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=190)

        tk.Label(self.frame, text="Contraseña", font=('Times', 14)).place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        tk.Label(self.frame, text="Correo", font=('Times', 14)).place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        tk.Label(self.frame, text="Rol", font=('Times', 14)).place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40)
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Admin", "Vendedor", "Cliente")

        
        self.btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), command=self.guardar_cliente)
        self.btn_guardar.place(x=70, y=220)

        self.btn_actualizar = tk.Button(self.frame, text="Actualizar", font=('Times', 14), command=self.actualizar_cliente, state="disabled")
        self.btn_actualizar.place(x=170, y=220)

        self.btn_eliminar = tk.Button(self.frame, text="Eliminar", font=('Times', 14), command=self.eliminar_cliente, state="disabled")
        self.btn_eliminar.place(x=270, y=220)

        self.btn_cargar = tk.Button(self.frame, text="Cargar", font=('Times', 14), command=self.cargar_cliente)
        self.btn_cargar.place(x=370, y=220)

        self.lbl_estado = tk.Label(self.frame, text="", font=('Times', 12), fg="blue")
        self.lbl_estado.place(x=70, y=260)

        self.listar_clientes()
   
    def listar_clientes(self):
        tk.Label(self.frame, text="LISTADO DE CLIENTES", font=('Times', 16)).place(x=70, y=290)

        self.tablaclientes = ttk.Treeview(self.frame, columns=("Nombre", "Apellido", "Username", "Email", "Rol"))
        self.tablaclientes.heading("#0", text="ID")
        self.tablaclientes.heading("Nombre", text="Nombre")
        self.tablaclientes.heading("Apellido", text="Apellido")
        self.tablaclientes.heading("Username", text="Username")
        self.tablaclientes.heading("Email", text="Email")
        self.tablaclientes.heading("Rol", text="Rol")
        self.tablaclientes.place(x=70, y=330)

        
        self.cargar_clientes()

    def cargar_clientes(self):
        self.tablaclientes.delete(*self.tablaclientes.get_children())
        clientes = Clientes()
        sql = "SELECT id, nombre, apellido, username, email, rol FROM clientes"
        resultado = clientes.db.select(sql)
        if resultado:
            for fila in resultado:
                self.tablaclientes.insert("", "end", text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5]))

    def cargar_cliente(self):
        selected = self.tablaclientes.selection()
        if not selected:
            messagebox.showwarning("Llamado de Atención", "Selecciona un cliente de la tabla antes de cargar porfavor.")
            return

        item = self.tablaclientes.item(selected[0])
        self.cliente_seleccionado_id = item["text"]  
        nombre, apellido, username, email, rol = item["values"]

        self.cnombre.delete(0, tk.END)
        self.cnombre.insert(0, nombre)

        self.capellido.delete(0, tk.END)
        self.capellido.insert(0, apellido)

        self.cusuario.delete(0, tk.END)
        self.cusuario.insert(0, username)

        self.ccorreo.delete(0, tk.END)
        self.ccorreo.insert(0, email)

        self.ctipo.set(rol)
        self.ccontrasena.delete(0, tk.END)

        self.btn_guardar.config(state="disabled")
        self.btn_actualizar.config(state="normal")
        self.btn_eliminar.config(state="normal")

    def guardar_cliente(self):
        nombre = self.cnombre.get()
        apellido = self.capellido.get()
        username = self.cusuario.get()
        clave = self.ccontrasena.get()
        email = self.ccorreo.get()
        rol = self.ctipo.get()

        clientes = Clientes()
        exito = clientes.guardar_cliente(nombre, apellido, email, username, clave, rol)
        if exito:
            messagebox.showinfo("excelente", "El cliente se guardado correctamente.")
            self.limpiar_campos()
            self.cargar_clientes()
        else:
            messagebox.showerror("ERROR", "No se pudo guardar el cliente")

    def actualizar_cliente(self):
        if self.cliente_seleccionado_id is None:
            messagebox.showwarning("Llamado de Atención", "Selecciona un cliente para actualizar.")
            return

        nombre = self.cnombre.get()
        apellido = self.capellido.get()
        username = self.cusuario.get()
        clave = self.ccontrasena.get()
        email = self.ccorreo.get()
        rol = self.ctipo.get()

        if not all([nombre, apellido, username, email, rol]):
            messagebox.showwarning("Llamado de Atención", "Todos los campos deben estar completos (excepto contraseña).")
            return

        clientes = Clientes()
        exito = clientes.actualizar_cliente(self.cliente_seleccionado_id, nombre, apellido, username, email, rol, clave)
        if exito:
            messagebox.showinfo("excelente", "Cliente actualizado correctamente.")
            self.limpiar_campos()
            self.cargar_clientes()
        else:
            messagebox.showerror("ERROR", "No se pudo actualizar el cliente.")

    def eliminar_cliente(self):
        if self.cliente_seleccionado_id is None:
            messagebox.showwarning("Llamado de Atención", "Selecciona un cliente para eliminar.")
            return

        confirm = messagebox.askyesno("Confirmar", "Estás seguro de que deseas eliminar este cliente?")
        if confirm:
            clientes = Clientes()
            exito = clientes.eliminar_cliente(self.cliente_seleccionado_id)
            if exito:
                messagebox.showinfo("excelente", "Cliente eliminado correctamente.")
                self.limpiar_campos()
                self.cargar_clientes()
            else:
                messagebox.showerror("ERROR", "No se pudo eliminar el cliente.")

    def limpiar_campos(self):
        campos = [self.cnombre, self.capellido, self.cusuario, self.ccontrasena, self.ccorreo]
        for campo in campos:
            campo.delete(0, tk.END)
        self.ctipo.set('')
        self.cliente_seleccionado_id = None

        self.btn_guardar.config(state="normal")
        self.btn_actualizar.config(state="disabled")
        self.btn_eliminar.config(state="disabled")
        self.lbl_estado.config(text="")