import time
import threading

# Valor inicial
tiempo_restante = 200

def iniciar_conteo():
    def loop_tiempo():
        global tiempo_restante
        while tiempo_restante > 0:
            time.sleep(1) # Espera un segundo
            tiempo_restante -= 1
            # print(f"Tiempo: {tiempo_restante}") # Opcional para ver en consola

    hilo = threading.Thread(target=loop_tiempo, daemon=True)
    hilo.start()

def obtener_tiempo():
    global tiempo_restante
    return tiempo_restante