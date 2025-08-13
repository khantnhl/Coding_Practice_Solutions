"""
"""

def convert(self, s: str, numRows: int) -> str:
    #edge case where len(s) is smaller than rows
    if(numRows==1 or len(s) <= numRows):
        return s
    step = -1
    rows = [''] * numRows
    curRow = 0
    for ch in s:
        rows[curRow] += ch

        if(curRow==0 or curRow==numRows-1): # flip direction when reaching the bounds 
            step = -step

        curRow += step
    return ''.join(rows)