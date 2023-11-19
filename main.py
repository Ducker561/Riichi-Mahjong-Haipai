from haipai import hai_pai, get_yama
from shanten import Handcards, get_handcards
import numpy

def samples(n):
    '''测试n次配牌的向听数平均'''
    shanten_list=[]
    for i in range(n):
        my_hai, tsumo = hai_pai()[0]
        my_haipai = my_hai+tsumo
        handcards = Handcards(get_handcards(my_haipai))
        shanten = handcards.shanten()
        print('第'+str(i+1)+'次配牌：'+my_haipai+'，向听数：'+str(shanten))
        shanten_list.append(shanten)
    return numpy.mean(shanten_list)

def single_haipai():
    '''
    单次配牌测试
    返回值为包含4个元组的列表，分别为东南西北家的各自配牌和向听数
    '''
    res = hai_pai()
    all_haipai = []
    for d in res:
        d_haipai = d[0]+d[1]
        d_handcards = Handcards(get_handcards(d_haipai))
        d_shanten = d_handcards.shanten()
        all_haipai.append((d_haipai, d_shanten))
    return all_haipai

if __name__ == '__main__':
    print(samples(100000))  #100000次独立重复实验
    print(single_haipai())  #获取单次配牌
    print(get_yama())       #获取该次配牌的牌山信息