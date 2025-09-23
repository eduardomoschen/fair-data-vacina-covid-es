# Proveniência do Conjunto de Dados
**Versão do Documento:** 1.0  
**Data da Última Atualização:** 22 de julho de 2025

## 1. Introdução
Este documento detalha a origem e a linhagem (o processo de transformação) do Conjunto de Dados FAIR de
Estabelecimentos de Saúde do Espírito Santo. O objetivo é fornecer um histórico transparente e
rastreável, em conformidade com o princípio **R1.2 (Reutilização)** dos dados FAIR, que exige que os
dados sejam associados à sua proveniência detalhada.

ORIGEM É DO OPEN DATASUS

## 2. Fonte de Dados Original
O ponto de partida para este projeto foi a tabela `dm_estabelecimento`, desenvolvida no Trabalho de
Conclusão de Curso de Everson de Oliveira, apresentado ao Instituto Federal do Espírito Santo (Ifes) em 2023.

A referência completa do trabalho original é:

>SILVA, Everson Henrich da. Criação de um pipeline de dados para análises dos registros de vacinação contra COVID-19. 2024. Trabalho de Conclusão de Curso (Graduação em Engenharia da Computação) – Universidade Federal do Espírito Santo, Centro Universitário Norte do Espírito Santo, Departamento de Computação e Eletrônica, São Mateus, ES, 2024.

A tabela original serviu como a base de registros de estabelecimentos, contendo informações primárias como código do
estabelecimento, razão social e município.

---

## 3. Processo de Curadoria e Enriquecimento FAIR
A partir da base inicial obtida do trabalho supracitado, foi realizado um rigoroso processo de curadoria e
enriquecimento de dados para aumentar seu valor e adequá-lo aos princípios FAIR. As seguintes etapas foram executadas:

### 3.1. Validação e Limpeza
* **Análise de Duplicidade:** Foi realizada uma verificação na coluna `CD_ESTABELECIMENTO` para
garantir a unicidade de cada registro de estabelecimento de saúde.
* **Análise de Completude:** Todas as colunas foram inspecionadas para verificar a ausência de
valores nulos nos campos essenciais, como `CD_ESTABELECIMENTO` e `CD_MUNICIPIO`.

### 3.2. Enriquecimento Semântico
* **Criação da Coluna `TP_ESTABELECIMENTO`:** Uma nova coluna foi adicionada para classificar cada
estabelecimento de saúde. Essa classificação foi feita a partir da análise dos nomes e tipos originais e
padronizada em um **vocabulário controlado** (ex: "Hospital", "Unidade de Saúde da Família", etc.).
Esta etapa melhora significativamente a **Interoperabilidade (I2)** dos dados.
* **Criação da Coluna `URI_MUNICIPIO`:** Para promover a conexão com outros conjuntos de dados
(Linked Data), a coluna `CD_MUNICIPIO` foi utilizada para gerar uma URI (Identificador Uniforme de Recurso)
persistente para cada município, utilizando o padrão de serviço de dados do IBGE.

### 3.3. Criação de Metadados e Documentação
Para garantir a máxima transparência e facilidade de reutilização, foram criados os seguintes artefatos de
documentação:
* **`dicionario_de_dados.md`**: Documentação detalhada de cada campo.
* **`qualidade_de_dados.md`**: Relatório com métricas de qualidade.
* **`schemas/estabelecimentos.json`**: Um schema legível por máquina que descreve a estrutura técnica da tabela.
* **`metadata.jsonld`**: Metadados ricos e legíveis por máquina sobre o conjunto de dados como um todo,
para promover a **Encontrabilidade (F2)**.

---

## 4. Resumo da Linhagem dos Dados

A trajetória dos dados pode ser resumida da seguinte forma:

**Dados Abertos da COVID-19 no ES** &rarr; **TCC de SILVA (2024)** 
&rarr; **Tabela `dm_estabelecimentos`** &rarr; **Processo de Melhoramento e Enriquecimento FAIR(este projeto)**
&rarr; **Versão Atual do Conjunto de Dados**