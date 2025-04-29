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

    clientes = []
    for i in range(50):
        nome = generate_name()
        clientes.append({
            "cpf": generate_cpf(),
            "nome": nome,
            "data_nascimento": generate_random_date(1960, 2005),
            "telefone": generate_phone(),
            "email": generate_email(nome),
            "endereco": f"Rua {random.choice(string.ascii_uppercase)}{random.randint(1, 999)}, Bairro {random.choice(string.ascii_uppercase)}"
        })
    
    corretores = []
    for i in range(10):
        nome = generate_name()
        corretores.append({
            "id_corretor": i + 1,
            "nome": nome,
            "registro": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            "comissao": round(random.uniform(5, 20), 2),
            "telefone": generate_phone()
        })

    veiculos = []
    for cliente in clientes:
        for _ in range(random.randint(1, 3)):
            veiculos.append({
                "renavam": generate_renavam(),
                "placa": generate_plate(),
                "marca": random.choice(["Toyota", "Ford", "Fiat", "Honda", "Chevrolet"]),
                "modelo": random.choice(["Civic", "Corolla", "Onix", "Ka", "Strada"]),
                "ano": random.randint(2000, 2024),
                "cor": random.choice(["Preto", "Branco", "Prata", "Vermelho", "Azul"]),
                "valor_mercado": round(random.uniform(20000, 150000), 2),
                "cpf_cliente": cliente["cpf"]
            })

    apolices = []
    for i in range(150):
        veiculo = random.choice(veiculos)
        corretor = random.choice(corretores)
        inicio = datetime.strptime(generate_random_date(2021, 2023), '%Y-%m-%d')
        fim = inicio + timedelta(days=365)
        apolices.append({
            "numero_apolice": i + 1,
            "data_inicio": inicio.strftime('%Y-%m-%d'),
            "data_fim": fim.strftime('%Y-%m-%d'),
            "valor_premio": round(random.uniform(1000, 5000), 2),
            "status": random.choice(["Ativa", "Cancelada", "Renovada"]),
            "renavam_veiculo": veiculo["renavam"],
            "id_corretor": corretor["id_corretor"]
        })

    coberturas = []
    tipos_cobertura = ["Roubo", "Colisão", "Incêndio", "Terceiros", "Fenômenos naturais", "Vidros", "Assistência 24h", "Carro reserva"]
    for i, tipo in enumerate(tipos_cobertura):
        coberturas.append({
            "id_cobertura": i + 1,
            "tipo": tipo,
            "descricao": f"Proteção contra {tipo.lower()}",
            "valor_maximo": round(random.uniform(5000, 100000), 2)
        })

    oficinas = []
    for i in range(20):
        oficinas.append({
            "cnpj": generate_cnpj(),
            "nome": f"Oficina {generate_name()}",
            "endereco": f"Avenida {random.choice(string.ascii_uppercase)}{random.randint(1, 999)}, Setor {random.choice(string.ascii_uppercase)}",
            "telefone": generate_phone(),
            "especialidade": random.choice(["Mecânica", "Funilaria", "Elétrica", "Pintura"])
        })

    sinistros = []
    for i in range(100):
        apolice = random.choice(apolices)
        sinistros.append({
            "id_sinistro": i + 1,
            "data_ocorrencia": generate_random_date(2022, 2024),
            "descricao": random.choice(["Colisão frontal", "Roubo total", "Danos por enchente", "Incêndio no motor"]),
            "local": random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]),
            "valor_estimado": round(random.uniform(2000, 80000), 2),
            "numero_apolice": apolice["numero_apolice"]
        })
