class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        ## 0 < each part < 256
        length = len(s)
        res = []
        if length < 4 or length > 12:
            return res
        self.dfs(s, res, [], 0)
        return res
    
    def dfs(self, s, res, path, layer):
        length = len(s)
        if length <= 0 and layer == 4:
            res.append('.'.join(path))
            return
        if layer >= 4:
            return
        if length >= 3 and s[0] != '0':
            addr3 = s[:3]
            if int(addr3) < 256:
                path.append(addr3)
                self.dfs(s[3:], res, path, layer+1)
                path.pop()
        if length >= 2 and s[0] != '0':
            addr2 = s[:2]
            path.append(addr2)
            self.dfs(s[2:], res, path, layer+1)
            path.pop()
        if length >= 1:
            addr1 = s[:1]
            path.append(addr1)
            self.dfs(s[1:], res, path, layer+1)
            path.pop()
