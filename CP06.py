# CP06 - Python - Turma 1ESPW
# Membros do grupo: 
# André Lambert (RM99148), 
# Lucas Feijó (RM99727), 
# Vitor Maia (RM99658)

import funcoes.compras as compras
import funcoes.entrada as entrada
import funcoes.estoque as estoque
import funcoes.fornecedor as fornecedor
import funcoes.saida as saida
import funcoes.suprimento as suprimento
import funcoes.pedidos as pedidos
import funcoes.tarefas as tarefas
import funcoes.crudBanco as crudBanco
import funcoes.gravacaoTxt as gravacaoTxt
import os
# criando função para limpar o terminal
limpa_a_tela = lambda: os.system('cls')

# crinado função para validar se a string é um numero:

def eh_numero(valor):
    if valor == '':
        return False

    numeros = '0123456789'

    for char in valor:
        if char not in numeros:
            return False
    return True

########### DEFINIÇÃO DE BASES INICIAIS ###############

# Registro incial de compras
comprasDB = crudBanco.carrega_compras()

# Registro inicial de saídas
saidasDB = crudBanco.carrega_saidas()

# Registro incicial de estoque
estoqueDB = crudBanco.carrega_estoque()

# Registro incial de suprimentos
suprimentosDB = crudBanco.carrega_suprimentos()
    
# Registro incial de fornecedores
fornecedoresDB = crudBanco.carrega_fornecedores()


# Registro de opcoes de pedidos
opcoesPedidosDB = crudBanco.carrega_pedidos()


# Registro incial de pedidos
pedidosDB = crudBanco.carrega_pedidos()


tarefasDB = crudBanco.carrega_tarefas()

# mostrar menu principal
def mostra_menu_principal():
    print("\n")
    print("==========================")
    print("||    MENU PRINCIPAL    ||")
    print("==========================")
    print("1. COMPRAS PARA O ESTOQUE")
    print("2. ESTOQUE")
    print("3. PEDIDOS CLIENTES")
    print("4. TAREFAS")
    print("0. FINALIZAR PROGRAMA")

########### DEFINIÇÃO DO PROGRAMA ###############

#O programa roda até que a opção de sair seja escolhida
while True:
    mostra_menu_principal()
    opcaoMenuPrincipal = input("DIGITE A OPÇÃO DESEJADA: ") 
    match opcaoMenuPrincipal:
        case "1": #COMPRAS
            limpa_a_tela()
            while True: 
                compras.mostra_menu_compras()
                opcaoCompra = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoCompra:
                    case "1": # COMPRAS > MENU DE FORNECEDORES
                        limpa_a_tela()
                        while True:
                            fornecedor.mostra_lista_de_fornecedores(fornecedoresDB)
                            opcaoFornecedor = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoFornecedor:
                                case "9": # COMPRAS > MENU DE FORNECEDORES > CADASTRAR NOVO FORNECEDOR
                                    limpa_a_tela()
                                    fornecedor.cadastrar_fornecedor(fornecedoresDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "2": # COMPRAS > MENU DE SUPRIMENTOS
                        limpa_a_tela()
                        while True:
                            suprimento.mostra_menu_comprar_suprimentos(suprimentosDB)
                            opcaoSuprimento = input('DIGITE A OPÇÃO DESEJADA: ')
                            match opcaoSuprimento:
                                case "1": # COMPRAS > MENU DE SUPRIMENTOS > COMPRAR SUPRIMENTO
                                    limpa_a_tela()
                                    suprimento.comprar_suprimento(suprimentosDB, estoqueDB, comprasDB)
                                    continue
                                case "2":# COMPRAS > MENU DE SUPRIMENTOS > CADASTRAR NOVO SUPRIMENTO
                                    limpa_a_tela()
                                    suprimento.cadastrar_suprimento(suprimentosDB, estoqueDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _:
                                    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                                    continue
                    case "3": # COMPRAS > VER TODAS AS COMPRAS
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    gravacaoTxt.gravar_saida_txt(compras.string_ver_compras(comprasDB))
                                case "2":
                                    limpa_a_tela()
                                    compras.ver_compras(comprasDB)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break         
                        continue
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _ :
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case "2": # ESTOQUE
            limpa_a_tela()
            while True:
                estoque.mostra_menu_estoque()
                opcaoEstoque = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoEstoque:
                    case "1": # ESTOQUE > MOSTRAR ENTRADAS
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    gravacaoTxt.gravar_saida_txt(entrada.string_lista_entradas(comprasDB))
                                case "2":
                                    limpa_a_tela()
                                    entrada.listar_entradas(comprasDB)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case "2": # ESTOQUE > MENU SAÍDAS
                        limpa_a_tela()
                        while True:
                            saida.mostra_menu_saidas()
                            opcaoSaida = input("DIGITE A OPÇÃO DESEJADA: ")
                            match opcaoSaida:
                                case "1": # ESTOQUE > MENU SAÍDAS > LISTAR SAÍDAS
                                    while True:
                                        gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                                        match gravacao:
                                            case "1":
                                                limpa_a_tela()
                                                gravacaoTxt.gravar_saida_txt(saida.string_lista_saidas(saidasDB))
                                            case "2":
                                                limpa_a_tela()
                                                saida.listar_saidas(saidasDB)
                                            case _:
                                                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                                continue
                                        break
                                    continue
                                case "2": # ESTOQUE > MENU SAÍDAS > CADASTRAR SAÍDAS
                                    limpa_a_tela()
                                    saida.cadastrar_saida(saidasDB, estoqueDB)
                                    continue
                                case "0": # VOLTAR
                                    limpa_a_tela()
                                    break
                                case _ :
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n")
                                    continue
                        continue
                    case "3": # ESTOQUE > MOSTRAR ESTOQUE
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    gravacaoTxt.gravar_saida_txt(estoque.string_mostra_estoque(estoqueDB))
                                case "2":
                                    limpa_a_tela()
                                    estoque.mostra_estoque(estoqueDB)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break

                        continue
                    case "0": # VOLTAR
                        limpa_a_tela()
                        break
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
            continue
        case "3": # PEDIDOS CLIENTES
            while True:
                pedidos.mostra_menu_pedidos()
                opcaoPedidos = input("DIGITE A OPÇÃO DESEJADA:")
                limpa_a_tela()
                match opcaoPedidos:
                    case '1':
                        carrinho = []
                        while True:
                            pedidos.mostra_menu_realizar_pedido(opcoesPedidosDB)
                            pedidos.mostra_carrinho(carrinho, opcoesPedidosDB)
                            opcaoFazerPedido = input('DIGITE A OPÇÃO DESEJADA: ')

                            # Lendo e validando a opção do pedido
                            if not eh_numero(opcaoFazerPedido):
                                limpa_a_tela()
                                print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                                continue
                            opcaoFazerPedido = int(opcaoFazerPedido)

                            if opcaoFazerPedido > len(opcoesPedidosDB) or opcaoFazerPedido < 1:
                                limpa_a_tela()
                                print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                                continue
                                
                            # Lendo e validando a quantidade do pedido
                            quantidadeFazerPedido = input('DIGITE A QUANTIDADE DESEJADA: ')
                            if not eh_numero(quantidadeFazerPedido):
                                limpa_a_tela()
                                print('QUANTIDADE INVÁLIDA! PENSE NOVAMENTE!')
                                continue
                            
                            quantidadeFazerPedido = int(quantidadeFazerPedido)
                            if (quantidadeFazerPedido <= 0 ):
                                limpa_a_tela()
                                print('QUANTIDADE INVÁLIDA! PENSE NOVAMENTE!')
                            else:
                                novoItem = {
                                    'idOpcaoPedido': opcaoFazerPedido-1,
                                    'quantidade': quantidadeFazerPedido
                                }
                                carrinho.append(novoItem)
                                limpa_a_tela()
                                print('ITEM ADICIONADO AO CARRINHO!')
                                pedidos.mostra_carrinho(carrinho, opcoesPedidosDB)
                                pedidos.mostrar_menu_continuar_comprando()
                                opcaoContinuarPedindo = ''
                                while True:
                                    opcaoContinuarPedindo = input('DIGITE A OPÇÃO DESEJADA: ')
                                    if not eh_numero(opcaoContinuarPedindo):
                                        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                                        continue
                                    if int(opcaoContinuarPedindo) > len(opcoesPedidosDB):
                                        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
                                        continue
                                    else:
                                        break
                                match opcaoContinuarPedindo:
                                    case '1':
                                        limpa_a_tela()
                                        continue
                                    case '2':
                                        descricao = input('ADICIONE UMA DESCRICAO AO SEU PEDIDO: ')
                                        valorCarrinho = pedidos.calcula_custo_carrinho(carrinho, opcoesPedidosDB)
                                        frete = pedidos.calcula_frete_carrinho(carrinho, opcoesPedidosDB)
                                        carrinhoSaida = pedidos.transforma_carrinho_em_carrinho_de_saidas(carrinho, estoqueDB)
                                        pedidos.registra_pedido(carrinhoSaida, pedidosDB, estoqueDB, descricao, frete, valorCarrinho)
                                        saida.deduz_carrinho_do_estoque(estoqueDB, carrinhoSaida)
                                        saida.registra_saida(carrinhoSaida, saidasDB, estoqueDB, f"Saida refente ao pedido {len(pedidosDB)}#")
                                        print("PEDIDO REGISTRADO COM SUCESSO!")
                                        break
                                    case '0':
                                        limpa_a_tela()
                                        carrinho = []
                                        print('CARRINHO ESVAZIADO!')
                                        continue
                                    case _:
                                        limpa_a_tela()
                                        continue
                    case '2':
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    gravacaoTxt.gravar_saida_txt(pedidos.string_lista_pedidos(pedidosDB))
                                case "2":
                                    limpa_a_tela()
                                    pedidos.listar_pedidos(pedidosDB)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case '0':
                        break
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue
        case "4": # TAREFAS
            limpa_a_tela()
            while True:
                tarefas.mostra_menu_tarefas()
                opcaoTarefas = input("DIGITE A OPÇÃO DESEJADA: ")
                match opcaoTarefas:
                    case "1":
                        limpa_a_tela()
                        tarefas.cadastrar_tarefa(tarefasDB)
                        continue
                    case "2":
                        tarefas.atualizar_complitude_real(tarefasDB)
                        continue
                    case "3":
                        limpa_a_tela()
                        gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                        match gravacao:
                            case "1":
                                limpa_a_tela()
                                gravacaoTxt.gravar_saida_txt(tarefas.string_mostra_tarefas(tarefasDB))
                            case "2":
                                limpa_a_tela()
                                tarefas.menu_tarefas_em_andamento()
                                tarefas.mostra_tarefas(tarefasDB)
                            case _:
                                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                continue
                        continue
                    case "4":
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            tarefasAndamento = tarefas.filtrar_tarefas_em_andamento(tarefasDB)
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    if tarefasAndamento == []:
                                        print('NÃO HÁ TAREFAS EM ANDAMENTO')
                                        gravacaoTxt.gravar_saida_txt('NÃO HÁ TAREFAS EM ANDAMENTO')
                                    else:
                                        gravacaoTxt.gravar_saida_txt(tarefas.string_mostra_tarefas(tarefasAndamento))
                                case "2":
                                    limpa_a_tela()
                                    if tarefasAndamento == []:
                                        print('NÃO HÁ TAREFAS EM ANDAMENTO')
                                    else:
                                        tarefas.menu_tarefas_em_andamento()
                                        tarefas.mostra_tarefas(tarefasAndamento)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case "5":
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            tarefasConcluidas = tarefas.filtrar_tarefas_concluidas(tarefasDB)
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    if tarefasConcluidas == []:
                                        print('NÃO HÁ TAREFAS CONCLUÍDAS')
                                        gravacaoTxt.gravar_saida_txt('NÃO HÁ TAREFAS CONCLUÍDAS')
                                    else:
                                        gravacaoTxt.gravar_saida_txt(tarefas.string_mostra_tarefas(tarefasConcluidas))
                                case "2":
                                    limpa_a_tela()
                                    if tarefasConcluidas == []:
                                        print('NÃO HÁ TAREFAS CONCLUÍDAS')
                                    else:
                                        tarefas.menu_tarefas_concluidas()
                                        tarefas.mostra_tarefas(tarefasConcluidas)
                                    
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case "6":
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            tarefasNaoIniciadas = tarefas.filtrar_tarefas_nao_iniciadas(tarefasDB)
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    if tarefasNaoIniciadas == []:
                                        print('NÃO HÁ TAREFAS NÃO INICIADAS')
                                        gravacaoTxt.gravar_saida_txt('NÃO HÁ TAREFAS NÃO INICIADAS')
                                    else:
                                        gravacaoTxt.gravar_saida_txt(tarefas.string_mostra_tarefas(tarefasNaoIniciadas))
                                case "2":
                                    limpa_a_tela()
                                    if tarefasNaoIniciadas == []:
                                        print('NÃO HÁ TAREFAS NÃO INICIADAS')
                                    else:
                                        tarefas.menu_tarefas_nao_iniciadas()
                                        tarefas.mostra_tarefas(tarefasNaoIniciadas)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case "7":
                        while True:
                            gravacao = gravacaoTxt.menu_deseja_gravar_saida()
                            tarefasAtrasadas = tarefas.filtrar_tarefas_atrasadas(tarefasDB)
                            match gravacao:
                                case "1":
                                    limpa_a_tela()
                                    if tarefasAtrasadas == []:
                                        print('NÃO HÁ TAREFAS ATRASADAS')
                                        gravacaoTxt.gravar_saida_txt('NÃO HÁ TAREFAS ATRASADAS')
                                    else:
                                        gravacaoTxt.gravar_saida_txt(tarefas.string_mostra_tarefas(tarefasAtrasadas))
                                case "2":
                                    limpa_a_tela()
                                    if tarefasAtrasadas == []:
                                        print('NÃO HÁ TAREFAS ATRASADAS')
                                    else:
                                        tarefas.menu_tarefas_atrasadas()
                                        tarefas.mostra_tarefas(tarefasAtrasadas)
                                case _:
                                    print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE!")
                                    continue
                            break
                        continue
                    case "8":
                        tarefas.insere_plano_para_complitude(tarefasDB)
                        continue
                    case "0":
                        break;
                    case _:
                        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
                        continue

        case "0": # FINALIZAR O PROGRAMA
            break
        case _:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE\n')
            continue


        

