import requests

url = 'http://inscripcion:5000'

data = {
    'nombre': (None, 'Juan'),
    'usuario': (None, 'juan.juan'),
    'correo': (None, 'juan.juan@test.com'),
    'paid': (None, ''),
}

response = requests.post(url, files=data)

print(response.json())