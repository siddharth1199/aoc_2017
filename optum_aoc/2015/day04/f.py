from hashlib import md5
import sys


def mine_adventcoin(key, n_zeroes):
    "Mine dem AdventCoins"
    return next(x for x in range(sys.maxsize) if is_adventcoin(key, x, n_zeroes))

def is_adventcoin(key: str, number: int, n_zeroes: int) -> bool:
    x = md5(bytes(key + str(number), encoding="utf-8"))
    return x.hexdigest().startswith("0"*n_zeroes)


if __name__ == "__main__":
    key = sys.argv[1]
    # part 1
    print(mine_adventcoin(key, 5))
    # part 2
    print(mine_adventcoin(key, 6))
