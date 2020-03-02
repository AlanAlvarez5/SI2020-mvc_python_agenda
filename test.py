from model.model import  Model
from view.view import View
from controller.controller import Controller

# c = Contacto(1, 'Juan Perez', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')
# c2 = Contacto(2, 'Alan Alvarez', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')

# cita = Cita(1,c.id_contacto, 'Mi casa', '11-11-2020', '12:00', 'El delicioso')

# contactos = []
# contactos.append(c)
# contactos.append(c2)

# guess = input('dame un perro nombre: ')

# for contacto in contactos:
#     if guess ==  contacto.nombre:
#         print("Si existe")
    
    
# print(c.nombre)
# print(cita.asunto)

# m = Model()

# m.agregar_contacto(1 , 'Juan Perez', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')
# m.agregar_contacto(2 , 'JJEJe', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')
# m.agregar_cita(1, 1,'aqui','mañana','12','nada')
# m.agregar_cita(2, 1,'aqui','mañana','12','nada de nada')

# s =  m.leer_contacto(2)
# print(s.nombre)

# m.actualizar_contacto(2, 'Mario', '12345', 'mario@gmail.com', 'free')
# s =  m.leer_contacto(2)
# print(s.nombre)


# citas = m.mostrar_citas()
# contactos = m.mostrar_contactos()
# for i in citas:
#     print(i.asunto)
# for i in contactos:
#     print(i.nombre)

# print("------")
# m.borrar_contacto(1)

# citas = m.mostrar_citas()
# contactos = m.mostrar_contactos()
# for i in citas:
#     print(i.asunto)
# for i in contactos:
#     print(i.nombre)

# v = View()
# s  = m.mostrar_contactos()
# v.mostrar_contactos(s)

# f, c = m.borrar_contacto(1)
# if f:
#     v.borrar_contacto(c)
# else:
#     v.contacto_no_existe(1)

cont = Controller()
cont.start()