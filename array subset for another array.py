#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        ca,cb = Counter(a),Counter(b)
        a = set(a)
        for i in b :
            if cb[i] > ca[i]:
                return False
        return True
    
    
