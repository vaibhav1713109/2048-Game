from tkinter import Frame,Label,CENTER

import game_logic
import constant as c

#inherite the frame class
class Game2048(Frame):
    def __init__(self):
        #inherite the fram_init function
        Frame.__init__(self)                

        self.grid()                         #the frame is visiulise as grid
        self.master.title('2048')           #it's the title of game at the center of frame
        #self.mater.bind is used if any key is pressed then it goes to self.key_dowm function
        self.master.bind("<Key>",self.key_down)
        self.commands={c.KEY_UP:game_logic.move_up, c.KEY_DOWN:game_logic.move_down,c.KEY_LEFT:game_logic.move_left, c.KEY_RIGHT:game_logic.move_right}

        self.grid_cells=[]                   
        self.init_grid()                     #initialize the grid and add the grid cells
        self.init_matrix()                   #it will create the matrix of 4*4
        self.update_grid_cells()             #it upgrade the grid cells according to the no present in grid cells

        self.mainloop()                      #it run the programm

    def init_grid(self):
        #inside a frame we make another frame(400*400) 
        backround=Frame(self, bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE,height=c.SIZE)
        backround.grid()

        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                #inside the background we make small size(100*100) of frames(cell)
                cell=Frame(backround,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.SIZE/c.GRID_LEN,height=c.SIZE/c.GRID_LEN)
                
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)

                
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=game_logic.start_game()
        game_logic.add_new_2(self.matrix)
        game_logic.add_new_2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])

        self.update_idletasks()             #it will wait untill all the color are changed

    def key_down(self,event):
        key=repr(event.char)                #it give exect value of keys(like "'w'")
        if key in self.commands:
            self.matrix,changed=self.commands[repr(event.char)](self.matrix)
            if changed:
                game_logic.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False
                if game_logic.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Win",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if game_logic.get_current_state(self.matrix)=="Lost":
                    self.grid_cells[1][1].configure(text="You",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="Lose!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrig=Game2048()
