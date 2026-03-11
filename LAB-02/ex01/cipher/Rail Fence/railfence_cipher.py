class RailFenceCipher:
    def encrypt(self, text, rails):
        if rails == 1:
            return text
        
        fence = [['' for _ in range(len(text))] for _ in range(rails)]
        direction_down = False
        row, col = 0, 0
        
        for char in text:
            if row == 0 or row == rails - 1:
                direction_down = not direction_down
            
            fence[row][col] = char
            col += 1
            
            if direction_down:
                row += 1
            else:
                row -= 1
        
        result = []
        for i in range(rails):
            for j in range(len(text)):
                if fence[i][j] != '':
                    result.append(fence[i][j])
        return "".join(result)

    def decrypt(self, cipher, rails):
        if rails == 1:
            return cipher
            
        fence = [['' for _ in range(len(cipher))] for _ in range(rails)]
        direction_down = None
        row, col = 0, 0
        
        for i in range(len(cipher)):
            if row == 0:
                direction_down = True
            if row == rails - 1:
                direction_down = False
            
            fence[row][col] = '*'
            col += 1
            
            if direction_down:
                row += 1
            else:
                row -= 1
        
        index = 0
        for i in range(rails):
            for j in range(len(cipher)):
                if fence[i][j] == '*' and index < len(cipher):
                    fence[i][j] = cipher[index]
                    index += 1
        
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                direction_down = True
            if row == rails - 1:
                direction_down = False
            
            if fence[row][col] != '':
                result.append(fence[row][col])
                col += 1
            
            if direction_down:
                row += 1
            else:
                row -= 1
        return "".join(result)