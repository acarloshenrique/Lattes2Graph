from pyvis.network import Network
from rdflib import Graph, FOAF

def generate_interactive_graph(rdf_file_path):
    # 1. Carregar o grafo RDF gerado anteriormente
    g = Graph()
    g.parse(rdf_file_path, format="turtle")

    # 2. Inicializar a rede do Pyvis
    # Configurada para ser responsiva e com fundo claro (aspecto profissional)
    net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black", notebook=False)
    
    # Física do grafo para que as bolinhas se espalhem organicamente
    net.barnes_hut()

    # 3. Iterar pelas triplas RDF e adicionar ao grafo visual
    for s, p, o in g:
        # Extrair IDs amigáveis das URIs
        subj_label = str(o) if p == FOAF.name else str(s).split('/')[-1]
        
        # Adicionar o nó do Pesquisador
        if p == FOAF.name:
            # Usamos o nome como label e o ID como identificador interno
            net.add_node(str(s), label=str(o), title=f"ID Lattes: {str(s).split('/')[-1]}", color="#2c3e50")
        
        # Exemplo de relação de coautoria (se houver a propriedade FOAF.knows no RDF)
        if p == FOAF.knows:
            net.add_edge(str(s), str(o), color="#bdc3c7")

    # 4. Salvar o arquivo final
    output_path = "output/index.html"
    net.save_graph(output_path)
    print(f"Grafo interativo gerado com sucesso: {output_path}")

if __name__ == "__main__":
    # Teste apontando para o arquivo gerado pelo architect.py
    generate_interactive_graph("output/conhecimento.ttl")
