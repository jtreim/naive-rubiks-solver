from rubiks_cube import RubiksCube

FRONT = 0
BACK = 1
TOP = 2
BOTTOM = 3
LEFT = 4
RIGHT = 5
MOVE_RANGE = 12
MAX_ITERATIONS = 10
BEST_MOVES_CUTOFF = 10000

MOVES = ['f', 'f-', 'b', 'b-', 't', 't-', 'd', 'd-', 'l', 'l-', 'r', 'r-']

def is_valid(move):
    last_move_face = int(move[-1] / 2)
    previous_move_face = int(move[-2] / 2)
    if previous_move_face == last_move_face and abs(move[-1] - move[-2]) == 1:
        return False
    return True


def branch_moves(last_moves):
    branches = []    
    if not last_moves:
        for i in range(MOVE_RANGE):
            branches.append([i])
    else:
        for move in last_moves:
            for i in range(MOVE_RANGE):
                new_move = move[1].copy()
                new_move.append(i)

                # two motions in move, it matches the last motion, it isn't counter-clockwise
                if len(new_move) < 3 and new_move[-1] == new_move[-2] and i % 2 != 1:
                    branches.append(new_move)
                # two motions in move, it doesn't match the last motion
                elif len(new_move) < 3 and new_move[-1] != new_move[-2]:
                    branches.append(new_move)
                # three or more motions in move, it matches the two motions before it
                elif len(new_move) >= 3 and new_move[-1] == new_move[-2] and new_move[-1] == new_move[-3]:
                    continue
                # three or more motions in move, it matches the motion before, and it is counter-clockwise
                elif len(new_move) >= 3 and new_move[-1] == new_move[-2] and i % 2 == 1:
                    continue
                elif len(new_move) >= 3 and is_valid(new_move):
                    branches.append(new_move)    

    return branches  


def try_new_moves(start_state, last_moves, tried_count):
    new_moves = branch_moves(last_moves)
    best_moves = []
    for move in new_moves:
        cube.set_state(start_state)
        for motion in move:
            if int(motion / 2) == FRONT:
                cube.rotate_front(motion % 2 == 0)
            elif int(motion / 2) == BACK:
                cube.rotate_back(motion % 2 == 0)
            elif int(motion / 2) == TOP:
                cube.rotate_top(motion % 2 == 0)
            elif int(motion / 2) == BOTTOM:
                cube.rotate_bottom(motion % 2 == 0)
            elif int(motion / 2) == LEFT:
                cube.rotate_left(motion % 2 == 0)
            elif int(motion / 2) == RIGHT:
                cube.rotate_right(motion % 2 == 0)
            else:
                print('Error! Invalid move! Asked to move {}'.format(motion))
                return False, best_moves, -1

        if cube.is_solved():
            tried_count += 1
            score = cube.get_score()
            best_moves.insert(0, (score, move.copy()))
            return True, best_moves, tried_count
        else:
            tried_count += 1
            score = cube.get_score()
            if len(best_moves) < BEST_MOVES_CUTOFF:
                best_moves.append((score, move.copy()))
                best_moves.sort(key=lambda el: el[0], reverse=True)
            elif best_moves[-1][0] < score:
                del best_moves[-1]
                best_moves.append((score, move.copy()))
                best_moves.sort(key=lambda el: el[0], reverse=True)
    return False, best_moves, tried_count

def solve(cube):
    start_state = cube.get_current_state()
    solved = False
    iterations = 0
    best_score = 0
    best_move = []
    last_moves = []
    tried_count = 0
    while not solved and iterations < MAX_ITERATIONS:
        iterations += 1
        print('iteration: {}'.format(iterations))
        solved, last_moves, tried_count = try_new_moves(start_state, last_moves, tried_count)
        if tried_count == -1:
            iterations = -1
            break

    if iterations == -1:
        print('Broke down...')
    else:
        print('Solved: {}\nTried solutions: {}\tBest Score: {}'.format(solved, tried_count, last_moves[0][0]))
        move_str = ''
        for step in last_moves[0][1]:
            move_str += '{} '.format(MOVES[step])
        print('Best move: [ {}]'.format(move_str))

    cube.set_state(start_state)
    for motion in best_move:
        if int(motion / 2) == FRONT:
            cube.rotate_front(motion % 2 == 0)
        elif int(motion / 2) == BACK:
            cube.rotate_back(motion % 2 == 0)
        elif int(motion / 2) == TOP:
            cube.rotate_top(motion % 2 == 0)
        elif int(motion / 2) == BOTTOM:
            cube.rotate_bottom(motion % 2 == 0)
        elif int(motion / 2) == LEFT:
            cube.rotate_left(motion % 2 == 0)
        elif int(motion / 2) == RIGHT:
            cube.rotate_right(motion % 2 == 0)


cube = RubiksCube()

print('Scrambling...')
cube.scramble(20)

print('Starting cube:')
print(cube.__str__())

print('Searching for solution...')
solve(cube)

print('final:')
print(cube.__str__())
