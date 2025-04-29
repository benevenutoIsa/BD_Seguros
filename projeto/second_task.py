import pandas as pd
import os

def validate_data_seguro():
    data_files = [
        "clientes.csv", "corretores.csv", "veiculos.csv", "apolices.csv",
        "coberturas.csv", "oficinas.csv", "sinistros.csv",
        "apolice_cobertura.csv", "sinistro_oficina.csv"
    ]

    missing_files = [f for f in data_files if not os.path.exists(f)]
    if missing_files:
        print(f"Erro: Os seguintes arquivos não foram encontrados: {missing_files}")
        return False

    df_clientes = pd.read_csv("clientes.csv")
    df_corretores = pd.read_csv("corretores.csv")
    df_veiculos = pd.read_csv("veiculos.csv")
    df_apolices = pd.read_csv("apolices.csv")
    df_coberturas = pd.read_csv("coberturas.csv")
    df_oficinas = pd.read_csv("oficinas.csv")
    df_sinistros = pd.read_csv("sinistros.csv")
    df_apolice_cobertura = pd.read_csv("apolice_cobertura.csv")
    df_sinistro_oficina = pd.read_csv("sinistro_oficina.csv")

    validations = []

    validations.append(("CPFs duplicados em clientes", df_clientes['cpf'].is_unique))
    validations.append(("Placas duplicadas em veículos", df_veiculos['placa'].is_unique))
    validations.append(("RENAVAM duplicado em veículos", df_veiculos['renavam'].is_unique))
    validations.append(("IDs de corretores únicos", df_corretores['id_corretor'].is_unique))
    validations.append(("Número de apólice único", df_apolices['numero_apolice'].is_unique))
    validations.append(("IDs de coberturas únicos", df_coberturas['id_cobertura'].is_unique))
    validations.append(("CNPJ de oficinas único", df_oficinas['cnpj'].is_unique))
    validations.append(("ID de sinistros único", df_sinistros['id_sinistro'].is_unique))
  
    validations.append(("Clientes válidos nos veículos", df_veiculos['cpf_cliente'].isin(df_clientes['cpf']).all()))
    validations.append(("Veículos válidos nas apólices", df_apolices['renavam_veiculo'].isin(df_veiculos['renavam']).all()))
    validations.append(("Corretores válidos nas apólices", df_apolices['id_corretor'].isin(df_corretores['id_corretor']).all()))
    validations.append(("Apólices válidas nos sinistros", df_sinistros['numero_apolice'].isin(df_apolices['numero_apolice']).all()))
    validations.append(("Apólices válidas em apolice_cobertura", df_apolice_cobertura['numero_apolice'].isin(df_apolices['numero_apolice']).all()))
    validations.append(("Coberturas válidas em apolice_cobertura", df_apolice_cobertura['id_cobertura'].isin(df_coberturas['id_cobertura']).all()))
    validations.append(("Sinistros válidos em sinistro_oficina", df_sinistro_oficina['id_sinistro'].isin(df_sinistros['id_sinistro']).all()))
    validations.append(("Oficinas válidas em sinistro_oficina", df_sinistro_oficina['cnpj_oficina'].isin(df_oficinas['cnpj']).all()))

    validations.append(("Percentual de cobertura entre 50 e 100", df_apolice_cobertura['percentual_cobertura'].between(50, 100).all()))
    validations.append(("Franquias positivas em apolice_cobertura", (df_apolice_cobertura['franquia'] > 0).all()))
    validations.append(("Valor estimado positivo nos sinistros", (df_sinistros['valor_estimado'] > 0).all()))
    validations.append(("Valor do prêmio positivo nas apólices", (df_apolices['valor_premio'] > 0).all()))

    all_ok = True
    for message, passed in validations:
        if not passed:
            print(f"ERRO: {message}")
            all_ok = False

    if all_ok:
        print("Todos os dados foram validados com sucesso.")
    else:
        print("Foram encontrados erros nos dados.")

    return all_ok

if __name__ == "__main__":
    validate_data_seguro()
