# # x = 123456
# # x = 123456789
# x = -25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)


# x = 123456
# x = 123456789
# x = 30
# epsilon = 0.01
# numGuesses = 0
# low = min(0, x)
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**3 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses =', numGuesses)
# print(ans, 'is close to cube root of', x)


def bisect_search1(L, e):
    # Time complexity O(nlogn) since every time through a recursive call, it makes
    # a copy of half a list.
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


def bisect_search2(L, e):
    # O(logn)
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid-1)
        else:
            return bisect_search_helper(L, e, mid+1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L)-1)                