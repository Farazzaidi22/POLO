class Position:
    def __init__(self, idx, ln, col):
        self.idx = idx
        self.ln  = ln
        self.col = col
    
    def advance(self, current_char= None):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col)