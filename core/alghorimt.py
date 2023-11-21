#%%
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

class CityGrid:
    def __init__(self, n, m, obstructed_prob=0.3):
        self.n = n
        self.m = m
        self.grid = np.random.rand(n, m) < obstructed_prob

    def visualize(self):
        plt.imshow(self.grid, cmap='gray', interpolation='none')
        plt.title('City Grid')
        plt.show()

    def place_tower(self, row, col, range_r):
        for i in range(max(0, row - range_r), min(self.n, row + range_r + 1)):
            for j in range(max(0, col - range_r), min(self.m, col + range_r + 1)):
                self.grid[i, j] = 2  # Marking tower coverage as 2

    def visualize_towers(self):
        grid_copy = np.copy(self.grid)
        grid_copy[self.grid == 2] = 0  # Reset tower coverage to 0 for visualization
        plt.imshow(grid_copy, cmap='viridis', interpolation='none')
        plt.title('City Grid with Towers')
        plt.show()

    def distance(self, tower1, tower2):
        return abs(tower1[0] - tower2[0]) + abs(tower1[1] - tower2[1])

    def min_towers(self, range_r):
        towers = []
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i, j] != 1:  # Check if it's not an obstructed block
                    towers.append((i, j))

        # Generate all possible combinations of towers
        tower_combinations = list(combinations(towers, 2))

        # Sort tower combinations by distance
        tower_combinations.sort(key=lambda x: self.distance(x[0], x[1]))

        selected_towers = set()
        for tower_pair in tower_combinations:
            if not any(tower in selected_towers for tower in tower_pair):
                selected_towers.add(tower_pair[0])
                selected_towers.add(tower_pair[1])

        # Visualize selected towers
        for tower in selected_towers:
            self.place_tower(tower[0], tower[1], range_r)

        self.visualize_towers()

# Example usage
city = CityGrid(10, 10)
city.visualize()

tower_range = 3
city.min_towers(tower_range)

# %%
