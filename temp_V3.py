# -*- coding: utf-8 -*-
"""
Q=k*A*DT*dt/dl
Q=(T2-T1)*dt/R
k=205 W/m.K e
Lambda=237 aluminio este es el valor de k a temperatura ambiente
c=910 J/kg.K calor especifico
Q=mc(T2-T1)
"""
# Esta version usa la seleccion del material como una funcion a diferencia de la version 2
# la cual tiene el condicional integrado dentro de la funcion propagacion
# INTEGRANTES DEL EQUIPO
# ANDRES BOLAÑOS
# CARLOS HERNANDO MANRIQUE
# JUAN CAMILO HERNANDEZ GOMEZ
# etc

def materiales(simb):
    if simb == 1:
        k = 237
        c = 900
        rho = 2700
        name = 'ALUMINIO'
    elif simb == 2:
        k = 401
        c = 390
        rho = 19300
        name = "COBRE"
    elif simb == 3:
        k = 429
        c = 234
        rho = 10500
        name = "PLATA"
    elif simb == 4:
        k = 80.2
        c = 448
        rho = 7860
        name = "HIERRO"
    else:
        print("***********************************************************************")
        print("El codigo del material seleccionado no esta en la lista ")
        print("Por favor inicie el proceso nuevamente ")
        print("***********************************************************************")
    return k, c, rho, name

def propagacion ():

    import numpy as np
    import matplotlib.pyplot as plt

    print("========================================================================")
    print("  ESTE PROGRAMA CALCULA LA DISIPACION DE CALOR EN UNA PLACA METALICA ")
    print("=========================================================================")
    # Seccion de toma de datos ingresados por usurio
    tamx = float(input("Ingrese longitud del lado X de la placa en milimetros :"))
    tamy = float(input("Ingrese longitud del lado y de la placa en milimetros :"))
    esp = float(input("Ingrese el espesor en milimetros de la placa :"))
    dl = float(input('Ingrese el tamaño del diferencial de longitud en milimetros :'))
    temp = float(input("Ingrese la temperatura inicial de la placa en grados celcius :"))
    TFuente = float(input("Ingrese la temperatura de la fuente en grados celcius :"))
    tf = float(input("Ingresa el tiempo total de calentamiento de la placa en segundos :"))
    dt = float(input("Ingresa el diferencial de tiempo en segundos :"))
    fx = float(input("Ingrese la posicion de la fuente en direccion x en milimetros :"))
    fy = float(input("Ingrese la posicion de la fuente en direccion y en milimetros :"))
    print("El programa tiene incorporado los valores de cuatro materiales por defecto")
    print("Estos son:")
    print("Aluminio    Codigo 1")
    print("Cobre       Codigo 2")
    print("Plata       Codigo 3")
    print("Hierro      Codigo 4")
    simb = int(input("Ingrese el codigo del material deseado :"))
    print("########################################################################")
    print("                  RESUMEN CARACTERISTICAS DE LA PLACA                   ")
    print("########################################################################")
    print("Dimención de placa: ", tamx, "X", tamy, "X", esp, " mm^3 ")
    print("Diferencial de longitud", dl, "mm", "Diferencial de tiempo", dt, "S")
    print("Temperatura inicial de placa ", temp, "ºC, Temperaura de la fuente", TFuente, "ºC")
    print("Tiempo maximo de calentamiento", tf, "S")
    #HASTA AQUI TOMA DE DATOS
    # Se da valor a las variables nx y ny las cuales definen las dimenciones de las matrices usadas
    nx = int(tamx) // int(dl)
    ny = int(tamy) // int(dl)
    # Las variables tfx y tfy dan el punto en donde se ubica la fuente de calor
    tfx = int(tamx - fx) // int(dl)
    tfy = int(tamy - fy) // int(dl)
    t = 0
    # Se crea la matris de temperaturas iniciales
    TS = np.ones((nx, ny), dtype=np.float) * temp
    A = dl * esp

    k, c, rho, name = materiales(simb)
    print("Las caracteristicas del material", name, "son:")
    print("Conductividad termica      k =", k, " [W/m .C]")
    print("Calor especifico           c =", c, " [J/kg.C]")
    print("Densidad                      ", rho, "[kg/m^3]")
    print("########################################################################")
    wait = input("PRESIONE ENTER PARA CONTINUAR...")
    print("########################################################################")
    m = rho * dl * dl * esp
    print("Matriz de temperaturas iniciales:")
    print(TS)
    TS[tfx, tfy] = TFuente
    TFin = TS.copy()
    print("matriz con temperatura de la fuente:")
    print(TFin)
    plt.close()
    fig, ax = plt.subplots()
    pl1 = ax.imshow(TS, cmap=plt.get_cmap("magma"))
    # inicio del ciclo if else - el cual tiene como propositos separar los materiales
    # propuestos y entregar los valores de las constantes al calculo de los diferenciales
    while t < tf:
        for i in range(nx):
            for j in range(ny):
                ti = TS[i, j]
                Q = []
                if i + 1 <= (nx - 1):
                    Q.append(k * A * (TS[i + 1, j] - ti) * dt / dl)
                if i - 1 >= 0:
                    Q.append(k * A * (TS[i - 1, j] - ti) * dt / dl)
                if j + 1 <= (ny - 1):
                    Q.append(k * A * (TS[i, j + 1] - ti) * dt / dl)
                if j - 1 >= 0:
                    Q.append(k * A * (TS[i, j - 1] - ti) * dt / dl)

                Qt = sum(Q)
                tem = ti + Qt / (m * c)
                if tem <= TFuente:
                    TFin[i, j] = tem
                else:
                    TFin[i, j] = TFuente

        TS = TFin.copy()
        TS[tfx, tfy] = TFuente
        pl1.set_data(TS)
        plt.title(t)
        plt.suptitle('Tiempo de procesamiento virtual')
        plt.pause(0.07)
        t += dt
    print(TFin)
    return ()
propagacion()


