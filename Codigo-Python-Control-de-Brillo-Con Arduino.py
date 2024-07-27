import serial
import screen_brightness_control as sbc

# Configurar la comunicación serial
ser = serial.Serial("COM6", 9600)
v = ""
brillo = 0

while True:
    # Leer el valor desde el Arduino
    response = ser.readline().decode("utf-8").strip()
    # Asegurarse de que el valor no sea nulo
    if(response):
        # Si la respuesta es diferente a la anterior
        if(v != response):
            v = response
            brillo = int(v)
            # Asegurarse de que el brillo esté en un rango válido (0-100)
            brillo = max(0, min(100, brillo))
            print(f"Configurando brillo a: {brillo}%")
            # Ajustar el brillo de la pantalla
            sbc.set_brightness(brillo)
