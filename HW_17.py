class Example:

    def func(self, arg):
        if isinstance(arg, str):
            if sum(x in "ауоыиэюяеё" for x in arg.lower()) * sum(
                    x not in "ауоыиэюяеё" for x in arg.lower()) <= len(arg):
                return ''.join([x for x in arg if x.lower() in "ауоыиэюяеё"])
            else:
                return ''.join([x for x in arg if x.lower() not in "ауоыиэюяеё"])
        elif isinstance(arg, int):
            return sum(int(x) for x in str(arg) if x in "2468") * self.func_2(arg)

    def func_2(self, arg):
        return len(str(arg))


obj = Example()
obj_1 = obj.func("Два метода в классе, один принимает в себя либо строку, либо число.")
obj_2 = obj.func("Длину строки и числа искать во втором методе.")
obj_3 = obj.func(2023)

print(obj_1)
print(obj_2)
print(obj_3)
