import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf: str) -> bool:
    # return len(cpf) != 11
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome: str) -> bool:
    return not nome.isalpha()

def celular_invalido(celular: str) -> bool:
    # return len(celular) != 13
    modelo = "[0-9]{2} [0-9]{5}-[0-9]{4}"
    resposta = re.findall(modelo, celular)
    return not resposta
