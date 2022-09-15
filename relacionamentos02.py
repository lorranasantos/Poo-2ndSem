class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print('Nome do médico: ', self.medico.nome)
        print('CRM: ', self.medico.crm)
        print('Especialização: ', self.medico.especializacao)
        print('Nome do paciente: ', self.paciente.nome)
        print('CPF: ', self.paciente.cpf)
        print('Idade: ', self.paciente.idade)
        print('Exame: ', self.descricao)
        print('Resultado: ', self.resultado)

paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo')
exame01.imprimir_exame()        
        