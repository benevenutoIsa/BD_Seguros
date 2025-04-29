from supabase import create_client, Client
import pandas as pd
import os

SUPABASE_URL = "..."
SUPABASE_KEY = "..."

def insert_data():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    tabelas = [
        ("clientes", "./data/clientes.csv"),
        ("corretores", "./data/corretores.csv"),
        ("veiculos", "./data/veiculos.csv"),
        ("apolices", "./data/apolices.csv"),
        ("coberturas", "./data/coberturas.csv"),
        ("oficinas", "./data/oficinas.csv"),
        ("sinistros", "./data/sinistros.csv"),
        ("apolice_cobertura", "./data/apolice_cobertura.csv"),
        ("sinistro_oficina", "./data/sinistro_oficina.csv"),
    ]

    for tabela, arquivo in tabelas:
        if not os.path.exists(arquivo):
            print(f"Arquivo {arquivo} não encontrado, pulando...")
            continue

        df = pd.read_csv(arquivo)
        records = df.to_dict(orient="records")

        for record in records:
            try:
                supabase.table(tabela).insert(record).execute()
            except Exception as e:
                print(f"Erro ao inserir em {tabela}: {e}")

if __name__ == "__main__":
    insert_data()
