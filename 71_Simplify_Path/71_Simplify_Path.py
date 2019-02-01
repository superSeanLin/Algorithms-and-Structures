class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ## use Stack (idea from discussion)
        stack = []
        place = path.split("/")
        for p in place:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)
