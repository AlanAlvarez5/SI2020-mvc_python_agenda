class View:

    # Contactos
    def mostrar_contacto(self, contacto):
        print('\n\n***** Datos del contacto *****')
        print('Nombre: ', contacto.nombre)
        print('Telefono: ', contacto.tel)
        print('Correo', contacto.correo)
        print('Dirección: ', contacto.dir)
        print('******************************')

    def mostrar_contactos(self, contactos):
        print('\n\n********* Contactos **********\n')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir, '\n')
        print('\n******************************\n')
    
    def crear_contacto(self, contacto):
        print('\n\n**** '+contacto.nombre+ 'ha nacido ***')
    def borrar_contacto(self, contacto):
        print('\n\n*** '+contacto.nombre+ 'ha sido asesinado ***')
    def modificar_contacto(self, id_contacto):
        print('\n\n*** Actualizacion Exitosa ***')
    def contacto_ya_existe(self, contacto):
        print( '*********\nID YA UTILIZADO\n*********')
    def contacto_no_existe(self, id_contacto):
        print(id_contacto, 'ID NO EXISTE')

    # Citas
    def mostrar_cita(self, cita):
        print('***** Datos de la cita *****')
        print('Contacto: ', cita.id_contacto)
        print('Lugar: ', cita.lugar)
        print('Fecha: ', cita.fecha)
        print('Hora: ', cita.hora)
        print('Asunto: ', cita.asunto)
        print('******************************')

    def mostrar_citas(self, citas):
        print('********* Citas **********')
        for c in citas:
            print(c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('******************************')
    
    def crear_cita(self, cita):
        print(cita.asunto, 'ha nacido')
    def borrar_cita(self, cita):
        print(cita.asunto, 'ha sido asesinado')
    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.asunto, 'ha sido perturbado')
    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'ID YA UTILIZADO')
    def cita_no_existe(self, id_cita):
        print(id_cita, 'ID NO EXISTE')

    def menu(self):
        print('\n\n1. Agregar Contacto')
        print('2. Buscar Contacto')
        print('3. Ver todos los Contactos')
        print('4. Actualizar Contacto')
        print('5. Borrar Contacto')
        print('6. Buscar Contacto')
        print('7. Salir\n\n')



    



    

    

