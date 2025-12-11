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


if __name__ == "__main__":
    queries = {
      "1": ("All moons in the ontology", query1),
      "2": ("Moons with planets and orbital periods", query2),
      ###etc etc until 5
    }

    while True:
      print("\n=== Space Ontology Query Menu ===")
      for num, (desc, _) in queries.items():
        print(f"{num}) {desc}")
      print("6) Exit")
      
      choice = input("\nSelect a query (1-6): ").strip()
      
      if choice == "6":
        break
      elif choice in queries:
        print(f"\n--- {queries[choice][0]} ---")
        write_query(queries[choice][0], queries[choice][1])
      else:
        print("Invalid choice. Please try again.")




