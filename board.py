from pprint import pprint

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
            row[0]=1
            row[-1]=1
        self.board.append([1]*(dimensions[0]+2))

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
        10201
        10001
        10001
        11111
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        10001
        10201
        10001
        11111
        <BLANKLINE>

        >>> b=Board((7,3))
        >>> b.board[0][2]=2 # We add a dynamic figure manually
        >>> b.board[0][3]=2 # We add a dynamic figure manually
        >>> b.board[1][3]=2 # We add a dynamic figure manually
        >>> b.print_board()
        102200001
        100200001
        100000001
        111111111
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        100000001
        102200001
        100200001
        111111111
        <BLANKLINE>
        >>> b.fall_figure()
        >>> b.print_board()
        100000001
        100000001
        102200001
        111211111
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
        10001
        10201
        10001
        11111
        <BLANKLINE>
        >>> b.move_left()
        >>> b.print_board()
        10001
        12001
        10001
        11111
        <BLANKLINE>
        >>> b.board[0][2]=2 # We add a dynamic figure manually
        >>> b.move_left()
        >>> b.print_board()
        10201
        12001
        10001
        11111
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
        10001
        10201
        10001
        11111
        <BLANKLINE>
        >>> b.move_right()
        >>> b.print_board()
        10001
        10021
        10001
        11111
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
        10001
        10201
        10001
        11111
        <BLANKLINE>
        >>> b.blit()
        False
        >>> b.print_board()
        10001
        10001
        10201
        11111
        <BLANKLINE>
        >>> b.blit()
        True
        >>> b.print_board()
        10001
        10001
        10101
        11111
        <BLANKLINE>
        """
        
        y=0
        # Check if figure can fall
        for row in self.board:
            x=0
            for element in row:
                if element==2:
                    if self.board[y+1][x]==1:
                        # Figure can't fall. Converting it into static figures
                        self.set_static()
                        return True
                x+=1
            y+=1
        # All pixels are able to fall
        self.fall_figure()
        return False
