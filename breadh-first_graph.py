class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        self.adjacency_list[node] = []

    def create_edge(self, node1, node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def breadth_first_reachable(self, starting_node, target_node):
        if starting_node not in self.adjacency_list or target_node not in self.adjacency_list:
            return False

        queue = [starting_node]
        traversed_nodes = set()

        while queue:
            current_node = queue.pop(0)

            if current_node == target_node:
                return True

            traversed_nodes.add(current_node)
            adjacency_list = self.adjacency_list[current_node]

            for node in adjacency_list:
                if node not in traversed_nodes:
                    queue.append(node)

        return False