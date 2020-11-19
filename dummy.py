def asteroidCollision(asteroids):

    solution = []
    _as = [*asteroids]
    f = asteroids.pop(0)

    solution.append(f)

    for i in asteroids:
        if((i >= 0 and solution[0] >= 0) or (i < 0 and solution[0] < 0)):
            solution.insert(0, i)
        else:
            if(i > 0 and solution[0] < 0):
                solution.insert(0, i)
                continue

            i = -1 * i
            for j in range(0, len(solution)):
                if(((-1 * i) >= 0 and solution[j] >= 0) or ((-1 * i) < 0 and solution[j] < 0)):
                    break
                if(solution[j] != 0):

                    if(solution[j] >= i):
                        solution[j] = solution[j] - i
                        i = 0
                        break
                    else:
                        i = i - solution[j]
                        solution[j] = 0
                        if(i == 0):
                            break
            if(i != 0):
                solution.insert(0, (-1*i))
            else:
                solution.insert(0, 0)
    print(solution)
    ans = []
    for i, j in enumerate(solution[::-1]):
        if(j != 0):
            ans.append(_as[i])

    print(ans)


# asteroidCollision([10, 2, -5])
# asteroidCollision([-8, 8])
# asteroidCollision([-2, -1, 1, 2])
# asteroidCollision([5, 10, -5])
asteroidCollision([-2, -2, 1, -2])
asteroidCollision([-2, 1, -2, -2])
asteroidCollision([-2, 1, 1, -2])
asteroidCollision([5, 10, 20, -50])

# 5 10 20 - 50

# 15 0 0 0


# def asteroidCollision(asteroids):
#     ans = []
#     for new in asteroids:
#         while ans and new < 0 < ans[-1]:
#             if ans[-1] < -new:
#                 ans.pop()
#                 continue
#             elif ans[-1] == -new:
#                 ans.pop()
#             break
#         else:
#             ans.append(new)
#     return ans


# # print(asteroidCollision([-2, -2, 1, -2]))
# # print(asteroidCollision([-2, 1, -2, -2]))
# print(asteroidCollision([-2, 1, 1, -2]))
# # print(asteroidCollision([5, 10, 20, -50]))
