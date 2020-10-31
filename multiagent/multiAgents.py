# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util
import math
from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        "*** YOUR CODE HERE ***"

        # keep the position close to the food
        newFood = successorGameState.getFood().asList()
        minFoodist = float("inf")
        for food in newFood:
            minFoodist = min(minFoodist, manhattanDistance(newPos, food))

        # keep away the ghost
        for ghost in successorGameState.getGhostPositions():
            if (manhattanDistance(newPos, ghost) < 2):
                return -float('inf')
        
        return successorGameState.getScore() + 1.0/minFoodist

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
      """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
          Returns a list of legal actions for an agent
          agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
          Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
          Returns the total number of agents in the game
      """
      "*** YOUR CODE HERE ***"
      # game state, agent_index, depth
      return self.get_max(gameState, 0, 0)[0]

    def process_state(self, game_state, agent_index, depth):
      if depth is self.depth * game_state.getNumAgents() or game_state.isLose() or game_state.isWin():
        return self.evaluationFunction(game_state)
      if agent_index is 0:
        return self.get_max(game_state, agent_index, depth)[1]
      else:
        return self.get_min(game_state, agent_index, depth)[1]

    def get_max(self, game_state, agent_index, depth):
      result = (None, -float("inf"))
      for action in game_state.getLegalActions(agent_index):
        next_result = (action, 
        self.process_state(game_state.generateSuccessor(agent_index, action), (depth+1)%game_state.getNumAgents(), depth+1))
        result = max(result, next_result, key=lambda x: x[1])
      return result

    def get_min(self, game_state, agent_index, depth):
      result = (None, float("inf"))
      for action in game_state.getLegalActions(agent_index):
        next_result = (action, 
        self.process_state(game_state.generateSuccessor(agent_index, action), (depth+1)%game_state.getNumAgents(), depth+1))
        result = min(result, next_result, key=lambda x: x[1])
      return result

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
      """
        Returns the minimax action using self.depth and self.evaluationFunction
      """
      "*** YOUR CODE HERE ***"
      return self.get_max(gameState, 0, 0, -float('inf'), float('inf'))[0]

    def process_state(self, game_state, agent_index, depth, alpha, beta):
      
      if depth is self.depth * game_state.getNumAgents() or game_state.isLose() or game_state.isWin():
        return self.evaluationFunction(game_state)
      
      if agent_index is 0:
        return self.get_max(game_state, agent_index, depth, alpha, beta)[1]
      
      else:
        return self.get_min(game_state, agent_index, depth, alpha, beta)[1]
    
    def get_min(self, game_state, agent_index, depth, alpha, beta):
      
      result = (None, float('inf'))
      
      for action in game_state.getLegalActions(agent_index):  
        
        next_result = (action,
        self.process_state(game_state.generateSuccessor(agent_index, action), (depth+1)%game_state.getNumAgents(), depth+1, alpha, beta))
        
        result = min(result, next_result, key=lambda x: x[1])
        
        if result[1] < alpha:
          return result
        
        beta = min(beta, result[1])
      
      return result

    def get_max(self, game_state, agent_index, depth, alpha, beta):
      
      result = (None, -float('inf'))
      
      for action in game_state.getLegalActions(agent_index):
        
        next_result = (action,
        self.process_state(game_state.generateSuccessor(agent_index, action), (depth+1)%game_state.getNumAgents(), depth+1, alpha, beta))
        
        result = max(result, next_result, key=lambda x: x[1])
        
        if result[1] > beta:
          return result
        
        alpha = max(alpha, result[1])
      
      return result

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.get_max(gameState, 0, 0)[0]

    def process_state(self, game_state, agent_index, depth, action):
      if depth is self.depth * game_state.getNumAgents() or game_state.isLose() or game_state.isWin():
        return self.evaluationFunction(game_state)
      if agent_index is 0:
        return self.get_max(game_state, agent_index, depth)[1]
      else:
        return self.get_avg(game_state, agent_index, depth, action)[1]

    def get_max(self, game_state, agent_index, depth):
      result = (None, -float("inf"))
      for action in game_state.getLegalActions(agent_index):
        next_result = (action, 
        self.process_state(game_state.generateSuccessor(agent_index, action), (depth+1)%game_state.getNumAgents(), depth+1, action))
        result = max(result, next_result, key=lambda x: x[1])
      return result

    def get_avg(self, game_state, agent_index, depth, action):
      result = 0
      probability = 1.0 / len(game_state.getLegalActions(agent_index))
      for legal_action in game_state.getLegalActions(agent_index):
        next_result = self.process_state(game_state.generateSuccessor(agent_index, legal_action), (depth+1)%game_state.getNumAgents(), depth+1, action)
        result += next_result * probability
      return (action, result)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood().asList()

    minFoodist = float('inf')
    for food in newFood:
        minFoodist = min(minFoodist, manhattanDistance(newPos, food))

    ghostDist = 0
    for ghost in currentGameState.getGhostPositions():
        ghostDist = manhattanDistance(newPos, ghost)
        if (ghostDist < 2):
            return -float('inf')

    foodLeft = currentGameState.getNumFood()
    capsLeft = len(currentGameState.getCapsules())

    foodLeftMultiplier = 950050
    capsLeftMultiplier = 10000
    foodDistMultiplier = 950

    additionalFactors = 0
    if currentGameState.isLose():
        additionalFactors -= 50000
    elif currentGameState.isWin():
        additionalFactors += 50000

    return  1.0/(foodLeft + 1) * foodLeftMultiplier + ghostDist + \
            1.0/(minFoodist + 1) * foodDistMultiplier + \
            1.0/(capsLeft + 1) * capsLeftMultiplier + additionalFactors
# Abbreviation
better = betterEvaluationFunction

