
import re,xlsxwriter 

filePath = r'D:\python362\test\demo1.xlsx'
# workbook = xw.Workbook(filePath)
# worksheet = workbook.add_worksheet('test1')
# worksheet.write('A1', 'Hello world')
# workbook.close()
#workbook = xlsxwriter.Workbook(filePath, {'in_memory': True})
with xlsxwriter.Workbook(filePath) as workbook:
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Hello world')
    
str = '''interface Ethernet1/0/1~|~ description acv1_1-11111_124-desgig0/0/0~|~ip binding vpn-instance vpnb~|~ ip address 10.1.1.1 2 255.255.255.0
#
interface gigerth0/0/1.1~|~undoshut abcd123_2222222~|~ip binding vpn-instance vpnb~|~ ip address 10.1.1.2 255.255.255.0
#
interface Vlanif1/0/1~|~ description abcd123_3333333~|~ip binding vpn-instance vpnb~|~ ip address 10.1.1.32 255.255.255.0
#
ntp-serverice interface gig0/0/0
#'''
def dict_to_xlsx(d,fname,headers):
        print (d)
        import xlsxwriter

        xlsx_file = xlsxwriter.Workbook(fname)
        xlsx_worksheet = xlsx_file.add_worksheet()
        bold = xlsx_file.add_format({'bold': True})

        for i,h in enumerate(headers):
            xlsx_worksheet.write(0,i,h,bold)

        keys = list(d.keys())
        #keys = d.keys()
        keys.sort()

        for i, key in enumerate(keys):
            xlsx_worksheet.write(i+1,0,key)
            for j in range(len(d[key])):
                xlsx_worksheet.write(i+1,j+1,d[key][j])
dictData ={}
list = []
flag = 0
for i in str.split('\n#\n'):
    #print ('i = ',i)
    t1 = re.search(r'description [\w\W]+?\~\|\~',i)
    t0 = re.search(r'^interface [\w\/\.]+',i)
    t2 = re.search(r' [0-255\.]+',i)
    #print(t0.group())
    #print(type(t1.group()))
    #print(t2.group())
    if t0 :
        dictData.setdefault('interface', []).append((t0.group()).replace('interface ',''))
        if t1 :
            dictData.setdefault('description', []).append((t1.group()).replace('description ','').replace('~|~',''))
            #print ('t1 = ', t1)
        else:
            #print ('t1 = na')
            dictData.setdefault('description', []).append([])
        if t2 :
            dictData.setdefault('ip address', []).append((t2.group()).replace(' ',''))
        else:
            #print ('t1 = na')
            dictData.setdefault('ip address', []).append([])
    
k = dictData.keys()

my_dict = {'a':'aaa','b':'bbb','c':'ccc'}
print ((my_dict.keys()))
#print (list(k))
#print (re.findall(r'interface [\w\/\.]+',str))
#print('list = ',list(dictData.keys()))
#for i in dict.keys(): la.append(i)
#dict_to_xlsx(dict,filePath,list(dictData.keys()))

{'interface': ['Ethernet1/0/1', 'gigerth0/0/1.1', 'Vlanif1/0/1'], 'description': ['acv1_1-11111_124-desgig0/0/0', [], 'abcd123_3333333'], 'ip address': ['10.1.1.1', '10.1.1.2', '10.1.1.']}




