import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: franco
apellido: salvatierra 
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca
          el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % 
        y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” 
        se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        combobox_cantidad = self.combobox_cantidad.get()
        cantidad = int(combobox_cantidad)
        mensaje = " "
    

        if cantidad >= 6 :
            subtotal = (cantidad * 800 * 0.5)
        elif cantidad == 5 and marca == "Argentinaluz" : 
            subtotal = (cantidad * 800 * 0.4)
        elif cantidad == 5 :
            subtotal = (cantidad * 800 * 0.3)   
        elif cantidad == 4 and (marca == "Argentinaluz" or marca == "FelipeLamparas") :
            subtotal = (cantidad * 800 * 0.25)
        elif cantidad == 4 : 
            subtotal = (cantidad * 800 * 0.2)
        elif cantidad == 3 and marca == "Argentinaluz" : 
            subtotal = (cantidad * 800 * 0.15)
        elif cantidad == 3 and marca == "FelipeLamparas" : 
            subtotal = (cantidad * 800 * 0.10)
        else :
            subtotal = (cantidad * 800 * 0.5) 

       
        if subtotal > int(4000) :
            mensaje = (cantidad * 800 * 0.5)
        else : 
            mensaje = subtotal


        alert("A PAGAR", subtotal)





      

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()