#https://indianpythonista.files.wordpress.com/2016/10/11.png
import  requests
from  bs4  import  BeautifulSoup
import html5lib





dailyStar = 'https://www.thedailystar.net'


r = requests.get(dailyStar)

soup = BeautifulSoup(r.content, 'html5lib')

print(soup.text)

link = soup.findAll('a')

#print(link)



htmlTop = '<html>\n <head>\n <title>Document</title>\n</head>\n<body>'






def writeTofile(con):

    with open('dailyStars.html','a') as wr:

        wr.write(con)



writeTofile(htmlTop)


hrf = '<a href=' + '"'+dailyStar + '"'+'>no link </a>'

print(hrf)


for i in  link:
    #print(i['href'])

    x= i


    try:
        i = i['href']

        if x.text.find('Nusrat') > 0:

            if i.startswith('http') == False:
                i = dailyStar + i
                hrf = '<a href=' + '"' + i + '"' + '>' + x.text + '</a> <br>'
                writeTofile(hrf + '\n')
    except:
        print('erro occured')
        print(i)





htmlBottom = '</body> \n </html> '

writeTofile(htmlBottom)





#print(soup.prettify())


'''
links = soup.findAll('img')

http=''
x  = [i['src'] for i in links if  i['src'].endswith('png')]
print(x[0])
for i in  x:

    fileGet = requests.get(i)

    with open(i.split('/')[-1], 'wb') as wr:
        wr.write(fileGet.content)
        
        '''










