import numpy as np

from NeuralNetworks.StockFish import StockFishEngine
from src.Controllers.GenerateMovesController import get_moves_by_move_model
from src.Helpers.GameEngineHelpers.MakeMoveHelper import make_move
from src.Models.GameStateModel import GameState


class MCTSNode:
    stock_fish_engine = StockFishEngine()

    def __init__(self, state: GameState, parent=None):
        self.game_state: GameState = state
        self.parent: MCTSNode = parent
        self.children: list[MCTSNode] = []
        self.visits: int = 0
        self.score: int = 0

    def expand(self):
        legal_moves: list[int] = get_moves_by_move_model(self.game_state)
        for move in legal_moves:
            child_state = self.game_state.copy()
            child_state.push(move)
            self.children.append(MCTSNode(child_state, parent=self))

    def select_child(self, exploration_param):
        scores = [child.score / child.visits + exploration_param * np.sqrt(np.log(self.visits) / child.visits) for child
                  in self.children]
        max_score_idx = np.argmax(scores)
        return self.children[max_score_idx]

    def simulate(self):
        sim_state: GameState = self.game_state.copy()
        while not sim_state.is_game_over():
            legal_moves = get_moves_by_move_model(sim_state)
            random_move = np.random.choice([move for move in legal_moves])
            make_move(random_move, sim_state)
        return sim_state.result()

    def back_propagate(self, result):
        self.visits += 1
        self.score += result
        if self.parent:
            self.parent.back_propagate(result)
