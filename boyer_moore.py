class BoyerMooreSubstringSearch:
    """Boyer-Moore substring search using the bad character heuristic."""

    def __init__(self, pattern: str):
        if not pattern:
            raise ValueError("Pattern must be a non-empty string.")
        self.pattern = pattern
        self.shift_table = self._build_shift_table(pattern)

    @staticmethod
    def _build_shift_table(pattern: str) -> dict:
        """Create shift table for the pattern."""
        table = {}
        length = len(pattern)

        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1

        table.setdefault(pattern[-1], length)
        return table

    def search(self, text: str) -> int:
        """Return start index of the first match in text, or -1 if not found."""
        i = 0
        pattern_length = len(self.pattern)
        text_length = len(text)

        while i <= text_length - pattern_length:
            j = pattern_length - 1

            while j >= 0 and text[i + j] == self.pattern[j]:
                j -= 1

            if j < 0:
                return i

            mismatched_char = text[i + j]
            bad_char_shift = self.shift_table.get(mismatched_char, pattern_length)
            # Adjust shift based on where mismatch occurred in the pattern
            i += max(1, bad_char_shift - (pattern_length - 1 - j))

        return -1
