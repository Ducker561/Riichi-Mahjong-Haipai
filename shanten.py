import re
def get_handcards(string):
    '''
    检查输入是否合法，并读取手牌内容.
    若输入不合法，输出错误提示并返回None.
    '''
    fullmatch = re.fullmatch(r'(\d+[mps]|[1-7]+z)+', string)
    if not fullmatch:
        print('无效的输入！')
        return None
    match = re.findall(r'\d+[mps]|[1-7]+z', string)
    carddict = {
        'm':[], 'p':[], 's':[], 'z':[]
    }
    for cards in match:
        type_ = cards[-1]
        for i in cards[:-1]:
            if i == '0':# 红宝牌
                carddict[type_].append(5)
            else:
                carddict[type_].append(int(i))
        carddict[type_].sort()
    num = sum(len(carddict[tp]) for tp in 'mpsz')
    if num != 14:
        print('牌数量错误！手牌数必须为14张！')
        return None
    for tp in 'mpsz':
        for i in set(carddict[tp]):
            if carddict[tp].count(i) > 4:
                break
        else:
            continue
    return carddict

class Handcards:
    def __init__(self, carddict):
        self.carddict = carddict
        self.num = sum(len(carddict[tp]) for tp in 'mpsz')

    def taatsucount(self):
        '''计算手牌中的面子、搭子、对子数，并返回一个三元元组'''
        toitsu, taatsu, mentsu = (0, 0, 0)
        carddict_cpy = {
            'm':self.carddict['m'].copy(),
            'p':self.carddict['p'].copy(),
            's':self.carddict['s'].copy(),
            'z':self.carddict['z'].copy()
        }# 创建原手牌的拷贝以进行删除操作，防止破坏原手牌
        # 因为一个面子能使向听数-2，选择先计算面子的贪心算法
        # step 1: 顺子
        for tp in 'mps':
            for i in range(1, 8):
                if i in carddict_cpy[tp]:
                    if i + 1 in carddict_cpy[tp] and i + 2 in carddict_cpy[tp]:
                        carddict_cpy[tp].remove(i)
                        carddict_cpy[tp].remove(i + 1)
                        carddict_cpy[tp].remove(i + 2)
                        mentsu += 1
        # step 2: 刻子
        for tp in 'mpsz':
            for i in range(1, 10):#不存在的89z不影响
                if carddict_cpy[tp].count(i) >= 3:
                    carddict_cpy[tp].remove(i)
                    carddict_cpy[tp].remove(i)
                    carddict_cpy[tp].remove(i)
                    # 4张字牌额外删除1张以便step5的检验
                    if tp == 'z' and carddict_cpy[tp].count(i) == 1:
                        carddict_cpy[tp].remove(i)
                    mentsu += 1
        # step 3: 对子
        toitsu_dict = {'m':[], 'p':[], 's':[]}# 用于解决step3.1的问题
        for tp in 'mps':
            for i in range(1, 10):
                if carddict_cpy[tp].count(i) == 2:
                    carddict_cpy[tp].remove(i)
                    carddict_cpy[tp].remove(i)
                    toitsu_dict[tp].append(i)
                    toitsu += 1
        for i in range(1, 8):
            if carddict_cpy['z'].count(i) == 2:
                carddict_cpy['z'].remove(i)
                carddict_cpy['z'].remove(i)
                toitsu += 1
        # step 3.1: 解决类似2446的问题
        for tp in 'mps':
            for i in toitsu_dict[tp]:
                if toitsu == 0:
                    break
                neighbor = [i - 2, i - 1, i + 1, i + 2]
                if sum(carddict_cpy[tp].count(j) for j in neighbor) >= 2:
                    # 删除其中的两个，改为搭子
                    count = 2
                    for j in neighbor:
                        if count == 0:
                            break
                        if j in carddict_cpy[tp]:
                            carddict_cpy[tp].remove(j)
                            count -= 1
                    toitsu -= 1
                    taatsu += 2
        # step 4: 搭子
        for tp in 'mps':
            for i in range(1, 9):
                if i in carddict_cpy[tp]:
                    if i + 1 in carddict_cpy[tp]:
                        carddict_cpy[tp].remove(i)
                        carddict_cpy[tp].remove(i + 1)
                        taatsu += 1
                    elif i + 2 in carddict_cpy[tp]:
                        carddict_cpy[tp].remove(i)
                        carddict_cpy[tp].remove(i + 2)
                        taatsu += 1
        # step 5: 剩余手牌检验
        # 若剩余的手牌均不存在靠张，将其删除
        # 若删除后手牌数+block数小于5（一般为4），则向听数+1
        # 数牌一般不存在完全没有靠张的情况，故只讨论字牌
        # 我们在step2中的操作已经完成了删除无效字牌的操作
        if mentsu + toitsu + taatsu + sum(len(carddict_cpy[tp]) for tp in 'mpsz') < 5:
            taatsu -= 1# 对函数本身而言这会导致搭子数计算错误，但能让向听数计算正确
        return (toitsu, taatsu, mentsu)
    
    def shanten(self):
        '''计算手牌的向听数'''
        # case 1: 国士无双
        st_kokushi = 13
        if self.num == 14:
            carddict_cpy = {
                'm':self.carddict['m'].copy(),
                'p':self.carddict['p'].copy(),
                's':self.carddict['s'].copy(),
                'z':self.carddict['z'].copy()
            }
            for tp in 'mps':
                if 1 in carddict_cpy[tp]:
                    st_kokushi -= 1
                    carddict_cpy[tp].remove(1)
                if 9 in carddict_cpy[tp]:
                    st_kokushi -= 1
                    carddict_cpy[tp].remove(9)
            for i in range(1,8):
                if i in carddict_cpy['z']:
                    st_kokushi -= 1
                    carddict_cpy['z'].remove(i)
            if carddict_cpy['z']:
                st_kokushi -= 1
            else:
                for tp in 'mps':
                    if 1 in carddict_cpy[tp] or 9 in carddict_cpy[tp]:
                        st_kokushi -= 1
                        break
        # case 2: 七对
        toitsu = 0
        dragon = 0 # 
        if self.num == 14:
            for tp in 'mpsz':
                for i in range(1,10):
                    if i in self.carddict[tp] and self.carddict[tp].count(i) == 4:
                        dragon += 1
                    elif i in self.carddict[tp] and self.carddict[tp].count(i) >= 2:
                        toitsu += 1
        # case 2.1: 塞满了，例如11112222333344z
        if toitsu + 2 * dragon == 7:
            st_chitoi = 2 * dragon - 1
        else:
            st_chitoi = 6 - toitsu - dragon
        # case 3: 一般形
        tuple_ = self.taatsucount()
        block = sum(tuple_)
        toitsu, taatsu, mentsu = tuple_
        if toitsu == 0:
            st_ippan = 8 - 2 * mentsu - taatsu + max(0, block - 4)
        else:
            st_ippan = 8 - 2 * mentsu - taatsu - toitsu + max(0, block - 5)

        return min(st_kokushi, st_chitoi, st_ippan)
