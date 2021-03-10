#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
for data in sys.stdin:
    # if filename == 'viewfs://marsX/storage/sogou/desktop/imeservice/vpare/201908/20190830':
    data = data.strip()
    if 'input=' not in data or 'ids=' not in data or '_100300_' not in data:
        continue
    try:
        x = data.split('\t')
        sessid = x[0]
        c = ''.join(x[1:])
        r = c.split("\x01")
        input = ''
        ids = ''
        id = []
        for i in range(len(r)):
            if 'input=' in r[i]:
                input = r[i][6:]
                continue
            if '_100300_' in r[i] and 'vac=4' in r[i]:
                idx = r[i].index('_100300_') + len('_100300_')
                id.append(r[i][idx:])
                continue
            if 'ids=' in r[i]:
                ids = '#'.join(r[i][4:].split('\x02'))
        id = '#'.join(id)
        if id=='':
            id = '-1'
        if input and ids:
            s = '\t'.join([sessid, input, ids, id])
            sys.stdout.write(s + '\n')
    except:
        pass
