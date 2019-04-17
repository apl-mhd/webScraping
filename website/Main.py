#https://indianpythonista.files.wordpress.com/2016/10/11.png
import  requests
from  bs4  import  BeautifulSoup
import html5lib




imageUrl ='https://www.pexels.com/search/HD%20wallpaper/'

gPhotos = 'https://photos.app.goo.gl/ABqF2NNL5GBh5288A'

prothomALo = 'https://www.prothomalo.com/'


r = requests.get(prothomALo)

soup = BeautifulSoup(r.content, 'html5lib')

print(soup.text)

link = soup.findAll('a')

#print(link)

def writeTofile(con):

    with open('links.html','a') as wr:

        wr.write(con)




hrf = '<a href=' + '"'+prothomALo + '"'+'>no link </a>'

print(hrf)


for i in  link:
    #print(i['href'])

    x= i

    i = i['href']

    if i.startswith('http') == False:
        i = 'https://www.prothomalo.com'+i
        hrf = '<a href=' + '"' +i+ '"' + '>'+x.text +'</a> <br>'
        writeTofile(hrf+'\n')






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










