#!/usr/bin/python
# -*- coding: utf-8 -*-

def countWords(filename):
    D={}
    tmp=[]
    with open(filename,'r') as f:
        for line in f:
            tmp = [strs.strip(string.punctuation)for strs in line.lower().split()]
            for words in tmp:
                if words.isalpha():
                    if D:
                        if D.has_key(words):
                            D[words]+=1
                        else:
                            D.update({words:1})
                    else:
                        D.update({words:1})
    D_sorted = sorted(D.iteritems(),key = lambda x:x[1],reverse = True)
    a=[]
    for i in range(10):
        a.append(D_sorted[i])
    return a
if __name__ == "__main__":
    import string 
    filename = 'get_words1.py'
    print countWords(filename)
