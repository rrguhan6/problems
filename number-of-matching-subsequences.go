// https://leetcode.com/problems/number-of-matching-subsequences/submissions/
// brute force method

func patternFound(pattern string, b string) bool {

	for _, currChar := range pattern {
		if string(currChar) == string(b[0]) {
			b = b[1:]
			if len(b) == 0 {
				return true
			}
		}
	}

	return false
}

func _numMatchingSubseq(S string, words []string) int {
	count := 0
	memo := make(map[string]bool)
	for _, w := range words {
		if memo[w] {
			count++
			continue
		}
		if patternFound(S, w) {
			memo[w] = true
			count++
		}
	}

	return count
}

func numMatchingSubseq(S string, words []string) (num int) {
	return _numMatchingSubseq(S, words)
}