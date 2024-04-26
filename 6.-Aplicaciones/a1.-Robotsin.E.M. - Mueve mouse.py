import pyautogui
import keyboard
#math: Librería que proporciona funciones y constantes matemáticas como seno, π, logaritmo, etc.
import math
#time: Librería para el manejo de tiempos, como retardos, contadores, etc.
import time

# Get the screen resolution
screen_width, screen_height = pyautogui.size()
# Calculate the center of the screen
center_x = screen_width // 2
center_y = screen_height // 2
# Set the radius of the circular motion
radius = 100
# Set the speed of the circular motion (adjust as needed)
speed = 0.05  # Adjust this value to control the speed

# Function to calculate the next position of the mouse
def calculate_next_position(angle):
    x = center_x + int(radius * math.cos(angle))
    y = center_y + int(radius * math.sin(angle))
    return x, y
# Main loop
angle = 0
while not keyboard.is_pressed('s'):
    # Calculate the next position
    next_x, next_y = calculate_next_position(angle)
    # Move the mouse to the next position
    pyautogui.moveTo(next_x, next_y, duration=0)
    # Increment the angle
    angle += speed
    # Wrap angle to keep it within 0 to 2*pi
    angle %= (2 * math.pi)
    # Add a slight delay to control the speed
    #time.sleep(): Método que se utiliza para suspender la ejecución de un programa durante un intervalo 
    #de tiempo específico dado en segundos.
    time.sleep(0.01)

print("Program stopped.")