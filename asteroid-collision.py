
def asteroidCollision(asteroids):
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else:
            ans.append(new)
    return ans


# print(asteroidCollision([-2, -2, 1, -2]))
# print(asteroidCollision([-2, 1, -2, -2]))
print(asteroidCollision([-2, 1, 1, -2]))
# print(asteroidCollision([5, 10, 20, -50]))
