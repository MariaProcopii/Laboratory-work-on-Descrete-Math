key1 = str("1c7bb1ae67670f7e6769b515c174414278e16c27e95b43a789099a1c7d55c717b2f0a0442a7d49503ee09552588ed9bb6eda4af738a02fb31576d78ff72b2499b347e49fef1028182f158182a0ba504902996ea161311fe62b86e6ccb02a9307d932f7fa94cde410619927677f94c571ea39c7f4105fae00415dd7d")
key2 = str("2710e45014ed7d2550aac9887cc18b6858b978c2409e86f80bad4b59ebcbd90ed18790fc56f53ffabc0e4a021da2e906072404a8b3c5555f64f279a21ebb60655e4d61f4a18be9ad389d8ff05b994bb4c194d8803537ac6cd9f708e0dd12d1857554e41c9cbef98f61c5751b796e5b37d338f5d9b3ec3202b37a32f")
key1D = int(key1, 16)
key2D = int(key2, 16)
# print(key1D, key2D)

def gcd(x, y):
    # Base case verything divides 0
    if (y == 0):
        return x
    return gcd(y, x % y)

num = str(gcd(key1D, key2D))
# print(num)
last6 = int(num[-6:])
print(last6)