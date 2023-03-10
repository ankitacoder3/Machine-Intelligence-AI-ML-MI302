"""
You can create any other helper funtions.
Do not modify the given functions
"""

import queue
import copy
from collections import deque

def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []

    # TODO
                            
    Priority_Queue = queue.PriorityQueue()             
    Priority_Queue.put((heuristic[start_point], ([start_point], start_point, 0)))
    n = len(cost)                                               
    Explored_Set = [0 for i in range(n)] 

    while(Priority_Queue.qsize() != 0):

        Cost_1, Start_Node = Priority_Queue.get()
        path = Start_Node[0]
        node = Start_Node[1]
        Cost_Node = Start_Node[2]

        if Explored_Set[node] == 0:
            
            Explored_Set[node] = 1

            if node in goals:
                
                return path

            for x in range(1, n):
                
                if cost[node][x] > 0 and Explored_Set[x] == 0:

                    Cost_Final = Cost_Node + cost[node][x]
                    Cost_2 = Cost_Final + heuristic[x]
                    Priority_1 = copy.deepcopy(path)
                    Priority_1.append(x)
                    Priority_Queue.put((Cost_2, (Priority_1, x, Cost_Final)))

    return list()
    #return path


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(liStack of ints)
    """
    #path = []
    # TODO
    
    Stack = deque()
    Stack.append({"node": start_point,"path": [start_point]})
    Nodes_Visited = set()
    
    while (Stack):
        
        Node_Prev = Stack.pop()

        if Node_Prev["node"] in Nodes_Visited:
            
            continue

        Nodes_Visited.add(Node_Prev["node"])

        if(Node_Prev["node"] in goals):
            
            return Node_Prev["path"]

        Adjacent_Value = Adjacent(cost[Node_Prev["node"]])

        for z in Adjacent_Value:
            
            if z not in Nodes_Visited:
                
                Node_n = {"node": z,"path": Node_Prev["path"] + [z]}
                Stack.append(Node_n)
                
    return []
    #return path

#helper functions                
def Adjacent(Adjacent_List):
    
    Adj_List = []

    for key, value in enumerate(Adjacent_List[1::], start=1):

        if value > 0:
            
            Adj_List.append(key)

    return Adj_List[::-1]

    
