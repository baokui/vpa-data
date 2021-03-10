import os
import sys
def parse_serve(data):
    #if '"AppName":"com.jingdong.app.mall"' not in data:
        #return []
    if '"AppName":"com.tencent.xin"' not in data:
        return []
    #if '"assistant_type":"jd:shopping_reviews"' not in data:
        #return []
    if '"assistant_type":"wechat:moments_reviews"' not in data:
        return []
    if '"Input":"' not in data:
        return []
    idx0 = data.find('"UserID":"')+len('"UserID":"')
    idx1 = idx0+data[idx0:].find('","')
    userid = data[idx0:idx1]
    idx0 = data.find('"SessionID":') + len('"SessionID":')
    idx1 = idx0 + data[idx0:].find(",")
    sessid = data[idx0:idx1]
    idx0 = data.find('"Input":"')+len('"Input":"')
    idx1 = idx0+data[idx0:].find('","')
    inputStr = data[idx0:idx1].strip()
    lenStr = len(inputStr.decode('utf-8'))
    if lenStr<2 or lenStr>15:
        return []
    return [sessid,userid,inputStr]
def parse_result(data):
    if '"request_class":"allSceneUpgrade"' not in data or '"vpaRequestedText"' not in data or 'session_id' not in data or '"cards":' not in data:
        return []
    idx0 = data.index('"session_id":')+len('"session_id":')
    idx1 = idx0+data[idx0:].index(',')
    sessid = data[idx0:idx1]
    idx0 = data.index('"vpaRequestedText":"')+len('"vpaRequestedText":"')
    idx1 = idx0+data[idx0:].index('"')
    inputStr = data[idx0:idx1]
    idx0 = data.index('"cards":')+len('"cards":[')
    idx1 = idx0+data[idx0:].index(']')
    data1 = data[idx0:idx1]
    ids = []
    contents = []
    S = data1.split('},{')
    for i in range(len(S)):
        data1 = S[i]
        idx0 = data1.index('"id":"')+len('"id":"')
        idx1 = idx0+data1[idx0:].find('"')
        id = data1[idx0:idx1]
        idx0 = data1.index('"display":"')+len('"display":"')
        idx1 = idx0+data1[idx0:].index('"')
        con = data1[idx0:idx1]
        ids.append(id)
        contents.append(con)
    ids = '#'.join(ids)
    for i in range(len(contents)):
        contents[i] = contents[i].replace('#',' ')
    contents = '#'.join(contents)
    return [sessid,inputStr,ids,contents]
def parse_pingback_android(data):
    if 'vpaBoard=1' not in data or 'vac=4' not in data or 'tab1=100300' not in data or 'sessionId=' not in data or 'conid=' not in data:
        return []
    idx0 = data.index('sessionId=')+len('sessionId=')
    idx1 = idx0+data[idx0:].index('&')
    sessid = data[idx0:idx1]
    idx0 = data.index('conid=')+len('conid=')
    idx1 = idx0+data[idx0:].index('&')
    conid = data[idx0:idx1]
    return [sessid,conid]
filepath = os.environ.get('mapreduce_map_input_file')
filename = os.path.split(filepath)[0].strip()
for data in sys.stdin:
    # if filename == 'viewfs://marsX/storage/sogou/desktop/imeservice/vpare/201908/20190830':
    data = data.strip()
    if 'vpa.venus.odin.sogou' in filename:
        # data = data.replace('\t','[seq]')
        try:
            x = parse_serve(data)
            if x:
                #s = '\t'.join(x)
                s = '\t'.join(x)
                sys.stdout.write(s + '\n')
        except:
            continue
    if 'pingback/ping/djt-pb-log/vpapb_android_shouji' in filename:
        try:
            x = parse_pingback_android(data)
            if x:
                #s = '\t'.join(x)
                s = '\t'.join(x)
                sys.stdout.write(s + '\n')
        except:
            continue
    if 'desktop/imeservice/vpare/' in filename:
        try:
            x = parse_result(data)
            if x:
                #s = '\t'.join(x)
                s = '\t'.join(x)
                sys.stdout.write(s + '\n')
        except:
            continue