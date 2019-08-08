from collections import deque
"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buffer = deque([])
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ptr = 0
        while (ptr < n and self.buffer):
            buf[ptr] = self.buffer.popleft()
            ptr += 1
        while (ptr < n):
            self.buffer = [''] * 4
            rd = read4(self.buffer)
            self.buffer = deque([c for c in self.buffer if c])
            while (ptr < n and self.buffer):
                buf[ptr] = self.buffer.popleft()
                ptr += 1
            if (rd < 4):
                break
        return ptr
