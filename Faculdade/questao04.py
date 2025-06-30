boasVindas = 'Bem Vindo a Empresa de Matheus Miari'
menuTitulo = 'MENU PRINCIPAL'
print(f'{boasVindas:-^50}')
print('-'*50)

lista_funcionarios = []
id_global = 5113146

def cadastrar_funcionarios(id):
    print(f'Id: {id}')
    nome = input('Nome do funcionário: ')
    setor = input('Setor do funcionário: ')
    salario = float(input('Salário do funcionário: R$'))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    lista_funcionarios.append(funcionario.copy())
    print('Funcionário cadastrado com sucesso ! \n')

def consultar_funcionarios():
    print('''
    1 - Consultar todos
    2 - Consultar por Id
    3 - Consultar por Setor
    4 - Retornar ao menu
    ''')
    op = input('Escolha uma opção: ')
    if op == '1':
        print(f"{'=' * 20} FUNCIONÁRIOS CADASTRADOS {'=' * 20}")
        for func in lista_funcionarios:
            print(f'ID: {func["id"]}')
            print(f'Nome: {func["nome"]}')
            print(f'Setor: {func["setor"]}')
            print(f'Salário: R${func["salario"]:.2f}')
            print('-' * 50)
    elif op == '2':
        id_consulta = int(input('Digite o ID do funcionário: '))
        encontrado = False
        for func in lista_funcionarios:
            if func['id'] == id_consulta:
                print(f'ID: {func["id"]}')
                print(f'Nome: {func["nome"]}')
                print(f'Setor: {func["setor"]}')
                print(f'Salário: R${func["salario"]:.2f}')
                print('-' * 50)
                encontrado = True
        if not encontrado:
            print(f'O id: {id_consulta} nao foi encontrado. \n')
    elif op == '3':
        setor = input('Digite o setor: ')
        encontrados = [func for func in lista_funcionarios if func ['setor'].lower() == setor.lower()]
        if encontrados:
            for func in encontrados:
                print(f'ID: {func["id"]}')
                print(f'Nome: {func["nome"]}')
                print(f'Setor: {func["setor"]}')
                print(f'Salário: R${func["salario"]:.2f}')
                print('-' * 50)
        else:
            print('Nenhum funcionario neste setor. ')
    elif op == '4':
        return
    else:
        print('Opção invalida. Tente Novamente. ')



def remover_funcionario():
    while True:
        try:
            id_remove = int(input('Id do funcionário:'))
            for func in lista_funcionarios:
                if func['id'] == id_remove:
                    lista_funcionarios.remove(func)
                    print(f'Funcinario com o id {id_remove} foi removido com sucesso. ')
                    return
            print('Id Invalido. ')
        except ValueError:
            print('Id Invalido.')

# Código principal
print(f'{menuTitulo:-^50}')
while True:
    menu = input('''
MENU PRINCIPAL
1 - Cadastrar Funcionários
2 - Consultar Funcionário(s)
3 - Remover Funcionário
4 - Sair

Escolha uma opção: ''')
    if menu == '1':
        cadastrar_funcionarios(id_global)
        id_global += 1
    elif menu == '2':
        consultar_funcionarios()
    elif menu == '3':
        remover_funcionario()
    elif menu == '4':
        print('Programa encerrado. ')
        break
    else:
        print('Opcao invalida. Tente novamente. \n')
