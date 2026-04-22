# Relatório de Melhorias - Lattes2Graph

Este relatório detalha os problemas identificados no repositório do projeto **Lattes2Graph** e as ações corretivas sugeridas (e implementadas) para aumentar a resiliência e usabilidade do pipeline.

## 1. Arquivos de Configuração Ausentes

### Problema
- O `README.md` orienta o usuário a instalar dependências através do comando `pip install -r requirements.txt`, mas o arquivo `requirements.txt` não existe no repositório.
- Não há um arquivo `.gitignore`, o que pode levar ao versionamento acidental de arquivos gerados (como a pasta `output/`) e arquivos de cache (`__pycache__`).

### Solução
- **Criação do `requirements.txt`**: Adição do arquivo contendo as bibliotecas essenciais identificadas no código fonte (`playwright`, `rdflib`, `pyvis`). Observação: A biblioteca `networkx` foi citada no README, mas não está sendo utilizada no código atual e não foi adicionada para evitar dependências desnecessárias.
- **Criação do `.gitignore`**: Inclusão do arquivo para ignorar `output/`, `__pycache__/`, `venv/`, `.env` e outros artefatos comuns do Python.

## 2. Dependência de Diretórios Pré-existentes

### Problema
- O pipeline salva os arquivos processados (`conhecimento.ttl` e `index.html`) dentro da pasta `output/`. No entanto, se o usuário executar o projeto pela primeira vez sem criar essa pasta manualmente, o script falhará com um erro de `FileNotFoundError`.

### Solução
- **Criação dinâmica de pastas**: Modificação no arquivo principal (`src/main.py`) para utilizar a biblioteca `os` e criar a pasta de saída automaticamente caso não exista: `os.makedirs('output', exist_ok=True)`.

## 3. Fragilidade no Web Scraper

### Problema
- O arquivo `src/scraper.py` utiliza chamadas diretas como `await page.inner_text(...)` para buscar dados. Se um ID não existir, se a estrutura da página Lattes for diferente ou se os elementos procurados não carregarem, o scraper lança uma exceção não tratada corretamente, parando a extração dos dados bruscamente.

### Solução
- **Tratamento de Exceções**: Adição de blocos `try-except` para cada campo extraído (`nome`, `resumo`, `producoes`). Dessa forma, se a página ou um campo não for carregado, o scraper registrará um aviso e definirá o valor como "Não encontrado", em vez de causar a interrupção de toda a aplicação.
- **Melhoria no manuseio de seletores**: Aumentamos a tolerância e garantimos que os scripts não quebrem o pipeline para IDs mal formatados ou páginas com problemas no CNPq.
