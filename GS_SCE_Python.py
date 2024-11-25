import os
import re
import random
import banco

usuarios = { "nome@gmail.com": "senha123", }

def efetuar_login_ou_cadastro():
    exibir_titulo()
    
    while True:
        try:
            print("1. Login")
            print("2. Cadastro")
            print("3. Entrar como visitante")
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == '1':
                while True:
                    try:
                        os.system('cls')
                        print('[Realizando Login]')
                        email = input("\nEmail: ")
                        
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                            raise ValueError("Email inválido. Favor inserir um email válido.")
                        
                        senha = input("Senha: ")
                        
                        if email in usuarios and usuarios[email] == senha:
                            entrar_no_menu_principal('Login realizado com sucesso!')
                            break
                        else:
                            os.system('cls')
                            print("Email ou senha inválidos.")
                            while True:
                                try:
                                    print("\n1. Tentar novamente \n2. Realizar cadastro")
                                    opcao = input('\nEscolha uma opção: ')
                                    if opcao == '1':
                                        break
                                    elif opcao == '2':
                                        main()
                                        break
                                    else:
                                        raise ValueError("Opção inválida. Favor digitar um número inteiro válido.")
                                except ValueError as erro:
                                    print(erro)
                    except ValueError as erro:
                        os.system('cls')
                        print(erro)
            
            elif opcao == '2':
                while True:
                    try:
                        os.system('cls')
                        print('[Realizando Cadastro]')
                        email = input("\nEmail: ")
                        
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                            raise ValueError("Email inválido. Favor inserir um email válido.")
                        
                        if email in usuarios:
                            print("Email já cadastrado.")
                            break
                        
                        senha = input("Senha: ")
                        usuarios[email] = senha
                        os.system('cls')
                        print("Cadastro realizado com sucesso!")
                        break
                    except ValueError as erro:
                        os.system('cls')
                        print(erro)
            
            elif opcao == '3':
                os.system('cls')
                entrar_no_menu_principal('Bem-vindo como visitante!')
                break
            
            else:
                print("Opção inválida.")
        
        except ValueError as erro:
            print(erro)
        except Exception as erro2:
            print(f"Ocorreu um erro inesperado: {erro2}")

def exibir_titulo():
    os.system('cls')
    print('='*40)
    print('  SAFE & CLEAN ENERGY'.center(40))
    print('='*40)

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def exibir_opcoes():
    os.system('cls')
    print('1. Integrantes')
    print('2. Listar Avaliações')
    print('3. Cadastrar Avaliação')
    print('4. Modificar Avaliação')
    print('5. Excluir Avaliação')
    print('6. Listar Clientes')
    print('7. Cadastrar Cliente')
    print('8. Modificar Cliente')
    print('9. Excluir Cliente')
    print('10. Listar Empresas')
    print('11. Cadastrar Empresa')
    print('12. Modificar Empresa')
    print('13. Excluir Empresa')
    print('14. Logout\n')

def escolher_opcoes():
    while True:
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if 1 <= opcao_escolhida <= 14:
                if opcao_escolhida == 1:
                    mostrar_integrantes()
                elif opcao_escolhida == 2:
                    listar_avaliacoes()
                elif opcao_escolhida == 3:
                    cadastrar_avaliacao()
                elif opcao_escolhida == 4:
                    modificar_avaliacao()
                elif opcao_escolhida == 5:
                    excluir_avaliacao()
                elif opcao_escolhida == 6:
                    listar_clientes()
                elif opcao_escolhida == 7:
                    cadastrar_cliente()
                elif opcao_escolhida == 8:
                    modificar_cliente()
                elif opcao_escolhida == 9:
                    excluir_cliente()
                elif opcao_escolhida == 10:
                    listar_empresas()
                elif opcao_escolhida == 11:
                    cadastrar_empresa()
                elif opcao_escolhida == 12:
                    modificar_empresa()
                elif opcao_escolhida == 13:
                    excluir_empresa()
                else:
                    finalizar_app()
                break
            else:
                print("\nOpção inválida. Por favor, escolha um número entre 1 e 14.")
        except ValueError:
            print("\nEntrada inválida. Por favor, digite um número inteiro.")

def gerar_id_unico(tabela: str) -> int:
    id_unico = 1  

    while True:
        if tabela == 'empresa' and not banco.buscar_empresa_by_id(id_unico):
            return id_unico  
        elif tabela == 'cliente' and not banco.buscar_cliente_by_id(id_unico):
            return id_unico  
        elif tabela == 'avaliacao' and not banco.buscar_avaliacao_by_id(id_unico):
            return id_unico 
        
        id_unico += 1 

def gerar_cnpj():

    cnpj = ''.join([str(random.randint(0, 9)) for _ in range(14)])
    
    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    
    return cnpj_formatado

def mostrar_integrantes():
    os.system('cls')  
    
    exibir_subtitulo(f"{'Integrantes do Grupo Safe & Clean Energy':^50}")
    print("=" * 50)
    
    integrantes = [
        ("Enzo Prado Soddano", "RM 557937"),
        ("Lucas Resende Lima", "RM 556564"),
        ("Vinicius Prates Altafini", "RM 559183")
    ]
    
    for nome, rm in integrantes:
        print(f"{nome:<30} | {rm:>8}")
    
    print("=" * 50)
    
    voltar_ao_menu_principal()


def listar_avaliacoes():
    exibir_subtitulo('Listando Avaliações')
    avaliacao = banco.listar_avaliacoes()
    if not avaliacao:
        print('Nenhuma avaliação encontrada ou ocorreu um erro ao buscar os dados.')
    else:
        print("="*120)
        print(f"{'ID':<10} | {'Avaliação':<20} | {'Comentário':<40}")
        print("="*120)
        for item in avaliacao:
            
            id_avaliacao = item[0] if item[0] is not None else "N/A"
            avaliacao_texto = item[2] if item[2] is not None else "N/A"
            comentario = item[3] if item[3] is not None else "N/A"
            
            print(f"{id_avaliacao:<10} | {avaliacao_texto:<20} | {comentario:<40}")
        print("="*120)
    voltar_ao_menu_principal()


def cadastrar_avaliacao():
    exibir_subtitulo('Cadastro de Avaliação')
    try:
        id_avaliacao = gerar_id_unico('avaliacao')
        id_cliente = input("Digite o ID do cliente: ")
        id_empresa = input("Digite o ID da empresa: ")
        nota = input("Digite a nota (1-10): ")
        comentario = input("Digite o comentário: ")

        cliente_existe = banco.buscar_cliente_by_id(id_cliente)
        if not cliente_existe:
            print("Erro: ID do cliente não encontrado.")
            return

        empresa_existe = banco.buscar_empresa_by_id(id_empresa)
        if not empresa_existe:
            print("Erro: ID da empresa não encontrado.")
            return

        dados_avaliacao = {
            'id_avaliacao': id_avaliacao,
            'id_cliente': id_cliente,
            'id_empresa': id_empresa,
            'nota': nota,
            'comentario': comentario  
        }

        banco.cadastrar_avaliacao(dados_avaliacao)
        print("\nAvaliação cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar avaliação: {e}")
    voltar_ao_menu_principal()

def modificar_avaliacao():
    os.system('cls')
    id_avaliacao = input("Digite o ID da avaliação que deseja modificar: ")
    avaliacao = banco.buscar_avaliacao_by_id(int(id_avaliacao))
    
    if not avaliacao:
        print(f"\nNenhuma avaliação encontrada com o ID {id_avaliacao}.")
        voltar_ao_menu_principal()

    
    print("\nDados atuais da avaliação:")
    print("=" * 40)  
    print(f"ID da Avaliação    : {avaliacao['id_avaliacao']}")
    print(f"ID do Cliente      : {avaliacao['id_cliente']}")
    print(f"ID da Empresa      : {avaliacao['id_empresa']}")
    print(f"Nota Atual         : {avaliacao['nota']}")
    print(f"Comentário Atual   : {avaliacao['comentario']}")
    print("=" * 40) 

    nova_nota = input("\nDigite a nova nota (deixe em branco para manter a atual): ")
    if nova_nota.strip() != "":
        avaliacao['nota'] = nova_nota

    novo_comentario = input("Digite o novo comentário (deixe em branco para manter o atual): ")
    if novo_comentario.strip() != "":
        avaliacao['comentario'] = novo_comentario

    banco.modificar_avaliacao(avaliacao)

    print("\nA avaliação foi modificada com sucesso!")
    voltar_ao_menu_principal()

def excluir_avaliacao():
    exibir_subtitulo('Excluindo Avaliação')
    id_avaliacao = input("Digite o ID da avaliação que deseja excluir: ")
    avaliacao = banco.buscar_avaliacao_by_id(int(id_avaliacao))
    
    if not avaliacao:
        print(f"\nNenhuma avaliação encontrada com o ID {id_avaliacao}.")
        voltar_ao_menu_principal()

    confirmacao = input(f"\nTem certeza que deseja excluir a avaliação? (s/n): ").lower()
    if confirmacao == 's':
        banco.excluir_avaliacao(int(id_avaliacao))
        print(f"\nA avaliação foi excluída com sucesso.")
    else:
        print("\nA exclusão foi cancelada.")
    voltar_ao_menu_principal()

def listar_clientes():
    exibir_subtitulo('Listando Clientes')
    clientes = banco.listar_clientes()
    
    if not clientes:
        print("\nNenhum cliente encontrado.")
    else:
        
        print("\nLista de Clientes:")
        print("=" * 80)  
        print(f"{'ID':<10} | {'Nome':<30} | {'Email':<30}")  
        print("=" * 80)  

        
        for cliente in clientes:
            print(f"{cliente[0]:<10} | {cliente[1]:<30} | {cliente[2]:<30}")  

        print("=" * 80)  

    voltar_ao_menu_principal()

def cadastrar_cliente():
    exibir_subtitulo('Cadastro de Cliente')
    try:
        nome_cliente = input("Nome do cliente: ")
        email_cliente = input("Email do cliente: ")
        
        id_cliente = gerar_id_unico('cliente')

        dados_cliente = {
            'id_cliente': id_cliente,  
            'nome': nome_cliente,
            'email': email_cliente,
            'genero': input("Gênero do cliente: ")
        }

        banco.cadastrar_cliente(dados_cliente)  
        print("Cliente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")
    voltar_ao_menu_principal()

def modificar_cliente():
    exibir_subtitulo('Modificar Cliente')
    id_cliente = input("Digite o ID do cliente que deseja modificar: ")
    cliente = banco.buscar_cliente_by_id(int(id_cliente))

    if not cliente:
        print(f"\nNenhum cliente encontrado com o ID {id_cliente}.")
        voltar_ao_menu_principal()

    
    print("\nDados atuais do cliente:")
    print("=" * 70)
    print(f"{'ID':<10} | {'Nome':<30} | {'Email':<30}")
    print("=" * 70)
    print(f"{cliente['id_cliente']:<10} | {cliente['nome']:<30} | {cliente['email']:<30}")
    print("=" * 70)

    
    nome_cliente = input(f"\nNome atual: {cliente['nome']}. Novo nome (deixe em branco para manter o atual): ")
    email_cliente = input(f"Email atual: {cliente['email']}. Novo email (deixe em branco para manter o atual): ")

    if nome_cliente.strip() != "":
        cliente['nome'] = nome_cliente
    if email_cliente.strip() != "":
        cliente['email'] = email_cliente

    banco.modificar_cliente(cliente)
    print(f"\nCliente atualizado com sucesso!")
    voltar_ao_menu_principal()

def excluir_cliente():
    exibir_subtitulo('Excluir Cliente')
    id_cliente = input("Digite o ID do cliente que deseja excluir: ")
    cliente = banco.buscar_cliente_by_id(int(id_cliente))

    if not cliente:
        print(f"\nNenhum cliente encontrado com o ID {id_cliente}.")
        voltar_ao_menu_principal()

    confirmacao = input(f"\nTem certeza que deseja excluir o cliente? (s/n): ").lower()
    if confirmacao == 's':
        banco.excluir_cliente(int(id_cliente))
        print(f"\nCliente excluído com sucesso.")
    else:
        print("\nA exclusão foi cancelada.")
    voltar_ao_menu_principal()

def listar_empresas():
    exibir_subtitulo('Listando Empresas')
    empresas = banco.listar_empresas()
    
    if not empresas:
        print("\nNenhuma empresa encontrada.")
    else:
        
        print("\nLista de Empresas:")
        print("=" * 110)  
        print(f"{'ID':<10} | {'Nome':<40} | {'Vantagens':<30}") 
        print("=" * 110)  

        for empresa in empresas:
            print(f"{empresa[0]:<10} | {empresa[1]:<40} | {empresa[3]:<30}") 

        print("=" * 110) 

    voltar_ao_menu_principal()


def cadastrar_empresa():
    exibir_subtitulo('Cadastro de Empresa')
    try:
        id_empresa = gerar_id_unico('empresa')
        nome = input("Digite o nome da empresa: ")
        cnpj = gerar_cnpj()  
        vantagens = input("Digite as vantagens da empresa: ")

        if not nome or not vantagens:
            raise ValueError("Todos os campos são obrigatórios!")

        dados_empresa = {
            'id_empresa': id_empresa,
            'nome': nome,
            'cnpj': cnpj,
            'vantagens': vantagens
        }

        banco.cadastrar_empresa(dados_empresa)
        print("Empresa cadastrada com sucesso!")

    except Exception as e:
        print(f"Erro ao cadastrar empresa: {e}")
    voltar_ao_menu_principal()

def modificar_empresa():
    exibir_subtitulo('Modificar Empresa')
    id_empresa = input("Digite o ID da empresa que deseja modificar: ")
    empresa = banco.buscar_empresa_by_id(int(id_empresa))

    if not empresa:
        print(f"\nNenhuma empresa encontrada com o ID {id_empresa}.")
        voltar_ao_menu_principal()

    
    print(f"\nDados atuais da empresa:")
    print("=" * 110)
    print(f"{'ID':<10} | {'Nome':<40} | {'Vantagens':<30}")
    print("=" * 110)
    print(f"{empresa['id_empresa']:<10} | {empresa['nome']:<40} | {empresa['vantagens']:<30}")
    print("=" * 110)

    
    nome_empresa = input(f"Nome atual: {empresa['nome']}. Novo nome (deixe em branco para manter o atual): ")
    vantagens_empresa = input(f"Vantagens atuais: {empresa['vantagens']}. Novas vantagens (deixe em branco para manter as atuais): ")

    if nome_empresa.strip() != "":
        empresa['nome'] = nome_empresa
    if vantagens_empresa.strip() != "":
        empresa['vantagens'] = vantagens_empresa

    banco.modificar_empresa(empresa)
    print(f"\nEmpresa atualizada com sucesso!")
    voltar_ao_menu_principal()

def excluir_empresa():
    exibir_subtitulo('Excluir Empresa')
    id_empresa = input("Digite o ID da empresa que deseja excluir: ")
    empresa = banco.buscar_empresa_by_id(int(id_empresa))

    if not empresa:
        print(f"\nNenhuma empresa encontrada com o ID {id_empresa}.")
        voltar_ao_menu_principal()
        return

    confirmacao = input(f"\nTem certeza que deseja excluir a empresa? (s/n): ").lower()
    if confirmacao == 's':
        try:
            banco.excluir_empresa(int(id_empresa))
            print(f"\nEmpresa excluída com sucesso.")
        except Exception as e:
            
            if 'ORA-02292' in str(e):
                os.system('cls')
                print("=" * 67)
                print("Não é possível excluir uma entidade referenciada em outras tabelas!")
                print("=" * 67)
            else:
                print(f"\nOcorreu um erro inesperado: {e}")
    else:
        print("\nA exclusão foi cancelada.")
    
    voltar_ao_menu_principal()

import os

def finalizar_app():
    os.system('cls') 
    
    
    print("="*60)
    print(f"{'Bem-vindo!':^60}")
    print(f"{'Você está logado com sucesso!':^60}")
    print("="*60)

    while True:
        try:
            
            print(f"{'O que você gostaria de fazer? ':^60}")
            print("="*60)
            print("1. Voltar ao menu principal")
            print("2. Encerrar o programa")
            print("="*60)
            
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                print("\nVoltando ao menu principal...\n")
                main() 
                break
            elif opcao == '2':
                print("\nEncerrando o programa... Até logo!")
                exit()  
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")
        except ValueError as erro:
            print(f"\nErro de valor: {erro}")
        except Exception as erro2:
            print(f"\nOcorreu um erro inesperado: {erro2}")

    print("="*60)

def entrar_no_menu_principal(mensagem=None):
    if mensagem:
        print(f"\n{mensagem}")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

def voltar_ao_menu_principal():
    input("\nPressione Enter para voltar ao menu principal...")
    main2()

def exibir_nome_do_programa():
    os.system('cls')
    print("Safe & Clean Energy")
    print("=" * 40)

def main():
    os.system('cls')
    efetuar_login_ou_cadastro()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

def main2():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()