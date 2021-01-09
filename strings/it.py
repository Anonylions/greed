# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})
# Current localization is Italian

# Currency symbol
currency_symbol = "R$"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} Disponível"

# Copies of a product in cart
in_cart_format_string = "{quantity} No carrinho"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Ordem #{id}"

# Order info string, shown to the admins
order_format_string = "Usuário {user}\n" \
                      "Criada {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Nota do cliente: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Ordem {status_text}</b>\n" \
                           "{items}\n" \
                           "TOTAL: <b>{value}</b>\n" \
                           "\n" \
                           "Nota: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>As transações estão carregando.\n" \
                       "Espere alguns segundos, por favor.</i>"

# Transactions page
transactions_page = "Pagina <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "E' estado gerado um arquivo .csv contenente todas as transações arquivadas no banco de dados do bot.\n" \
              "E' Você pode abrir este arquivo com outros programas, como o LibreOffice Calc, para processar" \
              " Os dados."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = ":)\n" \
                           ":)\n" \
                           ":)\n" \
                           ":)\n" \
                           ":)" \
                           " :)"

# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "O que você gostaria de fazer?\n" \
                              "💰 Você tem <b>{credit}</b> na carteira.\n" \
                              "\n" \
                              "<i>Para selecionar uma operação, pressione uma tecla no teclado abaixo.\n" \
                              "Se o teclado não estiver aberto, você pode abri-lo pressionando a tecla com quatro quadrados" \
                              " na barra de mensagens.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Você é um 💼 gerente desta loja! O que você gostaria de fazer? Para selecionar uma operação, pressione uma tecla no teclado abaixo. Se o teclado não estiver aberto, você pode abri-lo pressionando a tecla com quatro quadrados na barra de mensagens."

# Conversation: select a payment method
conversation_payment_method = "Como você deseja adicionar fundos à sua carteira"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Qual produto você deseja modificar?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Qual produto você deseja excluir?"

# Conversation: select a user to edit
conversation_admin_select_user = "Selecione um usuário para executar a ação selecionada."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Adicione produtos ao carrinho rolando para cima e pressionando o botão Adicionar abaixo" \
                            "os produtos que você deseja comprar. Quando terminar, volte para esta mensagem e" \
                            " pressione o botão Concluído.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Seu carrinho contém estes produtos:\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Se quiser continuar, pressione o botão Concluído abaixo desta mensagem..\n" \
                            "Para cancelar, pressione a tecla Cancelar.</i>"

# Live orders mode: start
conversation_live_orders_start = "Você está no modo de <b>Recebimento de pedidos</b>!\n" \
                                 "Todos os novos pedidos feitos pelos clientes aparecerão em tempo real neste" \
                                 " bate-papo e você pode marcá-los como concluídos✅" \
                                 " ou ✴️ devolver o crédito ao cliente"

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Pressione a tecla Parar abaixo desta mensagem para parar" \
                                " recepção.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Que tipo de assistência você gostaria de receber?"

# Conversação: confirmar promoção para administrador
conversation_confirm_admin_promotion = "Tem certeza de que deseja promover este usuário a 💼 Gerente?\n" \
                                       ":)' uma ação irreversível!"

# Conversation: language select menu header
conversation_language_select = "Selecione um idioma"

# Conversation: switching to user mode
conversation_switch_to_user_mode = "Você está mudando para o modo 👤 Cliente.\n" \
                                   "Se você quiser retomar a função de 💼 Gerente, reinicie a conversa com /start."

# Notification: the conversation has expired
conversation_expired = "🕐 Não recebo nenhuma mensagem há algum tempo, para economizar energia" \
                       " Eu encerrei a conversa.\n" \
                       "Se você deseja iniciar um novo, envie o comando novamente /start."

# User menu: order
menu_order = "🛒 Ordenar"

# User menu: order status
menu_order_status = "🛍 Minhas ordens"

# User menu: add credit
menu_add_credit = "💵 Adicionar fundos"

# User menu: bot info
menu_bot_info = "ℹ️ Informações sobre o bot"

# User menu: cash
menu_cash = "💵 Dinheiro"

# User menu: credit card
menu_credit_card = "💳 Com um cartão de crédito"

# Admin menu: products
menu_products = "📝️ Produtos"

# Admin menu: orders
menu_orders = "📦 Ordens"

# Menu: transactions
menu_transactions = "💳 Lista de transações"

# Menu: edit credit
menu_edit_credit = "💰 Criar transação"

# Admin menu: go to user mode
menu_user_mode = "👤 Mudar para o modo cliente"

# Admin menu: add product
menu_add_product = "✨ Novo produto"

# Admin menu: delete product
menu_delete_product = "❌ Deletar produto"

# Menu: cancel
menu_cancel = "🔙 Cancelar"

# Menu: skip
menu_skip = "⏭ Pular"

# Menu: done
menu_done = "✅️ Feito"

# Menu: pay invoice
menu_pay = "💳 Pago"

# Menu: complete
menu_complete = "✅ Completa"

# Menu: refund
menu_refund = "✴️ Reembolsar"

# Menu: stop
menu_stop = "🛑 Pare"

# Menu: add to cart
menu_add_to_cart = "➕ adicionar"

# Menu: remove from cart
menu_remove_from_cart = "➖ Retirar"

# Menu: help menu
menu_help = "❓ Ajuda e assistência"

# Menu: guide
menu_guide = "📖 Guia"

# Menu: next page
menu_next = "▶️ Frente"

# Menu: previous page
menu_previous = "◀️ De volta"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contate a loja"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Modificar gestoria"

# Menu: language
menu_language = "🇧🇷 Lingua"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "excepcional"

# Text: completed order
text_completed = "completado"

# Text: refunded order
text_refunded = "devolveu"

# Add product: name?
ask_product_name = "Qual deve ser o nome do produto?"

# Add product: description?
ask_product_description = "Qual deve ser a descrição do produto?"

# Add product: price?
ask_product_price = "Quanto deve custar o produto?\n" \
                    "Escreva <code>X</code> se você quer que o produto ainda não esteja à venda"

# Add product: image?
ask_product_image = "🖼 Que imagem você quer que o produto tenha??\n" \
                    "\n" \
                    "<i>Envie a foto, ou se preferir deixar o produto sem imagem aperte o botão Pular" \
                    " debaixo.</i>"

# Order product: notes?
ask_order_notes = "Você quer deixar uma nota com o pedido?\n" \
                  "💼 Ele ficará visível para os gerentes da loja.\n" \
                  "\n" \
                  "<i>Envie uma mensagem com a nota que deseja deixar ou pressione o botão Ignorar abaixo dela" \
                  " mensagem para não deixar nada.</i>"

# Refund product: reason?
ask_refund_reason = "Anexe um motivo para este reembolso..\n" \
                    "👤 Ele ficará visível para o cliente."

# Edit credit: notes?
ask_transaction_notes = "Anexe uma nota a esta transação.\n" \
                        "👤 Será visível para o cliente após o crédito/ debito" \
                        " e para os 💼 Gerentes no log de transações."

# Edit credit: amount?
ask_credit = "Quanto você deseja alterar o crédito do cliente?\n" \
             "\n" \
             "<i>Envie uma mensagem contendo o valor.\n" \
             "Coloque uma placa </i><code>+</code><i> se você deseja adicionar crédito à conta do cliente," \
             " ou um sinal </i><code>-</code><i> se você quiser deduzir.</i>"

# Header for the edit admin message
admin_properties = "<b>Licenças de {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Editar produtos"

# Edit admin: can receive orders?
prop_receive_orders = "Receber pedidos"

# Edit admin: can create transactions?
prop_create_transactions = "Gerenciar transações"

# Edit admin: show on help message?
prop_display_on_help = "Assistência ao cliente"

# Thread has started downloading an image and might be unresponsive
downloading_image = "Estou baixando sua foto!!\n" \
                    "Pode demorar um pouco ... Tenha paciência!\n" \
                    "Não poderei responder a você durante o download."

# Edit product: current value
edit_current_value = "O valor presente é:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Pressione a tecla Ignorar sob esta mensagem para manter o mesmo valor.</i>"

# Payment: cash payment info
payment_cash = "Você pode pagar usando, Ted, Pix, Nubank, Picpay. Entre em contado com: @Anonylions\n" \
               "Pague ao privado, e forneça ao gerente da loja esta identificação:\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Quantos fundos você deseja adicionar à sua carteira?\n" \
                    "\n" \
                    "<i>Selecione um valor com os botões abaixo ou insira-o manualmente com o teclado" \
                    " normal.</i>"

# Payment: add funds invoice title
payment_invoice_title = "Adicionando fundos"

# Payment: add funds invoice description
payment_invoice_description = "Pagar este recibo será adicionado {amount} para a carteira."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "recarregar"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Sobretaxa de cartão"

# Notification: order has been placed
notification_order_placed = "Um novo pedido foi feito::\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Seu pedido foi concluído!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Seu pedido foi reembolsado!!\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️ Uma nova transação foi aplicada à sua carteira:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Motivo de reembolso:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = ':) apenas um bot'

# Help: guide
help_msg = "©2021"

# Help: contact shopkeeper
contact_shopkeeper = "Atualmente, a equipe disponível para atendimento aos usuários é composta por:\n" \
                     "{shopkeepers}\n" \
                     "<i>Clique / toque em um de seus nomes para contatá-los em um chat do Telegram.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ O produto foi adicionado / editado com sucesso!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ O produto foi excluído com sucesso!"

# Success: order has been created
success_order_created = "✅ O pedido foi enviado com sucesso!!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Você marcou o pedido #{order_id} como concluído."

# Success: order was refunded successfully
success_order_refunded = "✴️ A ordem #{order_id} foi reembolsado com sucesso."

# Success: transaction was created successfully
success_transaction_created = "✅ A transação foi criada com sucesso!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ Este bot funciona apenas em chats privados."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ A conversa com o bot é interrompida.\n" \
                           "Para reiniciá-lo, envie o comando /start ao bot."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 A conversa com o bot está começando\n" \
                         "Aguarde um momento antes de enviar mais comandos!!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️O máximo de fundos que podem ser adicionados em uma única transação é  " \
                                "{max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ O mínimo de fundos que podem ser adicionados em uma única transação é " \
                                 "{min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ Este pagamento expirou e foi cancelado. Se você ainda deseja adicionar fundos, " \
                        "use a opção de menu Adicionar fundos."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Já existe um produto com este nome."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ Você não tem crédito suficiente para fazer seu pedido."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Este pedido já foi processado"

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Você ainda não fez pedidos, então não há nada para ver."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  O usuário selecionado não existe"

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh não! Un <b>errore</b> interrompeu esta conversa\n" \
                               "O erro foi relatado ao proprietário do bot para que eles possam corrigi-lo.\n" \
                               "Para iniciar uma nova conversa, envie o comando /start."
