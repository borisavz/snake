import curses
import random
import time

UP = 0
DOWN = 1
LEFT = 3
RIGHT = 4

def main(stdscr):
    stdscr.clear()

    snake = [(0, 0)]

    head_x = 0
    head_y = 0

    food_x = random.randint(0, curses.COLS - 1)
    food_y = random.randint(0, curses.LINES - 2)

    score = 0

    dir = RIGHT

    stdscr.nodelay(True)

    while True:
        k = stdscr.getch()

        if k == ord('q'):
            break

        if k == curses.KEY_UP and dir != DOWN:
            dir = UP
        elif k == curses.KEY_DOWN and dir != UP:
            dir = DOWN
        elif k == curses.KEY_LEFT and dir != RIGHT:
            dir = LEFT
        elif k == curses.KEY_RIGHT and dir != LEFT:
            dir = RIGHT

        i = len(snake) - 1
        while i > 0:
            snake[i] = snake[i - 1]
            i -= 1

        if dir == UP:
            head_y = head_y - 1 if head_y > 0 else curses.LINES - 2
        elif dir == DOWN:
            head_y = head_y + 1 if head_y < curses.LINES - 2 else 0
        elif dir == LEFT:
            head_x = head_x - 1 if head_x > 0 else curses.COLS - 1
        elif dir == RIGHT:
            head_x = head_x + 1 if head_x < curses.COLS - 1 else 0

        if head_x == food_x and head_y == food_y:
            food_x = random.randint(0, curses.COLS - 1)
            food_y = random.randint(0, curses.LINES - 2)
            snake.append((0, 0))
            score += 1

        snake[0] = (head_x, head_y)

        for i in range(1, len(snake)):
            if snake[0] == snake[i]:
                snake = [snake[0]]
                score = 0
                break

        stdscr.erase()

        for s in snake:
            stdscr.addch(s[1], s[0], 'X')

        stdscr.addch(food_y, food_x, '+')
        stdscr.addstr(curses.LINES - 1, 0, "Score: {}, head coordinates: ({}, {}), Q - Quit".format(score, head_x, head_y))
        stdscr.refresh()

        time.sleep(0.1)

curses.wrapper(main)