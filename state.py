class State():
    def __init__(self, missionarys, cannibals, side):
        self.right_side_missionarys = missionarys
        self.right_side_cannibals = cannibals
        #0 for right side, and 1 for left side
        self.side_of_boat = side;
        self.states_children = []
        self.cost = 0
        self.dad = None

    def number_of_missionarys_greater(self,States,Max):
        for s in States:
            if(s.right_side_missionarys >= s.right_side_cannibals or s.right_side_missionarys == 0):
                if(Max - s.right_side_missionarys >= Max - s.right_side_cannibals or
                Max - s.right_side_missionarys == 0):
                    if(s.right_side_missionarys >= 0 and s.right_side_cannibals >= 0):
                        if(s.right_side_missionarys <= Max and s.right_side_cannibals <= Max):
                            s.cost = self.cost + 1
                            s.dad = self
                            self.states_children.append(s)

    def generate_states(self, Max, Boat):
        #Generating all the sates for only 1 person in the boat
        States = []
        if self.side_of_boat == 0:
            M = Boat
            i = 0
            while(M >= 1):
                C = Boat - i
                while(C >= 0):
                    States.append(State(self.right_side_missionarys - (M - C),
                    self.right_side_cannibals - C, abs(self.side_of_boat - 1)))
                    C -= 1
                M -= 1
                i += 1
            self.number_of_missionarys_greater(States,Max)
        else:
            M = Boat
            i = 0
            while(M >= 1):
                C = Boat - i
                while(C >= 0):
                    States.append(State(self.right_side_missionarys + (M - C),
                    self.right_side_cannibals + C, abs(self.side_of_boat - 1)))
                    C -= 1
                M -= 1
                i += 1
            self.number_of_missionarys_greater(States, Max)

    def greedyHeuristic(self, Max):
        return (self.right_side_cannibals + self.right_side_missionarys) - (Max - self.right_side_cannibals)

    def aStarHeuristic(self, Max):
        return self.greedyHeuristic(Max) + self.cost

    def printDads(self, Max):
        self.print_state(Max)
        if self.dad is not None:
            self.dad.printDads(Max)

    def print_state(self, Max):
        print "_________________________"
        print "| G : " + str(self.cost) + " | H : "+ str(self.greedyHeuristic(Max)) + " | F : "+ str(self.aStarHeuristic(Max)) + "|"
        print "| M : " + str(self.right_side_missionarys) + " | C : " + str(self.right_side_cannibals) + "  | B : " + str(self.side_of_boat) + "|"
        print "-------------------------"

    def print_children_states(self):
        for s in self.states_children:
            s.print_state()
        print "_______"
