# implement Stack using list/array

class Stack:
    def __init__(self, size):
        self.__size = size
        self.__li = []
        self.__top = -1

    def push(self, ele):
        if self.__top == self.__size-1:
            print('Stack Overflow')
        else:
            self.__top = self.__top + 1
            self.__li.append(ele)

    def pop(self):
        if self.__top == -1:
            print('Stack is empty')
        else:
            del self.__li[self.__top]
            self.__top = self.__top - 1

    def __str__(self):
        final_str = ''
        for index in range(len(self.__li)-1, -1, -1):
            if index <= self.__top:
                final_str = final_str + "|" + str(self.__li[index]) + "|" + "\n----\n"
        return final_str

    def is_empty(self):
        if self.__top == -1:
            return True
        return False


s1 = Stack(3)
s1.push(2)
s1.push(4)
print(s1)
s1.pop()
print(s1)
print('is stack empty:', s1.is_empty())
