from collections import deque

# Function to add an edge to a list (the list is an array or arrays)
def add_edge(list, src, dest):
    list[src].append(dest)
    list[dest].append(src)

def bfs(list, src, dest, v, pred, dist):
    # A queue to maintain the needed to visit verticies
    queue = deque()
    
    # A boolean array to track if verticies are visited or not
    visited = [False for i in range(v)]
    
    # At the beginnign all nodes are infinite distance away w/ no predecessor
    for i in range(v):
        dist[i] = float('inf')
        pred[i] = -1
    
    # Now source is first to be visited add distance as 0
    visited[src] = True
    dist[src] = 0
    queue.append(src)
    
    # BFS alg
    while queue:
        curr = queue.popleft()
        for i in range(len(list[curr])):
            if not visited[list[curr][i]]:
                visited[list[curr][i]] = True
                dist[list[curr][i]] = dist[curr] + 1
                pred[list[curr][i]] = curr
                queue.append(list[curr][i])
                
                # We stop BFS when destination is reached
                if list[curr][i] == dest:
                    return True
    return False

def print_path(pred, dest):
    # Array to store path
    path = []
    last_node = dest
    path.append(last_node)
    
    while pred[last_node] != -1:
        path.append(pred[last_node])
        last_node = pred[last_node]
    
    # Printing path out by starting at path ang going backward
    for i in range(len(path)-1, -1, -1):
        if(i != 0): print(path[i], end="->")
        else: print(path[i])

def find_shortest_distance(adj, src, dest, v):
    # Array to store the path
    pred = [0 for i in range(v)]
    
    # Array to store distance from source to each vertex
    dist = [0 for i in range(v)]

    if not bfs(adj, src, dest, v, pred, dist):
        print("The distance is infinity :( (root and goal are not connected)")
        return -1
    
    # Print the path from r to g
    print("The root and goal are connected!")
    print_path(pred, dest)
    print("The distance is:", dist[dest])
    
    return dist[dest]

#GRAPHS CREATED AND RUN BELOW:

# GRAPH A
print("GRAPH A:")
v = 6  # Number of verticies in graph
list = [[] for i in range(v)] # List for storing which vertices are connected
add_edge(list, 0, 1)  # 0 is root r
add_edge(list, 1, 2)
add_edge(list, 2, 3)
add_edge(list, 2, 4)
add_edge(list, 3, 5)
add_edge(list, 4, 5)
src = 0  # r vertex
dest = 4  # g vertex
find_shortest_distance(list, src, dest, v)
print("\n")

# GRAPH B
print("GRAPH B:")
v = 6  # Number of verticies in graph
list = [[] for i in range(v)] # List for storing which vertices are connected
add_edge(list, 0, 1)  # 0 is root r
add_edge(list, 1, 2)
add_edge(list, 2, 3)
add_edge(list, 3, 4)
add_edge(list, 4, 5)
src = 0  # r vertex
dest = 5  # g vertex
find_shortest_distance(list, src, dest, v)
print("\n")

# GRAPH C
print("GRAPH C:")
v = 7  # Number of verticies in graph
list = [[] for i in range(v)] # List for storing which vertices are connected
add_edge(list, 0, 1)  # 0 is root r
add_edge(list, 0, 2)
add_edge(list, 1, 3)
add_edge(list, 2, 3)
add_edge(list, 3, 4)
add_edge(list, 3, 5)
add_edge(list, 4, 6)
add_edge(list, 5, 6)
src = 0  # r vertex
dest = 6  # g vertex
find_shortest_distance(list, src, dest, v)
print("\n")

# GRAPH D
print("GRAPH D:")
v = 7  # Number of verticies in graph
list = [[] for i in range(v)] # List for storing which vertices are connected
add_edge(list, 0, 1)  # 0 is root r
add_edge(list, 1, 2)
add_edge(list, 2, 3)
add_edge(list, 3, 4)
add_edge(list, 3, 5)
add_edge(list, 3, 5)
add_edge(list, 4, 5)
add_edge(list, 5, 6)
src = 0  # r vertex
dest = 4  # g vertex
find_shortest_distance(list, src, dest, v)
print("\n")

# GRAPH E
print("GRAPH E:")
v = 9  # Number of verticies in graph
list = [[] for i in range(v)] # List for storing which vertices are connected
add_edge(list, 0, 1)  # 0 is root r
add_edge(list, 1, 2)
add_edge(list, 1, 3)
add_edge(list, 2, 3)
add_edge(list, 3, 4)

add_edge(list, 5, 5)

add_edge(list, 6, 7)
add_edge(list, 6, 8)
add_edge(list, 7, 8)
src = 0  # r vertex
dest = 8  # g vertex
find_shortest_distance(list, src, dest, v)
print("\n")