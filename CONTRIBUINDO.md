Versão: 1.0.0
Data: 20/07/2025

# Guia de Contribuição para o Conjunto de Dados de Estabelecimentos de Saúde

Primeiramente, obrigado pelo seu interesse em contribuir com este projeto! Toda ajuda é bem-vinda e essencial para
manter a qualidade e a relevância destes dados.

Este documento fornece um conjunto de diretrizes para quem deseja contribuir.

## Como Posso Contribuir?

Existem duas maneiras principais de contribuir para o projeto: abrindo um **Apontamento (Issue)** ou enviando um
**Pedido de Inclusão (Pull Request)**.

### 1. Apontamentos (Issues)

As Issues são a melhor forma de iniciar uma conversa com a equipe do projeto. Você deve abrir uma Issue para:

* **Reportar um erro nos dados:** Se você encontrou um dado incorreto e não sabe como corrigi-lo diretamente.
* **Sugerir uma melhoria:** Propor uma nova coluna, uma nova análise ou uma melhoria na documentação.
* **Fazer uma pergunta:** Se você tem alguma dúvida sobre os dados que a documentação não esclarece.
* **Discutir uma mudança maior:** Antes de começar a trabalhar em uma grande contribuição (como um novo script de
análise), é sempre bom abrir umna Issue para discutir a ideia primeiro.

**-> [Abra uma nova Issue aqui](https://github.com/eduardomoschen/fair-data-vacina-covid-es/issues)**

### 2. Pedidos de Inclusão (Pull Requests)

Um Pull Request (PR) é a maneira de propor uma mudança direta nos arquivos do projeto. É o método preferido para
todas as contribuições que modificam o conteúdo do repositório.

**Você pode enviar um Pull Request para:**

* **Corigir erros nos dados:** Corrigir diretamente um erro em um dos arquivos `.csv`.
* **Melhorar a documentação:** Corrigir um erro de digitação, esclarecer uma seção ou adicionar novos exemplos nos
arquivos `.md`.
* **Aprimorar o código:** Refatorar um script, corrigir um bug ou adicionar uma nova funcionalidade de análise.

**Fluxo de Trabalho para um Pull Request:**

1. **Faça um "Fork"** do repositório para a sua própria conta do GitHub.
2. **Crie um "Branch"** para a sua modificação (ex: `corrige-nome-fantasia-123`).
3. **Faça as suas alterações** e realize o "commit" para o seu branch.
4. **Abra um Pull Request** do seu branch para o branch principal do nosso repositório.
5. **Descreva sua mudança:** No PR, explique claramente o que você mudou e por quê. Se o seu PR resolve uma Issue
existente, mencione o número dela (ex. `Fecha #42`).
6. **Aguarde a revisão:** Nós revisaremos o seu PR, poderemos fazer sugestões e, uma vez aprovado, faremos o "merge"
da sua contribuição.

## Guias de Estilo

Para manter a consistenência, pedimos que todas as contribuições via Pull Requests sigam os seguintes guias de estilo.

### Python

Todas as contribuições de código em Python devem seguir o guia de estilo
**[PEP 8](https://peps.python.org/pep-0008/)**.

### Padrão de Mensagens de Commit

Para manter um histórico de contribuiçoes claro e rastreável, este projeto adota o padrão
**[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)**. Cada mensagem de commit deve seguir
uma estrutura específica.

**Estrutura:**

[corpo opcional explicando a mudança]

[redapé opcional com BREAKING CHANGE ou referências a Issues]

**Tipos de Commit Permitidos:**

* **feat**: Uma nova funcionalidade (ex: adicionar uma nova coluna de dados ou um novo script de análise).
* **fix**: Uma correção de um erro nos dados ou no código.
* **docs**: Mudanças que afetam apenas a documentação (`.md` files).
* **style**: Alterações de formatação que não afetam o significado do código (espaços, ponto e vírgula, PEP 8).
* **refactor**: Uma mudança no código que não corrige um bug nem adiciona uma funcionalidade.
* **perf**: Uma mudança que melhora a performance.
* **test**: Adicionando testes que faltam ou corrigindo testes existentes.
* **chore**: Outras mudanças que não modificam arquivos de dados ou de cóigo-fonte (ex: atualizar o `.gitignore`).

**Exemplos Práticos:**

**Exemplo de um `fix` (correção):**

```bash
git commit -m "fix: corrige código do IBGE para o município de Vila Velha" -m "O código estava incorreto em
5 registros, afetando a junção com dados externos. Esta mudança atualiza os registros para o valor correto."
```

**Exemplo de um `feat` (nova funcionalidade):**

```bash
git commit -m "feat: adiciona coluna de tipo de estabelecimento" -m "Cria a nova coluna TP_ESTABELECIMENTO,
utilizando um vocabulário controlado ara melhorar a capacidade de agregação e análise dos dados."
```

**Exemplo de `docs` (documentação):**

```bash
git commit -m "docs: atualiza changelog para a versão 1.1.1"
```

### Documentação (Markdown)

* Mantenha as linhas com um limite razoável de até 120 caracteres.
* Use a sintaxe padrão do Markdown para garantir a portabilidade.

---

Agradecemos novamente por sua ajuda em tornar este um conjunto de dados aberto de alta qualidade para todos!