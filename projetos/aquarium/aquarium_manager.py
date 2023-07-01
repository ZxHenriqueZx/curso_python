import json 

arquivo_json = open("aquarium.json", encoding="utf8")
dados = json.load(arquivo_json)
marinhos = dados['data']

def verify_type(animal):
    if animal['type'] == 'fish':
        return True
    else:
        return False

#faz a mesma coisa que o filter, só que é uma generate function
#marinhos_fish = (peixe for peixe in marinhos if verify_type(peixe))

#faz a mesma coisa que marinhos_fish mas ele executa uma função lambda, 
#em vez da função verify_type declarada la em cima
#marinhos_fish_2 = list(filter(lambda animal: (animal['type'] == 'fish'), marinhos))

marinhos_fish = list(filter(verify_type, marinhos))
marinhos_fish_name = list(map(lambda animal: animal['name'], marinhos_fish))

def assing_fish_42(marinhos, fish_name, new_tank_number=42):
    def change_tank_number(animal):
        if animal['name'] in fish_name:
            animal['tank number'] = new_tank_number
        return animal
    return list(map(change_tank_number, marinhos))

new_aquarium = assing_fish_42(marinhos, marinhos_fish_name)

print(new_aquarium)
