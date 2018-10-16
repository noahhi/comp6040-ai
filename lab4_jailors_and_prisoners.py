# check if a state is valid (ie. can't have negative number of jailors or convicts) 
def is_valid(state):
	if state[0] < 0 or state[1] < 0 or state[3] < 0 or state[4] < 0:
		return False 
	
	return True
    
# check if the jailors get overrun in a given state 
def is_safe(state):
	if state[0] > 0 and state[0] < state[1]:
		# convicts on left bank get overrun
		return False 
	
	if state[3] > 0 and state[3] < state[4]:
		# convicts on right bank get overrun
		return False 
	
	return True 


# check if goal state completed 
def is_goal(state):
	if state[0] == 0 and state[1] == 0:
		# every jailor and convict has crossed the river 
		return True 

# yields possible moves from current state 	
def move(state):
	jl, cl, boat, jr, cr = state 

	########## move 2 jailors ###########################
	if boat == 0: 
		move2jailors = [jl-2,cl,1,jr+2,cr]
	else:
		move2jailors = [jl+2,cl,0,jr-2,cr]
	if is_valid(move2jailors) and is_safe(move2jailors):
		yield move2jailors
		
        ########## move 2 convicts ###########################    
	if boat == 0: 
		move2convicts = [jl,cl-2,1,jr,cr+2]
	else:
		move2convicts = [jl,cl+2,0,jr,cr-2]
	if is_valid(move2convicts) and is_safe(move2convicts):
		yield move2convicts
		
	########## move 1 convict ############################
	if boat == 0:
		moveconvict = [jl,cl-1,1,jr,cr+1]
	else:
		moveconvict = [jl,cl+1,0,jr,cr-1]
	if is_valid(moveconvict) and is_safe(moveconvict):
		yield moveconvict
	
	########## move 1 jailor ############################
	if boat == 0:
		movejailor = [jl-1,cl,1,jr+1,cr]
	else:
		movejailor = [jl+1,cl,0,jr-1,cr]
	if is_valid(movejailor) and is_safe(movejailor):
		yield movejailor
			
	########## move 1 of each ###########################
	if boat == 0:
		moveboth = [jl-1,cl-1,1,jr+1,cr+1]
	else:
		moveboth = [jl+1,cl+1,0,jr-1,cr-1]
	if is_valid(moveboth) and is_safe(moveboth):
		yield moveboth
		
		
# perform dfs recursively to find a solution		
def dfs_rec(path):
	if is_goal(path[-1]):
		return path
	else:
		for nextState in move(path[-1]):
			if nextState not in path:
				nextPath = path+[nextState]
				solution = dfs_rec(nextPath)
				if solution != None:
					return solution
	return None

# perform dfs iteratively via a stack 
def dfs_iter(intial_state):
    stack = [[intial_state]]
    while len(stack) > 0:
        path = stack.pop()
        if is_goal(path[-1]):
            return path 
        for nextState in move(path[-1]):
            if nextState not in path:
                nextPath = path+[nextState]
                stack.append(nextPath)

# given path to solution, display nicely 
def display_solution(solution):
    if solution == None:
        print('There is no solution')
        return 
    count = 0
    for step in solution:
        print('state {0:2} : {1}'.format(count,step)) 
        count += 1


# define initial state and goal state, and search for solution 
def main():
    # state[0]: number of jailors on left bank 
    # state[1]: number of convicts on left bank 
    # state[2]: 0 if boat on left bank, 1 if boat on right bank 
    # state[3]: number of jailors on right bank 
    # state[4]: number of convicts on right bank
    
    initial_state = [3,3,0,0,0]
    # sol = dfs_rec([initial_state])
    sol = dfs_iter(initial_state) 
    display_solution(sol)

if __name__ == "__main__":
    main()



                   
