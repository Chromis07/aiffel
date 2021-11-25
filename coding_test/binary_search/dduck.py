from bisect import bisect_right, bisect_left

# 인풋을 받으면,

# 4, 6


def height_search(array, m):

    start = 1
    end = max(array)

    while start <= end:

        mid = (start + end) // 2  # 10

        hap = sum([i - mid for i in array if i > mid])

        if m == hap:
            return mid
        elif m > hap:
            end = mid - 1
        else:
            start = mid + 1

    return None


n, m = map(int, input().split())

# [19, 15, 10, 17]
dduck = list(map(int, input().split()))

print(height_search(dduck, m))


# for i in height:
#     for j in sorted_dduck:
#         if j-i <= 0:
#             cutted.append(0)
#         else :
#             cutted.append(j-i)
#     if sum(cutted) == m:
#         return i
#     elif sum(cutted) > m:
