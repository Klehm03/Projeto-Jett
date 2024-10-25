# Professora: Kamylla Costa Abd El Jawad
# Disciplina: Programação de Aplicativos
# Integrantes: Isaque, Felipe de Lima, João, Vinicius Ângelo, Vinicius Chavier, Paulo Ricardo, Bruno e Gabriel Ramos


# Descrição: Nosso Programa é sobre uma Empresa que Gerencia os Funcionários da Empresa. Este programa utiliza ENCAPSULAMENTO, para que o salário não seja acessado diretamente.
# Gerente, Analista e Estagiario, são as subclasses desse programa, e implementamos o método calcular_salário em cada sublcasse. Usamos o POLIMORFISMO, para mostrar o salário final.

# Classe base para os Funcionários
class Funcionario:
    def __init__(self, nome, salario_base, cargo):
        self._nome = nome
        self._salario_base = salario_base  # Usando underscore para indicar que é um atributo protegido
        self._cargo = cargo

    def calcular_salario(self):
        return self._salario_base

# Subclasse para Gerentes
class Gerente(Funcionario):
    def calcular_salario(self):
        return self._salario_base * 1.2
    
# Subclasse para Analistas
class Analista(Funcionario):
    def calcular_salario(self):
        return self._salario_base * 1.1
    
# Subclasse para Estagiários
class Estagiario(Funcionario):
    pass  # Estagiários não têm aumento no salário

# Lista para armazenar os funcionários
funcionarios = []

# Função para exibir as informações dos Funcionários com base na quantidade e cargo escolhido
def exibir_funcionarios(quantidade, cargo=None):
    exibidos = 0
    for funcionario in funcionarios:
        if cargo and funcionario.cargo != cargo:
            continue  # Pula para o próximo funcionário se o cargo não corresponder
        print("-----------------------------------")
        print("Nome:", funcionario._nome)
        print("Cargo:", funcionario._cargo)
        print("Salário Base:", funcionario._salario_base)
        print("Salário Depois do Reajuste:", funcionario.calcular_salario())
        exibidos += 1
        if exibidos >= quantidade:
            break

# Função para adicionar um funcionário (pedido da sora)
def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    salario_base = float(input("Digite o salário base do funcionário: "))
    print("Escolha o cargo do funcionário:")
    print("1 - Gerente")
    print("2 - Analista")
    print("3 - Estagiário")
    cargo_escolhido = int(input("Escolha uma das opções: "))
    
    if cargo_escolhido == 1:
        cargo = "Gerente"
        funcionario = Gerente(nome, salario_base, cargo)
    elif cargo_escolhido == 2:
        cargo = "Analista"
        funcionario = Analista(nome, salario_base, cargo)
    elif cargo_escolhido == 3:
        cargo = "Estagiário"
        funcionario = Estagiario(nome, salario_base, cargo)
    else:
        print("Cargo inválido!")
        return
    
    funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!")

# Parte principal do programa onde tera escolhas, vai adicionar func, ou exibir os func, ou apenas sair do programa
while True:
    print("\nMenu:")
    print("1 - Adicionar Funcionário")
    print("2 - Exibir Funcionários")
    print("3 - Sair")
    escolha = int(input("Escolha uma das opções: "))
# Aqui vai fazer a parte das escolhas e tudo mais
    if escolha == 1:
        adicionar_funcionario()
    elif escolha == 2:
        quantidade = int(input("Quantos Funcionários você quer ver de uma vez? "))
        print("Quais cargos você quer ver?")
        print("1 - Gerentes")
        print("2 - Analistas")
        print("3 - Estagiários")
        print("4 - Todos os Cargos")
        cargo_escolhido = int(input("Escolha uma das opções: "))
        
        cargos = {1: "Gerente", 2: "Analista", 3: "Estagiário"}
        cargo = cargos.get(cargo_escolhido) if cargo_escolhido in cargos else None
        
        exibir_funcionarios(quantidade, cargo)
    elif escolha == 3:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")