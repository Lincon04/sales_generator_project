import json
import random
from datetime import datetime, timedelta

def generate_random_data(id):
    base_date = datetime(2024, 8, 1)

    base_date = datetime(2024, 8, 1)

    # Gera uma data base
    base_datetime = base_date + timedelta(days=id)

    # Gera horas, minutos e segundos aleatórios
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)

    # Cria data e hora aleatória
    data_recebimento = base_datetime.replace(hour=hours, minute=minutes, second=seconds).isoformat()
    data_venda = (base_datetime - timedelta(days=5)).replace(hour=hours, minute=minutes, second=seconds).isoformat()

    return {
        "data_recebimento": data_recebimento,
        "data_venda": data_venda,
        "meio_de_pagamento": random.randint(1, 3),
        "nsu": random.randint(100000000, 999999999),
        "parcela": random.randint(1, 5),
        "pv": random.randint(100, 110),
        "quantidade_parcelas": random.randint(1, 6),
        "rv_number": random.randint(100000000, 999999999),
        "bandeira": random.choice(["Master", "Visa", "Alelo", "Hipercar", "elo"]),
        "modalidade": random.choice(["Crédito", "Débito", "Voucher"]),
        "status": random.choice(["Aprovado", "Cancelado"]),
        "status_type": random.choice(["Completo", "Parcial", "Pago"]),
        "terminal": f"Term{random.randint(1, 10)}",
        "valor_bruto": round(random.uniform(100, 1000), 2),
        "desconto": round(random.uniform(0, 50), 2),
        "valor_liquido": round(random.uniform(50, 950), 2)
    }

def create_bulk_request_data(num_records):
    bulk_data = ""
    for i in range(1, num_records + 1):
        action = {
            "index": { "_index": "sales-v1" }
        }
        data = generate_random_data(i)
        bulk_data += json.dumps(action) + "\n" + json.dumps(data) + "\n"
    return bulk_data

def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

if __name__ == "__main__":
    num_records = 2  # Defina aqui a quantidade de dados a serem gerados
    bulk_data = create_bulk_request_data(num_records)
    save_to_file('../temp/bulk.txt', bulk_data)
    print(f"Dados gerados e salvos em 'bulk_data.txt'.")
