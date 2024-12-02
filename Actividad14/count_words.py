class CountWords:
    def count(self, s: str) -> int:
        words = 0 
        last = ' '
        s = s.lower()
        ending = {'s','r'}
        
        for char in s:
            if not char.isalpha() and last in ending:
                words += 1
            last = char
            
        if last in ending:
            words += 1
        
        return words