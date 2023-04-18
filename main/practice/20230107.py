def is_palindrome(num):
    step = 0
    a = str(num)
    while not a[::-1] == a:
        a = int(a) + int(a[::-1])
        a = str(a)
        step += 1
    if step > 30:
        return step
    return step

# n = map(int, input().split())

# print(list(map(int, input().split(','))))

# '20 30 40 60' -> [20, 30, 40, 60]
# '1 2 3 4' scores[0] -> [30, 40, 50, 70]
# max()

# for index, value in enumerate([30, 40, 50, 70]):
#     print(index, value)
#
#
# res1 = ['30', '40', '50']
# res2 = ['4']
# for v in [1,3,4]:
#     print(v)

# 0,1
# 1,3
# 2,4


# print('1234 523'.split())
# '1234 523'

# [1,2,3,4}
# def test(x):
#     return x * x

# [1,2,3,4,5] -> [1,4,9,16,25] -> map(test, [1,2,3,4,5])
# [1,2,3] => [1,8,27]

# 000000100 -> 2
# 000000001 -> 1
# print(2 << 1)

# scores = list(map(int, input().split()))  # 使用map映射函数
# indexes = list(map(int, input().split()))

scores = [61, 73, 56, 90]
indexes = [1,2,3,4]

for index in indexes:
    scores[index - 1] += 10

# 找出总分最高的选手
max_score = max(scores)  # 找出了最高分
# score.index(max_score)      #这种方法有一个弊端就是只能找到第一个最高分所在的下标，不符合题目要求

# 第一种方式
res1 = []
res2 = []
for index, score in enumerate(scores):
    if score == max_score:
        res2.append(str(index + 1))
    res1.append(str(score))

print(' '.join(res1))
print(' '.join(res2))


# if __name__ == '__main__':
    # print(is_palindrome(69))






