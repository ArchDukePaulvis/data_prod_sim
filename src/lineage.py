from graphviz import Digraph

def generate_lineage(file_path):
    try:
        dot = Digraph()
        dot.node('A', 'Raw Data')
        dot.node('B', 'Cleaned')
        dot.node('C', 'Enriched')
        dot.node('D', 'Validated')
        dot.node('E', 'Output')

        dot.edges(['AB', 'BC', 'CD', 'DE'])
        dot.render(file_path, format='png')

        print(f"Lineage diagrams saved.")


    except Exception as e:
        print(f"Failed to save lineage diagrams: {e}")