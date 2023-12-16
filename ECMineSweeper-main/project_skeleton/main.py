import pygame
import sys
from cell import Cell
from calcs import measure_distance

""" This is the main file you work on for the project"""

pygame.init()

SCREEN_MIN_SIZE = 640  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.25  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how large can each cell be?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []


def create_cells():
    """This function is meant to initialy generate all the cells and create the boundaries"""
    # This is a good base to go from (think about it thoroughly before you code!! We want to create 16x16 list with each object being a cell):
    print("READJUSTED_SIZE:", READJUSTED_SIZE, ", CELL_SIZE:", CELL_SIZE)
    row_position = 0
    for row in range(amount_of_cells):
        column_position = 0
        for column in range(amount_of_cells):
            new_cell = Cell(row_position, column_position, CELL_WIDTH, CELL_HEIGHT, bomb_chance)
            column_position = column_position + CELL_WIDTH
            cells.append(new_cell)
        row_position = row_position + CELL_HEIGHT

def update_neighbouring_bombs():
    for cell in cells:
        #left_neighbour_pos
        if (cell.x - cell.width) >= 0:
            left_neighbour_pos = (cell.x - cell.width, cell.y)
            print("left_neighbour_pos:", left_neighbour_pos)
            neighbour_cell = find_cell(left_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1
        
        #right_neighbour_pos
        if (cell.x + cell.width) < SCREEN_WIDTH:
            right_neighbour_pos = (cell.x + cell.width, cell.y)
            print("right_neighbour_pos:", right_neighbour_pos)
            neighbour_cell = find_cell(right_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1

        #top_neighbour_pos
        if (cell.y - cell.height) >= 0:
            top_neighbour_pos = (cell.x, cell.y - cell.height)
            print("top_neighbour_pos:", top_neighbour_pos)
            neighbour_cell = find_cell(top_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1                
        
        #bottom_neighbour_pos
        if (cell.y + cell.height) < SCREEN_HEIGHT:
            bottom_neighbour_pos = (cell.x, cell.y + cell.height)
            print("bottom_neighbour_pos:", bottom_neighbour_pos)
            neighbour_cell = find_cell(bottom_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1   

        #top_left_neighbour_pos
        if (cell.y - cell.height) >= 0 and (cell.x - cell.width) >= 0:
            top_left_neighbour_pos = (cell.x - cell.width, cell.y - cell.height)
            print("top_left_neighbour_pos:", top_left_neighbour_pos)
            neighbour_cell = find_cell(top_left_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1

        #top_right_neighbour_pos
        if (cell.y - cell.height) >= 0 and (cell.x + cell.width) < SCREEN_WIDTH:
            top_right_neighbour_pos = (cell.x + cell.width, cell.y - cell.height)
            print("top_right_neighbour_pos:", top_right_neighbour_pos)
            neighbour_cell = find_cell(top_right_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1

        #bottom_left_neighbour_pos
        if (cell.y + cell.height) < SCREEN_HEIGHT and (cell.x - cell.width) >= 0:
            bottom_left_neighbour_pos = (cell.x - cell.width, cell.y + cell.height)
            print("bottom_left_neighbour_pos:", bottom_left_neighbour_pos)
            neighbour_cell = find_cell(bottom_left_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1

        #bottom_right_neighbour_pos
        if (cell.y + cell.height) < SCREEN_HEIGHT and (cell.x + cell.width) < SCREEN_WIDTH:
            bottom_right_neighbour_pos = (cell.x + cell.width, cell.y + cell.height)
            print("bottom_right_neighbour_pos:", bottom_right_neighbour_pos)
            neighbour_cell = find_cell(bottom_right_neighbour_pos)
            if neighbour_cell.bomb:
                cell.neighbouring_bombs = cell.neighbouring_bombs + 1

def find_cell(pos):
    for cell in cells:
        if pygame.Rect(cell.x, cell.y, cell.width, cell.height).collidepoint(pos):
            print("Cell Found:", cell)
            cell.log()
            return cell
    return None

def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    for cell in cells:
        cell.draw(screen)


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    screen.fill((134,146,255))
    draw_cells()
    pygame.display.flip()


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()

    if event.type == pygame.MOUSEBUTTONUP:
      pos = pygame.mouse.get_pos()
      print(pos)
      selected_cell = find_cell(pos)
      selected_cell.selected = True
      draw()


def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()
    update_neighbouring_bombs()
    draw()


def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    while True:
        for event in pygame.event.get():
            event_handler(event)

    terminate_program()

if __name__ == "__main__":
    main()
