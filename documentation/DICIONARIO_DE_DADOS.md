| Nome do Campo | Descrição | Tipo de Dado | Exemplo | Restrições / Regras | Oberservações Adicionais
| :---| :---| :--- | :--- | :--- | :--- |
| **CD_ESTABELECIMENTO** | Seria o RG de cada estabelecimento CNES. É um identificador único que evita confusões entre registros. | `INTEGER` | `6960065` | `UNIQUE`, `NOT NULL` | --- |
| **DSC_RAZAO_SOCIAL** | É o nome oficial regristrado no CNPJ, aquele que aparece em documentos e contratos. | `STRING` | `PREFEITURA MUNICIPAL DE SÃO MATEUS` | `VARCHAR(255)`, `NOT NULL` | --- |
| **NM_FANTASIA** | O nome do estabelecimento, usado no dia a dia e nas placas. | `STRING` | `USF GURIRI SUL` | `VARCHAR(255)`, `NULL` | Nem todo estabelecimento tem fantasia, mas quando tem, está aqui. |
| **CD_MUNICIPIO** | Código oficial do IBGE que indica em qual município o estabelecimento está localizado. | `INTEGER` | `3204906` | `UNIQUE`, `NOT NULL` | Assim, não há erro entre cidades com nomes iguais. fazer uma observação sobre o range, que ageunta 7 posições. |
| **TP_ESTABELECIMENTO** | Tipo de estabelecimento derivado de NM_FANTASIA e classificado segundo um vocabulário controlado. | `STRING` | `Unidade de Saúde da Família` | `VARCHAR(255)`, `NOT NULL` | --- |
| **URI_MUNICIPIO** | URI padronizado para o município, conectando o dado a um identificador web persistente. | `STRING` | `https://servicodados.ibge.gov.br/api/v1/localidades/municipios/3204906` | `UNIQUE`, `VARCHAR(255)`, `NOT NULL` | Aumenta a interoerabilidade ao permitir que o dado seja conectado a outras fontes da Internet (Linked Data). |
