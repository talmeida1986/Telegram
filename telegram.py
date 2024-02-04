# Importa a classe Bot do módulo telegram
from telegram import Bot

# Substitua 'SEU_TOKEN' pelo token do seu bot
TOKEN = 'SEU_TOKEN'

def enviar_mensagem(chat_id, texto):
    """
    Envia uma mensagem para um chat ou usuário no Telegram.

    Parâmetros:
    chat_id (str): O ID do chat ou usuário ou grupo para o qual a mensagem será enviada.
    texto (str): O texto da mensagem a ser enviada.

    Retorna:
    None
    """
    # Cria uma instância do Bot com o token fornecido
    bot = Bot(token=TOKEN)
    
    # Envia a mensagem para o chat ou usuário especificado
    bot.send_message(chat_id=chat_id, text=texto)

# Substitua 'CHAT_ID' pelo ID do chat ou do usuário ou grupo para o qual você deseja enviar a mensagem
chat_id_destino = 'CHAT_ID'

# Substitua 'Sua mensagem aqui' pela mensagem que você deseja enviar
mensagem = 'Sua mensagem aqui'

# Chama a função enviar_mensagem com os parâmetros apropriados
enviar_mensagem(chat_id_destino, mensagem)
