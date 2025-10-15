Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # backend/app.py
... from flask import Flask, request, jsonify
... import networkx as nx
... import random
... 
... app = Flask(__name__)
... 
... # Example: simulate multi-platform cascade network
... def generate_network():
...     G = nx.Graph()
...     for i in range(1, 21):  # 20 users
...         G.add_node(i, platform=random.choice(['Twitter', 'Reddit', 'Facebook']))
...     edges = [(random.randint(1,20), random.randint(1,20)) for _ in range(40)]
...     G.add_edges_from(edges)
...     return G
... 
... # Community detection
... def detect_communities(G):
...     communities = list(nx.community.greedy_modularity_communities(G))
...     result = []
...     for idx, comm in enumerate(communities):
...         result.append({"community_id": idx+1, "members": list(comm)})
...     return result
... 
... @app.route('/detect', methods=['GET'])
... def detect():
...     G = generate_network()
...     communities = detect_communities(G)
...     return jsonify(communities)
... 
... if __name__ == "__main__":
...     app.run(debug=True)
