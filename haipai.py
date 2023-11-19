import random
hai = ['1m', '1m', '1m', '1m', '2m', '2m', '2m', '2m', '3m', '3m', '3m', '3m', '4m', '4m', '4m', '4m', '5m', '5m', '5m', '0m', '6m', '6m', '6m', '6m', '7m', '7m', '7m', '7m', '8m', '8m', '8m', '8m', '9m', '9m', '9m', '9m',
       '1p', '1p', '1p', '1p', '2p', '2p', '2p', '2p', '3p', '3p', '3p', '3p', '4p', '4p', '4p', '4p', '5p', '5p', '5p', '0p', '6p', '6p', '6p', '6p', '7p', '7p', '7p', '7p', '8p', '8p', '8p', '8p', '9p', '9p', '9p', '9p',
       '1s', '1s', '1s', '1s', '2s', '2s', '2s', '2s', '3s', '3s', '3s', '3s', '4s', '4s', '4s', '4s', '5s', '5s', '5s', '0s', '6s', '6s', '6s', '6s', '7s', '7s', '7s', '7s', '8s', '8s', '8s', '8s', '9s', '9s', '9s', '9s',
       '1z', '1z', '1z', '1z', '2z', '2z', '2z', '2z', '3z', '3z', '3z', '3z', '4z', '4z', '4z', '4z', '5z', '5z', '5z', '5z', '6z', '6z', '6z', '6z', '7z', '7z', '7z', '7z']
def ri_hai(my_hai):
    '''理牌'''
    m_list=[]
    m0 = 0
    p_list=[]
    p0 = 0
    s_list=[]
    s0 = 0
    z_list=[]
    for h in my_hai:
        if 'm' in h:
            num = h.split('m')[0]
            if num == '0':
                m0 = 1
                num = '5'
            m_list.append(num)
        elif 'p' in h:
            num = h.split('p')[0]
            if num == '0':
                p0 = 1
                num = '5'
            p_list.append(num)
        elif 's' in h:
            num = h.split('s')[0]
            if num == '0':
                s0 = 1
                num = '5'
            s_list.append(num)
        elif 'z' in h:
            z_list.append(h.split('z')[0])
    m_list.sort()
    p_list.sort()
    s_list.sort()
    z_list.sort()
    if m0 == 1:
        m_list[m_list.index('5')] = '0'
    if p0 == 1:
        p_list[p_list.index('5')] = '0'
    if s0 == 1:
        s_list[s_list.index('5')] = '0'
    
    m_str = ''.join(m_list)
    if m_str != '':
        m_str += 'm'
    p_str = ''.join(p_list)
    if p_str != '':
        p_str += 'p'
    s_str = ''.join(s_list)
    if s_str != '':
        s_str += 's'
    z_str = ''.join(z_list)
    if z_str != '':
        z_str += 'z'
    res_hai = m_str + p_str + s_str + z_str

    return res_hai

def hai_pai():
    '''
    获取配牌
    返回值为4个元组，分别为东南西北家的各自配牌和各自第一巡自摸的牌
    '''
    random.shuffle(hai)
    my_hai_0 = []
    my_hai_1 = []
    my_hai_2 = []
    my_hai_3 = []
    h = 0
    d=0 #d: 0=东起，1=南起，2=西起，3=北起
    for h in range(0+4*d, 48+4*d, 16):
        my_hai_0 += hai[h:h+4]
    my_hai_0.append(hai[h+4*(4-d)+d])

    d=1
    for h in range(0+4*d, 48+4*d, 16):
        my_hai_1 += hai[h:h+4]
    my_hai_1.append(hai[h+4*(4-d)+d])

    d=2
    for h in range(0+4*d, 48+4*d, 16):
        my_hai_2 += hai[h:h+4]
    my_hai_2.append(hai[h+4*(4-d)+d])

    d=3
    for h in range(0+4*d, 48+4*d, 16):
        my_hai_3 += hai[h:h+4]
    my_hai_3.append(hai[h+4*(4-d)+d])

    return ((ri_hai(my_hai_0), hai[52+4+0]), (ri_hai(my_hai_1), hai[52+4+1]), (ri_hai(my_hai_2), hai[52+4+2]), (ri_hai(my_hai_3), hai[52+4+3]))

def get_yama():
    '''
    获取牌山，由于全局变量hai是每次被打乱的，所以要获取牌山的话，需要在使用hai_pai()方法获取配牌后立即使用本方法，否则下一次配牌将打乱全局变量hai，无法获得本次配牌的牌山情况
    返回值为3个列表的元组，第一个列表为配牌，第二个列表为可摸的牌山，第三个列表为王牌区
    '''
    return (hai[:56], hai[56:-14], hai[-14:])
