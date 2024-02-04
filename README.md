Enviar de Mensagens para Telegram

Este é um simples script em Python que utiliza a biblioteca python-telegram-bot para enviar mensagens para um chat ou usuário específico no Telegram. O script é útil para notificações automáticas ou outras comunicações programadas.
Requisitos

    Python 3.x
    Biblioteca python-telegram-bot (instalável via pip install python-telegram-bot)

Configuração

    Criação do Bot no Telegram:
        Abra o Telegram e procure por BotFather.
        Inicie uma conversa com o BotFather e use o comando /newbot para criar um novo bot.
        Siga as instruções para escolher um nome e um username para o seu bot.
        Após a criação, o BotFather fornecerá um token único para o seu bot.

    Substituição do Token no Código:
        Abra o script em Python.
        Localize a linha TOKEN = 'SEU_TOKEN'.
        Substitua 'SEU_TOKEN' pelo token fornecido pelo BotFather.

    Obtenção do Chat ID:
        Converse com o bot @userinfobot no Telegram.
        Envie o comando /start.
        O bot fornecerá informações sobre sua conta, incluindo o ID do Chat. Substitua 'CHAT_ID' no script por este valor.

Uso

    Abra o terminal e navegue até o diretório do script.
    Execute o script com o comando python telegram.py

Notas

    Certifique-se de manter o token do bot em segredo, evitando compartilhá-lo publicamente.
    Este script é um exemplo simples. Personalize conforme necessário para atender às suas necessidades.
    O script enviará a mensagem configurada para o chat ou usuário especificado.
