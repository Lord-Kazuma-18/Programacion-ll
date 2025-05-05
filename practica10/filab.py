class Ministerio:
    def __init__(self, nombre="", direccion="", nroEmpleados=0):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = nroEmpleados
        self.empleados = []  
        self.edades = []     
        self.sueldos = []    

    def agregar_empleado(self, nombres, edad, sueldo):
        if self.nroEmpleados < 100:
            self.empleados.append(nombres)
            self.edades.append(edad)
            self.sueldos.append(sueldo)
            self.nroEmpleados += 1
        else:
            print("No se pueden agregar más empleados (límite alcanzado)")

    def eliminar_empleados_por_edad(self, edad_x):
        indices_a_eliminar = [i for i, edad in enumerate(self.edades) if edad == edad_x]
        for i in reversed(indices_a_eliminar):
            del self.empleados[i]
            del self.edades[i]
            del self.sueldos[i]
            self.nroEmpleados -= 1


    def __add__(self, otro):
        if otro.nroEmpleados == 0:
            print("El otro ministerio no tiene empleados para transferir")
            return self
        
        empleado_transferido = otro.empleados.pop(0)
        edad_transferida = otro.edades.pop(0)
        sueldo_transferido = otro.sueldos.pop(0)
        otro.nroEmpleados -= 1

        self.empleados.append(empleado_transferido)
        self.edades.append(edad_transferida)
        self.sueldos.append(sueldo_transferido)
        self.nroEmpleados += 1

        return self

    def mostrar_empleados_menor_edad(self):
        if self.nroEmpleados == 0:
            print("No hay empleados")
            return
        min_edad = min(self.edades)
        print(f"Empleados con la menor edad ({min_edad}):")
        for i, edad in enumerate(self.edades):
            if edad == min_edad:
                print(f" - {self.empleados[i]}, Edad: {edad}, Sueldo: {self.sueldos[i]}")

    def mostrar_empleados_menor_sueldo(self):
        if self.nroEmpleados == 0:
            print("No hay empleados")
            return
        min_sueldo = min(self.sueldos)
        print(f"Empleados con el menor sueldo ({min_sueldo}):")
        for i, sueldo in enumerate(self.sueldos):
            if sueldo == min_sueldo:
                print(f" - {self.empleados[i]}, Edad: {self.edades[i]}, Sueldo: {sueldo}")

ministerio1 = Ministerio("Rojo", "Estación Central, Estación Cementerio, Estación 16 de Julio")
ministerio1.agregar_empleado(["Pedro", "Lucy", "Ana", "Saul"], 35, 2500)
ministerio1.agregar_empleado(["Rojas", "Sosa", "Perez", "Arce"], 43, 3250)
ministerio1.agregar_empleado(["Luna", "Rios", "Rojas", "Calle"], 26, 2700)
ministerio1.agregar_empleado(["Juan", "Marta", "Luis", "Cesar"], 29, 2500)

ministerio2 = Ministerio()
ministerio2.nombre = "Azul"
ministerio2.direccion = "Av. Siempre Viva 123"
ministerio2.agregar_empleado(["Carlos", "Ana", "Luis", "María"], 30, 2800)
ministerio2.agregar_empleado(["Elena", "Jose", "Raul", "Marta"], 40, 3200)

print("\nAntes de eliminar empleados de edad 43 en Ministerio 1:")
ministerio1.mostrar_empleados_menor_edad()  
ministerio1.eliminar_empleados_por_edad(43)

print("\nDespués de eliminar empleados de edad 43 en Ministerio 1:")
ministerio1.mostrar_empleados_menor_edad()

print("\nTransferencia de un empleado de Ministerio 2 a Ministerio 1:")
ministerio1 + ministerio2

print("\nEmpleados Ministerio 1 luego de transferencia:")
for emp, edad, sueldo in zip(ministerio1.empleados, ministerio1.edades, ministerio1.sueldos):
    print(f"{emp}, Edad: {edad}, Sueldo: {sueldo}")

print("\nEmpleados Ministerio 2 luego de transferencia:")
for emp, edad, sueldo in zip(ministerio2.empleados, ministerio2.edades, ministerio2.sueldos):
    print(f"{emp}, Edad: {edad}, Sueldo: {sueldo}")

print("\nEmpleados con menor edad en Ministerio 1:")
ministerio1.mostrar_empleados_menor_edad()

print("\nEmpleados con menor sueldo en Ministerio 1:")
ministerio1.mostrar_empleados_menor_sueldo()