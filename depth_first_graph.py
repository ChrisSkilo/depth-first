class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Dictionary to store nodes and their adjacency lists

    # Method to add a node to the graph
    def add_node(self, node):
        self.adjacency_list[node] = []  # Initialize an empty adjacency list for the new node

    # Method to create an edge between two nodes
    def create_edge(self, node1, node2):
        # Add the second node to the adjacency list of the first node, and vice versa
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    # Method to check if a target node is reachable from a starting node using depth-first search
    def depth_first_reachable(self, starting_node, target_node):
        # Check if starting and target nodes exist in the graph
        if starting_node not in self.adjacency_list or target_node not in self.adjacency_list:
            return False

        stack = [starting_node]  # Initialize a stack with the starting node
        traversed_nodes = set()  # Use a set to track traversed nodes

        # Loop until the stack is empty
        while stack:
            current_node = stack.pop(0)  # Pop the front element from the stack

            # Check if the current node is the target node
            if current_node == target_node:
                return True  # Target node is reachable

            traversed_nodes.add(current_node)  # Add the current node to the set of traversed nodes

            # Get the adjacency list of the current node
            adjacency_list = self.adjacency_list[current_node]

            # Iterate through the neighbors in the adjacency list
            for node in adjacency_list:
                # If the neighbor has not been traversed, add it to the front of the stack
                if node not in traversed_nodes:
                    stack.insert(0, node)

        return False  # Target node is not reachable