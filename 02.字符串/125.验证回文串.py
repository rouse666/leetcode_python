"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
"""

# C++
# class Solution {
# public:
#     bool isPalindrome(string s) {
#       string sgood;
#       for(char ch:s){
#           if(isalnum(ch)){
#               sgood+=tolower(ch);
#           }
#
#       }
#       string sgood_rev(sgood.rbegin(),sgood.rend());
#       return sgood==sgood_rev;
#     }
# };