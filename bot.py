# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
from botcity.plugins.email import BotEmailPlugin

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Instanciar o plug-in
    email = BotEmailPlugin()

    # Configure IMAP com o servidor Gmail
    email.configure_imap("imap.gmail.com", 993)

    # Configure SMTP com o servidor Gmail
    email.configure_smtp("imap.gmail.com", 587)

    email.login("<Login>", "<Senha>")

    # Definindo informações do email
    para = ["<Destinatário>"]
    assunto = "Seja bem vindo ao melhor treinamento!"
    corpo_email = "<h1>Olá!</h1> Curso de Botcity da T2C!"

    # Enviando a mensagem de e-mail
    email.send_message(assunto, corpo_email, para, use_html=True)

    # Feche a conexão com os servidores IMAP e SMTP
    email.disconnect()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()