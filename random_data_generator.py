import random
import json


class GeneratorSales:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sale_data = self.load_sale_data()
        self.pv = None
        self.sale_date = None
        self.nsu = None
        self.rv_number = None
        self.amount = None
        self.discount = None
        self.net_amount = None
        self.modality = None
        self.means_payment = None
        self.terminal = None
        self.installment_quantity = None
        self.installment = None
        self.receive_date = None

    def load_sale_data(self):
        data_random = open(self.file_name)
        return json.load(data_random)

    def generate_row(self):
        self.pv = self.get_random_field('pvs')
        self.sale_date = self.get_random_field('data_venda')
        self.nsu = random.randrange(1000, 1000000)
        self.rv_number = random.randrange(1000, 1000000)
        self.amount = random.uniform(100, 1000).__round__(2)
        self.discount = random.uniform(1, 100).__round__(2)
        self.net_amount = (self.amount - self.discount).__round__(2)
        self.modality = self.get_random_field('modalidade')
        self.means_payment = self.get_random_field('meio_de_pagamento')
        self.terminal = self.get_random_field('maquininha')
        self.installment_quantity, self.installment = self.get_installments()
        self.receive_date = self.get_receive_date()

    def __str__(self):
        return f'{self.pv};{self.sale_date};{self.nsu};{self.rv_number};{self.amount};{self.discount};{self.net_amount};' \
               f'{self.modality};{self.means_payment};{self.terminal};{self.installment_quantity};{self.installment};{self.receive_date}\n'

    def get_random_field(self, field):
        index = random.randrange(0, len(self.sale_data[field]))
        return self.sale_data[field][index]

    def get_receive_date(self):
        sale_date = str(self.sale_date)
        dd, mm, yyyy = sale_date[6:8], sale_date[4:6], sale_date[0:4]
        if self.modality == 'C':
            mm = int(mm) + 1
            return f'{yyyy}0{mm}{dd}'
        else:
            dd = int(dd) + 1
            return f'{yyyy}{mm}0{dd}'

    def get_installments(self):
        if self.modality == 'C':
            installment_quantity = random.randrange(1, 10)
            return installment_quantity, random.randrange(1, installment_quantity + 1)
        else:
            return 1, 1


generator = GeneratorSales('data_base_random.json')
reports = open('relatorio-gerado.csv', 'w')
reports.write('pv;data_venda;nsu;rv_number;valor_bruto;desconto;valor_liquido;modalidade;meio_de_pagamento'
                ';maquininha;quantidade_parcelas;parcela;data_recebimento\n')
for x in range(100):
    generator.generate_row()
    reports.write(generator.__str__())
    print(generator)
