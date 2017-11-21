# -*- coding: utf-8 -*-
"""
Q=k*A*DT*dt/dl
Q=(T2-T1)*dt/R
k=205 W/m.K e
Lambda=237 aluminio este es el valor de k a temperatura ambiente
c=910 J/kg.K calor especifico
Q=mc(T2-T1)
"""

#  carga los modulos numpy y pyplot de matplotlib renombrados como  np y plt respectivamente
import numpy as np
import matplotlib.pyplot as plt

print("========================================================================")
print("  ESTE PROGRAMA CALCULA LA DISIPACION DE CALOR EN UNA PLACA METALICA ")
print("=========================================================================")
# Seccion de toma de datos
tamx = float(input("Ingrese longitud del lado X de la placa en milimetros :"))
tamy = float(input("Ingrese longitud del lado y de la placa en milimetros :"))
esp = float(input("Ingrese el espesor en milimetros de la placa :"))
dl = float(input('Ingrese el tamaño del deferencial de longitud en milimetros :'))
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
print("Diferencial de longitud", dl, "mm", "Diferencial de tiempo", dt,"S")
print("Temperatura inicial de placa ", temp, "ºC, Temperaura de la fuente", TFuente, "ºC")
print("Tiempo maximo de calentamiento", tf, "S")

nx = int(tamx) // int(dl)
ny = int(tamy) // int(dl)
tfx = int(tamx - fx) // int(dl)
tfy = int(tamy - fy) // int(dl)
t = 0
TS = np.ones((nx, ny), dtype=np.float) * temp
tamx *= 0.001
tamy *= 0.001
esp *= 0.001
dl *= 0.001
fx *= 0.001
fy *= 0.001
A = dl * esp
rho = 0
c = 0
k = 0
if simb == 1:
    k = 237
    c = 900
    rho = 2700
    name = 'ALUMINIO'
    print("Las caracteristicas del material", name, "son:")
    print("Conductividad termica         k =", k, " [W/m .C]")
    print("Calor especifico              c =", c, " [J/kg.C]")
    print("Densidad                         ", rho, "[kg/m^3]")
    print("########################################################################")
    wait = input("PRESIONE ENTER PARA CONTINUAR...")
    print("########################################################################")
    m = rho * dl * dl * esp
    print("Matriz de temperaturas iniciales:")
    print(TS)
    print(simb)
    print(k)
    TS[tfx, tfy] = TFuente
    TFin = TS.copy()
    print("matriz con temperatura de la fuente:")
    print(TFin)
    plt.close()
    fig, ax = plt.subplots()
    pl1 = ax.imshow(TS, cmap=plt.get_cmap("magma"))

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
        plt.pause(0.05)
        t += dt
elif simb == 2:
    k = 401
    c = 390
    rho = 19300
    name = "COBRE"
    print("Las caracteristicas del material", name, "son:")
    print("Conductividad termica       k =", k, " [W/m .C]")
    print("Calor especifico            c =", c, " [J/kg.C]")
    print("Densidad                      ", rho, "[kg/m^3]")
    print("########################################################################")
    wait = input("PRESIONE ENTER PARA CONTINUAR...")
    print("########################################################################")
    m = rho * dl * dl * esp
    print("Matriz de temperaturas iniciales:")
    print(TS)
    print(simb)
    print(k)
    TS[tfx, tfy] = TFuente
    TFin = TS.copy()
    print("matriz con temperatura de la fuente:")
    print(TFin)
    plt.close()
    fig, ax = plt.subplots()
    pl1 = ax.imshow(TS, cmap=plt.get_cmap("magma"))

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
        plt.pause(0.05)
        t += dt
elif simb == 3:
    k = 429
    c = 234
    rho = 10500
    name = "PLATA"
    print("Las caracteristicas del material", name, "son:")
    print("Conductividad termica        k =", k, " [W/m .C]")
    print("Calor especifico             c =", c, " [J/kg.C]")
    print("Densidad                       ", rho, "[kg/m^3]")
    print("########################################################################")
    wait = input("PRESIONE ENTER PARA CONTINUAR...")
    print("########################################################################")
    m = rho * dl * dl * esp
    print("Matriz de temperaturas iniciales:")
    print(TS)
    print(simb)
    print(k)
    TS[tfx, tfy] = TFuente
    TFin = TS.copy()
    print("matriz con temperatura de la fuente:")
    print(TFin)
    plt.close()
    fig, ax = plt.subplots()
    pl1 = ax.imshow(TS, cmap=plt.get_cmap("magma"))

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
        plt.pause(0.05)
        t += dt
elif simb == 4:
    k = 80.2
    c = 448
    rho = 7860
    name = "HIERRO"
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
    print(simb)
    print(k)
    TS[tfx, tfy] = TFuente
    TFin = TS.copy()
    print("matriz con temperatura de la fuente:")
    print(TFin)
    plt.close()
    fig, ax = plt.subplots()
    pl1 = ax.imshow(TS, cmap=plt.get_cmap("magma"))

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
        plt.pause(0.05)
        t += dt
else:
    print("***********************************************************************")
    print("El codigo del material seleccionado no esta en la lista ")
    print("Por favor inicie el proceso nuevamente ")
    print("***********************************************************************")



