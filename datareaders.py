

def get_txt_data(path):

    with open(path, 'r') as cnpjfile:
        cnpjs = cnpjfile.readlines()
        cnpjfile.close()

    return cnpjs