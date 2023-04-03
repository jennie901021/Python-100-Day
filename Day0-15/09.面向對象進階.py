"""
靜態方法和類方法
之前，我們在類中定義的方法都是對象方法，也就是說這些方法都是發送給對象的消息。實際上，我們寫在類中的方法並不需要都是對象方法，例如我們定義一個“三角形”類，
通過傳入三條邊長來構造三角形，並提供計算周長和麵積的方法，但是傳入的三條邊長未必能構造出三角形對象，因此我們可以先寫一個方法來驗證三條邊長是否可以構成三角形，
這個方法很顯然就不是對象方法，因為在調用這個方法時三角形對象尚未創建出來（因為都不知道三條邊能不能構成三角形）
，所以這個方法是屬於三角形類而並不屬於三角形對象的。我們可以使用靜態方法來解決這類問題，代碼如下所示。
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')


if __name__ == '__main__':
    main()