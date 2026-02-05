class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        index_1,index_2 = {},{}
        for index,string in enumerate(list1):
            index_1[string] = index
        for index,string in enumerate(list2):
            index_2[string] = index
        for string,index in index_1.items():
            if string in index_2:
                res.append([string,index + index_2[string]])
        res.sort(key= lambda a: a[1])
        ans = []
        for i in res:
            if i[1] == res[0][1]:
                ans.append(i[0])
        return ans
