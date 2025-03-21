from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = {recipe: 0 for recipe in recipes}  # Initialize all recipes in in_degree

        # Build the graph and in-degree count
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])  # Map ingredient to recipe
            in_degree[recipes[i]] = len(ingredients[i])  # Number of required ingredients

        # Topological sort using BFS
        available = deque(supplies)
        output = []

        while available:
            ing = available.popleft()
            if ing in graph:  # Only process if it's an ingredient in the graph
                for rcp in graph[ing]:
                    in_degree[rcp] -= 1
                    if in_degree[rcp] == 0:  # If all ingredients are available
                        available.append(rcp)
                        output.append(rcp)

        return output
