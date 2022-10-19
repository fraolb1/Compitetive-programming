class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        count = dict(count.most_common())
        c = sorted(count, key = lambda k: (-count[k], k))
        return c[:k]