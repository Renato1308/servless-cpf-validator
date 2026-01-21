# servless-cpf-validator
# 🛡️ Microsserviço Serverless de Validação de CPF

## 📋 Sobre o Projeto
Este projeto consiste em um microsserviço desenvolvido em Python para validar CPFs de forma eficiente. Ele foi projetado para rodar em arquiteturas **Serverless** (FaaS), permitindo escalabilidade automática e baixíssimo custo.

## ⚙️ Funcionalidades
- Remoção automática de pontos e traços.
- Verificação de CPFs com dígitos repetidos.
- Cálculo matemático dos dígitos verificadores (Algoritmo da Receita Federal).
- Resposta em formato JSON (padrão para APIs).

## 🚀 Tecnologias
- **Python 3.10+**
- **Azure Functions** (Arquitetura sugerida)
- **Regex** (Processamento de strings)

## 🛠️ Exemplo de Uso
```python
resultado = validar_cpf("123.456.789-01")
# Retorno: False
