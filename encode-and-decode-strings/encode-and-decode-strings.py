class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result
        # "1##3#bob1#14#zulu"
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        start = 0
        result = list()
        # "1##3#bob1#14#zulu"

        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            result.append(str(s[start:end]))
            start = end
        return result

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))