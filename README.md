Lattes2Graph: Engenharia de Dados e Bibliometria Semântica
Este projeto implementa um pipeline automatizado para a extração, modelagem e visualização de redes de colaboração científica a partir da Plataforma Lattes. Diferente de scrapers convencionais, o Lattes2Graph utiliza princípios de Linked Open Data e Curadoria Digital para transformar dados não-estruturados em um Grafo de Conhecimento interoperável.

🎯 Objetivos do Projeto
Automação de Coleta: Extração robusta de metadados de pesquisadores utilizando Playwright.

Modelagem Ontológica: Transformação de registros bibliográficos em triplas RDF, utilizando vocabulários padronizados como FOAF e Dublin Core.

Visualização Científica: Geração de grafos interativos para análise de coautoria e densidade de rede.

Princípios FAIR: Garantia de que os dados gerados sejam Encontráveis, Acessíveis, Interoperáveis e Reutilizáveis.

🛠️ Stack Tecnológica
Linguagem: Python 3.10+

Coleta: Playwright (Navegação emulada para contornar limitações de dados não-estruturados).

Web Semântica: rdflib para criação e serialização de grafos RDF (Turtle/Triplas).

Visualização: pyvis e networkx para renderização de redes complexas em HTML/JS.

🧬 Arquitetura do Pipeline
Ingestão (src/scraper.py): Captura o ID Lattes e extrai o resumo acadêmico e produções bibliográficas.

Modelagem (src/architect.py): Converte os dados em um grafo semântico. Aqui, cada pesquisador torna-se um URIRef único, garantindo a persistência do objeto informacional.

Visualização (src/visualizer.py): Mapeia as relações (ex: coautoria, mesma instituição) e gera uma interface interativa.

🚀 Como Executar
Instale as dependências:

Bash
pip install -r requirements.txt
playwright install chromium
Execute o pipeline:

Bash
python main.py
O resultado será gerado na pasta /output nos formatos .ttl (Turtle RDF) e .html (Grafo Interativo).

📊 Aplicação Acadêmica e Profissional
Este projeto é um exemplo prático de como a Ciência da Informação pode utilizar a Inteligência Artificial e a Automação para superar as limitações de metadados tradicionais. Ele reflete minha atuação no Instituto de Pesquisas Tecnológicas (IPT) e minha pesquisa de mestrado na UNESP, focada em infraestruturas de dados que suportem a tomada de decisão baseada em evidências.
