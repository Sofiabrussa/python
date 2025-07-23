#Multihilo
import threading
import time


# Esta es la función que cada hilo va a ejecutar
def tarea(nombre, duracion):
    print(f" {nombre} empezó (tarda {duracion} segundos)")
    time.sleep(duracion)
    print(f" {nombre} terminó")

# Crear tres hilos con distintas duraciones
hilo1 = threading.Thread(target=tarea, args=("Tarea 1", 5))
hilo2 = threading.Thread(target=tarea, args=("Tarea 2", 3))
hilo3 = threading.Thread(target=tarea, args=("Tarea 3", 1))

# Iniciar los hilos en paralelo
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que terminen todos
hilo1.join()
hilo2.join()
hilo3.join()

print("Todas las tareas finalizaron")

#----------------------------------------------------------------------------------------------------------------
#Multiprocessing 
import multiprocessing
import time

def tarea(nombre, duracion):
    print(f"🔹 {nombre} empezó (tarda {duracion} segundos)")
    time.sleep(duracion)
    print(f"✅ {nombre} terminó")

if __name__ == '__main__':
    # Crear tres procesos
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea 1", 5))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea 2", 3))
    proceso3 = multiprocessing.Process(target=tarea, args=("Tarea 3", 1))

    # Iniciar los procesos (se ejecutan en paralelo)
    proceso1.start()
    proceso2.start()
    proceso3.start()

    # Esperar a que todos terminen
    proceso1.join()
    proceso2.join()
    proceso3.join()

    

