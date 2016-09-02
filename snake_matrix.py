#!/usr/bin/env python
# coding: utf-8


def draw_matrix(begin, size, layer, arry, controlle_num):
    # 以顺时钟方向建立递增矩阵，按照层级
    # 根据递增1的特点，建立当前层的上下左右，四个list，形成资源池
    # 每个方向list的长度都等于size的长度
    # [1,2,3]
    # [8, ,4]
    # [7,6,5]
    top = range(begin, begin+size)
    right = range(begin+size-1, begin+size*2-1)
    bottom = range(begin+size*2-2, begin+size*3-2)
    left = range(begin+size*3-3, begin+size*4-3)
    left[size-1] = begin       # 顺时钟的左list最后一个值改为起始值

    # size相当矩阵的边长，i既可以表示长，也可以表示宽
    # 通过i步进来从本层的资源池里面取得各个值
    for i in range(size):
        arry[layer][layer+i] = top[i]      
        arry[layer+i][controlle_num-layer-1] = right[i]
        arry[controlle_num-layer-1][controlle_num-layer-i-1] = bottom[i]
        arry[controlle_num-1-layer-i][layer] = left[i]
    return arry


def Matrix(size, begin=1, layer=0):
    controlle_num = size
    arry = []
    for i in range(size):
        arry.append(range(size))
    while size > 0:
        arry = draw_matrix(begin, size, layer, arry, controlle_num)
        begin = begin+(4*(size-1))
        size = size - 2
        layer = layer + 1
    return arry


if __name__ == '__main__':
    n=input('输入一个整数：')
    dat = Matrix(n)
    a=[]
    print '%d*%d的顺时针蛇形矩阵:'.decode('UTF-8').encode('GBK')%(n,n)
    for i in dat:
        print i
         
    print '%d*%d顺时针蛇形矩阵列表输出:'.decode('UTF-8').encode('GBK')%(n,n)
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            a.append(dat[i][j])
    print a

        
