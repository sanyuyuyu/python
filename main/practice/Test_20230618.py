# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'

# bart = Student('Bart Simpson',59)
# bart.score

# bart.score = 99
# bart.score





# class Student(object):

#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

class Student(object):

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

