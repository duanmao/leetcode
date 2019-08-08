# The simplest but impractical one, keeps all messages inside
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if (message in self.messages and self.messages[message] > timestamp - 10):
            return False
        else:
            self.messages[message] = timestamp
            return True

# slower but practical one, only keeps messages that comes in within the time window
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = {}
        self.queue = collections.deque() # [(message, timestamp)]

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        while (self.queue and self.queue[0][1] <= timestamp - 10):
            del self.messages[self.queue[0][0]]
            self.queue.popleft()
            
        if (message in self.messages):
            return False
        else:
            self.messages[message] = timestamp
            self.queue.append((message, timestamp))
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
