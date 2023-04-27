

class Patient:
    kind = 'canine'
    consultas = []

    def __init__(self, kind = '', name='', sex='', age=0):
        self.kind = str.upper(kind)
        self.name = str.upper(name)
        self.sex = str.upper(sex)
        self.age = age

    def add_consulta(self, consulta):
        self.consultas.append(consulta)


if __name__ == '__main__':
    d = Patient('Canine', 'Snoopy', 'Male', 2)
    a = Patient('Canine', 'Angus', 'Male', 15)
    p = Patient('Canine', 'Pretinha', 'Female', 5)
    patient_list = [d, a, p]
    a.add_consulta('04/12/2022')
    a.add_consulta('01/01/2023')
    a.add_consulta('15/01/2023')

    for patient in patient_list:
        if 'a' == str.lower(patient.name)[0]:
            print('='*30)
            print(f'Patient file: \n Kind: {patient.kind} \n Name: {patient.name} \n Age: {patient.age} \n Sex: {patient.sex} \n Consultas: {patient.consultas}' + '\n' +'='*30)