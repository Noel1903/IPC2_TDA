# -*- coding: utf-8 -*-
"""TDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gBQ3qySOVB_lTih3vOnUlivI1p14f2b8

**Ejercicio de Listas Enlazadas**
"""

class cliente:
  def __init__(self,nombre,no_habitacion):
    self.nombre = nombre
    self.no_habitacion = no_habitacion

class node:
  def __init__(self,cliente=None, next=None):
    self.cliente = cliente
    self.next = next

class linked_list:
  def __init__(self):
    self.head = None

  def imprimir(self):
    node = self.head
    while node != None:
      print(node.cliente.nombre, end = "=>")
      node = node.next


  def insertar(self,cliente):
    if not self.head:
      self.head=node(cliente=cliente)
      return
    current = self.head  #actual
    while current.next:
      current = current.next
    current.next = node(cliente=cliente)


  def eliminar(self, no_habitacion):
    current = self.head
    previous = None
    while current and current.cliente.no_habitacion !=no_habitacion:
      previous = current
      current = current.next

    if previous is None:
      self.head = current.next
    elif current:
      previous.next = current.next
      current.next = None

c1 = cliente("Estuardo Zapeta", 101)
c2 = cliente("Marco Lopez", 103)
c3 = cliente("Josue Armas", 204)
c4 = cliente("Gladys Olmos", 302)

lista = linked_list()
lista.insertar(c1)
lista.insertar(c2)
lista.insertar(c3)
lista.insertar(c4)

lista.imprimir()
lista.eliminar(103)
print("")
lista.imprimir()

"""**Ejemplo de Listas Circulares**"""

class linked_list_circular:
  def __init__(self,head=None):
    self.head = head
    self.size = 0

  def insertar(self, cliente):
    if self.size ==0:
      self.head = node(cliente=cliente)
      self.head.next = self.head
    else:
      new_node = node(cliente=cliente, next=self.head.next)
      self.head.next = new_node
    self.size +=1

  def imprimir(self):
    if self.head is None:
      return 
    node = self.head
    print(node.cliente.nombre, end=" => ")
    while node.next != self.head:
      node = node.next
      print(node.cliente.nombre, end = " => ")

  def eliminar (self, no_habitacion):
    node = self.head
    previous = None

    while True:
      if node.cliente.no_habitacion == no_habitacion:
        if previous is not None:
          previous.next = node.next
        else:
          while node.next != self.head:
            node = node.next
          node.next = self.head.next
          self.head = self.head.next
        self.size -= 1
        return True
      elif node.next == self.head:
        return False
        
      previous = node
      node = node.next

lista_c = linked_list_circular()
lista_c.insertar(c1)
lista_c.insertar(c2)
lista_c.insertar(c3)
lista_c.insertar(c4)
lista_c.imprimir()
print()
lista_c.eliminar(101)
lista_c.imprimir()

"""### **Listas doblemente enlazadas**"""

class node_de:
  def __init__(self, cliente=None, next=None,previous=None):
    self.cliente = cliente
    self.previous = previous
    self.next = next