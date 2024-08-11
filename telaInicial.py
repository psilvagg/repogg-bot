import telebot as tl
import openai as open
import os
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

#Coloque aqui seu token gerado pelo BotFather
bot = tl.TeleBot("")

# Dicionário para armazenar os IDs das mensagens
messages = {}

#Instruções
# 1 - Caminho padrão da foto: C:/Program Files/RepoGG/repoggbot.png
# 2 - O arquivo se encontra na pasta do bot
# 3 - discord.gg/VDsf74sEgz

print("BOT ON!")

@bot.message_handler(commands=["start"])
def start(mensagem):
    nome = mensagem.from_user.first_name
    with open('C:/Program Files/RepoGG/repoggbot.png', 'rb') as photo:
        bot.send_photo(
            chat_id=mensagem.chat.id,
            photo=photo,
            caption=f'''Olá {nome}! 🤖 Seja Bem-Vindo ao GG Repo 🤖! \n ━━━━━━━━━━━━━━━━━━━━━━━━━━━
ℹ️Suporte: @psilvagg ou @lipinho022
ℹ️Nosso Discord: discord.gg/VDsf74sEgz
ℹ️Acesse o código fonte do nosso bot: github.com/pedrosxz
ℹ️Ajude a manter @repogg_Bot:\nhttps://link.mercadopago.com.br/psilvagg\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━
\n⚠️Acesse nosso repositório através do /menu
            '''
        )

@bot.message_handler(commands=["menu"])
def menu(msgmenu):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Repositório 📂", callback_data="files"))
    markup.add(InlineKeyboardButton("ChatGPT 🤖", callback_data="gpt"))
    markup.add(InlineKeyboardButton("Lista de Comandos 📋", callback_data="comandos"))

    # Envia a mensagem e salva o message_id
    sent_message = bot.reply_to(msgmenu, '''Menu📋''', reply_markup=markup)
    messages['menu'] = sent_message.message_id  # Armazena o ID da mensagem do menu


def menurepo(chat_id, message_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Grand Theft Auto San Andreas 🗺️", callback_data="gtasa"))
    markup.add(InlineKeyboardButton("Grand Theft Auto San Andreas Mod + SAMP 🚗 + 🗺", callback_data="gtasamod"))
    markup.add(InlineKeyboardButton("OMSI 2 | Mods | Mapa Salvador Norte 3.3 🚌", callback_data="omsi2"))
    markup.add(InlineKeyboardButton("(OMSI 2) Mods de ônibus 🚍", callback_data="busomsi2"))
    markup.add(InlineKeyboardButton("(Counter-Strike 2) Minhas CFG (@psilva.gg) ⚙️", callback_data="cfgpsgg"))
    markup.add(InlineKeyboardButton("Counter-Strike 1.6 🔫", callback_data="cs16"))
    markup.add(InlineKeyboardButton("Counter-Strike 1.6 + Mods PTBR 🔫🇵🇹", callback_data="cs16pt"))
    markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_menu"))
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text="Menu de Arquivos 📂\n\n\n⚠️ Clique no botão do arquivo selecionado para receber as orientações e o link para download.",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "files":
        menurepo(call.message.chat.id, call.message.message_id)
    elif call.data == "gtasa":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 9 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download do jogo <a href="https://bit.ly/4dGzTHQ">aqui</a>
2 - Extraia o Jogo
3 - Para ONLINE, execute o arquivo <u>San Andreas Multiplayer.exe</u> e para MODO HISTÓRIA execute <u>gta_sa.exe</u></i>''',
            parse_mode='HTML',
            reply_markup=markup
        )
    elif call.data == "gtasamod":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 14 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download do jogo <a href="https://bit.ly/gtasann">aqui</a>
2 - Extraia o Jogo
3 - Para ONLINE, execute o arquivo <u>San Andreas Multiplayer.exe</u> e para MODO HISTÓRIA execute <u>gta_sa.exe</u></i>''',
            parse_mode='HTML',
            reply_markup=markup
        )
    elif call.data == "omsi2":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 90 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download do jogo <a href="https://bit.ly/omsi2">aqui</a>
2 - Extraia o Jogo
3 - Execute o arquivo <u>omsi2.exe</u></i>''',
            parse_mode='HTML',
            reply_markup=markup
        )
    elif call.data == "busomsi2":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 3 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download dos Mods <a href="https://bit.ly/busomsi2">aqui</a>
2 - Extraia os arquivos
3 - Coloque os arquivos na pasta <u>RAIZ</u> do OMSi2</i>''',
            parse_mode='HTML',
            reply_markup=markup
        )
    elif call.data == "cfgpsgg":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''f✅ <b>Requisitos:</b>\n💾 3 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download dos Mods <a href="https://bit.ly/autoexecpsilvagg">aqui</a>
2 - Coloque o arquivo no seguinte diretório: Program Files (x86) > Steam > steamapps > common > Counter-Strike Global Offensive > game > csgo > cfg</i>''',
            parse_mode='HTML',
            reply_markup=markup
        )
    elif call.data == "cs16":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 1 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download dos Mods <a href="https://cs.csrevo.com/">aqui</a>
2 - Extraia os arquivos e instale o jogo</i>''',
            parse_mode='HTML',
            reply_markup=markup,
            disable_web_page_preview=True
        )
    elif call.data == "cs16pt":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Voltar 🔙", callback_data="back_to_files"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='''✅ <b>Requisitos:</b>\n💾 1 GB Livres\n🗜️ Descompactador (Winrar, 7Zip etc)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n
📝 <i><b>Orientações:</b>\n
1 - Realize o download dos Mods <a href="https://www.csbruxos.com.br/2024/02/counter-strike-16-full-ptbr-atualizado.html">aqui</a>
2 - Extraia os arquivos e instale o jogo</i>''',
            parse_mode='HTML',
            reply_markup=markup,
            disable_web_page_preview=True
        )
    elif call.data == "back_to_files":
        menurepo(call.message.chat.id, call.message.message_id)
    elif call.data == "back_to_menu":
        # Use a função menu para atualizar a mensagem existente com o menu principal
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Repositório 📂", callback_data="files"))
        markup.add(InlineKeyboardButton("ChatGPT 🤖", callback_data="gpt"))
        markup.add(InlineKeyboardButton("Lista de Comandos 📋", callback_data="comandos"))
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Menu📋",
            reply_markup=markup
        )

# Deixa o bot em loop, para não finalizar ao receber uma instrução
bot.infinity_polling()
