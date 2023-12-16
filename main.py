import streamlit as st
import time

# Inicialización de variables
timer_states = {"azul": 0, "rojo": 0, "verde": 0, "amarillo": 0}
timer_buttons = {"azul": True, "rojo": True, "verde": True, "amarillo": True}
game_duration = 1800  # 30 minutos
warning_time = 1500  # 25 minutos (5 minutos antes de finalizar)
game_active = True

# Crear la interfaz de usuario con Streamlit
st.title('Juego Laser Tag')

# Crear botones y mostrar cronómetros
for color in timer_states.keys():
    if timer_buttons[color]:
        if st.button(f'Activar {color.capitalize()}', key=color):
            timer_buttons[color] = False
            timer_states[color] = 600  # Establece cada temporizador a 10 minutos para este ejemplo
            # Aquí agregarías la lógica para iniciar y gestionar el cronómetro real
            
    # Mostrar el tiempo restante para cada color
    st.write(f'{color.capitalize()}: {timer_states[color]}')

# Finalizar el juego después de la duración del juego
if time.time() - start_time > game_duration:
    game_active = False
    st.error('¡El juego ha terminado!')

# Mostrar una advertencia cuando queden 5 minutos
if time.time() - start_time > warning_time and game_active:
    st.warning('¡Quedan 5 minutos!')

# La lógica del temporizador necesitaría ejecutarse en el servidor o como un evento en segundo plano.
# Streamlit no es ideal para realizar operaciones en tiempo real como cronómetros que se actualizan cada segundo.
# Se requiere una solución alternativa para gestionar los cronómetros en tiempo real.
