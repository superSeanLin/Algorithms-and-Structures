class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        ## method 1: compute empty slot, but I don't know why this guarantee the correct order
        # if #, use a slot; if number, create a new slot
        # preorder = preorder.split(',')
        # slot = 1
        # for e in preorder:
        #     if slot == 0:  # no empty slot to put node
        #         return False
        #     if e == "#":
        #         slot -= 1
        #     else:
        #         slot += 1
        # return slot == 0
        
        ## method 2: use stack;
        # if #: stack.top also #, pop twice until top != "#" and push # -> 3## => #; else push #;
        # if number: push number
        # eventually, check if len(stack)==1 and top == #
        stack = []
        preorder = preorder.split(',')
        for e in preorder:
            if e == "#":
                while stack and stack[-1] == "#":
                    stack.pop()
                    if not stack:
                        return False
                    stack.pop()
                stack.append("#")
            else:
                stack.append(e)
        return len(stack)==1 and stack[0]=="#"
                
                    
