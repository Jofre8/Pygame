import pygame
import os
import rulet
import time
import bateria_engine  # <--- Importamos el archivo de la batería
import tempios

pygame.init()

# --- CONEXIÓN CON EL CÓDIGO DE BATERÍA ---
# Esta variable 'activa' es la que pediste para la lógica de consumo
activa = 0 

# Diccionario para compartir datos con el hilo de segundo plano
datos_compartidos = {"estado": "principal", "activa": activa}

# Iniciamos el motor de la batería pasando el diccionario
bateria_engine.iniciar_hilo_bateria(datos_compartidos)
# -----------------------------------------

pantalla = pygame.display.set_mode((1920, 1800))
pygame.display.set_caption("Regla: Solo cambiar desde principal")

# Cargar imágenes
ruta = "py"
img_principal = pygame.image.load(os.path.join(ruta, "../fotos/PantallaD.jpg"))
PuertaAbiertaBien = pygame.image.load(os.path.join(ruta, "../fotos/PuertaAbiertaD.jpg"))
PuertaAbiertaMal = pygame.image.load(os.path.join(ruta, "../fotos/PuertaAbiertaBichoD.jpg"))
PuertaCerradaBien = pygame.image.load(os.path.join(ruta, "../fotos/PuertaCerradaD.jpg"))
PuertaCerradaMal = pygame.image.load(os.path.join(ruta, "../fotos/PuertaCerradaD.jpg"))
Ventana12 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana12.png"))
Ventana1 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana1.png"))
Ventana2 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana2.png"))
Ventana3 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana3.png"))
Ventana4 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana4.png"))
Ventana5 = pygame.image.load(os.path.join(ruta, "../fotos/Ventana5.png"))


Victoria = pygame.image.load(os.path.join(ruta, "../fotos/Victoria.png"))
Derrota = pygame.image.load(os.path.join(ruta, "../fotos/Derrota.png"))

PasilloPuertaPrincipal = pygame.image.load(os.path.join(ruta, "../fotos/CamaraPasilloPuertaD.jpg"))
PasilloPuertaPrincipalBicho = pygame.image.load(os.path.join(ruta, "../fotos/CamaraPasilloPuertaBichoD.jpg"))
Comedor = pygame.image.load(os.path.join(ruta, "../fotos/ComedorD.jpg"))
ComedorBicho = pygame.image.load(os.path.join(ruta, "../fotos/ComedorBichoD.jpg"))
Cocina = pygame.image.load(os.path.join(ruta, "../fotos/CocinaD.jpg"))
CocinaBicho = pygame.image.load(os.path.join(ruta, "../fotos/CocinaBichoD.jpg"))
Pasillo4 = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo4D.jpg"))
Pasillo4Bicho = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo4BichoD.jpg"))
Pasillo5 = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5D.jpg"))
Pasillo5Bicho = pygame.image.load(os.path.join(ruta, "../fotos/Pasillo5BichoD.jpg"))

# Estado actual
estado = "principal"
conhora = 0
abierta = 1
puer = 0
perdido = 0

def obtener_imagen(estado):
    if estado == "principal":
        return img_principal
    if estado == "victoria":
        return Victoria
    if estado == "derrota":
        return Derrota
    elif estado == "1":
        return PuertaAbiertaBien
    elif estado == "12":
        return PuertaAbiertaMal
    elif estado == "13":
        return PuertaCerradaBien
    elif estado == "14":
        return PuertaCerradaMal
    elif estado == "3":             #12
        return Ventana12
    elif estado == "31":             #1
        return Ventana1        
    elif estado == "32":             #2
        return Ventana2
    elif estado == "33":             #3
        return Ventana3
    elif estado == "34":             #4
        return Ventana4
    elif estado == "35":             #5
        return Ventana5
    elif estado == "4":
        return PasilloPuertaPrincipal
    elif estado == "5":
        return Cocina
    elif estado == "6":
        return Comedor
    elif estado == "7":
        return Pasillo4
    elif estado == "8":
        return Pasillo5
    elif estado == "41":
        return PasilloPuertaPrincipalBicho
    elif estado == "51":
        return CocinaBicho
    elif estado == "61":
        return ComedorBicho
    elif estado == "71":
        return Pasillo4Bicho    
    elif estado == "81":
        return Pasillo5Bicho    

tempios.iniciar_conteo()
    
corriendo = True
while corriendo:
    # Actualizamos los datos para que el hilo de la batería los lea
    datos_compartidos["estado"] = estado
    datos_compartidos["abierta"] = abierta
    
    # Consultamos el valor actual de la batería
    valor_bat = bateria_engine.obtener_bateria()
    valor_tiempo = tempios.obtener_tiempo()
    if valor_tiempo == 0:
        estado = "victoria"

    if valor_tiempo != 0:
        if perdido == 1:
                estado = "derrota"
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if estado == "principal":
                    if rulet.numero_actual == 1:
                        if evento.key == pygame.K_w:
                            estado = "41"
                    if rulet.numero_actual != 1:
                        if evento.key == pygame.K_w:
                            estado = "4"
                    if evento.key == pygame.K_d:
                        if conhora == 1:
                            if tempios.tiempo_restante <= 200 and tempios.tiempo_restante >= 167:
                                estado = "3"        #12
                            elif tempios.tiempo_restante <= 166 and tempios.tiempo_restante >= 134:
                                estado = "31"       #1
                            elif tempios.tiempo_restante <= 133 and tempios.tiempo_restante >= 101:
                                estado = "32"       #2
                            elif tempios.tiempo_restante <= 100 and tempios.tiempo_restante >= 67:
                                estado = "33"       #3
                            elif tempios.tiempo_restante <= 66 and tempios.tiempo_restante >= 34:
                                estado = "34"       #4
                            elif tempios.tiempo_restante <= 33 and tempios.tiempo_restante >= 0:
                                estado = "33"       #5
                    if evento.key == pygame.K_a:
                        puer = 1
                        if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                            if valor_bat != 0:
                                if abierta == 1:
                                    estado = "1"
                                else:
                                    estado = "13"
                            else:
                                estado = "1"
                            if valor_bat != 0:
                                if abierta == 0:
                                    estado = "13"
                                else:
                                    estado = "1"
                            else:
                                estado = "1"
                        if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                            if valor_bat != 0:
                                if abierta == 1:
                                    estado = "12"
                                else:
                                    estado = "14"
                            else:
                                estado = "12"
                            if valor_bat != 0:
                                if abierta == 0:
                                    estado = "14"
                                else:
                                    estado = "12"
                            else:
                                estado = "12"

                elif puer == 1:
                    if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                        enemigo = 1
                        if enemigo == 1:
                            if abierta == 1:
                                estado = "1"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                
                                # PARTE FALTANTE CON LA BATERIA
                                if evento.key == pygame.K_SPACE and valor_bat != 0: 
                                    enemigo = 1
                                    estado = "13"
                                    abierta = 0
                                
                                elif evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1

                            elif abierta == 0:
                                estado = "13"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1
                            elif estado == "13":
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 1
                                    estado = "1"
                                    abierta = 1

                    elif rulet.numero_actual == 5 or rulet.numero_actual == 6:
                        enemigo = 2
                        if enemigo == 2:
                            if abierta == 1:
                                estado = "12"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                
                                # PARTE FALTANTE CON LA BATERIA
                                if evento.key == pygame.K_SPACE and valor_bat != 0: 
                                    enemigo = 2
                                    estado = "14"
                                    abierta = 0


                            elif abierta == 0:
                                if valor_bat > 0:
                                    estado = "14"
                                else:
                                    estado = "12"
                                if evento.key == pygame.K_s:
                                    estado = "principal"
                                    puer = 0
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 2
                                    estado = "12"
                                    abierta = 1
                            elif estado == "14":
                                if evento.key == pygame.K_SPACE:
                                    enemigo = 2
                                    estado = "12"

                else:
                    if evento.key == pygame.K_s:
                        estado = "principal"
                        puer = 0
                    else:
                        if evento.type == pygame.KEYDOWN:
                # ----------- Cambios permitidos de la camara 8 ------------
                            if estado == "8":
                                if evento.key == pygame.K_5:
                                    if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                        estado = "81"
                                    elif rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                        estado = "8"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                # ----------- Cambios permitidos de la camara 8 ------------
                            if estado == "81":
                                if evento.key == pygame.K_5:
                                    if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                        estado = "81"
                                    elif rulet.numero_actual != 5  or rulet.numero_actual != 6:
                                        estado = "8"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"

                # ----------- Cambios permitidos de la camara 4 ------------
                            if estado == "4":
                                if evento.key == pygame.K_1:
                                    if rulet.numero_actual == 1:
                                        estado = "41"
                                    elif rulet.numero_actual != 1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"
                # ----------- Cambios permitidos de la camara 4 ------------
                            if estado == "41":
                                if evento.key == pygame.K_1:
                                    if rulet.numero_actual == 1:
                                        estado = "41"
                                    elif rulet.numero_actual != 1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"

                # ----------- Cambios permitidos de la camara 5 ------------
                            if estado == "5":
                                if evento.key == pygame.K_2:
                                    if rulet.numero_actual == 2:
                                        estado = "51"
                                    elif rulet.numero_actual != 2:
                                        estado = "5"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"
                # ----------- Cambios permitidos de la camara 5 ------------
                            if estado == "51":
                                if evento.key == pygame.K_2:
                                    if rulet.numero_actual == 2:
                                        estado = "51"
                                    elif rulet.numero_actual != 2:
                                        estado = "5"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"

                # ----------- Cambios permitidos de la camara 6 ------------
                            if estado == "6":
                                if evento.key == pygame.K_3:
                                    if rulet.numero_actual == 3:
                                        estado = "61"
                                    elif rulet.numero_actual != 3:
                                        estado = "6"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"
                # ----------- Cambios permitidos de la camara 6 ------------
                            if estado == "61":
                                if evento.key == pygame.K_3:
                                    if rulet.numero_actual == 3:
                                        estado = "61"
                                    elif rulet.numero_actual != 3:
                                        estado = "6"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 4:
                                    if evento.key == pygame.K_4:
                                        estado = "71"
                                if rulet.numero_actual != 4:
                                    if evento.key == pygame.K_4:
                                        estado = "7"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"

                # ----------- Cambios permitidos de la camara 7 ------------
                            if estado == "7":
                                if evento.key == pygame.K_4:
                                    if rulet.numero_actual == 4:
                                        estado = "71"
                                    elif rulet.numero_actual != 4:
                                        estado = "7"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"
                # ----------- Cambios permitidos de la camara 7 ------------
                            if estado == "71":
                                if evento.key == pygame.K_4:
                                    if rulet.numero_actual == 4:
                                        estado = "71"
                                    elif rulet.numero_actual != 4:
                                        estado = "7"
                                if rulet.numero_actual == 1:
                                    if evento.key == pygame.K_1:
                                        estado = "41"
                                if rulet.numero_actual != 1:
                                    if evento.key == pygame.K_1:
                                        estado = "4"
                                if rulet.numero_actual == 2:
                                    if evento.key == pygame.K_2:
                                        estado = "51"
                                if rulet.numero_actual != 2:
                                    if evento.key == pygame.K_2:
                                        estado = "5"
                                if rulet.numero_actual == 3:
                                    if evento.key == pygame.K_3:
                                        estado = "61"
                                if rulet.numero_actual != 3:
                                    if evento.key == pygame.K_3:
                                        estado = "6"
                                if rulet.numero_actual == 5 or rulet.numero_actual == 6:
                                    if evento.key == pygame.K_5:
                                        estado = "81"
                                if rulet.numero_actual != 5 or rulet.numero_actual != 6:
                                    if evento.key == pygame.K_5:
                                        estado = "8"

                # ----------- Perdido ------------
        if rulet.numero_actual == 6:
            if valor_bat != 0:
                if abierta == 1:
                    perdido = 1

            else:
                if abierta == 1:
                    perdido = 1

                else:
                    perdido = 1

    
    pantalla.blit(obtener_imagen(estado), (0, 360))
    pygame.display.update()
    if estado == "victoria" or estado == "derrota":
        time.sleep(5)
        pygame.quit()

pygame.quit()