# Desenvolva todas as suas classes aqui

from traceback import print_tb

import pytest

def create_tile(title):
        arr = title.title().split(' ')
        arr = list(filter(None, arr))
        for i in arr:
            str(filter(" ", i))
        fixed = ''
        for i in arr:
           fixed += i + " "
        fixed = fixed[:-1]
        return fixed.title()


class Funcionario:
   funcao = "Funcionário"
   
   def __init__(self, nome: str, sobrenome: str, cpf, salario = 3000) -> None:
       self.nome = nome.strip().capitalize()
       self.sobrenome = create_tile(sobrenome)
       self.cpf = str(cpf)
       self.salario = int(salario)
       self.nome_completo = self.nome+ " " + self.sobrenome


   def __str__(self) -> str:
       return f"<Funcionario: {self.nome_completo}>"
   def __repr__(self) -> str:
       return f"<Funcionario: {self.nome_completo}>"

class Gerente(Funcionario):
    funcao = "Gerente"

    def __init__(self, nome: str, sobrenome: str, cpf, salario=8000) -> None:
        super().__init__(nome, sobrenome, cpf)
        self.funcionarios = []
        self.salario = int(salario)
        self.nome_completo = self.nome + " " + self.sobrenome


    def aumento_salarial(self, funcionario, empresa):
        if isinstance(funcionario, Funcionario) == False or funcionario not in self.funcionarios:
            return False
        added_salary = (10 * funcionario.salario) / 100.0
        new_sallary = int(funcionario.salario) + int(added_salary)
        funcionario.salario = new_sallary
        if new_sallary >= 8000:
            Empresa.promocao(empresa, funcionario)
        return True




    def __str__(self) -> str:
       return f"<Gerente: {self.nome_completo}>"
    def __repr__(self) -> str:
       return f"<Gerente: {self.nome_completo}>"


class Empresa:
    todas_empresas = []

    def __init__(self, nome: str, cnpj) -> None:
        self.nome = create_tile(nome)
        self.cnpj = str(cnpj)
        self.contratados = []
        Empresa.todas_empresas.append(self)


    def create_email(self, nome):
        fixed_name = nome.replace(" ", ".")
        fixed_company_name = self.nome.replace(" ", '')
        return f"{fixed_name.lower()}@{str(fixed_company_name.lower())}.com"

    def contratar_funcionario(self, funcionario: Funcionario):
        for func in self.contratados:
            if func.cpf == funcionario.cpf:
                return "Funcionário com esse CPF já foi contratado."
        self.contratados.append(funcionario)
        funcionario.email = self.create_email(funcionario.nome_completo)
        return "Funcionário contratado!"
        
    def demissao(self, funcionario):
            if isinstance(funcionario,Gerente):
                self.contratados.remove(funcionario)
                return "Gerente demitido!"
            elif isinstance(funcionario, Funcionario):
                self.contratados.remove(funcionario)
                for i in self.contratados:
                    if isinstance(i, Gerente):
                        if funcionario in i.funcionarios:
                            i.funcionarios.remove(funcionario)
                return "Funcionário demitido!"
            
            else:
                return False
            
    @staticmethod
    def adicionar_funcionario_para_gerente(gerente: Gerente, funcionario: Funcionario):
        if isinstance(gerente, Gerente) == False or isinstance(funcionario, Gerente) == True:
            return False
        elif funcionario in gerente.funcionarios:
            return 'Funcionario já está na lista de funcionarios desse gerente.'
        else:
            gerente.funcionarios.append(funcionario)
            return 'Funcionário adicionado à lista do gerente!'

    
    @staticmethod
    def promocao(empresa, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) == False or funcionario not in empresa.contratados or isinstance(funcionario, Gerente):
            return False
        empresa.contratados.remove(funcionario)
        if funcionario.salario > 8000:
            promoved_employ = Gerente(funcionario.nome, funcionario.sobrenome, funcionario.cpf, funcionario.salario)
        else:
            promoved_employ = Gerente(funcionario.nome, funcionario.sobrenome, funcionario.cpf)
        empresa.contratar_funcionario(promoved_employ)
        return True

    def __str__(self) -> str:
       return str(f"<Empresa: {self.nome}>")
    def __repr__(self) -> str:
       return str(f"<Empresa: {self.nome}>")    


