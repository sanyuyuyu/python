# class Solution(object):
#     def romanToInt(self, s):
#         a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
#         ans=0        
#         for i in range(len(s)):            
#             if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
#                 ans-=a[s[i]]
#             else:
#                 ans+=a[s[i]]
#         return ans

# # class Student(object):
# #     __slots__ = ('name', 'age')
# #     def set_score(self,score):
# #         self.score = score

# # s = Student()
# # s.name = 'wss'

# class Student(object):

#     __slots__ = ('name', 'age', 'gender')
#     def __init__(self, name, age, gender):
#         self.__name = name
#         self.__age = age
#         self.__gender = gender

# s = Student('john', 16, 'male')




