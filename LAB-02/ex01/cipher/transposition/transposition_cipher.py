import math

class TranspositionCipher:
    def encrypt(self, text, key):
        text = text.replace(" ", "").upper()
        cols = int(key)
        rows = math.ceil(len(text) / cols)
        
        grid = [[''] * cols for _ in range(rows)]
        idx = 0
        for r in range(rows):
            for c in range(cols):
                if idx < len(text):
                    grid[r][c] = text[idx]
                    idx += 1
                    
        encrypted = ""
        for c in range(cols):
            for r in range(rows):
                if grid[r][c] != '':
                    encrypted += grid[r][c]
        return encrypted

    def decrypt(self, text, key):
        cols = int(key)
        rows = math.ceil(len(text) / cols)
        
        num_full_cols = len(text) % cols
        if num_full_cols == 0:
            num_full_cols = cols
            
        grid = [[''] * cols for _ in range(rows)]
        
        idx = 0
        for c in range(cols):
            current_rows = rows if c < num_full_cols else rows - 1
            for r in range(current_rows):
                if idx < len(text):
                    grid[r][c] = text[idx]
                    idx += 1
                    
        decrypted = ""
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '':
                    decrypted += grid[r][c]
        return decrypted