import smtplib

def enviar_correo(nombre, correo):
    fromaddr = "From: no-reply@mamochi.com"
    toaddrs  = f"To: {correo}"

    msg =f"""
    {fromaddr}
    {toaddrs}\n
    {nombre}:\n
    Venta procesada.
    """

    server = smtplib.SMTP('cliente', 1025)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()