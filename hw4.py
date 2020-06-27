'''
S = NP VP           -> 句子 = 名詞子句 + 動詞子句
NP = DET Adj* N PP* -> 名詞子句 = 定詞 + 名詞
VP = V NP           -> 動詞子句 = 動詞 + 名詞子句
PP = P NP           -> 副詞子句 = 副詞 + 名詞子句
黑化肥發灰會揮發灰化肥揮發會發黑
'''

import random as r

n = ['我', '你', '他']
x = r.choice(n)

def S():
    return N1() + VP()

def S2():
    x = r.choice(n)
    return N1() +'也'+ VP()

def NP():
    return DET() + N2()

def VP():
    return V() + N1() + NP()

def N1():
    return x 

def N2():
    return r.choice(['夢想', '堅持', '回憶', '感情', '天真'])

def V():
    return r.choice(['有', '想起', '放棄', '忘記'])

def DET():
    return r.choice(['重要的', '失敗的', '沉重的'])

print(S(),end='')
print('，')
print(S2(),end='')