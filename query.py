from rdflib import Graph

g = Graph()
g.parse("./space.ttl", format="ttl")

PREFIXES = """
PREFIX space: <http://www.semanticweb.org/mini-project-22/ontologies/2025/space#>
PREFIX obo:   <http://purl.obolibrary.org/obo/>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>
"""

def run_query(query):
    return g.query(PREFIXES + "\n" + query)

def print_query(query):
    results = run_query(query)
    for row in results:
        print(row)

def write_query(question, query):
  results = run_query(query)
  result_text = []
  for row in results:
      result_text.append(str(row) + "\n")
  # print(result_text)
  text = build_prompt(question, result_text)
  with open("query.txt", "w") as f:
    f.write(text)

def build_prompt(question, results):
    instructions = (
        "You are a helpful astronomy assistant. Use ONLY the provided "
        "Knowledge Graph facts as ground truth. If something is unknown, "
        "say you don't know. Answer concisely."
    )
    return f"{instructions}\n\n Facts: {results}\n\n Question: {question}\nAnswer:"

###List of all moons in the ontology
query1 = """
SELECT DISTINCT ?inst WHERE {
  ?inst rdf:type space:Moon .
}
"""
# print_query(query1)
###List of all moons with their respective planets and orbital periods (if available)
query2 = """
SELECT ?moon ?planet ?period
WHERE {
  ?moon rdf:type space:Moon .
  ?moon space:orbits ?planet .
  OPTIONAL { ?moon space:orbitalPeriodDays ?period }
}
ORDER BY ?planet ?moon
"""
# print_query(query2)

query5 = """
SELECT ?star ?galaxy
WHERE {
  ?star rdf:type/rdfs:subClassOf* space:Star ;
    space:distanceFromSunParsec ?distance ;
    space:locatedInGalaxy ?galaxy .
}
ORDER BY ?distance
LIMIT 1
"""

query6 = """

"""

query7 = """

"""

if __name__ == "__main__":
    queries = {
      "1": ("All moons in the ontology", query1),
      "2": ("Moons with planets and orbital periods", query2),
      "3": ("Q3"),
      "4": ("Q4"), 
      "5": ("In what Galaxy is the furthest star from our sun?", query5),
      "6": ("How many CelestialBodies are in Star System X?", query6),
      "7": ("What planets in the milky way are terrestrial and are located in a star system with more than 1 star?", query7)
    }

    while True:
      print("\n=== Space Ontology Query Menu ===")
      for num, (desc, _) in queries.items():
        print(f"{num}) {desc}")
      print("0) Exit")
      
      choice = input("\nSelect a query (1-6): ").strip()
      
      if choice == "0":
        break
      elif choice in queries:
        print(f"\n--- {queries[choice][0]} ---")
        write_query(queries[choice][0], queries[choice][1])
      else:
        print("Invalid choice. Please try again.")




