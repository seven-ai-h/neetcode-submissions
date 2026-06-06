#the space between the pair has to be even for it to be correspondable
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: #edge case
            return False
        result = []
        pair = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        for i in s:
            if i == "(" or i == "{" or i == "[":
                result.append(i)
            else:
                if len(result) == 0:
                    return False
                else:
                    if pair[i] == result[-1]:
                        result.pop(-1)
                    else:
                        return False

        if result == []:
            return True
        else:
            return False
        
        