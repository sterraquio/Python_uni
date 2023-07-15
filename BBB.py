import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import Calendar
from tkinter import simpledialog

root = tk.Tk()
root.title("MONITORES BBB")

# Variables globales
reportes = []
num_reportes_value = tk.StringVar()
selected_reporte = None




#------------------------------------------------------Arreglo de donde sale el número de factura-----------------------------------------------------------------------------------------------------
labels = ["Número de factura:","Nombre:", "Teléfono:", "Dirección:", "Identificación:", "Descripción del daño:"]
entries = []
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------Arreglo de donde se hace la comparación del Número de recibo---------------------------------------------------------------
labels = ["Número de factura:", "Nombre del atendedor:", "No. identificación del atendedor:", "Nombre del producto:", "Precio del producto:", "Informe:"]
entries_de_recibo = []
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Funciones
#-----------------------------------------Inicio de la ventana de reportes-------------------------------------------------------------------------------------------------
def mostrar_ventana_reportes():
    def mostrar_info_reporte():
        global selected_reporte
        if selected_reporte is None:
            messagebox.showwarning("Advertencia", "Debes seleccionar un número de reporte.")
            return
        
        reporte = reportes[selected_reporte]
        messagebox.showinfo("Reporte detallado", f"Información del reporte {selected_reporte}:\n\n{reporte}")

    def seleccionar_reporte(event):
        global selected_reporte
        selected_reporte = reportes_listbox.curselection()
        if selected_reporte:
            selected_reporte = selected_reporte[0]
        else:
            selected_reporte = None

    reportes_window = tk.Toplevel(root)
    reportes_window.title("Reportes")

    reportes_frame = tk.Frame(reportes_window, padx=20, pady=20)
    reportes_frame.pack()

    title_label = tk.Label(reportes_frame, text="Haz accedido a Reportes", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    num_reportes_label = tk.Label(reportes_frame, text="Cantidad de reportes:")
    num_reportes_label.grid(row=1, column=0, sticky="w")
    num_reportes = tk.Label(reportes_frame, textvariable=num_reportes_value)
    num_reportes.grid(row=1, column=1, pady=5)

    reportes_listbox = tk.Listbox(reportes_frame)
    reportes_listbox.grid(row=2, column=0, columnspan=2, pady=10)
    reportes_listbox.bind("<<ListboxSelect>>", seleccionar_reporte)

    for i, reporte in enumerate(reportes):
        reportes_listbox.insert(tk.END, f"Reporte {i}")

    info_button = tk.Button(reportes_frame, text="Ver información detallada", command=mostrar_info_reporte)
    info_button.grid(row=3, column=0, columnspan=2, pady=10)

def mostrar_ventana_usuarios():
    usuarios_window = tk.Toplevel(root)
    usuarios_window.title("Usuarios")

    form_frame = tk.Frame(usuarios_window, padx=20, pady=20)
    form_frame.pack()

    title_label = tk.Label(form_frame, text="Haz accedido a Generar Reporte de Usuario", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)
    for i, label_text in enumerate(labels):
        label = tk.Label(form_frame, text=label_text)
        label.grid(row=i+1, column=0, sticky="w")
        entry = tk.Entry(form_frame)
        entry.grid(row=i+1, column=1, pady=5)
        entries.append(entry)

    
    def open_calendar():
        def select_date():
            fecha_compra_entry.delete(0, tk.END)
            fecha_compra_entry.insert(0, cal.get_date())
            calendar_window.destroy()

        calendar_window = tk.Toplevel(usuarios_window)
        calendar_window.title("Seleccionar Fecha")
        cal = Calendar(calendar_window, selectmode="day", date_pattern="dd/MM/yyyy")
        cal.pack(pady=10)
        select_button = tk.Button(calendar_window, text="Seleccionar", command=select_date)
        select_button.pack(pady=10)

    fecha_compra_label = tk.Label(form_frame, text="Fecha de compra:")
    fecha_compra_label.grid(row=len(labels) + 1, column=0, sticky="w")
    fecha_compra_entry = tk.Entry(form_frame)
    fecha_compra_entry.grid(row=len(labels) + 1, column=1, pady=5)
    fecha_compra_button = tk.Button(form_frame, text="Seleccionar Fecha", command=open_calendar)
    fecha_compra_button.grid(row=len(labels) + 2, column=0, columnspan=2, pady=5)

    def submit_reporte():
        if fecha_compra_entry.get() == "":
            messagebox.showwarning("Advertencia", "Debes seleccionar una fecha de compra.")
            return

        try:
            fecha_compra = datetime.strptime(fecha_compra_entry.get(), "%d/%m/%Y")
        except ValueError:
            messagebox.showwarning("Advertencia", "El formato de fecha de compra es incorrecto. Utiliza el formato dd/mm/yyyy.")
            return

        if fecha_compra.date() > datetime.now().date():
            messagebox.showwarning("Advertencia", "La fecha de compra no puede ser posterior a la fecha actual.")
            return

        reporte = {
            "Fecha de compra": fecha_compra.strftime("%d/%m/%Y"),
            "Número de factura": entries[0].get(),
            "Nombre": entries[1].get(),
            "Teléfono": entries[2].get(),
            "Dirección": entries[3].get(),
            "Identificación": entries[4].get(),
            "Descripción del daño": entries[5].get()
            }
        reportes.append(reporte)
        num_reportes_value.set(str(len(reportes)))
        messagebox.showinfo("Éxito", "El reporte se ha guardado correctamente.")

        # Limpiar campos después de guardar el reporte
        for entry in entries:
            entry.delete(0, tk.END)
        fecha_compra_entry.delete(0, tk.END)

    submit_button = tk.Button(form_frame, text="Enviar", command=submit_reporte)
    submit_button.grid(row=len(labels)+3, column=0, columnspan=2, pady=10)

# Ventana de recibo
def mostrar_ventana_recibo():
    password = simpledialog.askstring("Contraseña", "Ingresa la contraseña:", show="*")
    if password == "12345":
        recibo_window = tk.Toplevel(root)
        recibo_window.title("Recibo")

        recibo_frame = tk.Frame(recibo_window, padx=20, pady=20)
        recibo_frame.pack()

        title_label = tk.Label(recibo_frame, text="Recibo", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        for i, label_text in enumerate(labels):
            label = tk.Label(recibo_frame, text=label_text)
            label.grid(row=i+1, column=0, sticky="w")
            entry = tk.Entry(recibo_frame)
            entry.grid(row=i+1, column=1, pady=5)
            entries_de_recibo.append(entry)

        informe_entry = tk.Text(recibo_frame, width=30, height=10)
        informe_entry.grid(row=len(labels)+1, column=1, pady=5)

        generar_button = tk.Button(recibo_frame, text="Generar", command=generar_recibo)
        generar_button.grid(row=len(labels)+2, column=0, columnspan=2, pady=10)
    else:
        messagebox.showerror("Error", "Contraseña incorrecta.")

#--------------------------------------Dónde irá el mensaje que dice si existe o no existe el número de recibo-----------------------------------------------------------------
def generar_recibo():
    if(entries[0] == entries[0]):
        messagebox.showinfo("Bien","El número de recibo si existe!")
    else:
        messagebox.showerror("Error","El número de recibo no existe")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
# Barra de menú
menubar = tk.Menu(root)

reportes_menu = tk.Menu(menubar, tearoff=0)
reportes_menu.add_command(label="Mostrar reportes", command=mostrar_ventana_reportes)
menubar.add_cascade(label="Reportes", menu=reportes_menu)

usuarios_menu = tk.Menu(menubar, tearoff=0)
usuarios_menu.add_command(label="Generar reporte de usuario", command=mostrar_ventana_usuarios)
menubar.add_cascade(label="Usuarios", menu=usuarios_menu)

recibo_menu = tk.Menu(menubar, tearoff=0)
recibo_menu.add_command(label="Generar recibo", command=mostrar_ventana_recibo)
menubar.add_cascade(label="Recibo", menu=recibo_menu)

root.config(menu=menubar)

root.mainloop()
