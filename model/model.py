from .contacto import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c        
        return False, 0
    
    def esta_id_cita(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0

    #Contacto Methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c
    
    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def actualizar_contacto(self, id_contacto, n_nombre ='0', n_tel ='0', n_correo='0' , n_dir='0' ):
        e, c = self.esta_id(id_contacto)
        if e:
            if n_nombre != '0':
                c.nombre = n_nombre
            if n_tel != '0':
                c.tel = n_tel
            if n_correo != '0':
                c.correo = n_correo
            if n_dir != '0':
                c.dir = n_dir
            return True
        return False
    
    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)
        

        if e:
            # for i in self.citas:
            #     if i.id_contacto == id_contacto:
            #         citas.append(i)
            citas = [c for c in self.citas if c.id_contacto == id_contacto ]
            
            for i in citas:
                self.citas.remove(i)

            # ids_temp = [c.id_contacto for c in self.citas]
            # for i in range(len(ids_temp)):
            #     if ids_temp[i] == id_contacto:
            #         self.citas.pop(i)
            self.contactos.remove(contacto)
            return True, contacto
        return False, 0


    #Cita Methods

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if self.esta_id(id_contacto)[0]:
            if not self.esta_id_cita(id_cita)[0]:
                c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(c)
                return True
        return False

    def leer_cita(self, id_cita):
        e, c = self.esta_id(id_cita)
        if e:
            return c
        return False


    
    def actualizar_cita(self, id_cita, n_id_contacto = None, n_lugar = None, n_fecha = None, n_hora = None, n_asunto = None):
        if self.esta_id(n_id_contacto)[0]:
            e, c = self.esta_id(id_cita)
            if  e:
                if n_id_contacto != None:
                    c.id_contacto = n_id_contacto
                if n_lugar != None:
                    c.lugar = n_lugar
                if n_hora != None:
                    c.hora = n_hora
                if n_asunto != None:
                    c.asunto = n_asunto
                return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        if e:
            self.citas.remove(c)
            return True, c
        return False, c
    

    def buscar_contactos(self, letra):

        # contactos = []
        # for c in self.contactos:
        #     if c.nombre.lower().startwith(letra.lower()):
        #         contactos.append(c.id_contacto)
        
        # return contactos
        return [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
    
    def buscar_citas_fecha(self, fecha):
        # citas = []
        # for c in self.citas:
        #     if c.fecha == fecha:
        #         citas.append(c.id_cita)
        
        return [c for c in self.citas if c.fecha.lower() == fecha.lower()] 


    def mostrar_citas(self):
        return self.citas

    def mostrar_contactos(self):
        return self.contactos

