# Time: O(n_words * wlen + n_queries * (qlen + max_f_in_words))...
# space: O(f_in_words)
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            freq = 0
            sc = '~'
            for c in s:
                if (c == sc):
                    freq += 1
                elif (c < sc):
                    freq = 1
                    sc = c
            return freq
        
        freqs = collections.defaultdict(int)
        for word in words:
            fw = f(word)
            freqs[fw] += 1
            
        answers = []
        for query in queries:
            fq = f(query)
            count = 0
            for fw in freqs:
                if (fw > fq): count += freqs[fw]
            answers.append(count)
        return answers

# well.. python.. of course there're some much shorter, occult version...
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            return s.count(min(s))
        fw = sorted([f(w) for w in words])
        return [len(words) - bisect.bisect(fw, f(q)) for q in queries]
