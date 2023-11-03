import requests
from faker import Faker
fake = Faker()

def enviar(ip, data):
    url = f'http://{ip}:5000'
    
    response = requests.post(url, files=data)

    print(response.json())
    print()


while True:
    print("1. Inscribirse.")
    print("2. Notificar falta de stock.")
    print("3. Venta realizada.")
    print("4. Salir.\n")
    print("Opción:", end=" ")
    
    opcion = int(input())
    
    if opcion == 1:
        # Datos del formulario de inscripción
        data = {
            'nombre': (None, fake.name()),
            'usuario': (None, fake.user_name()),
            'correo': (None, fake.ascii_safe_email()),
            'paid': (None, fake.pybool()),
        }
        enviar("inscripcion", data)

    elif opcion == 2:
        print("Ingrese su nombre de usuario:")  # Simular que se tiene iniciada una sesión
        usuario = input().strip()
        
        # Ingredientes sin stock. "True" es que necesita restock, "False" es que no necesita restock
        data = {
            'usuario': (None, usuario),
            'agua': (None, fake.pybool()),
            'huesillo': (None, fake.pybool()),
            'azucar': (None, fake.pybool()),
            'mote': (None, fake.pybool()),
            'canela': (None, fake.pybool()),
        }
        enviar("stock", data)
        
    elif opcion == 3:
        print("Ingrese su nombre de usuario:")  # Simular que se tiene iniciada una sesión
        usuario = input().strip()
        
        data = {
            'usuario': (None, usuario),
            'monto': (None, 2000),
        }
        enviar("venta", data)
        
    elif opcion == 4:
        response = requests.post('http://inscripcion:5000/salir')
        response = requests.post('http://stock:5000/salir')
        response = requests.post('http://venta:5000/salir')
        print("Petición enviada.")
        exit()
        
    else:
        print("Valor erróneo.\n")