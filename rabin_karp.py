class RabinKarpSubstringSearch:
    """Rabin-Karp substring search with rolling polynomial hash."""

    def __init__(self, pattern: str, base: int = 256, modulus: int = 101):
        if not pattern:
            raise ValueError("Pattern must be a non-empty string.")
        self.pattern = pattern
        self.base = base
        self.modulus = modulus
        self.pattern_hash = self._polynomial_hash(pattern)
        self.pattern_length = len(pattern)
        self.h_multiplier = pow(self.base, self.pattern_length - 1, self.modulus)

    def _polynomial_hash(self, s: str) -> int:
        """Return polynomial hash of string s."""
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(self.base, n - i - 1, self.modulus)
            hash_value = (hash_value + ord(char) * power_of_base) % self.modulus
        return hash_value

    def search(self, text: str) -> int:
        """Return start index of the first match in text, or -1 if not found."""
        n = len(text)
        m = self.pattern_length

        if m > n:
            return -1

        current_hash = self._polynomial_hash(text[:m])

        for i in range(n - m + 1):
            if self.pattern_hash == current_hash:
                if text[i : i + m] == self.pattern:
                    return i

            if i < n - m:
                current_hash = (
                    (current_hash - ord(text[i]) * self.h_multiplier) * self.base
                    + ord(text[i + m])
                ) % self.modulus

        return -1


if __name__ == "__main__":
    main_string = "Being a developer is not easy"
    substring = "developer"

    searcher = RabinKarpSubstringSearch(substring)
    position = searcher.search(main_string)

    if position != -1:
        print(f"Substring found at index {position}")
    else:
        print("Substring not found")
