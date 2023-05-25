from collections import List,defaultdict
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         class Item:
#             key:str
#             firstIndex: int
#             num: int
#             def __init__(self) -> None:
#                 self.num = 0
#         mapList = [0] * 500
#         mapDict = dict()
#         index = 0
#         while index < len(words):
#             key = words[index]
#             if key in mapDict:
#                 temp: Item = mapDict[key]
#                 temp.num += 1
#                 mapDict[key] = temp
#             else:
#                 item = Item()
#                 item.key = key
#                 item.num += 1
#                 item.firstIndex = index
#                 mapDict[key] = item
#             index += 1
        
#         index = 0
#         res = []
#         while index < k:
#             maxItem = Item()
#             for key in mapDict:
#                 item :Item = mapDict[key]
#                 if maxItem.num < item.num:
#                     maxItem = item
#                 elif maxItem.num == item.num:
#                     if maxItem.firstIndex <= item.firstIndex:
#                         maxItem = item
#             res.append(maxItem.key)
#             del mapDict[maxItem.key]
#             index += 1
#         return res
                
# so = Solution()
# words = ["i","love","leetcode","i","love","coding"]
# k=3
# print(so.topKFrequent(words,k))
            
from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] +=1
        def compare(a,b):
            if dic[a] > dic[b]:
                return 1
            elif dic[a] < dic[b]:
                return -1
            elif a>b:
                return -1
            elif a<b:
                return 1
            else:
                return 0

        sorted_words = sorted(list(dic.keys()),reverse = True, key=functools.cmp_to_key(compare))
        return sorted_words[:k]