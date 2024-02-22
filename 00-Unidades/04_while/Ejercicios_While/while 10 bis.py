import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    
Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0


        while True :
            numero = prompt("solicitar numero", "ingrese numero")
                     
            if numero == None :
                break 
            numero = int(numero) 
            
            if numero < 0 : 
                acumulador_negativos += numero
                contador_negativos += 1
            if numero > 0 :
                acumulador_positivos += numero
                contador_positivos += 1

            else :
                contador_ceros += 1
            
            numero = int(numero)
       
        diferencia = contador_positivos - contador_negativos
                   
        mensaje = f"acumulador negativos: {acumulador_negativos} \nAcumulador positivos: {acumulador_positivos} \nContador negativos: {contador_negativos} \nContador positivos: {contador_positivos} \nContador ceros: {contador_ceros} \nDiferencia :{diferencia}"       
        alert ("Resultados", mensaje)
    
        acumulador_positivos.delete(0, tkinter.END)
        acumulador_positivos.insert(0, acumulador_positivos)
        acumulador_negativos.delete(0, tkinter.END)
        acumulador_negativos.insert(0, acumulador_negativos)
        contador_positivos.delete(0, tkinter.END)
        contador_positivos.insert(0, contador_positivos)
        contador_negativos.delete(0, tkinter.END)
        contador_negativos.insert(0, contador_negativos)
        contador_ceros.delete(0, tkinter.END)
        contador_ceros.insert(0, contador_ceros)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

