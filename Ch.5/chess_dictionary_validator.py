##Chess Dictionary Validator

def isValidChessBoard(board):
    #check 1 - correct board
    rows = ['1','2','3','4','5','6','7','8']
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    #check for the right rows
    for position in board.keys():
        if position[0] in rows:
            valid_rows = True
        else:
            valid_rows = False
            break
    
    #check for the right columns
    for position in board.keys():
        if position[1] in cols:
            valid_columns = True
        else:
            valid_columns = False
            break
                
    valid_board = valid_rows and valid_columns
    
    print('Check #1: ' + str(valid_board))
    
    
    #check 2 - black and white pieces (pieces start with 'b' or 'w')
    #separate by players
    black_pieces = []
    white_pieces = []
    
    b_w_pieces = True 
    
    for piece in board.values():
        if piece[0] == 'b' or piece[0] == 'w':
            if piece[0] == 'b':
                black_pieces.append(piece[1:])
            elif piece[0] == 'w':
                white_pieces.append(piece[1:])
        else:
            b_w_pieces = False
            break
    
    print('Check #2: ' + str(b_w_pieces))
    
    
    #check 3 - number of pieces
    if len(black_pieces) <= 16 and len(white_pieces) <= 16:
        pieces_count = True
    else:
        pieces_count = False
        
    print('Check #3: ' + str(pieces_count))
        

    #check 4 - correct pieces
    valid_pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for piece in board.values():
        if piece[1:] in valid_pieces:
            all_valid_pieces = True
        else:
            all_valid_pieces = False
            break
            
    print('Check #4: ' + str(all_valid_pieces))
    
    
    #check 5 - number of pawns
    bpawn_count = 0
    wpawn_count = 0
    
    #count black pawns
    for piece in black_pieces:
        if piece == 'pawn':
            bpawn_count += 1
    
    #count white pawns
    for piece in white_pieces:
        if piece == 'pawn':
            bpawn_count += 1
    
    #check for the valid number of pawns
    if bpawn_count <= 8 and wpawn_count <= 8:
        pawn_count = True
    else:
        pawn_count = False
    
    print('Check #5: ' + str(pawn_count))


    #Check 6 - kings and queens
    must_have_pieces = ('bking', 'wking', 'bqueen', 'wqueen') 
    
    kings_queens = True
    
    for value in must_have_pieces:
        if value not in board.values():
            kings_queens = False
            break 
    
    print('Check #6: ' + str(kings_queens))
    
    
    #checks result
    if (valid_board and b_w_pieces and pieces_count and all_valid_pieces and pawn_count and kings_queens):
        print('All the checks passed. The board is valid.')
    else:
        print('At least one check failed. The board is not valid')
    
    
    
board = {'1h':'bking','6c': 'wqueen','2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

isValidChessBoard(board)


