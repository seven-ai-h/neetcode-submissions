#the space between the pair has to be even for it to be correspondable
#strategy: store open brackets, and match closed ones with the open ones that are already in stack
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: #edge case
            return False
        result = []
        pair = { #match the pairs -> helps me check later
            "}" : "{",
            "]" : "[",
            ")" : "(",
        }
        for i in s:
            if i == "(" or i == "{" or i == "[":
                result.append(i)
            else:
                if len(result) == 0: #make sure its not empty for index out of range, if closing as first, false
                    return False
                else:
                    if pair[i] == result[-1]: #match -> pop the first elelment
                        result.pop(-1)
                    else:
                        return False

        if result == []:
            return True
        else:
            return False

#used stack
        
        