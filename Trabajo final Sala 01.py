from tkinter import *
from tkinter import messagebox
from tkinter.constants import *


class suma(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=450, height=400, bg ="#ff9f00")
        self.master = master
        self.pack()
        self.controles()

    def controles(self):

        #Labels diseño
        self.lbc = Label(self, bg="#ff9f00")
        self.lbc.place(relwidth=1, y=0, height=40)

        self.lbc1 = Label(self, bg="#ffffff")
        self.lbc1.place(relwidth=0.96, x=9, y=168, height=150)

        self.lbc2 = Label(self, bg="#9b9b9b")
        self.lbc2.place(relwidth=0.96, x=9, y=195, height=1)

        self.lbc3 = Label(self, bg="#9b9b9b")
        self.lbc3.place(relwidth=0.96, x=9, y=225, height=1)

        self.lbc4 = Label(self, bg="#9b9b9b")
        self.lbc4.place(relwidth=0.96, x=9, y=255, height=1)

        self.lbc5 = Label(self, bg="#9b9b9b")
        self.lbc5.place(relwidth=0.96, x=9, y=285, height=1)

        # Labels
        self.label1 = Label(self, text='Ferretería "El Tornillo Feliz"', bg='#ff9f00', fg="white")
        self.label1.place(relx=0.25, y=5)
        self.label1.configure(font=("Arial", 14, "italic"))

        self.label2 = Label(self, text="DNI:", width=8, anchor=E, bg="#ff9f00")
        self.label2.place(x=10, y=50)
        self.label2.configure(font=("Arial", 10))

        self.label3 = Label(self, text="Apellidos:", width=8, anchor=E, bg="#ff9f00")
        self.label3.place(x=10, y=80)
        self.label3.configure(font=("Arial", 10))

        self.label4 = Label(self, text="Nombres:", width=8, bg="#ff9f00", anchor=E)
        self.label4.place(x=240, y=80)
        self.label4.configure(font=("Arial", 10))

        self.label5 = Label(self, text="Dirección:", width=8, bg="#ff9f00", anchor=E)
        self.label5.place(x=10, y=110)
        self.label5.configure(font=("Arial", 10))

        self.label6 = Label(self, text="Telefono:", width=8, bg="#ff9f00", anchor=E)
        self.label6.place(x=10, y=140)
        self.label6.configure(font=("Arial", 10))

        self.label7 = Label(self, text="Cod_Prod", bg="white")
        self.label7.place(x=10, y=170)
        self.label7.configure(font=("Arial", 10, "bold"))

        self.label8 = Label(self, text="Descripción", bg="white")
        self.label8.place(x=100, y=170)
        self.label8.configure(font=("Arial", 10, "bold"))

        self.label9 = Label(self, text="Unidad", bg="white")
        self.label9.place(x=200, y=170)
        self.label9.configure(font=("Arial", 10, "bold"))

        self.label10 = Label(self, text="Cantidad", bg="white")
        self.label10.place(x=260, y=170)
        self.label10.configure(font=("Arial", 10, "bold"))

        self.label11 = Label(self, text="Precio", bg="white")
        self.label11.place(x=330, y=170)
        self.label11.configure(font=("Arial", 10, "bold"))

        self.label12 = Label(self, text="Subtotal", bg="white")
        self.label12.place(x=380, y=170)
        self.label12.configure(font=("Arial", 10, "bold"))

        self.label13 = Label(self, text="Total: s/", bg="white")
        self.label13.place(x=320, y=290)
        self.label13.configure(font=("Arial", 10, "bold"))

        # Inputs
        # DNI
        self.txt1 = Entry(self, highlightcolor="black", highlightthickness=0.5, relief=FLAT, selectbackground="red")
        self.txt1.focus()
        self.txt1.place(x=85, y=50, width=80)
        # Apellido
        self.txt2 = Entry(self, highlightcolor="black", highlightthickness=0.5, relief=FLAT)
        self.txt2.place(x=85, y=80)
        # Nombre
        self.txt3 = Entry(self, highlightcolor="black", highlightthickness=0.5, relief=FLAT)
        self.txt3.place(x=315, y=80, width=100)
        # Direccion
        self.txt4 = Entry(self, highlightcolor="black", highlightthickness=0.5, relief=FLAT)
        self.txt4.place(x=85, y=110)
        # Telefono
        self.txt5 = Entry(self, highlightcolor="black", highlightthickness=0.5, relief=FLAT)
        self.txt5.place(x=85, y=140, width=80)
        # Codigo producto
        self.txt6 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt6.place(x=20, y=200, width=30)

        self.txt7 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt7.place(x=20, y=230, width=30)

        self.txt8 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt8.place(x=20, y=260, width=30)
        # Descipción
        self.des1 = StringVar(value='Clavos 1/2"')
        self.des2 = StringVar(value='Pintura Latex Pato')
        self.des3 = StringVar(value='Plástico 2m ancho')
        self.txt9 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.des1, border=0)
        self.txt9.place(x=80, y=200, width=110)

        self.txt10 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.des2, border=0)
        self.txt10.place(x=80, y=230, width=110)

        self.txt11 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.des3, border=0)
        self.txt11.place(x=80, y=260, width=110)
        # Unidad
        self.uni1 = StringVar(value="Kilo")
        self.uni2 = StringVar(value="Balde")
        self.uni3 = StringVar(value="Metros")
        self.txt12 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.uni1, border=0)
        self.txt12.place(x=205, y=200, width=40)

        self.txt13 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.uni2, border=0)
        self.txt13.place(x=205, y=230, width=40)

        self.txt14 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.uni3, border=0)
        self.txt14.place(x=205, y=260, width=40)
        # Cantidad
        self.txt15 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt15.place(x=270, y=200, width=30)

        self.txt16 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt16.place(x=270, y=230, width=30)

        self.txt17 = Entry(self, highlightcolor="black", highlightbackground="#9b9b9b", highlightthickness=0.5, relief=FLAT)
        self.txt17.place(x=270, y=260, width=30)
        # Precio
        self.pre1 = StringVar(value="s/ 4.00")
        self.pre2 = StringVar(value="s/ 30.00")
        self.pre3 = StringVar(value="s/ 8.00")
        self.txt18 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.pre1, border=0)
        self.txt18.place(x=320, y=200, width=50)

        self.txt19 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.pre2, border=0)
        self.txt19.place(x=320, y=230, width=50)

        self.txt20 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.pre3, border=0)
        self.txt20.place(x=320, y=260, width=50)
        # Subtotal
        self.sub1 = StringVar(value=0)
        self.sub2 = StringVar(value=0)
        self.sub3 = StringVar(value=0)
        self.txt21 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.sub1, border=0)
        self.txt21.place(x=385, y=200, width=40)

        self.txt22 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.sub2, border=0)
        self.txt22.place(x=385, y=230, width=40)

        self.txt23 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.sub3, border=0)
        self.txt23.place(x=385, y=260, width=40)
        # Total
        self.tot = StringVar()
        self.txt24 = Entry(self, disabledbackground="white", disabledforeground="black", state="disabled", textvariable=self.tot, border=0)
        self.txt24.place(x=385, y=293, width=40)

        # Boton
        self.btn1 = Button(self, text="Calcular", command=self.Calcular, bg="white", font=("Arial", 10), relief=FLAT, fg='#ff9f00', overrelief="raised")
        self.btn1.place(x=80, y=350)
        self.btn2 = Button(self, text="Limpiar", command=self.limpiar, bg="white", font=("Arial", 10), relief=FLAT, fg='#ff9f00', overrelief="raised")
        self.btn2.place(x=200, y=350)
        self.btn3 = Button(self, text="Imprimir", command=self.imprimir, bg="white", font=("Arial", 10), relief=FLAT, state="disabled", fg='#ff9f00', overrelief="raised", disabledforeground="#6E7C7C")
        self.btn3.place(x=310, y=350)

    def Calcular(self):
        try:
            self.sub1.set(float(self.txt15.get())*4)
            self.sub2.set(float(self.txt16.get())*30)
            self.sub3.set(float(self.txt17.get())*8)
            self.tot.set(float(self.sub1.get()) +
                         float(self.sub2.get()) + float(self.sub3.get()))
            self.btn3['state'] = "normal"
        except:
            messagebox.showinfo("AVISO IMPORTANTE", """Por favor, evite dejar celdas vacias.
Ingrese los datos del código o cantidad de los productos.""")

    def imprimir(self):
        if self.txt1.get()!='' and self.txt2.get()!='' and self.txt3.get()!='' and self.txt4.get()!='' and self.txt5.get()!='':
            try:
                dni = int(self.txt1.get())
                nom = self.txt2.get()
                ape = self.txt3.get()
                direc = self.txt4.get()
                tele = int(self.txt5.get())
                print(f"""
                     BOLETA DE VENTA
------------------------------------------------------------
                    DATOS DEL CLIENTE                     
------------------------------------------------------------
NOMBRES: {nom}		APELLIDOS: {ape}
DNI: {dni}
DIRECCIÓN: {direc}	TELÉFONO: {tele}
------------------------------------------------------------
                     DATOS DE LA COMPRA                   
------------------------------------------------------------
Código  Descripción		Unidad	  Cant.	Precio	Subtotal
 {self.txt6.get()}	Clavos 1/2"		{self.txt12.get()}	   {self.txt15.get()}	4.00	{float(self.txt21.get())}
 {self.txt7.get()}	Pintura Latex Pato	{self.txt13.get()}	   {self.txt16.get()}	30.00	{float(self.txt22.get())}
 {self.txt8.get()}	Plástico 2m ancho	{self.txt14.get()}	   {self.txt17.get()}	8.00	{float(self.txt23.get())}

						Total: {float(self.txt24.get())}
------------------------------------------------------------
                     GRACIAS POR SU VISTIA          
                       VUELVA PONTO!! :D
------------------------------------------------------------""")
            except:
                messagebox.showinfo(
                    "AVISO IMPORTANTE", "Por favor, ingrese bien los datos pedidos")

        else:
            messagebox.showinfo(
                "AVISO IMPORTANTE", """Por favor, evite dejar celdas vacias.
Es necesario que ingrese los datos del cliente para generar la boleta.""")

    def limpiar(self):
        self.sub1.set(0)
        self.sub2.set(0)
        self.sub3.set(0)
        self.tot.set("")
        self.txt1.delete(0, "end")
        self.txt2.delete(0, "end")
        self.txt3.delete(0, "end")
        self.txt4.delete(0, "end")
        self.txt5.delete(0, "end")
        self.txt6.delete(0, "end")
        self.txt7.delete(0, "end")
        self.txt8.delete(0, "end")
        self.txt15.delete(0, "end")
        self.txt16.delete(0, "end")
        self.txt17.delete(0, "end")


ventana = Tk()
ventana.title("FERRETERIA")
ventana.resizable(False, False)
operacion = suma(ventana)
ventana.mainloop()
