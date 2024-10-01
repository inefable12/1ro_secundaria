import streamlit as st
import random

# Función para generar un ejercicio aleatorio
def generar_ejercicio():
    divisor = random.randint(2, 10)
    cociente = random.randint(1, 10)
    residuo = random.randint(0, divisor - 1)
    dividendo = divisor * cociente + residuo
    return dividendo, divisor, cociente, residuo

# Mostrar el ejercicio y pedir que se calcule uno de los valores
def mostrar_ejercicio():
    st.title("Práctica de Dividendo, Divisor, Cociente y Residuo")

    # Generamos un ejercicio
    dividendo, divisor, cociente, residuo = generar_ejercicio()

    opciones = {
        "Dividendo": dividendo,
        "Divisor": divisor,
        "Cociente": cociente,
        "Residuo": residuo
    }

    # Seleccionamos aleatoriamente cuál de los valores pedir al usuario
    a_calcular = random.choice(list(opciones.keys()))

    st.write(f"Dado el siguiente ejercicio:")
    
    # Mostramos los otros valores
    for key, value in opciones.items():
        if key != a_calcular:
            st.write(f"{key}: {value}")
    
    # Solicitamos la respuesta del valor que falta
    respuesta = st.number_input(f"¿Cuál es el {a_calcular}?", min_value=0)

    # Verificación de la respuesta
    if st.button("Verificar respuesta"):
        if respuesta == opciones[a_calcular]:
            st.success(f"¡Correcto! El {a_calcular} es {respuesta}.")
        else:
            st.error(f"Incorrecto. El {a_calcular} correcto es {opciones[a_calcular]}.")

if __name__ == "__main__":
    mostrar_ejercicio()
