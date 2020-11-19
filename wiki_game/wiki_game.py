from utils import *
from igraph import *
import argparse 

class Wiki_Game:
    names_list = []
    names_map = {}
    edges = []

    def get_params(self, args=sys.argv[1: ]):
        parser = argparse.ArgumentParser(description="Select the files to use")
        parser.add_argument('--names', help="the file containing the wiki article names" )
        parser.add_argument('--edges', help="the file containing the edge information")
        params = parser.parse_args(args)
        return params

    def run_game(self):
        params = self.get_params()
        names_list = parse_article_names(params.names)
        names_map = create_names_map(names_list)
        edges = parse_graph_edges(params.edges)
        g = Graph()
        g = g.as_directed()
        g.add_vertices(names_list)
        g.add_edges(edges)

        while True:
            source = input("Please enter the name of the source article, or 'q' to quit\n").lower()
            if source == 'q':
                quit()
            target = input("Please enter the name of the target article, or 'q' to quit\n").lower()
            if target == 'q':
                quit()
            while(source not in names_map or target not in names_map):
                if (source not in names_map):
                    source = input("That source wasn't present in our graph. Please enter the name of a source article\n").lower()
                if (target not in names_map):
                    target = input("That target wasn't present in our graph. Please enter the name of the target article\n").lower()
            source_index = names_map[source]
            target_index = names_map[target]

            path = g.get_all_shortest_paths(v=source_index, to=target_index)
            self.print_path(path, names_list)

    def print_path(self, path, names):
        if (len(path) == 0):
            print("Could not find any path between the requested articles.")
            return
        path = path[0]
        for vertex in path[ : -1]:
            print(names[vertex], end=" --> ")
        print(names[path[-1]])

if __name__ == "__main__":
    game = Wiki_Game()
    game.run_game()