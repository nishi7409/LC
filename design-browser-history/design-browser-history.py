class Node:
    def __init__(self, url: str, next=None, prev=None):
        self.data = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps:
            steps -= 1
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
        return self.current.data

    def forward(self, steps: int) -> str:
        while steps:
            steps -= 1
            if self.current.next:
                self.current = self.current.next
            else:
                break
        return self.current.data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)