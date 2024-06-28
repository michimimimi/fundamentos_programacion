#lista de trabajadores
trabajadores = []

#cargos
CARGOS = ["ceo", "desarrollador", "analista de datos"]

#definir funciones
def registrar_trabajador(trabajadores):
    nombre = input("Ingrese nonbre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de Datos): ").lower()
    while cargo not in CARGOS:
        print ("Cargo no existe, intente nuevamente")
        cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de Datos): ").lower()
    sueldo_bruto = int(input("Ingrese sueldo bruto del trabajador: "))
    
    #calcular los descuentos
    descuento_salud = sueldo_bruto * 0.07
    descuento_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - descuento_salud - descuento_afp
    
    #agregar trabajadores
    trabajadores.append({
        "Nombre" : nombre,
        "Cargo" : cargo,
        "SueldoBruto" : sueldo_bruto,
        "DescuentoSalud" : descuento_salud,
        "DescuentoAFP" : descuento_afp,
        "LiquidoPagar" : liquido_pagar    
    })
        
    
    
def listar_trabajadores(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
        
#imprimir como txt    
def imprimir_plantilla(trabajadores):
    print()
    cargo_seleccionado = input("Ingrese cargo para impimir planilla o presione ENTER para selecionar todos: ").lower()
    if cargo_seleccionado == "":
        trabajadores_a_imprimir = trabajadores
        nombre_archivo = "planilla_todos.txt"
    elif cargo_seleccionado in CARGOS:
        trabajadores_a_imprimir = []
        for trabajador in trabajadores:
            if trabajador["Cargo"] == cargo_seleccionado:
                trabajadores_a_imprimir.append(trabajador)
        nombre_archivo = f"planilla_{cargo_seleccionado}.txt"
    else:
        print("Cargo no valido")
        return
    
    with open (nombre_archivo, "w") as archivo:
        for trabajador in trabajadores_a_imprimir:
        
            archivo.write(f"Nombre y apellido:  {trabajador["Nombre"]}\n")
            archivo.write(f"Cargo:  {trabajador["Cargo"]}\n")
            archivo.write(f"Sueldo bruto:  {trabajador["SueldoBruto"]}\n")
            archivo.write(f"Descuento de salud:  {trabajador["DescuentoSalud"]}\n")
            archivo.write(f"Descuento AFP:  {trabajador["DescuentoAFP"]}\n")
            archivo.write(f"Liquido a pagar:  {trabajador["LiquidoPagar"]}\n")
                            

#el menu
while True:
    print("Bienvenidos al super sistema de Pago de Sueldos")
    print("1. Registrar trabajador")
    print("2. Listar los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir")
    
    opcion=int(input("Ingrese su opcion: "))
    
    if opcion == 1:
        registrar_trabajador(trabajadores)
    elif opcion == 2:
        listar_trabajadores(trabajadores)
    elif opcion == 3:
        imprimir_plantilla(trabajadores)
    elif opcion == 4:
        break
    else:
        print ("Opcion no valida, seleccione nuevamente")
    