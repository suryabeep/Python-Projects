from tqdm import tqdm

def create_names_map(names_list: list):
    names_map = {}
    print("Creating article names map...")
    for i, name in tqdm(enumerate(names_list)):
        names_map[name] = i
    return names_map

def parse_article_names(filename: str):
    file = open(filename, "r")
    lines = file.readlines()
    names_list = []
    print("Parsing article names...")
    for line in tqdm(lines):
        line = line.strip()
        space_loc = line.find(" ")
        number = int(line[0: space_loc])
        name = line[space_loc + 1 : ]
        names_list.append(name.lower())
    return names_list

def parse_graph_edges(filename: str):
    file = open(filename, "r")
    lines = file.readlines()
    edges_list = []
    print("Parsing graph edges...")
    for line in tqdm(lines):
        line = line.strip()
        space_loc = line.find(" ")
        vertex_1 = int(line[0 : space_loc])
        vertex_2 = int(line[space_loc + 1 : ])
        pair = (vertex_1, vertex_2)
        edges_list.append(pair)
    return edges_list