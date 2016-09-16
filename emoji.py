#!/usr/bin/python
import urllib
from os import path
import os

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Folder_Creation():
    Path1=["images/","images/emojis/", "images/emojis/5", "images/emojis/6", "images/emojis/7", "images/ponies", "images/pitch"]
    for x in range (0,len(Path1)):
        if path.isdir(Path1[x]):
            print str(Path1[x])+" folder exists"
        else:
            os.mkdir(Path1[x])#make the paths if it doesnt
            print "made folder: "+str(Path1[x])

def Emoji_Grab():
    url = range(0, 4096)
    real_url=[]
    for x in range(0,len(url)):
        real_url.append('%03x' % url[x])
    getfile = urllib.URLopener()
    for x in range(5,8):
        for i in range(0,len(real_url)):
            full_url="http://ssl.gstatic.com/chat/emoji/"+str(x)+"/emoji_u1f"+str(real_url[i]+".png")
            try:
                getfile.retrieve(str(full_url), "./images/emojis/"+str(x)+"/emoji_u1f"+str(real_url[i])+".png")
            except Exception as e:
                print "DOESNT EXIST: "+ full_url

def Pitch_Grab():
    two_letter = []
    po1=0
    po2=0
    for i in range(0, 676):
        two_letter.append(letters[po2]+letters[po1])
        po1= po1+1
        if po1 == 26:
            po1=0
            po2=po2+1
    getfile = urllib.URLopener()
    a=0
    b=0
    c=0
    for i in range(0, 456976):
        full_url="https://ssl.gstatic.com/chat/babble/ee/"+str(letters[a]+letters[b]+"/"+two_letter[c]+".png")
        full_url2="https://ssl.gstatic.com/chat/babble/ee/"+str(letters[a]+letters[b]+"/"+two_letter[c]+".gif")
        if c==675:
            c=0
            b=b+1
            if b==26:
                b=0
                a=a+1
        c=c+1
        try:
            getfile.retrieve(str(full_url), "./images/pitch/"+str(letters[a]+letters[b]+"/"+two_letter[c]+".png"))
        except Exception as e:
            print "DOESNT EXIST: "+ full_url + str(e)
        try:	
            getfile.retrieve(str(full_url2), "./images/pitch/"+str(letters[a]+letters[b]+"/"+two_letter[c]+".gif"))
        except Exception as e:
            print "DOESNT EXIST: "+ full_url2 +str(e)

def Ponie_Grab():
    real_url = []
    po1=0
    po2=0
    for i in range(0, 676):
        real_url.append(letters[po2]+letters[po1])
        po1= po1+1
        if po1 == 26:
            po1=0
            po2=po2+1
    getfile = urllib.URLopener()
    for i in xrange(0,len(real_url)):
        full_url="https://ssl.gstatic.com/chat/babble/ee/"+str(real_url[i]+".png")
        full_url2="https://ssl.gstatic.com/chat/babble/ee/"+str(real_url[i]+".gif")
        try:
            getfile.retrieve(str(full_url), "./images/ponies/"+str(real_url[i])+".png")
        except Exception as e:
            print "DOESNT EXIST: "+ full_url
        try:	
            getfile.retrieve(str(full_url2), "./images/ponies/"+str(real_url[i])+".gif")
        except Exception as e:
            print "DOESNT EXIST: "+ full_url2

try:
    def main():
        Folder_Creation()
        Emoji_Grab()
        Pitch_Grab()
        Ponie_Grab()
except KeyboardInterrupt:
    print '\n'" Bye!"
    sys.exit()

#Call the main function
if __name__=='__main__':
    main()
    sys.exit()




