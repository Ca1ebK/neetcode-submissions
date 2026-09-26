class Solution:

    # ["Hello", "World"]
    # "5#Hello5#World"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # "5#Hello5#World"
    # ["Hello", "World"]
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = 0
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            res.append(s[j + 1 : j + 1 + l])
            i = j + 1 + l
        return res