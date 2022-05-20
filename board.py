from pprint import pprint
import rotation

class Board(object):
    def __init__(self,dimensions):
        """
        Initializes an empty board.

        param dimensions tuple: Dimensions of the board (pixels). (x,y)
        """
        self.dimensions=dimensions
        self.board = []
        for i in range(dimensions[1]):
            self.board.append([0]*(dimensions[0]+2))
        for row in self.board:
            row[0]=3
            row[-1]=3
        self.board.append([3]*(dimensions[0]+2))

    def set_static(self):
        """
        Converts all dynamic figures into static
        """
        y=0
        # Check if figure can fall
        for row in self.board:
            x=0
            for element in row:
                if element==2:
                    self.board[y][x]=1
                x+=1
            y+=1

    def fall_figure(self):
        """
        Makes all the dynamic figures fall. We don't consider if they are able to fall, 
        we force them.

        >>> b=Board((3,3))
        >>> b.board[0][2]=2 # We add a dynamic figure manually
        >>> b.print_board()
        30203
        30003
        30003
        33333
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        30003
        30203
        30003
        33333
        <BLANKLINE>

        >>> b=Board((7,3))
        >>> b.board[0][2]=2 # We add a dynamic figure manually
        >>> b.board[0][3]=2 # We add a dynamic figure manually
        >>> b.board[1][3]=2 # We add a dynamic figure manually
        >>> b.print_board()
        302200003
        300200003
        300000003
        333333333
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        300000003
        302200003
        300200003
        333333333
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        300000003
        300000003
        302200003
        333233333
        <BLANKLINE>
        """
        # We're iterating the board backwards.
        y=len(self.board)-1
        while y>0:
            x=0
            for element in self.board[y]:
                if self.board[y-1][x]==2:
                    self.board[y][x]=2
                    self.board[y-1][x]=0
                x+=1
            y-=1
    
    
    def move_left(self):
        """
        Makes all the dynamic figures move right. 

        >>> b=Board((3,3))
        >>> b.board[1][2]=2 # We add a dynamic figure manually
        >>> b.print_board()
        30003
        30203
        30003
        33333
        <BLANKLINE>
        >>> b.move_left()
        >>> b.print_board()
        30003
        32003
        30003
        33333
        <BLANKLINE>
        >>> b.board[0][2]=2 # We add a dynamic figure manually
        >>> b.move_left()
        >>> b.print_board()
        30203
        32003
        30003
        33333
        <BLANKLINE>
        """
        board_cpy = []
        for a in self.board:
            aux = []
            for b in a:
                aux.append(b)
            board_cpy.append(aux)
        y=0
        for row in board_cpy:
            x=1
            while x<(len(board_cpy[y])-1):
                if board_cpy[y][x]==2:
                    if board_cpy[y][x-1]==0:
                        board_cpy[y][x-1]=2
                        board_cpy[y][x]=0

                    else:
                        return
                x+=1
            y+=1
        self.board=board_cpy.copy()

    def move_right(self):
        """
        Makes all the dynamic figures move right. 

        >>> b=Board((3,3))
        >>> b.board[1][2]=2 # We add a dynamic figure manually
        >>> b.print_board()
        30003
        30203
        30003
        33333
        <BLANKLINE>
        >>> b.move_right()
        >>> b.print_board()
        30003
        30023
        30003
        33333
        <BLANKLINE>
        """
        board_cpy = []
        for a in self.board:
            aux = []
            for b in a:
                aux.append(b)
            board_cpy.append(aux)
        y=0
        for row in self.board:
            x=(len(board_cpy[0])-2)
            while x>0:
                if board_cpy[y][x]==2:
                    if board_cpy[y][x+1]==0:
                        board_cpy[y][x+1]=2
                        board_cpy[y][x]=0
                    else:
                        return
                x-=1
            y+=1
        self.board=board_cpy.copy()

    def rotate(self):
        """
        >>> b=Board((3,3))
        >>> b.board=[[3,0,0,0,0,0,3],[3,0,2,2,0,0,3],[3,0,2,2,0,0,3],[3,0,2,2,0,0,3],[3,0,0,0,0,0,3],[3,3,3,3,3,3,3],]
        >>> b.print_board()
        3000003
        3022003
        3022003
        3022003
        3000003
        3333333
        <BLANKLINE>
        >>> b=Board((10,22))
        >>> b.board[19][6]=2
        >>> b.board[19][7]=2
        >>> b.board[20][5]=2
        >>> b.board[20][6]=2
        >>> b.board[21][6]=1
        >>> b.print_board()
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000000003
        300000220003
        300002200003
        300000100003
        333333333333
        <BLANKLINE>
        >>> b.rotate()
        """
        # We check the smallest square where
        # the tetromino fits in
        min_dimension = [len(self.board)+2,len(self.board[0])+2]
        max_dimension = [0,0]
        y=0
        for row in self.board:
            x=0
            for pixel in row:
                if pixel==2:
                    if x>max_dimension[1]:
                        max_dimension[1]=x
                    if x<min_dimension[1]:
                        min_dimension[1]=x
                    if y>max_dimension[0]:
                        max_dimension[0]=y
                    if y<min_dimension[0]:
                        min_dimension[0]=y
                x+=1
            y+=1
        # We make the rectangle a square, in case it isn't
        size = max(max_dimension[0]-min_dimension[0],max_dimension[1]-min_dimension[1])
        #print(size)
        # We create the arrays board_before and board_after
        board_before=[]
        y=0
        for row in self.board:
            if y>=min_dimension[0] and y<=min_dimension[0]+size:
                board_before.append(row[min_dimension[1]:min_dimension[1]+size+1])
            y+=1
        if rotation.is_legal(board_before):
            board_after = rotation.copy_arr(board_before)
            rotation.rotate90(board_after)
            rotation.merge(board_before,board_after)
            y=min_dimension[0]
            for row in board_after:
                x=min_dimension[1]
                for pixel in row:
                    if (pixel==0 or pixel==2) and self.board[y][x]!=1 and self.board[y][x]!=3:
                        self.board[y][x]=pixel
                    x+=1
                y+=1
        
    def victory(self):
        """
        >>> b=Board((3,3))
        >>> b.board=[[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,3,3,3,3,3,3],]
        >>> b.print_board()
        3000003
        3000003
        3000003
        3000003
        3000003
        3333333
        <BLANKLINE>
        >>> b.victory()
        0
        >>> b.board=[[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,0,0,0,0,0,3],[3,1,1,4,4,5,3],[3,3,3,3,3,3,3],]
        >>> b.print_board()
        3000003
        3000003
        3000003
        3000003
        3114453
        3333333
        <BLANKLINE>
        >>> b.victory()
        1
        >>> b.print_board()
        3000003
        3000003
        3000003
        3000003
        3000003
        3333333
        <BLANKLINE>
        """
        y=0
        count =0
        while y<len(self.board)-1:
            if ((0 not in self.board[y]) and (2 not in self.board[y])):
                # Row can be removed
                count+=1
                self.board.remove(self.board[y])
                lst=[0]*len(self.board[0])
                lst[0]=3
                lst[-1]=3
                self.board.insert(0,lst)
            y+=1
        return count

    def print_board(self):
        """
        Prints the board to the terminal.
        """
        string = ''
        for row in self.board:
            for element in row:
                string +=str(element)
            string+="\n"
        print(string)

    def blit(self):
        """
        Check if there is a figure that can fall a pixel.
        :return bool: If all the figures stayed in place. So, a new figure can be added.

        >>> b=Board((3,3))
        >>> b.board[1][2]=2 # We add a dynamic figure manually
        >>> b.print_board()
        30003
        30203
        30003
        33333
        <BLANKLINE>
        >>> b.blit()
        False
        >>> b.print_board()
        30003
        30003
        30203
        33333
        <BLANKLINE>
        >>> b.blit()
        True
        >>> b.print_board()
        30003
        30003
        30103
        33333
        <BLANKLINE>
        """
        
        y=0
        # Check if figure can fall
        for row in self.board:
            x=0
            for element in row:
                if element==2:
                    if self.board[y+1][x]!=0 and self.board[y+1][x]!=2:
                        # Figure can't fall. Converting it into static figures
                        self.set_static()
                        return True
                x+=1
            y+=1
        # All pixels are able to fall
        self.fall_figure()
        return False