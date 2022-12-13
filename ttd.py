class Node:
    def init(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def init(self,root):
        self.root = root

    def add(self, data):
        monkey = self.root
        node= Node(data)
        while monkey:
            if data > monkey.data:
                if monkey.right:
                    monkey = monkey.right
                else:
                    monkey.right = node
                    return self
            else:
                if monkey.left:
                    monkey = monkey.left
                else:
                    monkey.left = node
                    return self
        return self

    def search(self, data):
        monkey= self.root
        while monkey:
            if data > monkey.data:
                monkey= monkey.right
            elif data < monkey.data:
                monkey = monkey.left
            elif data == monkey.data:
                return monkey.data, "FOUND IT!"
        return "NODE NOT FOUND"

    def mindata(self):
        monkey = self.root
        while monkey.left != None:
            monkey= monkey.left
        return monkey.data

    def maxdata(self):
        monkey = self.root
        while monkey.right != None:
            monkey= monkey.right
        return monkey.data

    def empty(self):
        monkey = self.root
        if monkey != null:
            print("There is no answer")
        else:
            pass

newtree= BST(Node(5))

newtree.add(5).add(18).add(3).add(9).add(-23)

print(newtree.root.left.data)
print(newtree.search(9))
print(newtree.mindata())
print(newtree.maxdata())