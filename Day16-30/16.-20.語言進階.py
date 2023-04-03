"""
從列表中找出最大的或最小的N個元素
堆結構(大根堆/小根堆)
"""
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
#collections模塊
"""
*namedtuple：命令元組，它是一個類工廠，接受類型的名稱和屬性列表來創建一個類。
*deque：雙端隊列，是列表的替代實現。 Python中的列表底層是基於數組來實現的，而deque底層是雙向鍊錶，因此當你需要在頭尾添加和刪除
        元素時，deque會表現出更好的性能，漸近時間複雜度為$O(1)$。
*Counter：dict的子類，鍵是元素，值是元素的計數，它的most_common()方法可以幫助我們獲取出現頻率最高的元素。 Counter和dict的繼承關
        係我認為是值得商榷的，按照CARP原則，Counter跟dict的關係應該設計為關聯關係更為合理。
*OrderedDict：dict的子類，它記錄了鍵值對插入的順序，看起來既有字典的行為，也有鍊錶的行為。
*defaultdict：類似於字典類型，但是可以通過默認的工廠函數來獲得鍵對應的默認值，相比字典中的setdefault()方法，這種做法更加高效。
"""

#找出序列中出現次數最多的元素

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

"""
排序算法（选择、冒泡和归并）和查找算法（顺序和折半）
"""

#简单选择排序
def select_sort(items, comp=lambda x, y: x < y):
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

#泡泡排序
def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

#搅拌排序(泡泡排序升级版)
def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

"""
快速排序 - 選擇樞軸對元素進行劃分，左邊都比樞軸小右邊都比樞軸大
"""
def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1

#動態規劃例子：子列表元素之和的最大值。
"""
說明：子列表指的是列表中索引（下標）連續的元素構成的列表；列表中的元素是int類型，
可能包含正整數、0、負整數；程序輸入列表中的元素，輸出子列表元素求和的最大值
"""
def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)


if __name__ == '__main__':
    main()

"""
面向對象相關知識
三大支柱：封裝、繼承、多態
"""
#工資結算系統。

"""
月薪結算系統 - 部門經理每月15000 程序員每小時200 銷售員1800底薪加銷售額5%提成
"""
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    """員工(抽像類)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """結算月薪(抽象方法)"""
        pass


class Manager(Employee):
    """部門經理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序員"""

    def __init__(self, name, working_hour=0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour


class Salesman(Employee):
    """銷售員"""

    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05


class EmployeeFactory:
    """創建員工的工廠（工廠模式 - 通過工廠實現對象使用者和對象之間的解耦合）"""

    @staticmethod
    def create(emp_type, *args, **kwargs):
        """創建員工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types[emp_type.upper()]
        return cls(*args, **kwargs) if cls else None


def main():
    """主函數"""
    emps = [
        EmployeeFactory.create('M', '曹操'), 
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85), 
        EmployeeFactory.create('S', '典韋', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()

"""
迭代器是實現了迭代器協議的對象。

Python中沒有像protocol或interface這樣的定義協議的關鍵字。
Python中用魔術方法表示協議。
__iter__和__next__魔術方法就是迭代器協議。
"""

#迭代器和生成器
class Fib(object):
    """迭代器"""
    
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
   
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()
    
#生成器是語法簡化版的迭代器。

def fib(num):
    """生成器"""
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a 