import asyncio
import os
from src.scraper import get_lattes_basic_info
from src.architect import create_research_graph
from src.visualizer import generate_interactive_graph

async def run_pipeline():
    print("🚀 Iniciando o pipeline Lattes2Graph...\n")

    # Garantir que a pasta output/ existe
    os.makedirs('output', exist_ok=True)

    # Passo 1: Extração (Simulando uma lista de IDs do seu grupo de pesquisa/Mestrado)
    lattes_ids = [
        "0000000000000000", # Substitua por um ID real
        "1111111111111111"  # Substitua por outro ID real
    ]
    
    dados_extraidos = []
    for lattes_id in lattes_ids:
        print(f"🔍 Extraindo dados para o ID: {lattes_id}")
        # Como o scraper é assíncrono (usa Playwright), precisamos do 'await'
        try:
            dados = await get_lattes_basic_info(lattes_id)
            dados_extraidos.append(dados)
        except Exception as e:
            print(f"⚠️ Erro ao extrair dados do ID {lattes_id}: {e}")

    if not dados_extraidos:
        print("❌ Nenhum dado extraído. Verifique os IDs Lattes.")
        return

    # Passo 2: Modelagem Semântica (Criar o RDF)
    print("\n📐 Gerando o Grafo de Conhecimento (RDF)...")
    create_research_graph(dados_extraidos)

    # Passo 3: Visualização (Gerar o HTML interativo)
    print("\n🎨 Renderizando o Grafo Interativo...")
    generate_interactive_graph("output/conhecimento.ttl")

    print("\n✅ Pipeline concluído com sucesso!")
    print("Abra o arquivo 'output/index.html' no seu navegador para ver o grafo.")

if __name__ == "__main__":
    # Como usamos Playwright (assíncrono), o main.py precisa rodar dentro de um loop de eventos
    asyncio.run(run_pipeline())
