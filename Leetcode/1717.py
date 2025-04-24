class Solution:
    "time limit failed"
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # points = {x:"ab", y:"ba"}
        if x>y and "ab" in s:
            new_s = s.replace("ab", "", 1)
            return x+self.maximumGain(new_s, x, y)
        elif "ba" in s:
            new_s = s.replace("ba", "", 1)
            return y+self.maximumGain(new_s, x, y)
        
        if y>x and "ba" in s:
            new_s = s.replace("ba", "", 1)
            return y+self.maximumGain(new_s, x, y)
        elif "ab" in s:
            new_s = s.replace("ab", "", 1)
            return x+self.maximumGain(new_s, x, y)
        
        return 0
    def run(self):
        