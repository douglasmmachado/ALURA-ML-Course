class FirstClass:
    def __init__(self, var_name='', var_surname=''):
        print('Classe iniciada')
        if ' ' in var_name and var_surname == '':
            self.name = str.split(var_name, ' ')[0]
            self.surname = str.split(var_name, ' ')[1]
        else:
            self.name = var_name
            self.surname = var_surname


#x = FirstClass('Douglas', 'Machado')
x = FirstClass('Carmen Lúcia', 'Rezende Mateus')
print(f'Nome: {x.name}, Sobrenome: {x.surname}')






