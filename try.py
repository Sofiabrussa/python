#TRY
#El código dentro del bloque try es donde intentas hacer algo que podría fallar. 
#Si ocurre un error dentro del try, Python busca un bloque except que maneje ese error.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

#Si no sabes qué error puede ocurrir o quieres capturarlos todos
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except Exception as e: 
    print(f"Ocurrió un error: {e}")
    
#Capturar varios tipos de error
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Debe ingresar un número válido.")


#ELSE Y FINALLY 
#else: se ejecuta si no hubo errores en el try
#Finally: se ejecuta siempre, haya o no error
try:
    x = int(input("Ingrese un número: "))
    resultado = 10 / x
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Debe ingresar un número válido.")
else:
    print(f"El resultado es {resultado}")
finally:
    print("Esto siempre se ejecuta.")

#--------------------------------------------------------------------------------------------------------------
#Python no tiene promesas, pero tiene async/await para manejar tareas asíncronas.
#El manejo de errores con try/except funciona en código sincrónico y en asíncrono.
#async se usa para definir una función asíncrona.
#await se usa para "pausar" la ejecución dentro de esa función hasta que la tarea asíncrona termine, pero sin bloquear todo el programa.
import asyncio

async def descargar_archivo(nombre, tiempo_descarga):
    print(f"Empezando descarga de {nombre}...")
    await asyncio.sleep(tiempo_descarga)  # simula el tiempo que tarda la descarga
    print(f"Descarga de {nombre} finalizada.")
    return f"{nombre} descargado"

async def main():
    # Crear tareas para descargar 3 archivos con diferentes tiempos
    tarea1 = descargar_archivo("archivo1.txt", 3)
    tarea2 = descargar_archivo("archivo2.txt", 2)
    tarea3 = descargar_archivo("archivo3.txt", 1)

    # Ejecutar las 3 tareas al mismo tiempo y esperar que terminen
    resultados = await asyncio.gather(tarea1, tarea2, tarea3)

    print("Todas las descargas terminaron.")
    print("Resultados:", resultados)

asyncio.run(main())

#Si dentro de una función necesitas usar await, la función debe ser async.
#Y si esa función es llamada desde otra función donde quieres esperar su resultado con await, esa otra función también debe ser async