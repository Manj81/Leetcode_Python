class Solution:
    def longestPalindrome(self, s: str) -> str:
        
	    result = ''
	    for i in range(len(s)):
			#odd case: 
		    temp = self.helper(s, i , i)
            #update longest string
		    if len(temp) > len(result):
			    result = temp           
			#even case:
		    temp = self.helper(s, i, i+1)
			#update longest string
		    if len(temp) > len(result):
			    result = temp
	    return result
			
    def helper(self, s, left, right):
        #find palindromic
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print("sub palindrome: ", s[left + 1 : right])
        return s[left + 1 : right]