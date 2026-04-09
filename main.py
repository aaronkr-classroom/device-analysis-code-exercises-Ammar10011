#main.py
from sensor import Temperaturesensor, lightsensor

temp = Temperaturesensor("Temp1")
light= lightsensor("Light1")

print(f"Temp: {temp.read()}")
print(f"Light: {Light.read()}")
