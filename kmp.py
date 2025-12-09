class KMPSubstringSearch:
    """Knuth-Morris-Pratt substring search."""

    def __init__(self, pattern: str):
        if not pattern:
            raise ValueError("Pattern must be a non-empty string.")
        self.pattern = pattern
        self.lps = self._compute_lps(pattern)

    @staticmethod
    def _compute_lps(pattern: str):
        """Compute the longest proper prefix-suffix table for the pattern."""
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self, text: str) -> int:
        """Return start index of the first match in text, or -1 if not found."""
        m = len(self.pattern)
        n = len(text)

        i = j = 0

        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1
            elif j != 0:
                j = self.lps[j - 1]
            else:
                i += 1

            if j == m:
                return i - j

        return -1


if __name__ == "__main__":
    raw = "This algorithm is often used in text editors and search systems for efficient substring search in text."
    pattern = "alg"

    matcher = KMPSubstringSearch(pattern)
    print(matcher.search(raw))
