# **Relatório de Qualidade do Conjunto de Dados de Estabelecimentos de Saúde**

Versão do Relatório: 1.0
Data da Análise: 27 de junho de 2025  
Versão do Dado Analisado: 1.0.0  

## **1. Introdução**
Este documento apresenta uma análise quantitativa da qualidade do Conjunto de Dados de Estabelecimentos de Saúde.
o objetivo é fornecer aos usuários uma visão transparente das características e limitações dos dados, em
conformidade com o princípio **Reutilização (Reusable)** dos dados FAIR.

## **2. Métricas de Qualidade**

### **2.1. Completude**
Mede a presença de valores nulos em cada coluna.

* `CD_ESTABELECIMENTO`: 0.00% nulos
* `DSC_RAZAO_SOCIAL`: 0.00% nulos
* `NM_FANTASIA`: 0.00% nulos
* `CD_MUNICIPIO`: 0.00% nulos
* `TP_ESTABELECIMENTO`: 0.00% nulos
* `URI_MUNICIPIO`: 0.00% nulos

**Análise:** A ausência de nulos nos campos garante a integridade referencial.

### **2.2. Unicidade**
Verifica se os identificadores únicos não possuem duplicatas.

* A coluna `CD_ESTABELECIMENTO` é 100% única? Sim

**Análise:** A unicidade de 100% confirma que não existem registros duplicados para os estabelecimentos de saúde.
Cada estabelecimento possui um identificador exclusivo, o que é fundamental para a integridade dos dados e para
a sua utilização como chave primária confiável em cruzamentos com outras fontes de informação.

### **2.3. Validade**
Avalia se os dados estão em conformidade com formatos, regras ou vocabulários pré-definidos.

* `TP_ESTABELECIMENTO` tem valores fora do vocabulário controlado? Não (0.00% inválidos)
* Todas as URIs em `URI_MUNICIPIO` seguem o padrão esperado? Sim

**Análise:** Os dados enriquecidos demonstram alta validade, com total conformidade ao vocabulário controlado
e ao padrão de URI definido, garantindo a interoperabilidade semântica.