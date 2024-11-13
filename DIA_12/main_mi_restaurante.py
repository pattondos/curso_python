from tkinter import *
import random, datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [12.32, 15.65, 27.31, 36.22, 17.22, 17.99, 27.05, 28.65]
precios_bebida = [30.25, 54.99, 15.21, 16.54, 17.08, 18.10, 29.00, 10.58]
precios_postres = [12.54, 14.68, 16.32, 18.97, 20.55, 21.14, 13.94, 15.74]

def on_click_btn(numero):
    global operador
    operador = operador + numero
    fr_calculadora.delete(0, END)
    fr_calculadora.insert(END, operador)

def on_click_delete_num():
    global operador
    operador = ""
    fr_calculadora.delete(0, END)

def on_click_resultado():
    global operador
    resultado = str(eval(operador))
    fr_calculadora.delete(0, END)
    fr_calculadora.insert(0, resultado)
    operador = ""
    
def verificar_check():
    
    #COMIDA
    contador_check_comida = 0
    for cont_com in cuadros_comida:
        if variables_comida[contador_check_comida].get() == 1:
            cuadros_comida[contador_check_comida].config(state=NORMAL)
            if cuadros_comida[contador_check_comida].get == "0":
                cuadros_comida[contador_check_comida].delete(0, END)
            cuadros_comida[contador_check_comida].focus()
        else:
            cuadros_comida[contador_check_comida].config(state=DISABLED)
            texto_comida[contador_check_comida].set("0")
        contador_check_comida += 1
        
    #BEBIDA
    contador_check_bebida = 0
    for cont_beb in cuadros_bebida:
        if variables_bebida[contador_check_bebida].get() == 1:
            cuadros_bebida[contador_check_bebida].config(state=NORMAL)
            if cuadros_bebida[contador_check_bebida].get == "0":
                cuadros_bebida[contador_check_bebida].delete(0, END)
            cuadros_bebida[contador_check_bebida].focus()
        else:
            cuadros_bebida[contador_check_bebida].config(state=DISABLED)
            texto_bebida[contador_check_bebida].set("0")
        contador_check_bebida += 1
        
    #POSTRE
    contador_check_postre = 0
    for cont_post in cuadros_postre:
        if variables_postre[contador_check_postre].get() == 1:
            cuadros_postre[contador_check_postre].config(state=NORMAL)
            if cuadros_postre[contador_check_postre].get == "0":
                cuadros_postre[contador_check_postre].delete(0, END)
            cuadros_postre[contador_check_postre].focus()
        else:
            cuadros_postre[contador_check_postre].config(state=DISABLED)
            texto_postre[contador_check_postre].set("0")
        contador_check_postre += 1

def calcula_total():
    #COMIDA
    subtotal_comida = 0
    ind_comida = 0
    for cant_com in texto_comida:
        subtotal_comida = subtotal_comida + float(cant_com.get()) * precios_comida[ind_comida]
        ind_comida += 1
    
    #BEBIDA
    subtotal_bebida = 0
    ind_bebida = 0
    for cant_beb in texto_bebida:
        subtotal_bebida = subtotal_bebida + float(cant_beb.get()) * precios_bebida[ind_bebida]
        ind_bebida += 1
    
    #POSTRE
    subtotal_postre = 0
    ind_postre = 0
    for cant_pos in texto_postre:
        subtotal_postre = subtotal_postre + float(cant_pos.get()) * precios_postres[ind_postre]
        ind_postre += 1
        
    #Cálculos con las cantidades  
    subtotal = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestos = subtotal * 0.16
    total = subtotal + impuestos
    
    #Envío de costos hacia las etiquetas correspondientes
    var_costo_comida.set(f"$ {round(subtotal_comida, 2)}")
    var_costo_bebida.set(f"$ {round(subtotal_bebida, 2)}")
    var_costo_postre.set(f"$ {round(subtotal_postre, 2)}")
    var_subtotal.set(f"$ {round(subtotal, 2)}")
    var_impuesto.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total, 2)}")


def crear_recibo():
    txt_recibo.delete(1.0, END)
    no_recibo = f"No. Recibo: {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    
    txt_recibo.insert(END, f"{no_recibo}\n")
    txt_recibo.insert(END, f"Fecha: {fecha_recibo}\n")
    txt_recibo.insert(END, f"*" * 55 +"\n")
    txt_recibo.insert(END, "Items\t\tCant\t\tCosto\n")
    txt_recibo.insert(END, f"-" * 55 +"\n")
    
    contador_comida = 0
    for comida in texto_comida:
        if comida.get() != "0":
            txt_recibo.insert(END, 
                              f"{lista_comidas[contador_comida]}\t\t{comida.get()}\t\t"
                              f"${round(int(comida.get()) * precios_comida[contador_comida], 2)}\n")
        contador_comida += 1    
    
    contador_bebida = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            txt_recibo.insert(END, 
                              f"{lista_bebidas[contador_bebida]}\t\t{bebida.get()}\t\t"
                              f"${round(int(bebida.get()) * precios_bebida[contador_bebida], 2)}\n")
        contador_bebida += 1    
    
    contador_postre = 0
    for postre in texto_postre:
        if postre.get() != "0":
            txt_recibo.insert(END, 
                              f"{lista_postres[contador_postre]}\t\t{postre.get()}\t\t"
                              f"${round(int(postre.get()) * precios_postres[contador_postre], 2)}\n")
        contador_postre += 1  
    
    txt_recibo.insert(END, f"-" * 55 + "\n")
    txt_recibo.insert(END, f"Costo total comida:\t\t{var_costo_comida.get()}\n")  
    txt_recibo.insert(END, f"Costo total bebida:\t\t{var_costo_bebida.get()}\n")  
    txt_recibo.insert(END, f"Costo total postre:\t\t{var_costo_postre.get()}\n")  
    txt_recibo.insert(END, f"-" * 55 + "\n")
    txt_recibo.insert(END, f"Subtotal:\t\t{var_subtotal.get()}\n") 
    txt_recibo.insert(END, f"Impuestos:\t\t{var_impuesto.get()}\n") 
    txt_recibo.insert(END, f"Total:\t\t{var_total.get()}\n") 
    txt_recibo.insert(END, f"*" * 55 +"\n")
    txt_recibo.insert(END, "¡Gracias por su visita!\nSi la ve, me la saluda.")

def guardar_recibo():
    info_recibo = txt_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    
    messagebox.showinfo("ATENCIÓN", "El recibo se ha guardado.")
    
def limpiar_pantalla():
    txt_recibo.delete(0.1, END)
    
    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_postre:
        texto.set("0")
        
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)      
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
        
    for variable in variables_comida:
        variable.set(0)
    for variable in variables_bebida:
        variable.set(0)
    for variable in variables_postre:
        variable.set(0)
        
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")

# Iniciar aplicación
app = Tk()

# Tamaño de la ventana
app.geometry("1020x980")

#Evitar redimencionar
app.resizable(0, 0)

#Título de la ventana
app.title('Restaurante "Rosas El Este"')

# Color de fondo de la pantalla
app.config(bg="gray")

#Panel superior
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#Etiqueta titulo
etiqueta_titulo = Label(panel_superior, 
                        text="Sistema de Facturación", 
                        fg="blue",
                        font=("Arial", 30), 
                        bg="white", 
                        width=30)
etiqueta_titulo.grid(row=0, column=0)
#################################################################################################
'''
DECLARACIÓN DE PÁNELES 1A PARTE
'''
#Panel izquierdo
panel_izquierdo = Frame(app, bd=1, relief=FLAT, pady=-30)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=130)
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Arial", 15, "bold"),
                           bd=1, relief=FLAT)
panel_comidas.pack(side=LEFT)

#Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Arial", 15, "bold"),
                           bd=1, relief=FLAT)
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Arial", 15, "bold"),
                           bd=1, relief=FLAT)
panel_postres.pack(side=LEFT)
##############################################################################################
'''
DECLARACIÓN DE PÁNELES 2A PARTE
'''
#Panel derecho
panel_derecho = Frame(app, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="gray")
panel_botones.pack()
############################################################################################
'''
PANEL DE COMIDAS
'''
#Lista de productos
lista_comidas = ["Milanesa", "Pescado", "Mole", "Pizza Hawaiana",
                 "Albóndigas", "Discada", "Burrito", "Camarones"]
lista_bebidas = ["Agua limón", "Agua horchata", "Coca-Cola", "Sprite", "Cerveza corona", 
                 "Vino tinto", "Cerveza Victoria", "Agua simple"]
lista_postres = ["Tiramisú", "Pastel choco.", "Gelatina", "Pie limón", "Pie queso",
                 "Volovan", "Fresas crema", "Ate"]
'''
Aqui guardaremos las comidas seleccionadas
'''
#Items para guardar la comida
variables_comida = []
cuadros_comida = []
texto_comida = []


contador = 0
for comida in lista_comidas:
    variables_comida.append("")
    variables_comida[contador] = IntVar()
    
    comida = Checkbutton(panel_comidas, text=comida.title(), 
                         font=("Arial", 12, "bold"),
                         onvalue=1, 
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=verificar_check)
    comida.grid(row=contador, column=0, sticky=W)
    
    #Crear check box
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    
    cuadros_comida[contador]=Entry(panel_comidas,
                                   font=("Arial", 12, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1
'''
Aqui guardaremos las bebidas seleccionadas
'''
#Items para guardar la bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []

contador = 0
for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[contador] = IntVar()
    
    bebida = Checkbutton(panel_bebidas, 
                         text=bebida.title(), 
                         font=("Arial", 12, "bold"),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_bebida[contador],
                         command= verificar_check)
    bebida.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #Crear check box
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    
    cuadros_bebida[contador]=Entry(panel_bebidas,
                                   font=("Arial", 12, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    
    contador += 1
'''
Aqui guardaremos los postres seleccionados
'''
#Items para guardar el postre
variables_postre = []
cuadros_postre = []
texto_postre = []

contador = 0
for postre in lista_postres:
    variables_postre.append("")
    variables_postre[contador] = IntVar()
    
    postre = Checkbutton(panel_postres, text=postre.title(), 
                         font=("Arial", 12, "bold"),
                         onvalue=1, 
                         offvalue=0, 
                         variable=variables_postre[contador],
                         command=verificar_check)
    postre.grid(row=contador, 
                column=0, 
                sticky=W)
    
    #Crear check box
    cuadros_postre.append("")
    texto_postre.append("")
    texto_postre[contador] = StringVar()
    texto_postre[contador].set("0")
    
    cuadros_postre[contador]=Entry(panel_postres,
                                   font=("Arial", 12, "bold"),
                                   bd=1,
                                   width=6,
                                   state=DISABLED,
                                   textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador,
                                  column=1)
    
    contador += 1

############################################################################################
'''
PANEL DE COSTOS
'''
# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


# Etiqueta de costo y campos de entrada
#COMIDAS
etq_costo_comida = Label(panel_costos,
                         text="Costos comida",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_costo_comida.grid(row=0, column=0)

txt_costo_comida = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costo_comida)
txt_costo_comida.grid(row=0, column=1, padx = 40)

#BEBIDAS
etq_costo_bebida = Label(panel_costos,
                         text="Costos bebida",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_costo_bebida.grid(row=1, column=0)

txt_costo_bebida = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costo_bebida)
txt_costo_bebida.grid(row=1, column=1, padx = 40)

#POSTRES
etq_costo_postre = Label(panel_costos,
                         text="Costos postre",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_costo_postre.grid(row=2, column=0)

txt_costo_postre = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_costo_postre)
txt_costo_postre.grid(row=2, column=1, padx = 40)

#SUBTOTAL
etq_subtotal = Label(panel_costos,
                         text="Subtotal",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_subtotal.grid(row=0, column=2)

txt_subtotal = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         width=10,
                         state="readonly",
                         textvariable=var_subtotal)
txt_subtotal.grid(row=0, column=3, padx = 40)

#IMPUESTOS
etq_impuesto = Label(panel_costos,
                         text="Impuesto",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_impuesto.grid(row=1, column=2)

txt_impuesto = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         fg="black",
                         width=10,
                         state="readonly",
                         textvariable=var_impuesto)
txt_impuesto.grid(row=1, column=3, padx = 40)

#TOTAL
etq_total = Label(panel_costos,
                         text="Total",
                         font=("Arial", 11, "bold"),
                         bg="azure4",
                         fg="black")
etq_total.grid(row=2, column=2)

txt_total = Entry(panel_costos,
                         font=("Arial", 10, "bold"),
                         bd=1,
                         fg="black",
                         width=10,
                         state="readonly",
                         textvariable=var_total)
txt_total.grid(row=2, column=3, padx=40)

############################################################################################
'''
BOTONES
'''
botones = ["Total", "Recibo", "Guardar", "Reiniciar"]
btns_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Arial", 9, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=8
                   )
    btns_creados.append(boton)
    
    boton.grid(row=0, 
                column=columnas)
    columnas += 1

btns_creados[0].config(command = calcula_total)
btns_creados[1].config(command = crear_recibo)
btns_creados[2].config(command = guardar_recibo)
btns_creados[3].config(command = limpiar_pantalla)
############################################################################################
'''RECIBO'''
txt_recibo = Text(panel_recibo,
                  font=("Arial", 8, "bold"),
                  bd=1,
                  width=40,
                  height=10)
txt_recibo.grid(row=0,
                column=0)
############################################################################################
'''CALCULADORA'''
fr_calculadora = Entry(panel_calculadora,
                       font=("Arial", 15, "bold"),
                       bd=1,
                       width=20)
fr_calculadora.grid(row=0,
                    column=0, 
                    columnspan=4)
btns_calc = ["7", "8", "9", "+",
             "4", "5", "6", "-",
             "1", "2", "3", "*",
             "R", "B", "0", "/"]
btns_guardar = []

fila_calc = 1
columna_calc = 0
for boton in btns_calc:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=("Arial", 15, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=4
                   )
    btns_guardar.append(boton)
    
    boton.grid(row=fila_calc,
               column=columna_calc)
    if columna_calc == 3:
        fila_calc += 1
    columna_calc += 1
    if columna_calc == 4:
        columna_calc = 0
        
        
btns_guardar[0].config(command = lambda : on_click_btn('7'))
btns_guardar[1].config(command = lambda : on_click_btn('8'))
btns_guardar[2].config(command = lambda : on_click_btn('9'))
btns_guardar[3].config(command = lambda : on_click_btn('+'))
btns_guardar[4].config(command = lambda : on_click_btn('4'))
btns_guardar[5].config(command = lambda : on_click_btn('5'))
btns_guardar[6].config(command = lambda : on_click_btn('6'))
btns_guardar[7].config(command = lambda : on_click_btn('-'))
btns_guardar[8].config(command = lambda : on_click_btn('1'))
btns_guardar[9].config(command = lambda : on_click_btn('2'))
btns_guardar[10].config(command = lambda : on_click_btn('3'))
btns_guardar[11].config(command = lambda : on_click_btn('*'))
btns_guardar[12].config(command = on_click_resultado)
btns_guardar[13].config(command = on_click_delete_num)
btns_guardar[14].config(command = lambda : on_click_btn('0'))
btns_guardar[15].config(command = lambda : on_click_btn('/'))

############################################################################################


#Loop para evitar que la ventana se cierre
app.mainloop()
