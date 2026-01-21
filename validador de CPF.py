import re

def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)

    # Verifica se tem 11 dígitos ou se todos os dígitos são iguais (ex: 111.111...)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito_1 = resto if resto < 10 else 0

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito_2 = resto if resto < 10 else 0

    return cpf[-2:] == f"{digito_1}{digito_2}"

# Simulação de gatilho HTTP (Como seria no Azure Functions)
def main(requisicao_cpf):
    if validar_cpf(requisicao_cpf):
        return {"status": 200, "mensagem": "CPF Válido"}
    else:
        return {"status": 400, "mensagem": "CPF Inválido"}

# Teste rápido
print(main("12345678909")) # Exemplo