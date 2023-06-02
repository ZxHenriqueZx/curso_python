"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = int(input('Escolha a velocidade do carro: ')) # velocidade atual do carro
local_carro = int(input('Escolha o local do carro: '))  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_utrapassada = velocidade > RADAR_1
carro_passar_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and\
                local_carro <= (LOCAL_1 + RADAR_RANGE) and\
                velocidade_utrapassada

if velocidade_utrapassada:
    print('O carro passou da velocidade permitida!\nCuidado com o radar')
else:
    print('Seu carro esta na velocidade permitida!\nDiriga com cuidado')

if carro_passar_radar_1:
    print('O seu carro foi multado!!')