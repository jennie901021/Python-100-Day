"""
驗證輸入用戶名和QQ號是否有效並給出對應的提示信息

要求：用戶名必須由字母、數字或下劃線構成且長度在6~20個字符之間，QQ號是5~12的數字且首位不能為0
"""
import re


def main():
    username = input('請輸入ID: ')
    qq = input('請輸入QQ號: ')
    # match函數的第一個參數是正則表達式字符串或正則表達式對象
    # 第二個參數是要跟正則表達式做匹配的字符串對象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('請輸入有效的ID.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('請輸入有效的QQ號.')
    if m1 and m2:
        print('你輸入的信息是有效的!')


if __name__ == '__main__':
    main()

import re

#請輸入正確的手機號碼
def main():
    # 創建正則表達式對象 使用了前瞻和回顧來保證手機號前後不應該出現數字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情說8130123456789遍，我的手機號是13512346789這個靚號，
    不是15600998765，也是110或119，王大錘的手機號才是15600998765。
    '''
    # 查找所有匹配並保存到一個列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------華麗的分隔線--------')
    # 通過迭代器取出匹配對象並獲得匹配的內容
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('--------華麗的分隔線--------')
    # 通過search函數指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == '__main__':
    main()