import requests

r = requests.get('https://www.receitaws.com.br/v1/cnpj/' + '00000000')
resultado = r.json()


atividade_principal = resultado.get('atividade_principal')

if atividade_principal is None:
    atividade_principal = "Ocorerram erros ao consultar esse cnpj"

print(atividade_principal)