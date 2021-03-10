import os
def getDocs():
    import pymysql
    conn = pymysql.connect(
        host='mt.tugele.rds.sogou',
        user='tugele_new',
        password='tUgele2017OOT',
        charset='utf8',
        port=3306,
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
    # 2. 创建游标对象，
    cur = conn.cursor()
    # 4). **************************数据库查询*****************************
    # sqli = 'SELECT * FROM tugele.ns_flx_wisdom_words_new'
    sqli = 'SELECT a.id,a.content,a.isDeleted FROM (tugele.ns_flx_wisdom_words_new a)'
    result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    info = cur.fetchall()  # 3). 获取所有的查询结果
    # print(info)
    # print(len(info))
    # 4. 关闭游标
    cur.close()
    # 5. 关闭连接
    conn.close()
    S = {str(info[i][0]): info[i][1] for i in range(len(info)) if info[i][2] == 0}
    return S
def getfiles(rootpath):
    datas = []
    def eachFile(filepath):
        if os.path.isfile(filepath):  # 如果是文件
            if 'part-' in filepath:
                datas.append(filepath)
                return
        fileNames = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
        for file in fileNames:
            newDir = filepath + '/' + file  # 将文件命加入到当前文件路径后面
            # print(newDir)
            # if os.path.isdir(newDir): # 如果是文件夹
            if os.path.isfile(newDir):  # 如果是文件
                if 'part-' in newDir:
                    datas.append(newDir)
            else:
                eachFile(newDir)  # 如果不是文件，递归这个文件夹的路径
    eachFile(rootpath)
    return datas
path_data = 'data/wtt'
files = getfiles(path_data)
D = []
for file in files:
    with open(file,'r') as f:
        s = f.read().strip().split('\n')
    for ss in s:
        c = ss.split('\t')
        inputStr = c[1]
        r = c[2].split('#')
        n = len([rr for rr in r if '-' not in rr])
        D.append([inputStr,n,c[3]])

D1 = [d for d in D if d[1]>=3]
D2 = [d for d in D if d[1]<3]
D3 = [d for d in D if d[1]<1]
with open('data/tmp.txt','w') as f:
    f.write('\n'.join([d[0] for d in D2]))

D4 = [d for d in D if d[2]!='-1']
D5 = []
for d in D4:
    t = d[2].split('#')
    for tt in t:
        D5.append([d[0],d[1],tt])
S = getDocs()
D6 = []
for d in D5:
    if d[2] in S:
        D6.append([d[0],d[1],S[d[2]]])


