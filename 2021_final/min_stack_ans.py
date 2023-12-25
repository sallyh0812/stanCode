class MinStack:
    def __init__(self):
        self.__data = []
        self.__min = []
    
    def push(self, x):
        """
        Push element x onto stack.
        ——————————————————————
        :param x: int, the data to be added into stack
        :return: None
        """
        self.__data.append(x)
        if len(self.__min) != 0:
            if x <= self.__min[-1]:
                self.__min.append(x)
        else:
            self.__min.append(x)
    
    def pop(self):
        """
        Removes the element on top of the stack.
        ——————————————————————
        :return: None
        """
        ele = self.__data.pop()
        if ele == self.__min[-1]:
            self.__min.pop()
    
    def top(self):
        """
        Get the top element.
        ——————————————————————
        :return: int, the top element
        """
        return self.__data[-1]
    
    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        ——————————————————————
        :return: int, the minimum element
        """
        return self.__min[-1]


def main():
    min_stack = MinStack()
    min_stack.push(4)
    min_stack.push(5)
    print(min_stack.getMin())
    print(min_stack.top())
    min_stack.push(2)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.getMin())
    print(min_stack.top())


if __name__ == '__main__':
    main()
