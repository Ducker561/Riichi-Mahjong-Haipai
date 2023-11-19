from haipai import hai_pai
from shanten import Handcards, get_handcards
import numpy

def samples(n):
    '''测试n次配牌的向听数平均'''
    shanten_list=[]
    for i in range(n):
        my_hai, tsumo = hai_pai(d=1)
        my_haipai = my_hai+tsumo
        handcards = Handcards(get_handcards(my_haipai))
        shanten = handcards.shanten()
        print('第'+str(i+1)+'次配牌：'+my_haipai+'，向听数：'+str(shanten))
        shanten_list.append(shanten)
    return numpy.mean(shanten_list)

def one_haipai():
    '''单次配牌测试'''
    my_hai, tsumo = hai_pai(d=1)
    my_haipai = my_hai+tsumo
    handcards = Handcards(get_handcards(my_haipai))
    shanten = handcards.shanten()
    return my_haipai, shanten

if __name__ == '__main__':
    print(one_haipai())
    print(samples(100000))