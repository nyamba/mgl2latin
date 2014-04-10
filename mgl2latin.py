# -*- coding: utf-8 -*-

def check_to_latin(src, result):
    '''
    >>> check_to_latin([u'ф', u'ц', u'у', u'ж', u'э', u'н', u'г', u'ш', u'ү', u'з', u'к', u'ъ', u'е', u'щ', \
            u'й', u'ы', u'б', u'ө', u'а', u'х', u'р', u'о', u'л', u'д', u'п', u'я', u'ч', u'ё', u'с', u'м', \
            u'и', u'т', u'ь', u'в', u'ю'], ['p,f', 'ts', 'u,y', 'j', 'e', 'n', 'g', 'sh', 'u,y', 'z', 'k', 'i', \
            'e', 'sh', 'i', 'i,ii,y', 'b', 'o,u', 'a', 'h,x,kh', 'r', 'o', 'l', 'd', 'p,f', 'ya', 'ch', 'yo', \
            's,c', 'm', 'i', 't', 'i', 'v', 'yu'])
    True
    '''
    assert len(src) == len(result), 'No same length'

    for i in range(len(src)):
        ws = to_latin(src[i])
        rr = ','.join(ws)
        assert rr == result[i], 'failed on %s -%s' % (rr, result[i])


def to_latin(cyrilic_text):
    chars = {
            u'ф':('p', 'f'), u'ц':['ts'], u'у':('u', 'y'), u'ж':('j'), u'э':('e'), u'н':('n'), u'г':('g'), u'ш':['sh'],
            u'ү':('u', 'y'), u'з':('z'), u'к':('k'), u'ъ':('i'), u'е':('e'), u'щ':['sh'], u'й':('i'), u'ы':('i', 'ii', 'y'),
            u'б':('b'), u'ө':('o', 'u'), u'а':('a'), u'х':('h', 'kh', 'x'), u'р': ('r', 'p'), u'о':('o'), u'л':('l'),
            u'д':('d'), u'п':('p', 'f'), u'я':['ya'], u'ч':['ch'], u'ё':['yo'], u'с':('s', 'c'), u'м':('m'),
            u'и':('i'), u'т':('t'), u'ь':('i'), u'в':('v'), u'ю':['yu'],
            }

    words = ['']
    for c in cyrilic_text:
        cc = chars[c]
        _words = []
        for ch in cc:
            for w in words:
                _words.append(w+ch)
        words = _words

    return words


if __name__ == '__main__':
    check_to_latin([u'хадаа'], ['hadaa,khadaa,xadaa'])
    check_to_latin([u'хөдөө'], ['hodoo,khodoo,xodoo,huduu,khuduu,xuduu'])
    check_to_latin([u'ф', u'ц', u'у', u'ж', u'э', u'н', u'г', u'ш', u'ү', u'з', u'к', u'ъ', u'е', u'щ', \
            u'й', u'ы', u'б', u'ө', u'а', u'х', u'р', u'о', u'л', u'д', u'п', u'я', u'ч', u'ё', u'с', u'м', \
            u'и', u'т', u'ь', u'в', u'ю'], ['p,f', 'ts', 'u,y', 'j', 'e', 'n', 'g', 'sh', 'u,y', 'z', 'k', 'i', \
            'e', 'sh', 'i', 'i,ii,y', 'b', 'o,u', 'a', 'h,kh,x', 'r,p', 'o', 'l', 'd', 'p,f', 'ya', 'ch', 'yo', \
            's,c', 'm', 'i', 't', 'i', 'v', 'yu'])
