def Menu(Lista):
    print("a-Actualizar el valor del vehiculo")
    print("b-Mostrar código de un plan, modelo y versión del vehículo")
    print("c-Mostrar el monto que se debe haber pagado para licitar el vehículo")
    print("d-Modificar cantidad de cuotas pagas para licitar")
    op=input("Elija una opción: ")
    if(op=="a"):
        Vehiculo=int(input("Ingrese el código del plan: "))
        for i in range(len(Lista)):
            if Vehiculo==Lista[i].getCodPlan():
                print("El codigo del plan de ese vehículo es: {}".format(Lista[i].getCodPlan()))
                print("El modelo es: {}".format(Lista[i].getModelo()))
                print("La versión del vehículo es: {} ".format(Lista[i].getVersion()))
                valor=input("Ingrese el nuevo valor del vehículo: ")
                print("Nuevo valor cambiado correctamente!---->{}".format(Lista[i].nuevoValor(valor)))
    elif(op=="b"):
        i=0
        valor=int(input("Ingrese valor del vehículo: "))
        cuota=int(input("Ingrese una cuota: "))
        while i<len(Lista):
              if (valor==Lista[i].getvalor() and cuota>12):
                    print("El codigo del plan de ese vehículo es: {}".format(Lista[i].getCodPlan()))
                    print("El modelo es: {}".format(Lista[i].getModelo()))
                    print("La versión del vehículo es: {} ".format(Lista[i].getVersion()))
              i+=1
    elif(op=="c"):
         cod=int(input("Ingrese el código del plan: "))
         for i in range(len(Lista)):
             if cod==Lista[i].getCodPlan():
                 cuenta=(Lista[i].getvalor()/Lista[i].getCuotasPlan())+Lista[i].getvalor()*0.10
                 print("El monto que se debe pagar para licitar el vehiculo es de: ${0:.2f} ".format(Lista[i].getCuotasLicitar()*cuenta))
                 
    elif(op=="d"):
         cod=int(input("Ingrese el código del plan: "))
         for i in range(len(Lista)):
             if cod==Lista[i].getCodPlan():
                 cuota=int(input("Ingrese nuevo valor de la cuota para licitar: "))
                 print("Nuevo valor de la cuota actualizado correctamente!--->{}". format(Lista[i].NuevaCuotaLicitar(cuota)))