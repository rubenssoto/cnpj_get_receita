from datareaders import *
from datawriters import *
import os

def do_checkpoint(cnpj):
    write_txt(cnpj, 'checkpoint.txt')

def get_checkpoint(cnpjs_list):

    resultado = []

    if os.path.exists('checkpoint.txt'):
        checkpoint = clean_cnpj(get_txt_data('checkpoint.txt'))


        for cnpj in cnpjs_list:
            if cnpj not in checkpoint:
                resultado.append(cnpj)

    if len(resultado) == 0:
        resultado = cnpjs_list

    return resultado


def clean_cnpj(cnpjs_list):
    resultado = []

    for cnpj in cnpjs_list:
        resultado.append(cnpj.replace('\n', ''))

    return resultado





