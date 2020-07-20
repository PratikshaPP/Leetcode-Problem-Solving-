class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:     
        result = []
        state = []
        self.backtrack(n, result, state, 0)
        finalresult = self.convertToBoard(n, result)
        return finalresult
    
    def convertToBoard(self, n, result):
        row = ['.']*n
        boards = []
           
        for placement in result:
            board = []
            for col in placement:
                row[col] = 'Q'       
                board.append("".join(row))
                row[col] = '.'
                
            boards.append(board)
            
        return boards
            
                        
    def backtrack(self, n, result, state, cursor):        
        #isValid
        if cursor == n:
            res = []
            for x in state:
                res.append(x)
            result.append(res)
            return
        
        for j in range(n):
            if self.canPlace(n, state, cursor, j):
                state.append(j)
                self.backtrack(n, result, state, cursor+1)
                state.pop()
                
                                
    def canPlace(self, n, state, row, col):
        return self.canPlaceVertically(n, state, row, col) and self.canPlaceDiagonally(n, state, row, col)
    
    def canPlaceVertically(self, n, state, row, col):
        i = row-1
        j = col
        while i>=0:
            if state[i] == j:
                return False
            i -=1
        return True

    def canPlaceDiagonally(self, n, state, row, col):
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if state[i] == j:
                return False
            i -=1
            j -=1
        
        i = row-1
        j = col+1
        while i>=0 and j<n:
            if state[i] == j:
                return False
            i-=1
            j+=1
        
        return True