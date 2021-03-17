class MCState:
    
    moves = [(-1,0,1,0,1),(0,-1,0,1,1),(-1,-1,1,1,1),(-2,0,2,0,1),(0,-2,0,2,1),
             (1,0,-1,0,-1),(0,1,0,-1,-1),(1,1,-1,-1,-1),(2,0,-2,0,-1),(0,2,0,-2,-1)]
    
    
    def __init__(self,state):
        self.state = state

    def allowableState(self): #checks if state is none goal endstate 
        if( (self.state[0]< self.state[1]) and self.state[0]!=0):
            return False
        elif((self.state[2] < self.state[3]) and self.state[2] !=0):
            return False
        return True
    def legalMove(self): #checks if state is legal
        if(any(map(lambda x: x < 0, self.state))):
            return False
        elif(any(map(lambda x: x > 3, self.state))):
            return False
        elif(self.state[4] > 1):
            return False
        return True
    def goalTest(self):
        return self.state == MCState((0,0,3,3,1))

    def transition(self): #Returns all legal states
        possible_moves = []
        if self.state == (0,0,3,3,1):
            return possible_moves
        
        elif self.state != (0,0,3,3,1):
            possible_moves = []
            for i in self.moves:
                newState = tuple(map(sum, zip(i,self.state)))
                newState = MCState(newState)
                possible_moves += [newState]
        possible_moves = list(filter(lambda x: x.legalMove(), possible_moves))
        possible_moves = list(filter(lambda x: x.allowableState(), possible_moves))
        return possible_moves

    
    
    def __repr__(self):
        return str(self.state)
    def __str__(self):
        return str(self.state)

   # Performing the search    
def search(dfs=True):
    
    from collections import deque
    
    root = MCState((3,3,0,0,0))

    goal = (0,0,3,3,1)
    
    search = deque()
    
    statesSeen = set()
    
    solutions = list()
    
    search.append(root)
    
    loopCount = 0
    
    maxLoop = 10000
    
    while len(search) > 0:
        loopCount += 1
        if loopCount > maxLoop:
            print(len(search))
            break
    
    
        currentState = search.pop()
        
        
        if currentState == root:
                print("Initial state:" , root)
        else:
                print("State " + str(loopCount), ":" + " " + str(currentState))
        print()
        if goal not in statesSeen:
            print("            Possible nodes        ")    
        nextStates = currentState.transition()
        
        if goal in statesSeen:
            search.clear()
        else:
            for i in nextStates:
                print('[' + str(i)[1:-1] + ']', end = "   ")
        print()
        for possiblenextState in nextStates[::-1]:
            possiblestate = possiblenextState.state

            if possiblestate == goal:
                possiblestate == goal
                search.clear()
            
            if possiblestate not in statesSeen:
                
                
                if possiblenextState.goalTest():
                    continue

                    
                if dfs:
                    search.append(possiblenextState)
                else:
                    search.appendleft(possiblenextState)

                statesSeen.add(possiblestate)
    print("Solution Found: " + str(currentState))
    print()
    return solutions
    solutions.append(possiblenextState)

solDfs = search(True)
solBfs = search(False)


