import requests
import time
from datareaders import *
from datawriters import *
import json
from services import *

cnpjs = get_txt_data('cnpjs.txt')
cnpjs = clean_cnpj(cnpjs)
checkpoint = get_checkpoint(cnpjs)

cnpjs_count = len(checkpoint)
cnpjs_progress = 0
estimated_time = 0
for cnpj in checkpoint:

    cnpjs_progress = cnpjs_progress + 1
    estimated_time = int((cnpjs_count - cnpjs_progress)/3)
    print(f'Lendo o Cnpj número {cnpjs_progress} de {cnpjs_count} cnpjs.')
    print(f'Tempo estimado para termino: {estimated_time} minutos.')
    print('-------------------------------------------------------------------')
    print('-------------------------------------------------------------------')

    try:
        r = requests.get('https://www.receitaws.com.br/v1/cnpj/' + cnpj, timeout=15)
        resultado = r.json()
        atividade_principal = resultado.get('atividade_principal')

        if atividade_principal is None:
            atividade_principal = ["Ocorerram erros ao consultar esse cnpj"]

        acitivity_dict = {
                          "Cnpj": cnpj,
                          "Atividade Principal": resultado.get('atividade_principal')
                         }

        write_json(acitivity_dict, 'resultado.json')

        do_checkpoint(cnpj)
    except requests.ReadTimeout as e:
        print('Timeout')


    time.sleep(20)