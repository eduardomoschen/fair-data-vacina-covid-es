# **Guia de Uso e Análise do Conjunto de Dados de Estabelcimentos de Saúde do Espírito Santo**

Autor: Eduardo Nandorf Moschen  
Data: 27/06/2025  
Versão: 1.1

## **1. Introdução**
Este documento serve como um guia metodológico para a utilização do conjunto de dados de Estabelecimentos de Saúde
do Espírito Santo. O objetivo é fornecer a usuários, sejam eles desenvolvedores, analistas de dados ou pesquisadores,
todas as ferramentas necessárias para carregarm estruturar e consultar os dados de forma eficiente. A estruturação
deste guia segue as melhores práticas de gerenciamento de dados, visando potencializar a Acessibilidade,
Interoperabilidade e Reusabilidade dos dados, mediante os Princípios FAIR.

Para uma descrição detalhada de cada campo, suas definições e regras de negócio, consulte o arquivo ![dicionario_de_dados.md](./dicionario_de_dados.md).

## **2. Estrutura do Banco de Dados (SQL)**
Para a correta persistência e manipulação dos dados em um ambiente de banco de dados relacional, é fundamental a
criação de uma tabela que respeite as regras definidas no dicionário de dados. O script SQL a seguir pode ser
executado para criar a tabela `estabelecimento_saude_es`.

```sql
CREATE TABLE estabelecimentos_saude_es (
    CD_ESTABELECIMENTO INTEGER NOT NULL UNIQUE,
    DSC_RAZAO_SOCIAL VARCHAR(255) NOT NULL,
    NM_FANTASIA VARCHAR(255),
    CD_MUNICIPIO VARCHAR(255) NOT NULL,
    TP_ESTABELECIMENTO VARCHAR(255),
    URI_MUNICIPIO VARCHAR(255) NOT NULL
);
```

## **3. Exemplos de Conusltas SQL**
A seguir, são apresentados exemplos de consultas SQL, partindo de cenários básicos a otimizados.

### **3.1. Consulta Básica: Contagem de Estabelecimentos**
Esta consulta retorna o número total de estabelecimentos cadastrados na tabela.

```sql
SELECT COUNT(*) AS total_estabelecimentos
FROM estabelecimentos_saude_es;
```

### **3.2. Consulta com Filtro: Buscar por Nome Fantasia**
Esta consulta localiza todos os estabelecimentos que contenham "USF"(Unidade de Saúde da Família) em seu nome fantasia.

```sql
SELECT CD_ESTABELECIMENTO, DSC_RAZAO_SOCIAL, NM_FANTASIA
FROM estabelecimentos_saude_es
WHERE NM_FANTASIA ILIKE '%USF%;
```

## **4. Próximos Passos e Publicação**
Como o escopo do projeto seria sobre o que é necessário para tornar os dados FAIR, podemos apenas manter essa estapa
do trabalho até esta documentação. A partir do segundo ano, que foi o projeto enviado em Maio, utilizaremos a base
construída hoje para implementar e disponibilizar os dados; tornando-o então FAIR.

## **5. Licença** (REUSABLE)
Este conjunto de dados e sua documentação são disponibilizados sob a **Licença Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**.

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licença Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

Isso significa que você tem a liberdade de:

* **Compartilhar** - copiar e redistribuir o material em qualquer suporte ou formato.
* **Adaptar** - remixar, transformar e criar a partir do material para qualquer fim, mesmo que comercial.

Desde que você atribua o devido crédito, forneça um link para a licença e indique se foram feitas alterações.

### **6. Como Citar**
MOSCHEN, Eduardo Nandorf. Guia de Uso e Análise do Conjunto de Dados de Estabelcimentos de Saúde do Espírito Santo. 
Versão 1.1, 27 de jun. de 2025. Disponível em: https://github.com/eduardomoschen/fair-data-vacina-covid-es/tree/master.
Acesso em: [data de acesso].