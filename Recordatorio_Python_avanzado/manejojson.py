# Manejo json

import json

# ¿Qué es un json?

# Creamos uno

String_json_persona = json.dumps({'nombre':'jose', 'apellidos':'escribano', 'edad':28, 'ciudad':"Madrid"})

jsonPerson = json.loads(String_json_persona)
print(str(jsonPerson['nombre'] + " " + jsonPerson['apellidos']))

# Con .dumps() pasamos un diccionario a string y con .loads() al revés
