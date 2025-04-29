--1. Listar todos os clientes com seus veículos
SELECT c.nome, v.placa, v.marca, v.modelo, v.ano
FROM clientes c
JOIN veiculos v ON c.cpf = v.cpf_cliente
ORDER BY c.nome;

--2. Listar apólices ativas e seus respectivos corretores
SELECT a.numero_apolice, a.data_inicio, a.data_fim, c.nome AS corretor
FROM apolices a
JOIN corretores c ON a.id_corretor = c.id_corretor
WHERE a.status = 'Ativa';

--3. Contar quantas apólices cada corretor possui
SELECT c.nome AS corretor, COUNT(*) AS total_apolices
FROM corretores c
JOIN apolices a ON c.id_corretor = a.id_corretor
GROUP BY c.nome
ORDER BY total_apolices DESC;

--4. Valor médio das apólices por status
SELECT status, AVG(valor_premio) AS media_valor_premio
FROM apolices
GROUP BY status;

--5. Listar sinistros e os veículos envolvidos
SELECT s.id_sinistro, v.placa, v.marca, v.modelo, s.descricao, s.valor_estimado
FROM sinistros s
JOIN apolices a ON s.numero_apolice = a.numero_apolice
JOIN veiculos v ON a.renavam_veiculo = v.renavam;

--6. Sinistros com valor estimado acima de R$ 50.000
SELECT id_sinistro, descricao, valor_estimado
FROM sinistros
WHERE valor_estimado > 50000
ORDER BY valor_estimado DESC;

--7. Apólices que cobrem "Roubo"
SELECT DISTINCT a.numero_apolice
FROM apolices a
JOIN apolice_cobertura ac ON a.numero_apolice = ac.numero_apolice
JOIN coberturas c ON ac.id_cobertura = c.id_cobertura
WHERE c.tipo = 'Roubo';

--8. Oficinas com mais de 5 reparos realizados
SELECT o.nome, COUNT(*) AS total_reparos
FROM oficinas o
JOIN sinistro_oficina so ON o.cnpj = so.cnpj_oficina
GROUP BY o.nome
HAVING COUNT(*) > 5
ORDER BY total_reparos DESC;

--9. Valor total orçado por oficina
SELECT o.nome, SUM(so.valor_orcamento) AS total_orcado
FROM oficinas o
JOIN sinistro_oficina so ON o.cnpj = so.cnpj_oficina
GROUP BY o.nome
ORDER BY total_orcado DESC;

--10. Clientes que possuem mais de 2 veículos
SELECT c.nome, COUNT(v.renavam) AS quantidade_veiculos
FROM clientes c
JOIN veiculos v ON c.cpf = v.cpf_cliente
GROUP BY c.nome
HAVING COUNT(v.renavam) > 2
ORDER BY quantidade_veiculos DESC;
