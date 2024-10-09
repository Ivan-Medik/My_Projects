from collections import deque


n, m = map(int, input().split())
cames = [1 for _ in range(n)]
homes = [0 for _ in range(n)]
parking = [0 for _ in range(n)]
stop = [float("inf")]
deque_out = []
for i in range(m):
    s = input().split()
    k = int(s[1]) - 1
    if s[0] == "+":
        cames[k] = 0
        if k <= stop[-1]:
            homes[k] = 1
        else:
            parking[k] = 1

        if k < stop[-1]:
            stop.append(k)
    else:
        if parking[k]:
            parking[k] = 0
        elif k > stop[-1]:
            deque_out.append(k)
        else:
            stop.pop()
            homes[k] = 0
            deque_out = deque(sorted(deque_out))
            flag = True

            while flag and (len(deque_out) > 0):
                if deque_out[0] <= stop[-1]:
                    homes[deque_out[0]] = 0
                    deque_out.popleft()
                    stop.pop()
                else:
                    flag = False



for i in range(n):
    if cames[i]:
        print("-1")
    elif parking[i] or homes[i]:
        print("NO")
    else:
        print("YES")
