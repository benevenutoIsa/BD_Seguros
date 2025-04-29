import random
import string
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os

random.seed(42)
np.random.seed(42)

def generate_fake_data_seguro():
    def generate_name():
        nomes = ["João", "Maria", "Pedro", "Ana", "Carlos", "Juliana", "Lucas", "Beatriz",
                 "Marcos", "Fernanda", "Rafael", "Gabriela", "Luiz", "Camila", "André",
                 "Patrícia", "Ricardo", "Daniela", "Gustavo", "Mariana"]
        sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Pereira", "Costa", "Rodrigues",
                      "Almeida", "Nascimento", "Carvalho", "Gomes", "Martins", "Araújo", "Moreira",
                      "Ribeiro", "Ferreira", "Barbosa", "Cardoso", "Mendes"]
        return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

    def generate_email(nome):
        nomes = nome.lower().split()
        base = f"{nomes[0]}.{nomes[-1]}"
        dominios = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]
        return f"{base}@{random.choice(dominios)}"

    def generate_phone():
        ddd = random.choice(["11", "21", "31", "41", "51", "61", "71", "81", "91"])
        num = ''.join(random.choice(string.digits) for _ in range(9))
        return f"({ddd}) {num[:5]}-{num[5:]}"

    def generate_cpf():
        return ''.join(random.choices(string.digits, k=11))

    def generate_renavam():
        return ''.join(random.choices(string.digits, k=11))

    def generate_plate():
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=4))
        return f"{letters}-{numbers}"

    def generate_cnpj():
        return ''.join(random.choices(string.digits, k=14))

    def generate_random_date(start_year=2020, end_year=2024):
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')
