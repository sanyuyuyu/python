# /usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: sanyuyuyu
# @Date:   2022-09-18 16:59:
class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int n = s.length(), ans = -1;
        char[] chars = s.toCharArray();
        int[] pos = new int[26];
        for (int i = 0; i < n; i++) {
            int now = chars[i] - 'a';
            if (pos[now] != 0) ans = Math.max(ans, i - pos[now]);
            else pos[now] = i + 1;
        }
        return ans;
    }
}