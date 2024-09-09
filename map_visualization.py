import networkx as nx
import matplotlib.pyplot as plt

def create_campus_map():
    campus_map = nx.Graph()
    campus_map.add_edge('Campus Entrance', 'Building_1_Entrance', mode='walk')
    campus_map.add_edge('Campus Entrance', 'Building_2_Entrance', mode='cycle')
    campus_map.add_edge('Campus Entrance', 'Building_3_Entrance', mode='vehicle')
    return campus_map

def visualize_map(campus_map):
    pos = nx.spring_layout(campus_map)
    nx.draw(campus_map, pos, with_labels=True, node_size=3000, node_color="lightblue")
    plt.show()

if __name__ == "__main__":
    campus_map = create_campus_map()
    visualize_map(campus_map)
