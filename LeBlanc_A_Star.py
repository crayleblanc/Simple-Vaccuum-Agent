import numpy as np
import math


class vaccuum_matrix():
    def __init__(self, graphMatrix):
        self.graphMatrix=graphMatrix
        self.agentPosition=np.where(graphMatrix=='A')
        self.totalCost=0
        self.agentAction=""

    #gives the index of the dirty square that is closest to the agent
    def closest_dirt_position(self):
        distanceMatrix=[]
        dirtPositions=[]
        agentRow,agentCol=self.agentPosition

        #returns the arrays for the dirt row positions, and the dirt column positions
        for dirtRow,dirtCol in zip(*np.where(self.graphMatrix=='1')):
            dirtPositions.append((dirtRow,dirtCol))

            #this is the distance formula ==> sqrt( (y2-y1)^2 + (x2-x1)^2 )
            h1_distance=math.sqrt(math.pow(dirtRow-agentRow,2) + math.pow(dirtCol-agentCol,2))
            distanceMatrix.append(h1_distance)

        #find the min value in the distance matrix
        minValue=np.min(distanceMatrix)

        #this returns the tuple of the position for whatever dirt square is closest to the agent
        return dirtPositions[distanceMatrix.index(minValue)]
    
    #given the closest piece of dirt to the agent, this function will determine which movement
    #up,down,left,or right will get the agent nearest to the closest piece of dirt
    def find_direction(self):
        dirtRow,dirtCol=self.closest_dirt_position()

        agentMoves=[]
        allowable_agent_moves=[]

        currentAgentRow,currentAgentCol=self.agentPosition

        #find the position of the potential moves
        agentUpRow,agentUpCol=currentAgentRow-1,currentAgentCol
        agentDownRow,agentDownCol=currentAgentRow+1,currentAgentCol
        agentLeftRow,agentLeftCol=currentAgentRow,currentAgentCol-1
        agentRightRow,agentRightCol=currentAgentRow,currentAgentCol+1

        agentMoves.append((agentUpRow,agentUpCol))
        agentMoves.append((agentDownRow,agentDownCol))
        agentMoves.append((agentLeftRow,agentLeftCol))
        agentMoves.append((agentRightRow,agentRightCol))

        #get the dimensions of the matrix to determine which moves are allowable
        matrix_num_rows, matrix_num_cols= self.graphMatrix.shape

        for possibleAgentRow, possibleAgentCol in agentMoves:
            #only allow the moves that wouldn't go beyond the bounds of the matrix
            if(possibleAgentRow in range(0,matrix_num_rows) and possibleAgentCol in range(0, matrix_num_cols)):
                allowable_agent_moves.append((possibleAgentRow,possibleAgentCol))
        
        distanceMatrix=[]

        #for the moves that are allowed, find the distance that the agent is from the dirt
        for allowedRow,allowedCol in allowable_agent_moves:
            min_distance=math.sqrt(math.pow(dirtRow-allowedRow,2) + math.pow(dirtCol-allowedCol,2))
            distanceMatrix.append(min_distance)
        
        #find the minimum distance that the agent can be within the dirt, given one move
        movement_min_val=np.min(distanceMatrix)

        #find the agent move that gives the minimum distance
        bestMoveRow,bestMoveCol=allowable_agent_moves[distanceMatrix.index(movement_min_val)]

        #this gives the relative position of the agent after the movement
        agentMovement=(currentAgentRow-bestMoveRow,currentAgentCol-bestMoveCol)

        if agentMovement==(1,0):
            self.move_agent_up()
        elif agentMovement==(-1,0):
            self.move_agent_down()
        elif agentMovement==(0,1):
            self.move_agent_left()
        elif agentMovement==(0,-1):
            self.move_agent_right()
        else:
            print('Something has gone horribly wrong')

    #returns the position of the dirt square that is farthest from the agent
    def farthest_dirt_position(self):
        distanceMatrix=[]
        dirtPositions=[]
        agentRow,agentCol=self.agentPosition

        #returns the arrays for the dirt row positions, and the dirt column positions
        for dirtRow,dirtCol in zip(*np.where(self.graphMatrix=='1')):
            dirtPositions.append((dirtRow,dirtCol))

            #this is the distance formula ==> sqrt( (y2-y1)^2 + (x2-x1)^2 )
            h1_distance=math.sqrt(math.pow(dirtRow-agentRow,2) + math.pow(dirtCol-agentCol,2))
            distanceMatrix.append(h1_distance)

        #find the max value in the distance matrix
        maxValue=np.min(distanceMatrix)

        #this returns the tuple of the position for whatever dirt square is closest to the agent
        return dirtPositions[distanceMatrix.index(maxValue)]
    
    def find_direction_h2(self):
        dirtRow,dirtCol=self.farthest_dirt_position()

        agentMoves=[]
        allowable_agent_moves=[]

        currentAgentRow,currentAgentCol=self.agentPosition

        #find the position of the potential moves
        agentUpRow,agentUpCol=currentAgentRow-1,currentAgentCol
        agentDownRow,agentDownCol=currentAgentRow+1,currentAgentCol
        agentLeftRow,agentLeftCol=currentAgentRow,currentAgentCol-1
        agentRightRow,agentRightCol=currentAgentRow,currentAgentCol+1

        agentMoves.append((agentRightRow,agentRightCol))
        agentMoves.append((agentLeftRow,agentLeftCol))
        agentMoves.append((agentDownRow,agentDownCol))
        agentMoves.append((agentUpRow,agentUpCol))

        #get the dimensions of the matrix to determine which moves are allowable
        matrix_num_rows, matrix_num_cols= self.graphMatrix.shape

        for possibleAgentRow, possibleAgentCol in agentMoves:
            #only allow the moves that wouldn't go beyond the bounds of the matrix
            if(possibleAgentRow in range(0,matrix_num_rows) and possibleAgentCol in range(0, matrix_num_cols)):
                allowable_agent_moves.append((possibleAgentRow,possibleAgentCol))
        
        distanceMatrix=[]

        moveCount=1

        #for the moves that are allowed, find the distance that the agent is from the dirt
        for allowedRow,allowedCol in allowable_agent_moves:
            min_distance=math.sqrt(math.pow(dirtRow-allowedRow,2) + math.pow(dirtCol-allowedCol,2))
            distanceMatrix.append(min_distance)
        
        #find the minimum distance that the agent can be within the dirt, given one move
        movement_min_val=np.min(distanceMatrix)

        #find the agent move that gives the minimum distance
        bestMoveRow,bestMoveCol=allowable_agent_moves[distanceMatrix.index(movement_min_val)]

        #this gives the relative position of the agent after the movement
        agentMovement=(currentAgentRow-bestMoveRow,currentAgentCol-bestMoveCol)

        if agentMovement==(1,0):
            self.move_agent_up()
        elif agentMovement==(-1,0):
            self.move_agent_down()
        elif agentMovement==(0,1):
            self.move_agent_left()
        elif agentMovement==(0,-1):
            self.move_agent_right()
        else:
            print('Something has gone horribly wrong')

    def print_matrix(self):
        print(self.graphMatrix)

    #returns true if still at least one dirty square, false if none
    def not_clean(self):
        return len(self.graphMatrix[self.graphMatrix=='1'])>=1
    
    #gives the number of remaining dirty squares, used for total cost calculation
    def number_dirty_squares(self):
        return len(self.graphMatrix[self.graphMatrix=='1'])

    def move_agent_up(self):
        currentAgentRow,currentAgentCol=self.agentPosition
        self.graphMatrix[self.agentPosition]='0'
        self.agentPosition=currentAgentRow-1,currentAgentCol
        self.graphMatrix[self.agentPosition]='A'
        self.agentAction="Move Up"
    
    def move_agent_down(self):
        currentAgentRow,currentAgentCol=self.agentPosition
        self.graphMatrix[self.agentPosition]='0'
        self.agentPosition=currentAgentRow+1,currentAgentCol
        self.graphMatrix[self.agentPosition]='A'
        self.agentAction="Move Down"
    
    def move_agent_left(self):
        currentAgentRow,currentAgentCol=self.agentPosition
        self.graphMatrix[self.agentPosition]='0'
        self.agentPosition=currentAgentRow,currentAgentCol-1
        self.graphMatrix[self.agentPosition]='A'
        self.agentAction="Move Left"
    
    def move_agent_right(self):
        currentAgentRow,currentAgentCol=self.agentPosition
        self.graphMatrix[self.agentPosition]='0'
        self.agentPosition=currentAgentRow,currentAgentCol+1
        self.graphMatrix[self.agentPosition]='A'
        self.agentAction="Move Right"

    #this will solve the problem using the h1 heuristic
    def solve_problem_h1(self):
        self.print_matrix()
        print('step 0: initial position\n')

        step_count=1

        while(self.not_clean()):
            self.find_direction()

            #each turn has a step cost of 1
            self.totalCost=self.totalCost+1

            #after each step, there is a cost of 2 for each remaining dirty square
            self.totalCost=self.totalCost + 2*(self.number_dirty_squares())

            self.print_matrix()

            print("step {}: {}".format(step_count, self.agentAction))
            print("f(n):{}\n".format(self.totalCost))
            step_count=step_count+1
    
    def solve_problem_h2(self):
        self.print_matrix()
        print('step 0: initial position\n')

        step_count=1

        while(self.not_clean()):
            self.find_direction_h2()

            #each turn has a step cost of 1
            self.totalCost=self.totalCost+1

            #after each step, there is a cost of 2 for each remaining dirty square
            self.totalCost=self.totalCost + 2*(self.number_dirty_squares())

            self.print_matrix()

            print("step {}: {}".format(step_count, self.agentAction))
            print("f(n):{}\n".format(self.totalCost))
            step_count=step_count+1


#this the matrix that represents the agent and the dirty room
#the 1's are the dirty squares, the 0's are the clean squares
#A is the agent
dirt_matrix=np.array([
                        ['1','1','1','1','1'],
                        ['0','0','0','0','0'],
                        ['0','0','0','0','0'],
                        ['0','0','0','0','0'],
                        ['A','0','0','0','0']
                    ])

#the action of moving the agent (up,down,left, or right) is determined by what
#will minimize the distance between the agent and the closest dirty square(h1)

#the second hueristic will try to minimize the distance between the agent and the farthest square

#problem1=vaccuum_matrix(graphMatrix=dirt_matrix)
#problem1.solve_problem_h1()

problem2=vaccuum_matrix(graphMatrix=dirt_matrix)
problem2.solve_problem_h2()