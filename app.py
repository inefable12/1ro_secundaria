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
    st.title("Practicando la división")

    # Si no hay un ejercicio en el estado de sesión, lo generamos
    if "ejercicio" not in st.session_state or st.session_state.nuevo_ejercicio:
        st.session_state.ejercicio = generar_ejercicio()
        st.session_state.a_calcular = random.choice(["Dividendo", "Divisor", "Cociente", "Residuo"])
        st.session_state.nuevo_ejercicio = False  # Reiniciamos el indicador de nuevo ejercicio

    dividendo, divisor, cociente, residuo = st.session_state.ejercicio

    opciones = {
        "Dividendo": dividendo,
        "Divisor": divisor,
        "Cociente": cociente,
        "Residuo": residuo
    }

    a_calcular = st.session_state.a_calcular

    st.write(f"Dado el siguiente ejercicio:")

    # Mostramos los valores disponibles, excepto el que se debe calcular
    for key, value in opciones.items():
        if key != a_calcular:
            st.write(f"{key}: {value}")

    # Solicitamos la respuesta del valor que falta
    respuesta = st.number_input(f"¿Cuál es el {a_calcular}?", min_value=0, step=1)

    # Verificación de la respuesta
    if st.button("Verificar respuesta"):
        if respuesta == opciones[a_calcular]:
            st.success(f"¡Correcto! El {a_calcular} es {respuesta}. 🎉")
            st.balloons()  # Animación de fuegos artificiales
        else:
            st.error(f"Incorrecto. El {a_calcular} correcto es {opciones[a_calcular]}.")

    # Botón para generar un nuevo ejercicio
    if st.button("Generar nuevo ejercicio"):
        st.session_state.nuevo_ejercicio = True  # Indicamos que se debe generar un nuevo ejercicio
        st.experimental_rerun()  # Actualizamos la página

if __name__ == "__main__":
    mostrar_ejercicio()
