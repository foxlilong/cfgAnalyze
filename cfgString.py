
import re,os
from pandas import DataFrame, ExcelWriter
import pandas as pd
'''
echo "# cfgAnalyze" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:foxlilong/cfgAnalyze.git
git push -u origin master
'''
str = '''interface Ethernet1/0/1~|~ description acv1_1-11111_124-desgig0/0/0~|~ip binding vpn-instance vpnb~|~ ip address 10.1.1.1 2 255.255.255.0
#
interface gigerth3/2/1.1~|~undoshut abcd123_2222222~|~ip binding vpn-instance vpnb~|~ ip address 222.111.1.244 255.255.255.0
#
interface Vlanif1/12/1~|~ description 123123123~|~ip binding vpn-instance vpnb~|~ ip address 10.1.1.244 255.255.255.0
#
ntp-serverice interface gig0/0/0
#'''
def toPortInfor(strData=''):
    d ={}
    for i in strData.split('\n#\n'):
        #print(i)
        t0 = re.search(r'^interface [\w\/\.]+',i);    
        t1 = re.search(r'description [\w\W]+?\~\|\~',i)
        t2 = re.search(r' [0-255\.]+',i)
        #print(t2.group())
        if t0:
            d.setdefault('interface', []).append((t0.group()).replace('interface ',''))
            if t1 :d.setdefault('description', []).append((t1.group()).replace('description ','').replace('~|~',''))
            else:  d.setdefault('description', []).append([])
            if t2 : d.setdefault('ip address', []).append((t2.group()).replace(' ',''))
            else:d.setdefault('ip address', []).append([])
    #print(list(d.keys()))
    return d

def saveDictToExcel(fileP,dfData):
    if not os.path.exists(fileP) : pd.ExcelWriter(fileP)
    oldData = pd.read_excel(fileP, sheet_name=0)#sheet_name = 'test'
    newData = pd.DataFrame(dfData)
    oldData.update(newData)
    writer = pd.ExcelWriter(fileP)
    print(oldData,'\n',newData)
    newData.to_excel(writer,sheet_name = 'test',index=False)
    writer.save()

myData = toPortInfor(str)
filePath = r'D:\python362\test\demo1.xlsx'
saveDictToExcel(filePath,myData)


