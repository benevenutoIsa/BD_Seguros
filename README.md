#### Isabella Benevenuto RA: 22.123.007-1
#### Mateus Marana       RA: 22.123.026-1
---

# 🏛️ Projeto: Sistema de Seguros de Veículos

Este projeto simula o ambiente de uma seguradora de veículos por meio de um banco de dados relacional completo. Ele foi desenvolvido com o objetivo de apoiar atividades de ensino e prática em:

- 📐 Modelagem de dados (MER e DDL)
- 🧬 Geração de dados fictícios com Python
- ✅ Validação de integridade e consistência dos dados
- 🔍 Execução e testes de queries SQL com Supabase (PostgreSQL) ou MySQL

A base contempla os principais elementos de um sistema de seguros de veículos:

- *Clientes*
- *Veículos*
- *Corretores*
- *Apólices de seguro*
- *Coberturas*
- *Sinistros*
- *Oficinas de reparo*

Todos os relacionamentos foram modelados de forma a refletir situações reais de uma seguradora, incluindo o controle de coberturas contratadas, acompanhamento de sinistros e gerenciamento financeiro de apólices.

---

## 🗂️ Estrutura do Projeto

```bash
/
├── data/
│   ├── clientes.csv
│   ├── corretores.csv
│   ├── veiculos.csv
│   ├── apolices.csv
│   ├── coberturas.csv
│   ├── oficinas.csv
│   ├── sinistros.csv
│   ├── apolice_cobertura.csv
│   └── sinistro_oficina.csv
│
├── first_task.py         # Geração de dados fictícios
├── second_task.py        # Validação de dados gerados
├── third_task.py         # Geração de comandos SQL e inserção no Supabase
├── insert_data.sql       # Arquivo SQL gerado para inserção de dados
├── README.md             # (este arquivo)
└── requirements.txt      # (bibliotecas necessárias)
```

---

## ⚙️ Como Executar o Projeto

### 1. Preparação do ambiente

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deve conter:

```
pandas
supabase
```
> **Observação:** Caso esteja usando Supabase, você precisa configurar a URL e a API KEY corretamente no `third_task.py`.

---

### 2. Gerar dados fictícios

Execute o script que gera os dados:

```bash
python first_task.py
```

- Isso irá criar arquivos `.csv` contendo os dados no diretório `data/`.

---

### 3. Validar os dados

Execute o script de validação para garantir que os dados gerados são consistentes:

```bash
python second_task.py
```

- O script irá informar no terminal se encontrou algum erro.

---

### 4. Gerar comandos SQL e inserir no Supabase

Gere o arquivo `insert_data.sql` e insira automaticamente os dados na sua instância Supabase:

```bash
python third_task.py
```

- Este script cria os comandos `INSERT INTO` e executa diretamente no banco.
- Para que funcione, certifique-se de que a tabela no Supabase já foi criada com o modelo correto.

---

## 🚀 Considerações Finais

Este projeto foi idealizado para demonstrar a construção de bases de dados completas, integrando:

- Modelagem de dados prática
- Geração e validação de grandes volumes de dados
- Integração com plataformas modernas (como o Supabase)
- Práticas SQL avançadas

Contribuições e melhorias são sempre bem-vindas! 💬

---

```mermaid
erDiagram
    Cliente ||--o{ Veiculo : possui
    Veiculo ||--o{ Apolice : possui
    Corretor ||--o{ Apolice : gerencia
    Apolice ||--o{ Sinistro : gera
    Apolice ||--o{ Apolice_Cobertura : contem
    Cobertura ||--o{ Apolice_Cobertura : pertence
    Sinistro ||--o{ Sinistro_Oficina : acontece_em
    Oficina ||--o{ Sinistro_Oficina : realiza_reparo

    Cliente {
        varchar cpf
        varchar nome
        date data_nascimento
        varchar telefone
        varchar email
        varchar endereco
    }
    
    Veiculo {
        varchar renavam
        varchar placa
        varchar marca
        varchar modelo
        int ano
        varchar cor
        decimal valor_mercado
        varchar cpf_cliente
    }
    
    Corretor {
        int id_corretor
        varchar nome
        varchar registro
        decimal comissao
        varchar telefone
    }
    
    Apolice {
        int numero_apolice
        date data_inicio
        date data_fim
        decimal valor_premio
        varchar status
        varchar renavam_veiculo
        int id_corretor
    }
    
    Cobertura {
        int id_cobertura
        varchar tipo
        text descricao
        decimal valor_maximo
    }
    
    Sinistro {
        int id_sinistro
        date data_ocorrencia
        text descricao
        varchar local
        decimal valor_estimado
        int numero_apolice
    }
    
    Oficina {
        varchar cnpj
        varchar nome
        varchar endereco
        varchar telefone
        varchar especialidade
    }
    
    Apolice_Cobertura {
        int numero_apolice
        int id_cobertura
        decimal valor_especifico
        decimal franquia
        decimal percentual_cobertura
    }
    
    Sinistro_Oficina {
        int id_sinistro
        varchar cnpj_oficina
        decimal valor_orcamento
        date data_entrada
        date data_prevista
        varchar status_reparo
    }

```
