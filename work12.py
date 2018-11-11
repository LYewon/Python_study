r = requests.get(url)
r.encoding = 'utf8'
data = str(r.text)
begin = data.find('Madam President, Mr. Secretary-General, world leaders, ambassadors, and distinguished delegates:')

end = data.rfind('Thank you very much. Thank you. (Applause.)')
words = data[begin:end]

words = words.replace("."," ")
words = words.replace(","," ")
words = words.replace("p>"," ")
words = words.replace("<p"," ")
words = words.replace("/"," ")
words = words.replace("<"," ")
words = words.replace(">","")
words = words.replace("="," ")
words = words.replace("—"," ")
words = words.replace('"',' ')
words = words.replace(":"," ")
words = words.replace("-"," ")
words = words.replace("'"," ")
words = words.replace("</p>"," ")


mydict = {}
word = words.split()

for w in word:
    if w in mydict:
        mydict[w] += 1
    else:
        mydict[w] = 1
i = 0
for k in sorted(mydict, key=mydict.__getitem__,reverse=True):
    if i == 20:
        break
    print('%s:%s'%(k,mydict[k]))
    i += 1

