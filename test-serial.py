import serial

try:
    ser = serial.Serial("COM6", 9600)
    print("Conexión exitosa")
except Exception as e:
    print(f"Error al conectar: {e}")