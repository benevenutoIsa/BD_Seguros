-- Tabela Cliente
CREATE TABLE clientes (
    cpf CHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100),
    endereco VARCHAR(200)
);

-- Tabela Corretor
CREATE TABLE corretores (
    id_corretor INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    registro VARCHAR(20) NOT NULL,
    comissao DECIMAL(5,2),
    telefone VARCHAR(15)
);

-- Tabela Veículo
CREATE TABLE veiculos (
    renavam CHAR(11) PRIMARY KEY,
    placa VARCHAR(10) NOT NULL,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    cor VARCHAR(30),
    valor_mercado DECIMAL(12,2),
    cpf_cliente CHAR(11) NOT NULL,
    FOREIGN KEY (cpf_cliente) REFERENCES clientes(cpf)
);

-- Tabela Apólice
CREATE TABLE apolices (
    numero_apolice INT PRIMARY KEY,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    valor_premio DECIMAL(12,2) NOT NULL,
    status VARCHAR(20),
    renavam_veiculo CHAR(11) NOT NULL,
    id_corretor INT NOT NULL,
    FOREIGN KEY (renavam_veiculo) REFERENCES veiculos(renavam),
    FOREIGN KEY (id_corretor) REFERENCES corretores(id_corretor)
);

-- Tabela Cobertura
CREATE TABLE coberturas (
    id_cobertura INT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    descricao TEXT,
    valor_maximo DECIMAL(12,2)
);

-- Tabela Oficina
CREATE TABLE oficinas (
    cnpj CHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(200),
    telefone VARCHAR(15),
    especialidade VARCHAR(50)
);

-- Tabela Sinistro
CREATE TABLE sinistros (
    id_sinistro INT PRIMARY KEY,
    data_ocorrencia DATE NOT NULL,
    descricao TEXT,
    local VARCHAR(100),
    valor_estimado DECIMAL(12,2),
    numero_apolice INT NOT NULL,
    FOREIGN KEY (numero_apolice) REFERENCES apolices(numero_apolice)
);

-- Tabela Apolice_Cobertura (relacionamento n:m com atributos)
CREATE TABLE apolice_cobertura (
    numero_apolice INT,
    id_cobertura INT,
    valor_especifico DECIMAL(12,2),
    franquia DECIMAL(12,2),
    percentual_cobertura DECIMAL(5,2),
    PRIMARY KEY (numero_apolice, id_cobertura),
    FOREIGN KEY (numero_apolice) REFERENCES apolices(numero_apolice),
    FOREIGN KEY (id_cobertura) REFERENCES coberturas(id_cobertura)
);

-- Tabela Sinistro_Oficina (relacionamento n:m com atributos)
CREATE TABLE sinistro_oficina (
    id_sinistro INT,
    cnpj_oficina CHAR(14),
    valor_orcamento DECIMAL(12,2),
    data_entrada DATE,
    data_prevista DATE,
    status_reparo VARCHAR(30),
    PRIMARY KEY (id_sinistro, cnpj_oficina),
    FOREIGN KEY (id_sinistro) REFERENCES sinistros(id_sinistro),
    FOREIGN KEY (cnpj_oficina) REFERENCES oficinas(cnpj)
);
