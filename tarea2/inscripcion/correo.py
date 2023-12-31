import smtplib

def enviar_correo(nombre, usuario, correo, clave):
    fromaddr = "From: no-reply@mamochi.com"
    toaddrs  = f"To: {correo}"

    msg =f"""
    {fromaddr}
    {toaddrs}\n
    {nombre}:\n
    Su inscripcion en el gremio de Maestros Motehuesilleros de Chile (MAMOCHI) ha sido procesada.\n
    Sus credenciales son:
    Usuario: {usuario}
    Clave: {clave}
    """
    
    server = smtplib.SMTP('cliente', 1025)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()