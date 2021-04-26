from random import randint

class RubiksCube:
    SOLVED = [
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]],
        [[2, 2, 2],
         [2, 2, 2],
         [2, 2, 2]],
        [[3, 3, 3],
         [3, 3, 3],
         [3, 3, 3]],
        [[4, 4, 4],
         [4, 4, 4],
         [4, 4, 4]],
        [[5, 5, 5],
         [5, 5, 5],
         [5, 5, 5]],
    ]

    def __init__(self, size=3, config=None):
        self.size = 3
        self.front = [[0]*size]*size
        self.back = [[1]*size]*size
        self.top = [[2]*size]*size
        self.bottom = [[3]*size]*size
        self.left = [[4]*size]*size
        self.right = [[5]*size]*size

    def get_current_state(self):
        state = []

        # Front
        side = []
        for row in self.front:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        # Back
        side = []
        for row in self.back:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        # Top
        side = []
        for row in self.top:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        # Bottom
        side = []
        for row in self.bottom:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        # Left
        side = []
        for row in self.left:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        # Right
        side = []
        for row in self.right:
            r = []
            for col in row:
                r.append(col)
            side.append(r)
        state.append(side)

        return state

    def set_state(self, state):
        for r, row in enumerate(state[0]):
            self.front[r] = row
        for r, row in enumerate(state[1]):
            self.back[r] = row
        for r, row in enumerate(state[2]):
            self.top[r] = row
        for r, row in enumerate(state[3]):
            self.bottom[r] = row
        for r, row in enumerate(state[4]):
            self.left[r] = row
        for r, row in enumerate(state[5]):
            self.right[r] = row

    def get_score(self):
        state = self.get_current_state()
        score = 0
        for s in range(6):
            for r in range(self.size):
                for c in range(self.size):
                    if state[s][r][c] == self.SOLVED[s][r][c]:
                        score += 1
        return score
    
    def is_solved(self):
        state = self.get_current_state()
        for s in range(self.size):
            for r in range(self.size):
                for c in range(self.size):
                    if state[s][r][c] != self.SOLVED[s][r][c]:
                        return False
        return True

    def get_solved_state(self):
        result = []
        for i in range(6):
            result.append([[i]*self.size]*self.size)
        
        return result

    def rotate_front(self, clockwise):
        if clockwise:
            new_top = [i[0] for i in self.front[::-1]]
            new_right = self.front[0][:]
            new_bottom = [i[-1] for i in self.front[::-1]]
            new_left = self.front[-1][:]

            new_top_col = [i[-1] for i in self.left[::-1]]
            new_right_col = self.top[-1][:]
            new_bottom_col = [i[0] for i in self.right[::-1]]
            new_left_col = self.bottom[0][:]

        else:
            new_top = [i[-1] for i in self.front]
            new_right = self.front[-1][::-1]
            new_bottom = [i[0] for i in self.front]
            new_left = self.front[0][::-1]
        
            new_top_col = [i[0] for i in self.right]
            new_right_col = self.bottom[0][::-1]
            new_bottom_col = [i[-1] for i in self.left]
            new_left_col = self.top[-1][::-1]

        for i in range(self.size):
            self.front[i][0] = new_left[i]
            self.front[i][-1] = new_right[i]
            self.left[i][-1] = new_left_col[i]
            self.right[i][0] = new_right_col[i]
        self.front[0] = new_top
        self.front[-1] = new_bottom

        self.top[-1] = new_top_col
        self.bottom[0] = new_bottom_col

    def rotate_back(self, clockwise):
        if clockwise:
            new_top = [i[0] for i in self.back[::-1]]
            new_right = self.back[0][:]
            new_bottom = [i[-1] for i in self.back[::-1]]
            new_left = self.back[-1][:]

            new_left_col = self.top[0][::-1]
            new_top_col = [i[-1] for i in self.right]
            new_right_col = self.bottom[-1][::-1]
            new_bottom_col = [i[0] for i in self.left]

        else:
            new_top = [i[-1] for i in self.back]
            new_right = self.back[-1][::-1]
            new_bottom = [i[0] for i in self.back]
            new_left = self.back[0][::-1]
        
            new_left_col = self.bottom[-1][:]
            new_top_col = [i[0] for i in self.left[::-1]]
            new_right_col = self.top[0][:]
            new_bottom_col = [i[-1] for i in self.right[::-1]]

        for i in range(len(self.back)):
            self.back[i][0] = new_left[i]
            self.back[i][-1] = new_right[i]
            self.left[i][0] = new_left_col[i]
            self.right[i][-1] = new_right_col[i]
    
        self.back[0] = new_top
        self.back[-1] = new_bottom
        self.top[0] = new_top_col
        self.bottom[-1] = new_bottom_col

    def rotate_right(self, clockwise):
        if clockwise:
            new_top = [i[0] for i in self.right[::-1]]
            new_right = self.right[0][:]
            new_bottom = [i[-1] for i in self.right[::-1]]
            new_left = self.right[-1][:]

            new_front_col = [i[-1] for i in self.bottom]
            new_top_col = [i[-1] for i in self.front]
            new_back_col = [i[-1] for i in self.top]
            new_bottom_col = [i[0] for i in self.back[::-1]]

        else:
            new_top = [i[-1] for i in self.right]
            new_right = self.right[-1][::-1]
            new_bottom = [i[0] for i in self.right]
            new_left = self.right[0][::-1]

            new_front_col = [i[-1] for i in self.top]
            new_top_col = [i[0] for i in self.back[::-1]]
            new_back_col = [i[-1] for i in self.bottom]
            new_bottom_col = [i[-1] for i in self.front]
        
        for i in range(self.size):
            self.right[i][0] = new_left[i]
            self.right[i][-1] = new_right[i]

            self.front[i][-1] = new_front_col[i]
            self.top[i][-1] = new_top_col[i]
            self.back[i][0] = new_back_col[i]
            self.bottom[i][-1] = new_bottom_col[i]
        self.right[0] = new_top
        self.right[-1] = new_bottom

    def rotate_left(self, clockwise):
        if clockwise:            
            new_top = [i[0] for i in self.left[::-1]]
            new_right = self.left[0][:]
            new_bottom = [i[-1] for i in self.left[::-1]]
            new_left = self.left[-1][:]

            new_front_col = [i[0] for i in self.top]
            new_top_col = [i[-1] for i in self.back[::-1]]
            new_back_col = [i[0] for i in self.bottom]
            new_bottom_col = [i[0] for i in self.front]

        else:
            new_top = [i[-1] for i in self.left]
            new_right = self.left[-1][::-1]
            new_bottom = [i[0] for i in self.left]
            new_left = self.left[0][::-1]

            new_front_col = [i[0] for i in self.bottom]
            new_top_col = [i[0] for i in self.front]
            new_back_col = [i[0] for i in self.top]
            new_bottom_col = [i[-1] for i in self.back[::-1]]

        for i in range(self.size):
            self.left[i][0] = new_left[i]
            self.left[i][-1] = new_right[i]

            self.front[i][0] = new_front_col[i]
            self.top[i][0] = new_top_col[i]
            self.back[i][-1] = new_back_col[i]
            self.bottom[i][0] = new_bottom_col[i]
        self.left[0] = new_top
        self.left[-1] = new_bottom

    def rotate_top(self, clockwise):
        if clockwise:
            new_top = [i[0] for i in self.top[::-1]]
            new_right = self.top[0][:]
            new_bottom = [i[-1] for i in self.top[::-1]]
            new_left = self.top[-1][:]

            new_front_col = self.right[0][:]
            new_right_col = self.back[0][:]
            new_back_col = self.left[0][:]
            new_left_col = self.front[0][:]

        else:
            new_top = [i[-1] for i in self.top]
            new_right = self.top[-1][::-1]
            new_bottom = [i[0] for i in self.top]
            new_left = self.top[0][::-1]

            new_front_col = self.left[0][:]
            new_right_col = self.front[0][:]
            new_back_col = self.right[0][:]
            new_left_col = self.back[0][:]

        for i in range(self.size):
            self.top[i][0] = new_left[i]
            self.top[i][-1] = new_right[i]
        self.top[0] = new_top
        self.top[-1] = new_bottom

        self.front[0] = new_front_col
        self.right[0] = new_right_col
        self.back[0] = new_back_col
        self.left[0] = new_left_col

    def rotate_bottom(self, clockwise):
        if clockwise:
            new_top = [i[0] for i in self.bottom[::-1]]
            new_right = self.bottom[0][:]
            new_bottom = [i[-1] for i in self.bottom[::-1]]
            new_left = self.bottom[-1][:]
        
            new_front_col = self.left[-1][:]
            new_right_col = self.front[-1][:]
            new_back_col = self.right[-1][:]
            new_left_col = self.back[-1][:]
        
        else:
            new_top = [i[-1] for i in self.bottom]
            new_right = self.bottom[-1][::-1]
            new_bottom = [i[0] for i in self.bottom]
            new_left = self.bottom[0][::-1]

            new_front_col = self.right[-1][:]
            new_right_col = self.back[-1][:]
            new_back_col = self.left[-1][:]
            new_left_col = self.front[-1][:]

        for i in range(self.size):
            self.bottom[i][0] = new_left[i]
            self.bottom[i][-1] = new_right[i]
        self.bottom[0] = new_top
        self.bottom[-1] = new_bottom

        self.front[-1] = new_front_col
        self.right[-1] = new_right_col
        self.back[-1] = new_back_col
        self.left[-1] = new_left_col

    def scramble(self, moves=None):
        m = 3
        if moves is not None:
            m = moves

        for i in range(m):
            face = randint(0, 11)
            move = int(face / 2)
            rotation = (face % 2 == 0)
            if move == 0:
                self.rotate_front(rotation)
            elif move == 1:
                self.rotate_right(rotation)
            elif move == 2:
                self.rotate_back(rotation)
            elif move == 3:
                self.rotate_left(rotation)
            elif move == 4:
                self.rotate_top(rotation)
            elif move == 5:
                self.rotate_bottom(rotation)            

    def _front_str(self):
        return ('front:\n[{}\n {}\n {}]'.format(self.front[0], self.front[1], self.front[2]))
    def _back_str(self):
        return ('back:\n[{}\n {}\n {}]'.format(self.back[0], self.back[1], self.back[2]))
    def _top_str(self):
        return ('top:\n[{}\n {}\n {}]'.format(self.top[0], self.top[1], self.top[2]))
    def _bottom_str(self):
        return ('bottom:\n[{}\n {}\n {}]'.format(self.bottom[0], self.bottom[1], self.bottom[2]))
    def _left_str(self):
        return ('left:\n[{}\n {}\n {}]'.format(self.left[0], self.left[1], self.left[2]))
    def _right_str(self):
        return ('right:\n[{}\n {}\n {}]'.format(self.right[0], self.right[1], self.right[2]))

    def __str__(self):
        return ('{}\n{}\n{}\n{}\n{}\n{}'.format(
            self._front_str(), self._back_str(), self._top_str(),
            self._bottom_str(), self._left_str(), self._right_str()
        ))
