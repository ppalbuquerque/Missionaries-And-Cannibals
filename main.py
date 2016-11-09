from state import State

Explored_States = []

def BackTracking(State):
    for s in Explored_States:
        if(State.right_side_missionarys == s.right_side_missionarys and
           State.right_side_cannibals == s.right_side_cannibals and
           State.side_of_boat == s.side_of_boat):
                return True
    return False

def Final_State(State):
    if(State.right_side_missionarys == 0
    and State.right_side_cannibals == 0
    and State.side_of_boat == 1):
        return True
    else:
        return False

def print_state_queue(State_Queue, Max):
    print '| Fronteira |'
    for s in State_Queue:
        s.print_state(Max)

def BFS(State_Queue, Max, Boat):
    Actual_State = State_Queue.pop(0)
    print_state_queue(State_Queue, Max)
    if(BackTracking(Actual_State)):
        BFS(State_Queue, Max, Boat)
    else:
        Explored_States.append(Actual_State)
        if(Final_State(Actual_State)):
            return
        Actual_State.generate_states(Max, Boat)
        for s in Actual_State.states_children:
            if(not BackTracking(s)):
                State_Queue.append(s)
        BFS(State_Queue, Max, Boat)

def DFS(State_Queue, Max, Boat):
    Actual_State = State_Queue.pop()
    print_state_queue(State_Queue, Max)
    if(BackTracking(Actual_State)):
        DFS(State_Queue, Max, Boat)
    else:
        Explored_States.append(Actual_State)
        if(Final_State(Actual_State)):
            return
        Actual_State.generate_states(Max, Boat)
        for s in Actual_State.states_children:
            if(not BackTracking(s)):
                State_Queue.append(s)
        DFS(State_Queue, Max, Boat)

def greedy(State_Queue, Max, Boat):
    State_Queue = sorted(State_Queue, key=lambda state: state.greedyHeuristic(Max), reverse=False)
    if len(State_Queue) == 0 :
        print "De merda ai!"
        return

    Actual_State = State_Queue.pop(0)
    del State_Queue[:]
    print_state_queue(State_Queue, Max)
    if(BackTracking(Actual_State)):
        greedy(State_Queue, Max, Boat)
    else:
        Explored_States.append(Actual_State)
        if(Final_State(Actual_State)):
            return
        Actual_State.generate_states(Max, Boat)
        for s in Actual_State.states_children:
            if(not BackTracking(s)):
                State_Queue.append(s)
        greedy(State_Queue, Max, Boat)

def aStar(State_Queue, Max, Boat):
    State_Queue = sorted(State_Queue, key=lambda state: state.aStarHeuristic(Max), reverse=False)
    Actual_State = State_Queue.pop(0)
    print_state_queue(State_Queue, Max)
    if(BackTracking(Actual_State)):
        aStar(State_Queue, Max, Boat)
    else:
        Explored_States.append(Actual_State)
        if(Final_State(Actual_State)):
            return
        Actual_State.generate_states(Max, Boat)
        for s in Actual_State.states_children:
            if(not BackTracking(s)):
                State_Queue.append(s)
        aStar(State_Queue, Max, Boat)

if __name__ == "__main__":
    missionarys = int(raw_input("Quantos missionarios e canibais ao total :"))
    cannibals = missionarys
    Boat = int(raw_input("Quantas pessoas cabem no barco: "))
    print "___________________________________________"
    print "| 0 - BFS | 1 - DFS | 2 - Greedy | 3 - A* |"
    print "-------------------------------------------"
    userChoise = int(raw_input("Qual metodo de busca voce deseja usar: "))

    initial_state = State(missionarys,cannibals, 0)
    State_Queue = []
    State_Queue.append(initial_state)
    if userChoise == 0:
        BFS(State_Queue, missionarys, Boat)
    elif userChoise == 1:
        DFS(State_Queue, missionarys, Boat)
    elif userChoise == 2:
        greedy(State_Queue, missionarys, Boat)
    elif userChoise == 3:
        aStar(State_Queue, missionarys, Boat)
