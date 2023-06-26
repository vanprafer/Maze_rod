from model import MazeState


def is_empty(maze, x, y):
    """Checks if there is no wall at coordinates (x, y) 

    Args:
        maze (List[List[str]]): objective maze
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        bool: True if there is no wall at coordinates (x, y) 
    """
    
    # Generalizes the '#' character as wall
    return maze[y][x] != '#'


def possible_movs(maze, s):
    """Returns a list with every possible move from state s

    Args:
        maze (List[List[str]]): objective maze
        s (MazeState): current state in the maze

    Returns:
        List[str]: a list of elements that represent the different moves you can make. They can be either 'W', 'E', 'S', 'N' or 'R' 
    """
    h = len(maze)
    w = len(maze[0])
    
    movs = []

    # Each case tests different possible empty blocks depending on the move you want to make. Borders are also checked
    if s.o:
        if s.x > 1 and is_empty(maze, s.x - 2, s.y): movs.append('W')
        if s.x < (w - 2) and is_empty(maze, s.x + 2, s.y): movs.append('E')
        if s.y > 0 and is_empty(maze, s.x, s.y - 1) and is_empty(maze, s.x - 1, s.y - 1) and is_empty(maze, s.x + 1, s.y - 1): movs.append('N')
        if s.y < (h - 1) and is_empty(maze, s.x, s.y + 1) and is_empty(maze, s.x - 1, s.y + 1) and is_empty(maze, s.x + 1, s.y + 1): movs.append('S')
    
    else:
        if s.x > 0 and is_empty(maze, s.x - 1, s.y) and is_empty(maze, s.x - 1, s.y - 1) and is_empty(maze, s.x - 1, s.y + 1): movs.append('W')
        if s.x < (w - 1) and is_empty(maze, s.x + 1, s.y) and is_empty(maze, s.x + 1, s.y - 1) and is_empty(maze, s.x + 1, s.y + 1): movs.append('E')
        if s.y > 1 and is_empty(maze, s.x, s.y - 2): movs.append('N')
        if s.y < (h - 2) and is_empty(maze, s.x, s.y + 2): movs.append('S')
    
    # Checks the entire neighborhood in order to rotate avoiding collisions
    if (s.x > 0 and s.x < (w - 1) and s.y > 0 and s.y < (h - 1) and 
        is_empty(maze, s.x - 1, s.y) and is_empty(maze, s.x + 1, s.y) and 
        is_empty(maze, s.x, s.y - 1) and is_empty(maze, s.x, s.y + 1) and
        is_empty(maze, s.x - 1, s.y - 1) and is_empty(maze, s.x + 1, s.y - 1) and
        is_empty(maze, s.x - 1, s.y + 1) and is_empty(maze, s.x + 1, s.y + 1)): 
        movs.append('R')

    return movs


def next_state(state, mov):
    """Returns a new state from the previous position and an action returned by possible_movs

    Args:
        state (MazeState): current state in the maze
        mov (str): action to perform

    Returns:
        MazeState: next state
    """
    new_state = MazeState(state.x, state.y, state.o)
    
    if mov == 'W': new_state.x -= 1
    if mov == 'E': new_state.x += 1
    if mov == 'N': new_state.y -= 1
    if mov == 'S': new_state.y += 1
    if mov == 'R': new_state.o = not new_state.o
    
    return new_state


def make_movement(maze, states):
    """Returns a list with every possible move that can come from any of the given ones 

    Args:
        maze (List[List[str]]): objective maze
        states (List[MazeState]): list of states

    Returns:
        List[MazeState]: every possible move 
    """
    nxt_pos_sates = []
    
    for state in states:
        for mov in possible_movs(maze, state):
            nxt_pos_sates.append(next_state(state, mov))
    
    return nxt_pos_sates


def breadth_first_search(maze):
    """Breadth First Search algorithm. Uses a graph search in order to obtain the shortest route from the starting position to the end of the maze

    Args:
        maze (List[List[str]]): objective maze

    Returns:
        int: number that represents the minimum movements to make to solve the maze. Returns -1 if it is not possible
    """
    states = [MazeState(1, 0, True)]
    seen = {states[0]}
    n_movs = 0
    
    h = len(maze)
    w = len(maze[0])
    
    # Iterates while no final state is found
    while not any(i.is_final(w, h) for i in states):
        states = make_movement(maze, states)
        
        states = list(filter(lambda i: i not in seen, states))
        
        if len(states) == 0:
            return -1
        
        n_movs += 1
        
        seen.update(states)
        
    return n_movs
        
        
def solution(maze):
    """Solves the proposed maze problem by means of BFS

    Args:
        maze (List[List[str]]): objective maze

    Returns:
        int: number that represents the minimum movements to make to solve the maze. Returns -1 if it is not possible
    """
    return breadth_first_search(maze)
