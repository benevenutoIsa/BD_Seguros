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
        char(11) cpf PK
        varchar nome
        date data_nascimento
        varchar telefone
        varchar email
        varchar endereco
    }
    
    Veiculo {
        char(11) renavam PK
        varchar placa
        varchar marca
        varchar modelo
        int ano
        varchar cor
        decimal valor_mercado
        char(11) cpf_cliente FK
    }
    
    Corretor {
        int id_corretor PK
        varchar nome
        varchar registro
        decimal comissao
        varchar telefone
    }
    
    Apolice {
        int numero_apolice PK
        date data_inicio
        date data_fim
        decimal valor_premio
        varchar status
        char(11) renavam_veiculo FK
        int id_corretor FK
    }
    
    Cobertura {
        int id_cobertura PK
        varchar tipo
        text descricao
        decimal valor_maximo
    }
    
    Sinistro {
        int id_sinistro PK
        date data_ocorrencia
        text descricao
        varchar local
        decimal valor_estimado
        int numero_apolice FK
    }
    
    Oficina {
        char(14) cnpj PK
        varchar nome
        varchar endereco
        varchar telefone
        varchar especialidade
    }
    
    Apolice_Cobertura {
        int numero_apolice FK
        int id_cobertura FK
        decimal valor_especifico
        decimal franquia
        decimal percentual_cobertura
        PK (numero_apolice, id_cobertura)
    }
    
    Sinistro_Oficina {
        int id_sinistro FK
        char(14) cnpj_oficina FK
        decimal valor_orcamento
        date data_entrada
        date data_prevista
        varchar status_reparo
        PK (id_sinistro, cnpj_oficina)
    }

```
