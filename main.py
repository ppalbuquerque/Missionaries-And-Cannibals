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

def BFS(State_Queue, Max, Boat):
    Actual_State = State_Queue.pop(0)
    Actual_State.print_state()
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


if __name__ == "__main__":
    missionarys = int(raw_input("Quantos missionarios ao total :"))
    cannibals = int(raw_input("Quantos cannibais ao total :"))
    Boat = int(raw_input("Quantas pessoas cabem no barco: "))
    initial_state = State(missionarys,cannibals, 0)
    State_Queue = []
    State_Queue.append(initial_state)
    BFS(State_Queue, missionarys, Boat)
