# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-17 16:39:21
#回文数
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int 
        :rtype: bool
        """
        return str(x) == str(x)[::-1]



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int 
        :rtype: bool 
        """

        xx = x 
        if x < 0:
            return False

        reverse = 0 
        while x > 0:
            x, tmp = divmod(x, 10)
            reverse = reverse * 10 + tmp 


        return reverse == xx