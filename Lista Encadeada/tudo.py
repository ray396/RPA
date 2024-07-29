class Paciente:
    def __init__(self, nome, motivo):
        self.nome = nome
        self.motivo = motivo
        self.proximo = None

class FilaDeEspera:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def registrar_paciente(self, nome, motivo):
        novo_paciente = Paciente(nome, motivo)
        if not self.primeiro:
            self.primeiro = novo_paciente
            self.ultimo = self.primeiro
        else:
            self.ultimo.proximo = novo_paciente
            self.ultimo = novo_paciente
    def chamar_proximo_paciente(self):
        if not self.primeiro:
            print("Não há pacientes na fila")
            return
        paciente_chamado = self.primeiro
        self.primeiro = self.primeiro.proximo
        print(f"Paciente {paciente_chamado.nome} foi chamado para o atendimento!")
    def listar_pacientes(self):
        temp = self.primeiro
        while temp:
            print(f"Nome: {temp.nome}, Motivo: {temp.motivo}")
            temp = temp.proximo
consultorio = FilaDeEspera()
consultorio.registrar_paciente("Joao", "Dor de cabeca")
consultorio.registrar_paciente("Ana", "Dor de barriga")
consultorio.registrar_paciente("Lucas", "Febre")
print("Pacientes na fila de espera:")
consultorio.listar_pacientes()
consultorio.chamar_proximo_paciente()
print("\n")
consultorio.chamar_proximo_paciente()
consultorio.chamar_proximo_paciente()
consultorio.chamar_proximo_paciente()