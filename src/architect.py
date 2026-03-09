from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, DCTERMS

def create_research_graph(data_list):
    g = Graph()
    # Namespace customizado para o projeto
    LATTES = Namespace("http://exemplo.org/lattes#")
    
    for person in data_list:
        subject = URIRef(f"http://lattes.cnpq.br/{person['id']}")
        
        # Triplas básicas (Princípios FAIR: Identificadores Persistentes)
        g.add((subject, RDF.type, FOAF.Person))
        g.add((subject, FOAF.name, Literal(person['nome'])))
        g.add((subject, DCTERMS.abstract, Literal(person['resumo'])))
        
        # Aqui poderíamos adicionar relações de coautoria
        # g.add((subject, FOAF.knows, URIRef(outro_id)))

    # Salva em formato Turtle (mais legível que XML/RDF)
    g.serialize(destination='output/conhecimento.ttl', format='turtle')
    print("RDF gerado com sucesso em output/conhecimento.ttl")
    return g
