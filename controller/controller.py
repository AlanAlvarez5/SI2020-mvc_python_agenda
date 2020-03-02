from model.model import  Model
from view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if e:
            self.view.crear_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
    
    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def leer_todos_contactos(self):
        c = self.model.mostrar_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = None, n_tel = None, n_correo = None, n_dir = None):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.modificar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def borrar_contacto(self, id_contacto):
        e,c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def leer_contactos_letra(self, letra):
        c = self.model.buscar_contactos(letra)
        self.view.mostrar_contactos(c)


    #Cita conttrollers



    # def insertar_contactos(self):
    #     self.agregar_contacto(1 , 'Juan Perez', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')
    #     self.agregar_contacto(2 , 'Juanito', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')
    #     self.agregar_contacto(3 , 'Pedro', 46464641251, 'alan_s098@hotmail.es','Calle chida 1212 colonia perrona')

    def insertar_citas(self):
        # self.agregar_cita(1, 1,'aqui','mañana','12','nada')
        # self.agregar_cita(2, 1,'aqui','mañana','12','nada de nada')
        pass

    # def start(self):
    #     print("Start -----")
    #     self.insertar_contactos()
    #     self.insertar_citas()
    #     self.leer_todos_contactos()
    #     self.leer_contactos_letra('j')

    def start(self):
        while True:
            self.view.menu()
            o = int(input('> Selecciona una opcion: '))
            
            if o == 1:
                id_contacto = int(input('> Ingrese un ID de contacto: '))
                nombre = input('> Ingrese un nombre de contacto: ')
                tel = input('> Ingrese el telefono de ' + nombre + ': ')
                correo = input('> Ingrese el correo de ' + nombre + ': ')
                dir = input('> Ingrese la dirección de ' + nombre + ': ')
                self.agregar_contacto(id_contacto, nombre, tel, correo, dir)
            elif o ==2:
                id_contacto = int(input('> Ingrese un ID de contacto: '))
                self.leer_contacto(id_contacto)
            elif o ==3:
                self.leer_todos_contactos()
            elif o ==4:
                self.leer_todos_contactos()
                id_contacto = int(input('> Ingresa el ID del contacto a actualizar: ' ))
                print('----- Ingresa los datos a actualizar -----')
                print('----- Si no deseas actualizar un dato ingresa un 0 -----')
                nombre = input('> Ingrese un nombre de contacto: ')
                tel = input('> Ingrese el telefono de ' + nombre + ': ')
                correo = input('> Ingrese el correo de ' + nombre + ': ')
                dir = input('> Ingrese la dirección de ' + nombre + ': ')
                self.actualizar_contacto(id_contacto, nombre, tel, correo, dir)
            elif o ==5:
                self.leer_todos_contactos()
                id_contacto = input('> Ingresa el ID del contacto a borrar: ')
                q = input('> Estas seguro de eliminar el ID' + id_contacto+'?\n 1 SI\n 2 NO\n > ')
                if q == '2':
                    continue
                else:
                    self.borrar_contacto(int(id_contacto))

            elif o ==6:
                letra = input('> Ingresa la letra con la que empieza el nombre del contacto que buscas: ')
                self.leer_contactos_letra(letra)
            elif o == 7:
                print('*******Vuelva pronto*******')
                break 
    
