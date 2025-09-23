# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.1.2] - 2025-09-22

### Adicionado
- **Adição de Scripts de Automação da Curadoria de Dados**: Foram adicionados os scripts Python
que compõem o pipeline de processamento, garantindo a rastreabilidade e reprodutibilidade do tratamento dos
dados. A importância de cada um é:
    - **`filter_establishments_by_state.py`**: Essencial para a primeira etapa de **escopo e filtragem**. Sua função
    é consumir um dataset nacional de estabelecimentos e isolar apenas os registros pertencentes ao
    Espírito Santo (UF 32), garantindo que o conjunto de dados final seja relevante e focado no objetivo do projeto.
    - **`correct_municipality_codes.py`**: Crucial para a **correção e validação dos dados**. O script utiliza APIs externas
    (CNES e ViaCEP) para verificar e corrigir o código de município (`CD_MUNICIPIO`) de cada estabelecimento,
    aumentando significativamente a acurácia e a confiabilidade dos dados geográficos.
    - **`enrich_and_classify_data.py`**: Representa a etapa de **enriquecimento semântico**, um pilar da
    Interoperabilidade (FAIR). Ele cria a coluna `TP_ESTABELECIMENTO` ao classificar os estabelecimentos
    segundo um vocabulário controlado e gera a coluna `URI_MUNICIPIO` para conectar os dados a identificadores
    persistentes (Linked Data).
    - **`finalize_and_clean_data.py`**: Realiza a **limpeza final** do dataset. A remoção de chaves
    substitutas (`SK_DM_ESTABELECIMENTOS`), que são artefatos de sistemas internos, torna o
    conjunto de dados mais limpo e focado nas informações relevantes para o usuário final, melhorando a Reutilização.
    - **`generate_data_quality_report.py`**: Automatiza a **verificação da qualidade dos dados**. Este
    script gera o relatório final de métricas de completude, unicidade e validade, oferecendo
    uma avaliação transparente e programática que garante a confiança no resultado final do pipeline.


## [1.1.1] - 2025-07-02

### Adicionado
- Estrutura para o guia de Contribuição (`CONTRIBUINDO.md`).

### Removido
- Removida a seção comentada "Otimização de Consultas com Índices" do guia de uso (`COMO_USAR.md`) para simplificar
o documento e focar no escopo principal.

## [1.1.0] - 2025-06-30

Esta versão representa um grande avanço na interoperabilidade e governança do conjunto de dados, com a introdução
de colunas semânticas e metadados ricos.

### Adicionado
- **Coluna `TP_ESTABELECIMENTO`**: Adicionada uma nova coluna que classifica cada estabelecimento de acordo com um
vocabulário controlado, melhorando a Interoperabilidade (I2).
- **Coluna `URI_MUNICIPIO`**: Adicionada uma nova coluna com um identificador web persistente (URI) para cada
município, promovendo os princípios de Linked Data.
- **Schemas Legíveis por Máquina**:
    - **Metadados de Descoberta (`metadata.jsonld`/`estabelecimentos_dataset.json`)**: Adicionado um arquivo de
    metadados de alto nível usando o padrão `schema.org`. Este arquivo cumpre a função do `metadata.jsonld`
    mencionado na proveniência, tornando o dataset encontrável em mecanismos de busca.
    - **Schema de Tabela (`estabelecimentos_table_schema.json`)**: Adicionado um schema técnico detalhado
    (`Table Schema`) que descreve a estrutura, tipos de dados e restrições de cada coluna, como a lista de
    valores permitidos (`enum`) para `TP_ESTABELECIMENTO`.

### Modificado
- **Guia de Uso**: O arquivo de guia de uso foi atualizado para a versão 1.1.
- **Script `CREATE TABLE`**: O script de criação da tabela no guia de uso foi atualizado para incluir as novas
colunas `TP_ESTABELECIMENTO` e `URI_MUNICIPIO`.
- **Dicionário de Dados**: O arquivo `dicionario_de_dados.md` foi atualizado para incluir as definições das
novas colunas.
- **Citação do Projeto**: Uma seção "Como Citar" com formato de citação e link para o repositório foi adicionada
ao guia de uso.

## [1.0.0] - 2025-06-27

### Adicionado
- **Versão Inicial do Conjunto de Dados**: A primeira versão do dataset foi criada, tendo como base a
tabela `dm_estabelecimento` do Trabalho de Conclusão de Curso de Everson de Oliveira (SILVA, 2024).
- **Documento de Proveniência**: Foi criado o arquivo `PROVENIENCIA.md` para detalhar a origem e a
linhagem dos dados, em conformidade com o princípio FAIR R1.2.
- **Relatório de Qualidade de Dados**: Foi criado o `QUALIDADE_DOS_DADOS.md` para apresentar métricas de
qualidade, como a ausência de valores nulos (0.00%) em campos chave e a unicidade de 100% da coluna `CD_ESTABELECIMENTO`.
- **Dicionário de Dados**: A primeira versão do `DICIONARIO_DE_DADOS.md` foi criada, detalhando os
campos iniciais.
- **Guia de Uso**: A primeira versão do `COMO_USAR.md` (v1.0) foi criada, contendo o script SQL para
criação da tabela e exemplos de consulta.
- **Licença**: Foi definida a licença **Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)**,
explicitada no guia de uso para garantir a Reutilização dos dados.
- **Changelog**: Este arquivo (`CHANGELOG.md`) foi criado para rastrear o histórico de mudanças do projeto.