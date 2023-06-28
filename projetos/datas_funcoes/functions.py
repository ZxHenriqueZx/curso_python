from datetime import datetime

def hoje():
    hoje = datetime.now()
    return hoje 

def verificar_data_user(data):
    try:
        data_format = datetime.strptime(data, '%d-%m-%Y')
        return data_format
    except:
        print('Formato inválido - exemplo: dd-mm-aaaa')
        exit()

def verificacao_val(data_usu):
    date_due = verificar_data_user(data=data_usu)
    if hoje() > date_due:
        return 'Fora da válidade!!!'
    else:
        return 'Dentro da válidade!!!'
    
