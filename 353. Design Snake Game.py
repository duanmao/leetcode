class SnakeGame:
    direc = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.snake = collections.deque([[0, 0]])
        self.food = collections.deque(food)
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # print(self.board)
        mover, movec = self.direc[direction]
        r, c = self.snake[0]
        nr, nc = r + mover, c + movec
        # cross boundary
        if (nr < 0 or nc < 0 or nr >= self.height or nc >= self.width): return -1
        # bites its body
        if ([nr, nc] in self.snake and [nr, nc] != self.snake[-1]): return -1
        # move head
        self.snake.appendleft([nr, nc])
        if (self.food and self.snake[0] == self.food[0]):
            self.score += 1
            self.food.popleft()
            return self.score
        # move tail
        self.snake.pop()
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
