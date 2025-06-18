from typing import List

digits_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def combs(prefix: str, remaining: str, res: List[str]):
    if not remaining and not prefix:
        return

    if not remaining and prefix:
        res.append(prefix)
        return

    # print(f"prefix={prefix}, remaining={remaining}, res={res}")
    for char in digits_map[remaining[0]]:
        combs(prefix + char, remaining[1:], res)

    # print("exiting")


def letter_combinations(digits: str) -> List[str]:
    res = []
    combs("", digits, res)
    print(res)
    return res
