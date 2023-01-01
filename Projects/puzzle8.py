import copy
import queue


class Node:

    def __init__(self, grid=None):
        if grid is None:
            grid = [[3, 6, 8], [1, " ", 4], [7, 2, 5]]
        self.grid = grid
        self.neighbors = []

    def __lt__(self, other):
        return self.__hash__() < other.__hash__()

    def __gt__(self, other):
        return self.__hash__() > other.__hash__()

    def __eq__(self, other):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True

    def __hash__(self):
        s = ""
        for row in self.grid:
            for col in row:
                if col == " ":
                    s += "0"
                else:
                    s += str(col)
        return int(s)

    def euc_dist(self):
        distance = 0
        win_board = [[1, 2, 3], [4, 5, 6], [7, 8, " "]]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                num = self.grid[i][j]
                for num_row in range(len(win_board)):
                    for num_col in range(len(win_board[num_row])):
                        if win_board[num_row][num_col] == num:
                            num_dist = abs(num_row-i) + abs(num_col-j)
                distance += num_dist
        return distance

    def check_win(self):
        return self.grid == [[1, 2, 3], [4, 5, 6], [7, 8, " "]]

    def find_empty(self):
        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                if self.grid[i][k] == " ":
                    return i, k

    def __str__(self):
        string = ""
        for i in self.grid:
            for k in i:
                string += str(k) + " "
            string += "\n"
        return string


class Tree:

    def __init__(self, root):
        self.root = root

    def gen_neighbors(self, node):
        c = None
        row, col = node.find_empty()
        down = row + 1
        up = row - 1
        left = col - 1
        right = col + 1

        if down <= 2:
            c = copy.deepcopy(node.grid)
            temp = node.grid[down][col]
            c[down][col] = " "
            c[row][col] = temp
            n1 = Node(c)
            node.neighbors.append(n1)

        if up >= 0:
            c = copy.deepcopy(node.grid)
            temp = node.grid[up][col]
            c[up][col] = " "
            c[row][col] = temp
            n2 = Node(c)
            node.neighbors.append(n2)

        if left >= 0:
            c = copy.deepcopy(node.grid)
            temp = node.grid[row][left]
            c[row][left] = " "
            c[row][col] = temp
            n3 = Node(c)
            node.neighbors.append(n3)

        if right <= 2:
            c = copy.deepcopy(node.grid)
            temp = node.grid[row][right]
            c[row][right] = " "
            c[row][col] = temp
            n4 = Node(c)
            node.neighbors.append(n4)

    def bfs(self):
        q = [(self.root, [self.root])]
        visited = set()
        while len(q) != 0:
            current, path = q.pop(0)
            visited.add(current)
            if current.check_win():
                return path
            self.gen_neighbors(current)
            for nd in current.neighbors:
                if nd not in visited:
                    q.append((nd, path + [nd]))

    def a_star_search(self):
        t = 0
        current = self.root
        q = queue.PriorityQueue()
        depth = 0
        h = current.euc_dist()
        q.put((depth+h, current, [current]))
        visited = set()
        while not q.empty():
            f, current, path = q.get()
            if current.check_win():
                return path
            if current not in visited:
                self.gen_neighbors(current)
                visited.add(current)
                depth += 1
                for nd in current.neighbors:
                    t += 1
                    q.put((depth+nd.euc_dist(), nd, path+[nd]))
        return []


default = Node()
puzzle_tree = Tree(default)
x = puzzle_tree.a_star_search()
for n in x:
    print(n)