# -*- coding: utf-8 -*-
"""Taller con colores

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ySQGMHmHTymhaEVfkAUWqr4EY04_Gwl2
"""

class Helado:
  def __init__(self,sabor,numSab,Presentacion,textura,color):
    self.sabor = sabor
    self.numSab = numSab
    self.Presentacion=Presentacion
    self.textura=textura
    self.color=color
  #atributos
  sabor="fresa"
  numSab=int(2)
  Presentacion="cono"
  textura="cremosa"
  color="rosado"
  #Metodos
  def cambiarSabor(self):
    print("su sabor ha cambiado a manzana")
  def cambiarNumSab(self):
    print("su numeros de sabores ha cambiado a 3")
  def agregartopping(self):
    print("se han agregado gomitas y un brownie")
  def Derretirhelado(self):
    print("El helado se ha derretido a 30 grados ")
  def ajustarpresentacion(self):
    print("La presentacion se ha ajustado a un vaso")

h1=Helado("fresa",2,"cono","cremosa","rosado")
h2=Helado("chocolate", 1 , "vaso" , "cremosa" , "marron")
h3=Helado("Arequipe" , 3 , "cono", "cremosa", "marron claro")
h1.cambiarSabor()
h2.cambiarNumSab()
h3.agregartopping()

class Banco:
  def __init__(self, area, trabajadores, ventanas, puertas, altura):
    #atributos
    self.area=int(500)
    self.trabajadores=int(83)
    self.ventanas=int(20)
    self.puertas=int(5)
    self.altura=int(50)

#Metodos
  def Ampliar(self):
    print("El área del banco se ha ampliado")
  def Contratar(self):
    print("Se han contratado trabajadores")
  def Cerrar(self):
    print("Las ventanas se han cerrado")
  def Abrir(self):
    print("Las puertas del banco se han abierto")
  def Aumentar(self):
    print("La altura del banco ha aumentado")
b1=Banco(400, 57, 6, 14, 30)
b2=Banco(350, 61, 17, 12, 25)
b3=Banco(300, 48, 15, 8, 28)
b1.Ampliar()
b2.Contratar()
b3.Cerrar()
b1.Abrir()
b1.Aumentar()