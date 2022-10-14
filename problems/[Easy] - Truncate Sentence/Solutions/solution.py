class solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ")[x] for x in range(k))
        ''''
        ##### Complexity:  ***O(n)***
        ### How this Works:
        `s.split(" ")` Converts String to List using a regex, in this case, `" "`.

        Example: `"Hello I'm Keion"` -> `["Hello", "I'm", "Keion"]`

        Next, a **List Comprehension** For-Loop will iterate over the numbers `0` through `k`, ultimately appending every k*th* word to this new List.

        Finally, the `" ".join()` Method will **concatinate** the new List, giving a `" "` between every element, forming the new sentence.
        ''''
