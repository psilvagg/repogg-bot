import smtplib
import time
import os
import telebot as tl
from email.message import EmailMessage
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def enviarEmail(email):
    time.sleep(6)
    bodyEmail = """
    <!doctype html>
<html>
  <head>
    <meta name="viewport" content="width=device-width" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Confirmação de inscrição!</title>
    <style>
      /* -------------------------------------
          GLOBAL RESETS
      ------------------------------------- */
      img {
        border: none;
        -ms-interpolation-mode: bicubic;
        max-width: 100%; }

      body {
        background-color: #f6f6f6;
        font-family: sans-serif;
        -webkit-font-smoothing: antialiased;
        font-size: 14px;
        line-height: 1.4;
        margin: 0;
        padding: 0;
        -ms-text-size-adjust: 100%;
        -webkit-text-size-adjust: 100%; }

      table {
        border-collapse: separate;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        width: 100%; }
        table td {
          font-family: sans-serif;
          font-size: 14px;
          vertical-align: top; }

      /* -------------------------------------
          BODY & CONTAINER
      ------------------------------------- */

      .body {
        background-color: #f6f6f6;
        width: 100%; }

      /* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
      .container {
        display: block;
        Margin: 0 auto !important;
        /* makes it centered */
        max-width: 580px;
        padding: 10px;
        width: 580px; }

      /* This should also be a block element, so that it will fill 100% of the .container */
      .content {
        box-sizing: border-box;
        display: block;
        Margin: 0 auto;
        max-width: 580px;
        padding: 10px; }

      /* -------------------------------------
          HEADER, FOOTER, MAIN
      ------------------------------------- */
      .main {
        background: #ffffff;
        border-radius: 3px;
        width: 100%; }

      .wrapper {
        box-sizing: border-box;
        padding: 20px; }

      .content-block {
        padding-bottom: 10px;
        padding-top: 10px;
      }

      .footer {
        clear: both;
        Margin-top: 10px;
        text-align: center;
        width: 100%; }
        .footer td,
        .footer p,
        .footer span,
        .footer a {
          color: #999999;
          font-size: 12px;
          text-align: center; }

      /* -------------------------------------
          TYPOGRAPHY
      ------------------------------------- */
      h1,
      h2,
      h3,
      h4 {
        color: #000000;
        font-family: sans-serif;
        font-weight: 400;
        line-height: 1.4;
        margin: 0;
        Margin-bottom: 30px; }

      h1 {
        font-size: 35px;
        font-weight: 300;
        text-align: center;
        text-transform: capitalize; }

      p,
      ul,
      ol {
        font-family: sans-serif;
        font-size: 14px;
        font-weight: normal;
        margin: 0;
        Margin-bottom: 15px; }
        p li,
        ul li,
        ol li {
          list-style-position: inside;
          margin-left: 5px; }

      a {
        color: #3498db;
        text-decoration: underline; }

      /* -------------------------------------
          BUTTONS
      ------------------------------------- */
      .btn {
        box-sizing: border-box;
        width: 100%; }
        .btn > tbody > tr > td {
          padding-bottom: 15px; }
        .btn table {
          width: auto; }
        .btn table td {
          background-color: #ffffff;
          border-radius: 5px;
          text-align: center; }
        .btn a {
          background-color: #ffffff;
          border: solid 1px #3498db;
          border-radius: 5px;
          box-sizing: border-box;
          color: #3498db;
          cursor: pointer;
          display: inline-block;
          font-size: 14px;
          font-weight: bold;
          margin: 0;
          padding: 12px 25px;
          text-decoration: none;
          text-transform: capitalize; }

      .btn-primary table td {
        background-color: #3498db; }

      .btn-primary a {
        background-color: #3498db;
        border-color: #3498db;
        color: #ffffff; }

      /* -------------------------------------
          OTHER STYLES THAT MIGHT BE USEFUL
      ------------------------------------- */
      .last {
        margin-bottom: 0; }

      .first {
        margin-top: 0; }

      .align-center {
        text-align: center; }

      .align-right {
        text-align: right; }

      .align-left {
        text-align: left; }

      .clear {
        clear: both; }

      .mt0 {
        margin-top: 0; }

      .mb0 {
        margin-bottom: 0; }

      .preheader {
        color: transparent;
        display: none;
        height: 0;
        max-height: 0;
        max-width: 0;
        opacity: 0;
        overflow: hidden;
        mso-hide: all;
        visibility: hidden;
        width: 0; }

      .powered-by a {
        text-decoration: none; }

      hr {
        border: 0;
        border-bottom: 1px solid #f6f6f6;
        Margin: 20px 0; }

      /* -------------------------------------
          RESPONSIVE AND MOBILE FRIENDLY STYLES
      ------------------------------------- */
      @media only screen and (max-width: 620px) {
        table[class=body] h1 {
          font-size: 28px !important;
          margin-bottom: 10px !important; }
        table[class=body] p,
        table[class=body] ul,
        table[class=body] ol,
        table[class=body] td,
        table[class=body] span,
        table[class=body] a {
          font-size: 16px !important; }
        table[class=body] .wrapper,
        table[class=body] .article {
          padding: 10px !important; }
        table[class=body] .content {
          padding: 0 !important; }
        table[class=body] .container {
          padding: 0 !important;
          width: 100% !important; }
        table[class=body] .main {
          border-left-width: 0 !important;
          border-radius: 0 !important;
          border-right-width: 0 !important; }
        table[class=body] .btn table {
          width: 100% !important; }
        table[class=body] .btn a {
          width: 100% !important; }
        table[class=body] .img-responsive {
          height: auto !important;
          max-width: 100% !important;
          width: auto !important; }}

      /* -------------------------------------
          PRESERVE THESE STYLES IN THE HEAD
      ------------------------------------- */
      @media all {
        .ExternalClass {
          width: 100%; }
        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
          line-height: 100%; }
        .apple-link a {
          color: inherit !important;
          font-family: inherit !important;
          font-size: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
          text-decoration: none !important; }
        .btn-primary table td:hover {
          background-color: #34495e !important; }
        .btn-primary a:hover {
          background-color: #34495e !important;
          border-color: #34495e !important; } }

    </style>
  </head>
  <body class="">
    <table border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader">Confirmação de inscrição, HelperBot.</span>
            <table class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <table border="0" cellpadding="0" cellspacing="0">
                    <tr>
                      <td>
                        <p>Olá!</p>
                        <p>Por meio deste E-Mail venho informa-ló que sua inscrição foi realizada com sucesso!</p>
                        <table border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                          <tbody>
                            <tr>
                              <td align="left">
                                <table border="0" cellpadding="0" cellspacing="0">
                                  <tbody>
                                    <tr>
                                      <td> <a href="https://link.mercadopago.com.br/psilvagg" target="_blank">Contribuir</a> </td>
                                    </tr>
                                  </tbody>
                                </table>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <p>É gratificante saber  o seu interesse! XD</p>
                        <p><b>BotHelper, psgg</b></p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

            <!-- END MAIN CONTENT AREA -->
            </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">Salvador, Bahia, Brasil </span>
                    <br> Suporte? <a href="https://linktr.ee/pedrosxz">Aqui</a>.
                  </td>
                </tr>
                <tr>
                </tr>
              </table>
            </div>
            <!-- END FOOTER -->

          <!-- END CENTERED WHITE CONTAINER -->
          </div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
  </body>
</html>
"""

    #EmailMessage
    msg = EmailMessage()
    msg['Subject'] = 'Obrigado por sua inscrição!'
    msg['From'] = f'HelperBot <helperbot@outlook.com.br>'
    msg['To'] = email
    msg.set_content(bodyEmail, subtype='html')
    password = 'blcntqshzvawjtnr'
    # Configuração do servidor SMTP
    with smtplib.SMTP('smtp.office365.com', 587) as s:
        s.starttls()
        s.login('helperbot@outlook.com.br', password)  # Use apenas o e-mail
        s.send_message(msg)
    print('Cadastro realizado com sucesso! \n')


while True:
    print("Carregando...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Seja Bem-Vindo!\nSuporte: https://discord.gg/VDsf74sEgz\n")
    email = input("> Cadastre-se digitando seu Email: ")
    enviarEmail(email)
    print("> Gere o TOKEN do seu BOT através do BotFather --> (https://t.me/BotFather)")
    tokenUser = input("Insira o TOKEN do seu BOT gerado pelo BotFather: ")
    if tokenUser == '' or len(tokenUser) < 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Verificando TOKEN...")
        time.sleep(2)
        print("Quase lá!")
        time.sleep(1)
        print("> O token inserido é inválido. Tente novamente!")
        print(">> Aperte CTRL + C simultaneamente para finalizar.")
    else:
        try:
            bot = tl.TeleBot(tokenUser)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Verificando TOKEN...")
            time.sleep(2)
            print("Quase lá!")
            time.sleep(1)
            print("Token validado com sucesso! Seu bot está online!")
            break
        except Exception as e:
            print(f"Erro ao validar o token: {e}")
            print("Tente novamente!")

#Dicionário para armazenar os IDs das mensagens
messages = {}

#Instruções
# 1 - Caminho padrão da foto: C:/Program Files/RepoGG/repoggbot.png
# 2 - O arquivo se encontra na pasta do bot
# 3 - discord.gg/VDsf74sEgz


@bot.message_handler(commands=["start"])
def start(mensagem):
    nome = mensagem.from_user.first_name
    with open('photo/repoggbot.png', 'rb') as photo:
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
