import networkx as nx

def construct_graph(rules):
    graph = nx.Graph()
    
    for rule in rules:
        a,b = rule.split('-')
        graph.add_edge(a,b)

    return graph



def day23Q1(rules):
    graph = construct_graph(rules)

    cliques = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]

    result = sum([clique[0].startswith('t') or clique[1].startswith('t') or clique[2].startswith('t') for clique in cliques])
    return result








def day23Q2(rules):
    graph = construct_graph(rules)
    
    cliques = [clique for clique in nx.enumerate_all_cliques(graph)]
    biggest_clique = cliques[0]
    for clique in cliques[1:]:
        if len(clique) > len(biggest_clique):
            biggest_clique = clique
    return ",".join(sorted(biggest_clique))
        








if __name__ == "__main__":
    rules = []

    with open("Inputs/Day23Input.txt", "r") as file:
        rules = [line.split()[0] for line in file if line.strip()]
    
    result_part_one = day23Q1(rules)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day23Q2(rules)
    print("Result for part two: "+str(result_part_two))