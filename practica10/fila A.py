class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas, empleados):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.empleados = empleados  
        self.nroEmpleados = len(empleados)

    def eliminar_por_apellido(self, apellido):
        self.empleados = [e for e in self.empleados if apellido not in e['apellido']]
        self.nroEmpleados = len(self.empleados)

    def __add__(self, x):
        nuevos_empleados = []
        for e in self.empleados:
            nuevo = e.copy()
            nuevo["sueldo"] += x
            nuevos_empleados.append(nuevo)
        return LineaTeleferico(self.color, self.tramo, self.nroCabinas, nuevos_empleados)

    def __rshift__(self, other):
        nombre = input("Ingrese el nombre del empleado a transferir: ")
        for e in self.empleados:
            if e['nombre'].lower() == nombre.lower():
                other.empleados.append(e)
                self.empleados.remove(e)
                break
        self.nroEmpleados = len(self.empleados)
        other.nroEmpleados = len(other.empleados)
        return self, other

    def mostrar_mayor_edad(self):
        mayor = max(self.empleados, key=lambda e: e['edad'])
        print(f"Mayor edad: {mayor['nombre']} {mayor['apellido']} - {mayor['edad']} años")

    def mostrar_mayor_sueldo(self):
        mayor = max(self.empleados, key=lambda e: e['sueldo'])
        print(f"Mayor sueldo: {mayor['nombre']} {mayor['apellido']} - Bs {mayor['sueldo']}")

empleados1 = [
    {"nombre": "Pedro", "apellido": "Rojas", "edad": 35, "sueldo": 2500},
    {"nombre": "Lucy", "apellido": "Sosa", "edad": 43, "sueldo": 3250},
    {"nombre": "Ana", "apellido": "Perez", "edad": 26, "sueldo": 2700},
    {"nombre": "Saul", "apellido": "Arce", "edad": 29, "sueldo": 2500}
]

empleados2 = [
    {"nombre": "Laura", "apellido": "Castro", "edad": 40, "sueldo": 3000},
    {"nombre": "Mario", "apellido": "Torrez", "edad": 30, "sueldo": 2800}
]

lt1 = LineaTeleferico("Rojo", "Estación Central, Cementerio", 20, empleados1)
lt2 = LineaTeleferico("Azul", "Estación Busch, Terminal", 15, empleados2)

lt1.eliminar_por_apellido("Rojas")

lt1, lt2 = lt1 >> lt2  

lt1 = lt1 + 200

lt1.mostrar_mayor_edad()
lt1.mostrar_mayor_sueldo()
