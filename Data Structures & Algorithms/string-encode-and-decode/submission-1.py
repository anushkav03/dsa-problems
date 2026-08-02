class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            length = str(len(i))
            encoded = "".join([encoded, length])
            encoded = "".join([encoded, '.'])
            encoded = "".join([encoded, i])
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        while len(s) != 0:
            # get length and remove from string
            dot_index = s.index('.')
            length = int(s[:dot_index])
            s = s[dot_index+1:]
            # get word, append to list and remove from string
            word = ''.join(s[:length])
            decoded.append(word)
            s = s[length:]
        return decoded
