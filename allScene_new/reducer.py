import sys
lastid = '****'
conid0 = ''
inputStr0 = ''
ids0 = ''
contents0 = ''
for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data)==2:
        sessid,conid = data
    elif len(data)==4:
        sessid,inputStr,ids,contents = data
    else:
        continue
    if sessid!=lastid:
        if lastid!='****':
            if conid0 and inputStr0:
                S = '\t'.join([lastid,conid0,inputStr0,ids0,contents0])
                sys.stdout.write(S + '\n')
        lastid = sessid
        conid0 = ''
        inputStr0 = ''
        ids0 = ''
        contents0 = ''
    if len(data)==2:
        conid0 = conid
    else:
        inputStr0, ids0, contents0 = inputStr,ids,contents
