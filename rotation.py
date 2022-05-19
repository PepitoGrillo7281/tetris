"""
Some utile functions helpful to rotate
arrays and tetrominoes
"""

def reverseColumns(arr):
    for i in range(len(arr)):
        j = 0
        k = len(arr)-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

def transpose(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t


def rotate90(arr):
    """
    We rotate a matrix 90º anti-clockwise
    :param list arr: Array of the matrix
    """
    transpose(arr)
    reverseColumns(arr)

def copy_arr(arr):
    """
    Copyies an array without copying its
    ID
    >>> a = [[1,1],[2,2]]
    >>> b = copy_arr(a)
    >>> a.append(4)
    >>> print(b)
    [[1, 1], [2, 2]]
    """
    new = []
    for a in arr:
        new_i = []
        for b in a:
            new_i.append(b)
        new.append(new_i)
    return new

def pixel_movement(pixel_before,pixel_after):
    """
    We check if it is legal to change a pixel.
    :param int pixel_before: Pixel before change.
    :param int pixel_after: Pixel after change.
    """
    if pixel_before==0 or pixel_after == 0:
        return True
    if pixel_before==2 and pixel_after==2:
        return True
    return False
    

def is_legal(subboard_before,subboard_after):
    """
    We check if it is legal to rotate the tetrominoe.
    :param list subboard_before: Subboard before rotation.
    :param list subboard_after: Subboard after rotation.
    >>> subboard=[[3,0,0],[3,0,2],[3,1,2]]
    >>> ssubboard = copy_arr(subboard)
    >>> rotate90(ssubboard)
    >>> is_legal(subboard,ssubboard)
    True
    >>> subboard=[[3,0,1],[3,0,2],[3,1,2]]
    >>> ssubboard = copy_arr(subboard)
    >>> rotate90(ssubboard)
    >>> is_legal(subboard,ssubboard)
    False
    """
    y=0
    for row_after in subboard_after:
        x=0
        for pixel_after in row_after:
            if pixel_after==2:
                if not pixel_movement(subboard_before[y][x],pixel_after):
                    return False
            x+=1
        y+=1
    return True






