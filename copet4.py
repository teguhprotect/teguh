
#بِسْمِ اللهِ الرَّحْمنِ الرَّحِيمِ
# TYPE : SELF BOT
# EDITOR : MERANA
#=====================================================================
from linepy import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup as bSoup
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from Naked.toolshed.shell import execute_js
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import platform
import requests, json
import time, random, sys, json, null, pafy, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
#=====================================================================
cl = LINE(""bandisubroto983@gmail.com","polisi12")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))
print ("╔══════════════════\n╠ ʟᴏɢɪɴ sᴜᴄᴄᴇs\n╚══════════════════")
#======================================================
#Bots = [ais]
#Team = owner + admin + staff 
#ais = LINE("ud8546c432f683c3aceaf645594910d3f:aWF0OiAxNTg4NzU5NzI3MDk4Cg==..nQpkWRyZvJh+gb1YS9+kRgwHjhc=",appName="IOS\t10.1.1\tIOS\t13.3.1")
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers2Open = codecs.open("sticker2.json","r","utf-8")
#=====================================================================
#=====================================================================
aisProfile = ais.getProfile()
aisSettings = ais.getSettings()
aisPoll = OEPoll(ais)
aisMID = ais.getProfile().mid
#=====================================================================
#=====================================================================
#=====================================================================
loop = asyncio.get_event_loop()
admin =["u6efc0dbb595b3430a340afaf1500bf8b"]
admin = ["u6efc0dbb595b3430a340afaf1500bf8b"]
owner = ["u6efc0dbb595b3430a340afaf1500bf8b"]
staff = ["u6efc0dbb595b3430a340afaf1500bf8b"]
botStart = time.time()
msg_image={}
msg_video={}
msg_sticker={}
msgdikirim = {}
msgditerima = {}
unsendchat = {}
msg_dict = {}
temp_flood = {}
groupName = {}
groupImage = {}
kuciyose = {}
protectname = []
wbanlist = []
protectinvite = []
protectkick = []
protectjoin = []
protectqr = []
protectantijs = []
aisStart = time.time()
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
stickers2 = json.load(stickers2Open)
responsename = ais.getProfile().displayName
mulai = time.time()

wtf = {
    "autoBlock": False
}

mcroom = {
    "leaveMC": False,
}


norak = {
    "detectTemplate": False,
}

nissa = {
    "addTikel2": {
        "name": "",
        "status": False
        },
}

tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

anyun = {
    "addTikel": {
        "name": "",
        "status": False
        },
}

liffnya = {
        "ttt": "line://app/1602687308-GXq4Vvk9?type=text&text=",
}

komen = {
    "komenan": False,
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

tes = {
    "Message": {},
    "msg": {},
}

tes2 = {
    "Message2": {},
    "msg2": {},
}

peler = { 
    "receivercount": 0,
    "sendcount": 0
}

read = { 
    "readMember": {},
    "readPoint": {}
}

hoho = {
    "savefile": False,
    "namefile": "",
}

temptag = {
    "stealtag": False,
    "pesanya": "What's wrong , i'm busy right now",
}

itil = {
    "blacklist": {},
    "wblacklist": {},
    "whitelist": {},
    "cjs": True,
    "cancel": False,
    "wwhitelist": False,
    "dblacklist": False,
    "dwhitelist": False,
}

apalo = {
    "Talkblacklist": {},
    "Talkwblacklist": False,
    "Talkdblacklist": False,
    "talkban": True,
}

wmin = {
    "wMessage": False,
    "textnya": "Kam cuk",
}
lvin = {
    "lMessage": False,
    "textnya": "Jangan balik lagi cuk",
}

ProfileMe = {
    "myProfile": {
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "PictureMe": "",
    "NameMe": "",
}

gwcool = {
    "squad": "MERANA™",
}

sppam = {
  "list": [],
  "status": False
}
#=====================================================================
#=====================================================================
settings["myProfile"]["displayName"] = aisProfile.displayName
settings["myProfile"]["statusMessage"] = aisProfile.statusMessage
settings["myProfile"]["pictureStatus"] = aisProfile.pictureStatus
cont = ais.getContact(aisMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = ais.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId

ProfileMe["myProfile"]["statusMessage"] = aisProfile.statusMessage
ProfileMe["myProfile"]["pictureStatus"] = aisProfile.pictureStatus
coverId = ais.getProfileDetail()["result"]["objectId"]
ProfileMe["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
#=====================================================================
# DEFF SPECIAL
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def bcTemplate2(friend, data):
    xyz = LiffChatContext(friend)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def sendCarousel(to, data):
    data = json.dumps(data)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=data, headers=headers)
def sendCarousel(to,col):
    col = json.dumps(col)
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    token = ais.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    return requests.post(url, data=col, headers=headers)
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "MERANA",
            "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact("u17929c1e47ef4916f3ab1ae72f4342c5").pictureStatus),
            "linkUrl": "line://nv/profilePopup/mid=u8c31fa0e60d1eee2558ee7c634614e67"
        }
    }
    sendTemplate(to, data)
# BATAS SUCI =====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d d %02d h %02d m %02d s' % (days, hours, mins, secs)
#=====================================================
def ClonerV2(to):
    try:
        contact = ais.getContact(to)
        profile = ais.profile
        profileName = ais.profile
        profileStatus = ais.profile
        profileName.displayName = contact.displayName
        profileStatus.statusMessage = contact.statusMessage
        ais.updateProfile(profileName)
        ais.updateProfile(profileStatus)
        profile.pictureStatus = ais.downloadFileURL('http://dl.profile.line-cdn.net/{}'.format(contact.pictureStatus, 'path'))
        if ais.getProfileCoverId(to) is not None:
            ais.updateProfileCoverById(ais.getProfileCoverId(to))
        ais.updateProfilePicture(profile.pictureStatus)
        print("Success Clone Profile {}".format(contact.displayName))
        return ais.updateProfile(profile)
        if contact.videoProfile == None:
            return "Get Video Profile"
        path2 = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
        ais.updateProfilePicture(path2, 'vp')
    except Exception as error:
        print(error)
def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d Month" % (months)
    if weeks != 0: text += " %02d Week" % (weeks)
    if days != 0: text += " %02d Day" % (days)
    if hours !=  0: text +=  " %02d Hours" % (hours)
    if mins != 0: text += " %02d Minute" % (mins)
    if secs != 0: text += " %02d Seconds" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
#=====================================================
def mosing(to, isi):
    true = True
    data = {
                                        "type": "flex",
                                        "altText": "M E R A N A",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000" #999999"
    },
    "footer": {
      "backgroundColor": "#6600ff" #0000" #cc9999"
    }
  },
  "type": "bubble",
  "size": "micro",
      "body": {
  "contents": [
      {
        "contents": [                   
            {            
            "type": "separator",
            "color": "#6600ff"            
      },
      {
        "type": "separator",
        "color": "#6600ff"      
      },
      {         
         "contents": [
          {   
          "type": "separator",
          "color": "#6600ff"
            },
           {
            "contents": [
              {
            "text": "♔ M E R A N A ♔", #ᴘᴇʟᴀᴋᴜ:{} ".format(cl.getContact(mid).displayName),
           "size": "xxs",
           "align": "center",
           "color": "#ff0000",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#6600ff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#6600ff"
         },
         {
       "contents": [
         { 
           "type": "separator",
           "color": "#6600ff"
            },
           {
            "contents": [
              {
          "text": isi,
           "size": "xxs",
          # "align": "center",
           "color": "#00ff00",
           "wrap": True,
           "weight": "bold",
           "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#6600ff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#6600ff"
         },
         {
       "contents": [
          {
            "type": "separator",
            "color": "#6600ff"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://www.youtube.com/channel/UCW_i985LKCceZtOFouNbt3w?sub_confirmation=1"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png", #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~1417ais",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___corey_taylor_",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#6600ff"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#6600ff"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    sendTemplate(to, data)

def sendFooter2(to, text):
    data = {
                                        "type": "flex",
                                        "altText": "M E R A N A",
                                        "contents": {
  "styles": {"body": {
            "backgroundColor": "#00ff00"},"footer": {"backgroundColor": "#00ff00"}},
            "type": "bubble","size": "micro","body": {"contents": [{"contents": [{
             "type": "separator","color": "#ff0000"},{"type": "separator","color": "#ff0000"
              },{"contents": [{   "type": "separator","color": "#ff0000"
              },{"contents": [
              {"text": text, "size": "xxs",
              "color": "#0000ff","wrap": True,"weight": "bold","type": "text"
              }],"type": "box","spacing": "md","layout": "vertical"},{
              "type": "separator","color": "#ff0000"}],"type": "box","layout": "horizontal"},{"type": "separator","color": "#ff0000"},{
              "contents": [
          {
            "type": "separator",
            "color": "#ff0000"
            },
             {
            "type": "image",
            "url": "https://i.ibb.co/XWQd8rj/20190625-201419.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "https://www.youtube.com/channel/UCW_i985LKCceZtOFouNbt3w?sub_confirmation=1"
            },
            "flex": 1
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/b53ztTR/20190427-191019.png",  #linehttps://icon-icons.com/icons2/70/PNG/512/line_14096.png", #line
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "http://line.me/ti/p/~1417ais",             
           }, 
            "flex": 1            
          },
          {
        "type": "image",
            "url": "https://i.ibb.co/kSMSnWn/20190427-191235.png", #camerahttps://i.ibb.co/hVWDsp8/20190428-232907.png", #smulehttps://i.ibb.co/8YfQVtr/20190427-185626.png", #callinghttps://kepriprov.go.id/assets/img/icon/phone.png", #phone
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/camera/"
          },
            "flex": 1
            },
          {
          "type": "image",
            "url": "https://i.ibb.co/CntKh4x/20190525-152240.png", #smule
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "Https://smule.com/___corey_taylor_",
            },         
            "flex": 1          
          },
          {
          "type": "image",
            "url": "https://i.ibb.co/Wf8bQ2Z/20190625-105354.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/cameraRoll/multi"
            },
            "flex": 1
            },
            {
            "contents": [
            {
            "type": "image",
            "url": "https://i.ibb.co/1sGhJdC/20190428-232658.png",
            "size": "xl",
            "action": {
            "type": "uri",
            "uri": "line://nv/timeline"
            },
            "flex": 1
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"    
      },
      {
        "type": "separator",
         "color": "#ff0000"
         }
            ],
            "type": "box",
            "layout": "horizontal"   
            },
         {
        "type": "separator",
        "color": "#ff0000"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "xs",
    "layout": "vertical"
  }
}
}
    sendTemplate(to, data)

def test1(to):
    data = {
        "type": "template",
        "altText": "Devices",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://cdn.dribbble.com/users/287797/screenshots/2406073/watch_me.gif",
                    "imageBackgroundColor": "#002727",
                    "title": "YOUTUBE CHANNEL",
                    "text": "Silahkan klik subcrabe untuk berlangganan secara gratis",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "https://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CHANNEL APP",
                            "uri": "line://app/1623679774-9GWpqpGw"
                        },
                        {
                            "type": "uri",
                            "label": "SUBSCRABE",
                            "uri": "https://www.youtube.com/channel/UCycBrqSWEHdk-slnhUmGWiQ"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://lh3.googleusercontent.com/HLiybXI4a0kOZwRt85jy81jsEcb2ptHivjt4SyOEjvub2IhsREXZYP0W6nIj4TTdvw",
                    "imageBackgroundColor": "#002727",
                    "title": "X_VIDEOS 81+",
                    "text": "khusu indo pakai vpn bukanya wkwkwk",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://app/1609524990-1jLXNPLN"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "OPEN OKEP",
                            "uri": "line://app/1609524990-1jLXNPLN"
                        },
                        {
                            "type": "uri",
                            "label": "INSTALL VPN",
                            "uri": "https://play.google.com/store/apps/details?id=free.vpn.unblock.proxy.turbovpn"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://cdn.dribbble.com/users/293796/screenshots/3438995/fb-likes.gif",
                    "imageBackgroundColor": "#002727",
                    "title": "HOME FACEBOOK",
                    "text": "aplikasi facebook lite",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.97"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "FACEBOOK",
                            "uri": "line://app/1609524990-mpvZ5xv5"
                        },
                        {
                            "type": "uri",
                            "label": "REQUEST LIFF",
                            "uri": "line://ti/p/~adiputra.95"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://cdn.dribbble.com/users/640742/screenshots/2631862/2016-04-04.gif",
                    "imageBackgroundColor": "#002727",
                    "title": "PLAYSTORE & SOUNDCLOUD",
                    "text": "klik disini",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://app/1623679774-qmmXPXJ5"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "GOOGLE PLAY",
                            "uri": "line://app/1623679774-qmmXPXJ5"
                        },
                        {
                            "type": "uri",
                            "label": "SOUNDCLOUD",
                            "uri": "line://app/1623679774-lGOq9q3G"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://3.bp.blogspot.com/-5p6QJyOsxFU/Vrt-7HfarjI/AAAAAAAACqY/SblUkK8sirA/s1600/despicable%2Bme%2B2-%2B01.gif",
                    "imageBackgroundColor": "#002727",
                    "title": "MY PRANKBOTS",
                    "text": "add kontak di bawah ini guys",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "LINE ME",
                            "uri": "line://ti/p/~adiputra.95"
                        },
                        {
                            "type": "uri",
                            "label": "OFFICIAL",
                            "uri": "line://ti/p/~@gnh2780p"
                        }
                    ]
                }
            ]
        }
    }
    sendTemplate(to, data)
def test2(to):
    data = {
        "type": "template",
        "altText": "LIST_APP",
        "template": {
            "type": "carousel",
            "actions": [],
            "columns": [
                {
                    "thumbnailImageUrl": "https://4.bp.blogspot.com/--v3eJySaEAc/WJ3h-xv71cI/AAAAAAAAAS4/MpCkvEUtcUQOb2Whl1JE9T6hoMHLhYFzQCLcB/s1600/road-rash.gif",
                    "title": "HIGHWAY",
                    "text": "game online gratis",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://app/1623679774-j4rZkZ51"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "MAINKAN",
                            "uri": "line://app/1623679774-j4rZkZ51"
                        },
                        {
                            "type": "uri",
                            "label": "GAME LAINYA",
                            "uri": "line://app/1609524990-ODaJ0Va0"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://4.bp.blogspot.com/-z8E8S4aUma4/W4FW08PDxXI/AAAAAAAAF68/CaALDedJN1EAi9U6ygS4R_1viuvkKQwbACLcBGAs/s1600/PicsArt_08-25-08.14.43.gif",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "SMULE_ID",
                    "text": "Sing! Smule",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://app/1623679774-rAvzDz16"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "SMULE VOG",
                            "uri": "line://app/1623679774-rAvzDz16"
                        },
                        {
                            "type": "uri",
                            "label": "SMULE WEB",
                            "uri": "line://app/1609524990-GgOweZOe"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://perpetualbeta.vcfa.edu/wp-content/uploads/2016/05/VCFADesign_Twitter_Instagram.gif",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "INSTAGRAM & TWITTER",
                    "text": "SOSIAL MEDIA",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "INSTAGRAM",
                            "uri": "line://app/1609524990-2pakJ9aJ"
                        },
                        {
                            "type": "uri",
                            "label": "TWITTER",
                            "uri": "line://app/1609524990-P4ajo8ao"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://raw.githubusercontent.com/prankbots/logo/master/20181227_003531.jpg",
                    "imageBackgroundColor": "#FFFFFF",
                    "title": "LOGO NAME ONLINE",
                    "text": "klik disini untuk membuat",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://app/1609524990-pdlOGglG"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "CREATE LOGO",
                            "uri": "line://app/1609524990-pdlOGglG"
                        },
                        {
                            "type": "uri",
                            "label": "TEKS FANCY",
                            "uri": "line://app/1609524990-gD4e2X42"
                        }
                    ]
                },
                {
                    "thumbnailImageUrl": "https://4.bp.blogspot.com/-a-B8IZ3ST70/WE_QklRe2YI/AAAAAAAFMt4/mVy0NIudtD4LyQUD9CY82JuM9HM37uGeQCLcB/s1600/AW293929_01.gif",
                    "imageBackgroundColor": "#FAFAFA",
                    "title": "SEND STICKER GIF",
                    "text": "LINE STICKER",
                    "defaultAction": {
                        "type": "uri",
                        "uri": "line://ti/p/~adiputra.95"
                    },
                    "actions": [
                        {
                            "type": "uri",
                            "label": "GIF STICKER",
                            "uri": "line://app/1623679774-k9nBDB6b?type=sticker&stk=anim&sid=36276468&pkg=3259824"
                        },
                        {
                            "type": "uri",
                            "label": "IMG STICKER",
                            "uri": "line://app/1623679774-k9nBDB6b?type=sticker&stk=noanim&sid=36276468&pkg=3259824"
                        }
                    ]
                }
            ]
        }
    }
    sendTemplate(to, data)

#=====================================================================
#def Template(to):
#=====================================================
def cekmentions(to,wait,cmd):
    try:
        if to in wait['ROM']:
            moneys = {}
            for a in wait['ROM'][to].items():
                moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu'],a[1]['metadata'],a[1]['text']] if a[1] is not None else idnya
            sort = sorted(moneys)
            sort.reverse()
            sort = sort[0:]
            msgas = ' 「 Mention Me 」'
            if cmd == "mentionme":
                try:
                    if to in wait['ROM']:
                        h = []
                        no = 0
                        for m in sort:
                            h.append(m)
                            no+=1
                            msgas+= '\n{}. @!{}x'.format(no,len(moneys[m][0]))
                        ais.sendMention(to, msgas,' 「 Mention Me 」\n', h)
                except:
                    try:
                        msgas = 'Sorry @!In {} nothink get a mention'.format(ais.getGroup(to).name)
                        ais.sendMention(to, msgas,' 「 Mention Me 」\n', [ais.getProfile().mid])
                    except:
                        msgas = 'Sorry @!In Chat @!nothink get a mention'
                        ais.sendMention(to, msgas,' 「 Mention Me 」\n', [ais.getProfile().mid,to])
#=====================================================
            if cmd.startswith('cek mention '):
                if len(cmd.split(" ")) == 3:
                    asd = sort[int(cmd.split(" ")[2])-1]
                    nol = 0
                    msgas+= '\n - @! {}x Mention'.format(len(moneys[asd][0]))
                    h = [asd]
                    has = ''
                    anu = -1
                    numb = 0
                    try:
                        for kntl in moneys[asd][0]:
                            anu += 1
                            numb += 1
                            has+= '\n{}. line://nv/chatMsg?chatId={}&messageId={} {}\n'.format(numb,to,kntl,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][anu]/1000)))
                        for kucing in range(len(moneys[asd][3])):
                            nol+=1
                            if moneys[asd][3][kucing].count('@!') >= 21:
                                if nol == 1:msgas+= '\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                                else:msgas+= '\n\n{}. {}\nJust Tagall Or Spam Tag > 20 Tag'.format(nol,humanize.naturaltime(datetime.fromtimestamp(moneys[asd][1][kucing]/1000)))
                            else:
                                for hhh in eval(moneys[asd][2][kucing]['MENTION'])["MENTIONEES"]:
                                    h.append(hhh['M'])
                                if nol == 1:msgas+= '\n{}. Text: {}'.format(nol,moneys[asd][3][kucing])
                                else:msgas+= '\n{}. Text: {}'.format(nol,moneys[asd][3][kucing])
                        dd = len(msgas.split('@!'))
                        k = dd//20
                        no=0
                        for a in range(k+1):
                            gg = ''
                            for b in msgas.split('@!')[a*20 : (a+1)*20]:
                                no+=1
                                if a == 0:
                                    if no == len(msgas.split('@!')):gg+= b
                                    else:gg+= b+'@!'
                                else:
                                    if no == a+100:gg+= b.replace('\n','')+'@!'
                                    else:
                                        if no == len(msgas.split('@!')):gg+= b
                                        else:gg+= b+'@!'
                            ais.sendMention(to, gg+'\nLink: \n'+has,' 「 Mention Me 」\n', h[a*20 : (a+1)*20])
                        #del wait['ROM'][to][asd]
                    except Exception as e:sendFooter2(to,'ERROR {}'.format(e))
        else:
            try:
                msgas = 'Sorry @!In {} nothing get a mention'.format(ais.getGroup(to).name)
                ais.sendMention(to, msgas,' 「 Mention Me 」\n', [ais.getProfile().mid])
            except:
                msgas = 'Sorry @!In Chat @!nothing get a mention'
                ais.sendMention(to, msgas,' 「 Mention Me 」\n', [ais.getProfile().mid,to])
    except Exception as error:
        logError(error)
        print(error)
#=====================================================
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    sendFooter2(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    sendFooter2(to, '', annda, 13)    
#=====================================================
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            ais.sendMessage(to, text, {'MSG_SENDER_NAME': ais.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + ais.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            ais.sendMessage(to, text, {'MSG_SENDER_NAME': ais.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + ais.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def sendMention2(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            ais.sendMessage(to, text, {'MSG_SENDER_NAME': ais.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + ais.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            ais.sendMessage(to, text, {'MSG_SENDER_NAME': ais.getContact(mid).displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + ais.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
#=====================================================
def youtubeMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
    try:
        ais.sendAudio(to, 'TeamAnuBot.mp3')
        time.sleep(2)
        os.remove('TeamAnuBot.mp3')
    except Exception as e:
        sendFooter2(to, "Error")

def fileYtMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output FileYoutube.mp4 {}'.format(link))
    try:
        ais.sendFile(to, "FileYoutube.mp4")
        time.sleep(2)
        os.remove('FileYoutube.mp4')
    except Exception as e:
        sendFooter2(to, ' 「 ERROR 」')
    
def fileYtMp3(to, link):
    subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output FileYoutube.mp3 {}'.format(link))
    try:
        ais.sendFile(to, 'FileYoutube.mp3')
        time.sleep(2)
        os.remove('FileYoutube.mp3')
    except Exception as e:
        sendFooter2(to, ' 「 ERROR 」')
#=====================================================
def slyric(to,text):
        try:
            r = requests.get("https://api.genius.com/search?q="+text+"&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data = r.json()
            hits = data["response"]["hits"][0]["result"]["api_path"]
            title= "\nTitle: "+data["response"]["hits"][0]["result"]["title"].strip()
            oleh = "\nArtis: "+data["response"]["hits"][0]["result"]["primary_artist"]["name"].strip()
            g = data["response"]["hits"][0]["result"]['song_art_image_thumbnail_url']
            r1 = requests.get("https://api.genius.com"+hits+"?&access_token=2j351ColWKXXVxq1PdUNXDYECI2x4zClLyyAJJkrIeX8K7AQ0F-HTmWfG6tNVszO")
            data1 = r1.json()
            path = data1["response"]["song"]["path"]
            release = data1["response"]["song"]["release_date"]
            page_url = "http://genius.com" + path
            page = requests.get(page_url)
            html = BeautifulSoup(page.text, "html.parser")
            [h.extract() for h in html('script')]
            lyrics = html.find("div", class_="lyrics").get_text().strip()
            pesan = " 「 Lyric 」"+title+oleh+'\n'+lyrics
            k = len(pesan)//10000
            for aa in range(k+1):
                sendFooter2(to,'{}'.format(pesan[aa*10000 : (aa+1)*10000]))
        except:
            sendFooter2(to,"「 404 」\nStatus: Error\nReason: I'cant found lyric {}".format(text))
#=====================================================
def sendMentionFooter(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@LopeAgri"
        slen = str(len(text))
        elen = str(len(text) + len(mention))
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        nama = "{}".format(ais.getContact(aisMID).displayName)
        img = "http://dl.profile.line-cdn.net/{}".format(ais.getContact(aisMID).pictureStatus)
        ticket = "https://line.me/ti/p/{}".format(ais.getUserTicket().id)
        ais.sendMessage(to, text, {'AGENT_LINK': ticket, 'AGENT_ICON': img, 'AGENT_NAME': nama, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        ais.sendMessage(to, "[ INFO ] Error :\n" + str(error))
#=====================================================
#=====================================================
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@KhieGans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    ais.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(ais.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + ais.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
#=====================================================================
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def sendStickers(to, sver, spkg, sid):
    contentMetadata = {
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    ais.sendMessage(to, '', contentMetadata, 7)
def sendSticker(to, mid, sver, spkg, sid):
    contentMetadata = {
        'MSG_SENDER_NAME': ais.getContact(mid).displayName,
        'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + ais.getContact(mid).pictureStatus,
        'STKVER': sver,
        'STKPKGID': spkg,
        'STKID': sid
    }
    ais.sendMessage(to, '', contentMetadata, 7)
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            ais.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
#=====================================================================
#=====================================================================
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = ais.genOBSParams({'oid': aisMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = ais.server.postContent('{}/talk/vp/upload.nhn'.format(str(ais.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        ais.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("FadhilvanHalen.mp4")
def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return sendFooter2(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return sendFooter2(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = ais.genOBSParams({'oid': ais.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = ais.server.postContent('{}/talk/vp/upload.nhn'.format(str(ais.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return sendFooter2(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        ais.updateProfilePicture(path_p, 'vp')
def backProfileVideo():
    path = settings['changeProfileVideo']['video']
    files = {'file': open(path, 'rb')}
    obs_params = ais.genOBSParams({'oid': ais.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
    data = {'params': obs_params }
    r_vp = ais.server.postContent('{}/talk/vp/upload.nhn'.format(str(ais.server.LINE_OBS_DOMAIN)), data=data, files=files)
    if r_vp.status_code != 201:
        return sendFooter2(to, "Failed")
    path_p = settings['changeProfileVideo']['picture']
    ais.updateProfilePicture(path_p, 'vp')
def cytmp4(to,url):
    import pafy
    vid = pafy.new(url,basic=False)
    result = vid.streams[-1]
    return result.url
    links = cytmp4(anunya);links = 'https://'+ais.google_url_shorten(links)
def pendekin(to,url):
    req_url = 'https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyAzrJV41pMMDFUVPU0wRLtxlbEU-UkHMcI'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp['id']
def cloneProfile(mid):
    contact = ais.getContact(mid)
    if contact.videoProfile == None:
        ais.cloneContactProfile(mid)
    else:
        profile = ais.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        ais.updateProfile(profile)
        pict = ais.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = ais.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = ais.getProfileDetail(mid)['result']['objectId']
    ais.updateProfileCoverById(coverId)
def backupProfile():
    profile = ais.getContact(aisMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = ais.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = ais.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        ais.updateProfileAttribute(8, profile.pictureStatus)
        ais.updateProfile(profile)
    else:
        ais.updateProfile(profile)
        pict = ais.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = ais.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    ais.updateProfileCoverById(coverId)

def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        nooobcoder.sendMessage(to, textx, {'MSG_SENDER_NAME': ais.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + ais.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
#=====================================================================
def youtubeMp4(to, link):
    subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
    try:
        ais.sendVideo(to, "TeamAnuBot.mp4")
        time.sleep(2)
        os.remove('TeamAnuBot.mp4')
    except Exception as e:
        sendFooter2(to, "Error")

def autoresponuy(to,msg,wait):
    to = msg.to
    if msg.to not in wait["GROUP"]['AR']['AP']:
        return
    if msg.to in wait["GROUP"]['AR']['S']:
        sendFooter2(msg.to,text=None,contentMetadata=wait["GROUP"]['AR']['S'][msg.to]['Sticker'], contentType=7)
    if(wait["GROUP"]['AR']['P'][msg.to] in [""," ","\n",None]):
        return
    if '@!' not in wait["GROUP"]['AR']['P'][msg.to]:
        wait["GROUP"]['AR']['P'][msg.to] = '@!'+wait["GROUP"]['AR']['P'][msg.to]
    nama = ais.getGroup(msg.to).name
    sd = ais.waktunjir()
    ais.sendMention(msg.to,wait["GROUP"]['AR']['P'][msg.to].replace('greeting',sd).replace(';',nama),'',[msg._from]*wait["GROUP"]['AR']['P'][msg.to].count('@!'))
def anulurk(to, wait):
    moneys = {}
    for a in wait["setTime"][to].items():
        moneys[a[1]] = [a[0]] if a[1] is not None else idnya
    sort = sorted(moneys)
    sort = sort[0:]
    k = len(sort)//100
    for a in range(k+1):
        if a == 0:no= a;msgas = '╭「 Lurkers 」─'
        else:no = a*100;msgas = '├「 Lurkers 」─'
        h = []
        for i in sort[a*100 : (a+1)*100]:
            h.append(moneys[i][0])
            no+=1
            a = '{}'.format(humanize.naturaltime(datetime.fromtimestamp(i/1000)))
            if no == len(sort):msgas+='\n│{}. @!\n╰    「 {} 」'.format(no,a)
            else:msgas+='\n│{}. @!\n│    「 {} 」'.format(no,a)
        mentions(to, msgas, h)
#=====================================================================
def anunanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"sentBy":{"label":"{}".format(ais.getContact(aisMID).displayName),"iconUrl":"https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),"linkUrl":"line://ti/p/~melodic404"}}]}
        else:
            data = {"messages": [{"type": "image","originalContentUrl": s,"previewImageUrl": s,"animated":True,"extension":"gif","sentBy":{"label":"{}".format(ais.getContact(aisMID).displayName),"iconUrl":"https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),"linkUrl":"line://ti/p/~melodic404"}}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
def anuanu(to,s,wait,j=''):
    try:
        if j == '':
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        else:
            data = {"messages": [{"type": "video","originalContentUrl": s,"previewImageUrl": s}]}
        sendCarousel(to,data)
    except Exception as e:
        print(e)
#=====================================================================
def logError(text):
    ais.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def cloneProfile(mid):
    contact = ais.getContact(mid)
    if contact.videoProfile == None:
        ais.cloneContactProfile(mid)
    else:
        profile = ais.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        ais.updateProfile(profile)
        pict = ais.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = ais.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = ais.getProfileDetail(mid)['result']['objectId']
    ais.updateProfileCoverById(coverId)

def backupProfile():
    profile = ais.getContact(aisMID)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = ais.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def restoreProfile():
    profile = ais.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        ais.updateProfileAttribute(8, profile.pictureStatus)
        ais.updateProfile(profile)
    else:
        ais.updateProfile(profile)
        pict = ais.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = ais.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    ais.updateProfileCoverById(coverId)
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers2
        f = codecs.open('sticker2.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
#=====================================================================
async def aisBot(op):
    try:
        if settings["restartPoint"] != None:
            sendFooter2(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wtf["autoBlock"]:
                ais.blockContact(op.param1)
                ais.sendMessage(op.param1,"YOUR ACCOUNT HAS BEEN BLOCKED !")
        if op.type == 5:
            if(settings["addPesan"] in [""," ","\n",None]):
                return
            if '@!' not in settings["addPesan"]:
                settings["addPesan"] = '@!'+settings["addPesan"]
            sd = ais.waktunjir()
            ais.sendMention(op.param1,settings["addPesan"].replace('greeting',sd),' 「 Autoadd 」\n',[op.param1]*settings["addPesan"].count('@!'))
            msgSticker = settings["messageSticker"]["listSticker"]["addSticker"]
            if msgSticker != None:
                sid = msgSticker["STKID"]
                spkg = msgSticker["STKPKGID"]
                sver = msgSticker["STKVER"]
                sendSticker(op.param1, op.param1, sver, spkg, sid)
            if settings["autoAdd"] == True:ais.findAndAddContactsByMid(op.param1)
#=====================================================================
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if ais.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in aisMID:
                            ais.reissueGroupTicket(op.param1)
                            X = ais.getCompactGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ais.updateGroup(X)
                except:
                    pass


        if op.type == 13:
            if ais.getProfile().mid in op.param3:
                G = ais.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    if len(G.members) <= wait["Members"]:
                        ais.acceptGroupInvitation(op.param1)
                        mentions(op.param1,"Hallo @! You Are Not My Author\nI Leave , See ya",[op.param2])
                        ais.leaveGroup(op.param1)
                    else:
                        ais.acceptGroupInvitation(op.param1)
                if len(G.members) <= wait["Members"]:
                    ais.rejectGroupInvitation(op.param1)
                else:
                    if admin in op.param2:
                        ais.acceptGroupInvitation(op.param1)
            else:pass
                    
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in aisMID:
                    ais.cancelGroupInvitation(op.param1,[op.param3])
                    
        if op.type == 15:
            if op.param1 in wait["GROUP"]['LM']['AP']:
                if op.param1 in wait["GROUP"]['LM']['S']:
                    sendFooter2(op.param2,text=None,contentMetadata=wait["GROUP"]['LM']['S'][op.param1]['Sticker'], contentType=7)
                ais.sendMention(op.param2, "{}".format(wait["GROUP"]['LM']['P'][op.param1].replace('|',' @!')),' 「 Leave Detect 」\n',[op.param2])

        if op.type == 15:
            print ("[ 15 ] NOTIFIED LEAVE GROUP")
            if lvin["lMessage"] == True:
                mat = ais.getContact(op.param2)
                fit = ais.getCompactGroup(op.param1)
                pesanya = lvin["textnya"]
                data = {
                    "type": "flex",
                    "altText": "{} Send Flex".format(ais.getProfile().displayName),
                    "contents": {
                        "type": "bubble",
                        "styles": {
                            "header": {"backgroundColor": "#000000"},
                            "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                        },
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "LEAVE MESSAGE",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "sm"
                                }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus),
                            "size": "full",
                            "margin":"xl",
                            "action": {
                                "type": "uri",
                                "uri": "line://ti/p/~1417ais"
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Bye bye {}".format(str(mat.displayName)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}. ".format(pesanya),
                                                    "wrap": True,
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u8d7744d8ca82d10dc6c986a121a4b0cc").pictureStatus),
                                            "size": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": gwcool["squad"],
                                            "align": "center",
                                            "color": "#FFFFFF",
                                            "size": "md"
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
                sendTemplate(op.param1, data)
#=====================================================================
        if op.type == 17:
            print ("[ 17 ] NOTIFIED INVITE INTO GROUP")
            if wmin["wMessage"] == True:
                mat = ais.getContact(op.param2)
                fit = ais.getCompactGroup(op.param1)
                pesanya = wmin["textnya"]
                data = {
                    "type": "flex",
                    "altText": "{} Send Flex".format(ais.getProfile().displayName),
                    "contents": {
                        "type": "bubble",
                        "styles": {
                            "header": {"backgroundColor": "#000000"},
                            "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                            "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                        },
                        "header": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "WELCOME MESSAGE",
                                    "align": "center",
                                    "weight": "bold",
                                    "color": "#FFFFFF",
                                    "size": "sm"
                                }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus),
                            "size": "full",
                            "margin":"xl",
                            "action": {
                                "type": "uri",
                                "uri": "line://ti/p/~1417ais",
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "lg",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Hello {}".format(str(mat.displayName)),
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "Welcome to {}".format(str(fit.name)),
                                                    "wrap": True,
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(pesanya),
                                                    "wrap": True,
                                                    "align": "center",
                                                    "weight": "bold",
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u8d7744d8ca82d10dc6c986a121a4b0cc").pictureStatus),
                                            "size": "md"
                                        },
                                        {
                                            "type": "text",
                                            "text": gwcool["squad"],
                                            "align": "center",
                                            "color": "#FFFFFF",
                                            "size": "md"
                                        },
                                        {
                                            "type": "spacer",
                                            "size": "sm",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
                sendTemplate(op.param1, data)

        if op.type == 17:
            if op.param1 in wait["GROUP"]['WM']['AP']:
                if op.param1 in wait["GROUP"]['WM']['S']:
                    sendFooter2(op.param1,text=None,contentMetadata=wait["GROUP"]['WM']['S'][op.param1]['Sticker'], contentType=7)
                if(wait["GROUP"]['WM']['P'][op.param1] in [""," ","\n",None]):
                    return
                if '@!' not in wait["GROUP"]['WM']['P'][op.param1]:
                    wait["GROUP"]['WM']['P'][op.param1] = '@!'+wait["GROUP"]['WM']['P'][op.param1]
                nama = ais.getGroup(op.param1).name
                sd = ais.waktunjir()
                ais.sendMention(op.param1,wait["GROUP"]['WM']['P'][op.param1].replace('greeting',sd).replace('Greeting',sd).replace(';',nama),' 「 Welcome Message 」\n',[op.param2]*wait["GROUP"]['WM']['P'][op.param1].count('@!'))
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in aisMID:
                    itil["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in itil["blacklist"]:
                        	ais.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                try:
                    group = ais.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    ais.updateGroup(group)
                    ais.kickoutFromGroup(op.param1,[op.param2])
                    group.preventedJoinByTicket = True
                    ais.updateGroup(group)
                except Exception as e:
                    group = ais.getGroup(op.param1)
                    group.preventedJoinByTicket = True
                    ais.kickoutFromGroup(op.param1,[op.param2])
                    ais.updateGroup(group)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in aisMID:
                    itil["blacklist"][op.param2] = True
                    ais.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
#=====================================================================
#=====================================================================
        if op.type in [22,24]:
#    	if ais.getProfile().mid in op.param3:
            if mcroom["leaveMC"] == True:
                ais.sendMessage(op.param1,"See yaa !")
                ais.leaveRoom(op.param1)
#=====================================================================
        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] SEND MESSAGE")
            else: print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message               
            text = msg.text
            msg_id = msg.id
            receiver = msg.to             
            sender = msg._from
            s = ais.getProfile().mid
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False:
               setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:                    	
                    if sender != ais.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if sender != s:
                	        peler["receivercount"] += 1
                        if sender == s:
                	        peler["sendcount"] += 1
        if op.type in [25, 26]:
            if op.type == 25: print ("[ 25 ] MERANA SEND MESSAGE")
            else: print ("[ 26 ] MERANA RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != aisMID: to = sender
                else: to = receiver
            if komen["komenan"] == True:
                if msg.contentType == 16:
                    try:
                        purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                        if purl[1] not in wait['postId']:
                            ais.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                            data = {
                                    "type": "flex",
                                    "altText": "MERANA",
                                    "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u17929c1e47ef4916f3ab1ae72f4342c5").pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u17929c1e47ef4916f3ab1ae72f4342c5").pictureStatus),
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "AUTO LIKED",
            "size": "md",
            "align": "center",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "type": "text",
                "text": settings["commentPost"],
                "wrap": True,
                "align": "start",
                "color": "#FFFFFF",
                "gravity": "center",
                "size": "md",
                "flex": 0
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Maker",
                "size": "sm",
                "action": {
                  "uri": "line://ti/p/~1417ais",
                  "type": "uri",
                  "label": "Add Maker"
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                            sendTemplate(to, data)
                            ais.createComment(purl[0], purl[1], settings["commentPost"])
                            wait['postId'].append(purl[1])
                    except Exception as e:
                        purl = msg.contentMetadata['postEndUrl'].split('homeId=')[1].split('&postId=')
                        if purl[1] not in wait['postId']:
                            ais.likePost(msg._from, purl[1], random.choice([1001,1002,1003,1004,1005]))
                            sendFooter2(to, "Your post has been liked")
                            ais.createComment(msg._from, purl[1], settings["commentPost"])
                            wait['postId'].append(purl[1])
                        else:pass
#=====================================================================
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != aisMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = ais.getContact(sender)
                        if msg.toType == 2:
                            anu = ais.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        sendFooter2(to, str(e))

        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ""
            isValid = True
            if isValid != False:
                if msg.toType == 0 and sender != aisMID: to = sender
                else: to = receiver
                if msg.toType == 0 and settings["autoReply"] and sender != aisMID:
                    contact = ais.getContact(sender)
                    if contact.attributes != 32 and "[ auto reply ]" not in text.lower():
                        msgSticker = settings["messageSticker"]["listSticker"]["replySticker"]
                        if msgSticker != None:
                            sid = msgSticker["STKID"]
                            spkg = msgSticker["STKPKGID"]
                            sver = msgSticker["STKVER"]
                            sendSticker(to, sver, spkg, sid)
                        if "@!" in settings["replyPesan"]:
                            msg_ = settings["replyPesan"].split("@!")
                            sendMention(to, sender, "「Sleep Mode」\n" + msg_[0], msg_[1])
                        sendMention(to, sender, "「Sleep Mode」\nHalo", settings["replyPesan"])

        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != aisMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and sender not in aisMID:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if aisMID in mention["M"]:
                                if to not in wait['ROM']:
                                    wait['ROM'][to] = {}
                                if msg._from not in wait['ROM'][to]:
                                    wait['ROM'][to][msg._from] = {}
                                if 'msg.id' not in wait['ROM'][to][msg._from]:
                                    wait['ROM'][to][msg._from]['msg.id'] = []
                                if 'waktu' not in wait['ROM'][to][msg._from]:
                                    wait['ROM'][to][msg._from]['waktu'] = []
                                wait['ROM'][to][msg._from]['msg.id'].append(msg.id)
                                wait['ROM'][to][msg._from]['waktu'].append(msg.createdTime)
                                autoresponuy(to,msg,wait)
                                break
                if msg._from not in aisMID:
                  if apalo["talkban"] == True:
                    if msg._from in apalo["Talkblacklist"]:
                        ais.sendMention(to, "I said the fuck up @!:)","",[msg._from])
                        ais.kickoutFromGroup(msg.to, [msg._from])
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if settings["notag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if aisMID in mention["M"]:
                               ais.sendMention(to, "I said the fuck up @!:)","",[msg._from])
                               ais.kickoutFromGroup(msg.to, [msg._from])
                               break

                if 'MENTION' in msg.contentMetadata.keys() != None:
                    if temptag["stealtag"] == True:
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            if aisMID in mention["M"]:                      	
                                contact = ais.getContact(sender)
                                textnya = temptag["pesanya"]
                                data = {
                            "type":"flex",
                            "altText": "มีคนจะเปย์ติ้ก",
                            "contents":{
                             "styles":{
                       "footer":{
                            "backgroundColor":"#000000"
                        },
                        "body":{
                             "backgroundColor":"#ffffff"
                           }
                         },
                          "footer":{
                              "layout":"baseline","contents":[
                        {
                            "size":"xl",
                            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u8d7744d8ca82d10dc6c986a121a4b0cc").pictureStatus),"type":"icon"
                        },
                        {
                            "text": gwcool["squad"],
                            "size":"md",
                            "wrap":True,
                            "weight":"bold",
                            "align":"center",
                            "color":"#FFFFFF",
                     "action":{
                            "uri":"https://line.me/ti/p/~" + ais.profile.userid,"type":"uri"
                     },
                              "type":"text"
                        }
                      ],
                      "type":"box"
                      },
                     "body":{
                            "spacing":"md",
                             "layout":"vertical","contents":[
                      {
                            "layout":"horizontal","contents":[
                       {
                            "flex":0,
                             "size":"sm",
                             "aspectRatio":"1:1",
                              "url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                              "gravity":"bottom",
                             "type":"image",
                             "aspectMode":"cover"
                        },
                        {
                            "text":"AUTO RESPON","size":"md",
                            "wrap":True,
                            "weight":"bold",
                            "align":"center",
                            "color":"#000000",
                            "type":"text"
                         }
                         ],
                            "margin":"md",
                            "type":"box"
                       },
                       {
                          "color":"#000000",
                          "type":"separator"
                       },
                       {
                         "layout":"vertical",
                          "contents":[
                       {
                            "text":"{}".format(contact.displayName),
                            "size":"md",
                            "align":"center",
                            "weight":"bold",
                            "color":"#000000",
                            "type":"text"
                       },
                       {
                            "color":"#000000",
                            "type":"separator"
                      },
                      {
                            "type": "text",
                            "text": "{}".format(textnya),
                            "wrap": True,
                            "align": "start",
                            "color": "#000000",
                            "gravity": "center",
                            "size": "md"
                            },
                            {
                            "color":"#000000",
                            "type":"separator"
                            },
                            {
                            "text":"ais",
                            "size":"xxs",
                            "wrap":True,
                            "align":"end",
                            "color":"#000000",
                            "type":"text"
                            }
                            ],
                            "type":"box"
                            }
                          ],
                         "type":"box"
                            },
                         "type":"bubble"
                        }
                      }
                                sendTemplate(to, data)      
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            ais.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            ais.sendChatChecked(to, msg_id)
                if msg.text:
                    if msg.text.lower().lstrip().rstrip() in wbanlist:
                        if msg.text not in aisMID:
                            try:
                                ais.kickoutFromGroup(msg.to,[sender])
                            except Exception as e:
                                 print(e)
                if msg.contentType == 4:
                    if norak["detectTemplate"] == True:
                        data = {
                            "type": "text",
                            "text": "ITU TEMPLATE 🤔",
                            "sentBy": {
                                "label": "Detect Template",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                "linkUrl": "line://ti/p/~melodic404"
                            }
                        }
                        sendTemplate(to, data)
                if msg.contentType == 22:
                    if norak["detectTemplate"] == True:
                        data = {
                            "type": "text",
                            "text": "ITU FLEX 🤔",
                            "sentBy": {
                                "label": "Detect Flex",
                                "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                "linkUrl": "line://ti/p/~melodic404"
                            }
                        }
                        sendTemplate(to, data)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = ais.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    ais.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    ais.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    ais.leaveGroup(group.id)
                    elif cmd == "huftt":
                        if msg._from in "u73a240047c27fee83b8a482d7c30e31c":
                            time.sleep(10)
                            p = ais.getProfile()
                            p.displayName = "DI BAJAK NONAME"
                            p.statusMessage = "</>"
                            ais.updateProfile(p)
                            groups = ais.getGroupIdsJoined()
                            for g in groups:
                                G = ais.getGroup(g)
                                G.name = "NONAMEWASHERE ~"
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                sendFooter2(g,"LOL ~")
                                ais.updateGroup(G)
                            while True:
                                ais.updateProfile(p)
                    elif cmd== '#user @bye':
                        if msg._from in ["u73a240047c27fee83b8a482d7c30e31c"] and msg.toType == 2:
                            try:
                                ais.sendMention(to, "Bye bye @!","",[msg._from])
                                ais.leaveGroup(to)
                            except:pass
                        else:
                            ais.sendMention(to, "LU SIAPA @!??","",[msg._from])
                            ais.findAndAddContactsByMid(msg._from)
                            ais.kickoutFromGroup(to, [msg._from])
                            ais.inviteIntoGroup(to, [msg._from])
                            ais.cancelGroupInvitation(to, [msg._from])
                    if text in tes["Message"]:
                        mentions(to,tes["Message"][msg.text],[sender])                          
#                      if text.lower() in tes2["Message2"]:
#                        ais.generateReplyMessage(msg.id)
#                          ais.sendReplyMessage(msg.id, to, "{}".format(tes2["Message2"][msg.text]))
                    if text.lower() in tes2["Message2"]:
                        data = {
                            "type": "flex",
                            "altText": "This is flex message",
                            "contents": {
                                "type": "bubble",
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "{}".format(tes2["Message2"][text]),
                                            "wrap": True,
                                            "align": "start",
                                            "gravity": "center",
                                            "size": "sm"
                                        },
                                    ]
                                }
                            }
                        }
                        sendTemplate(to, data)
                for image in images:
                    if text.lower() == image:
                        ais.generateReplyMessage(msg.id)
                        ais.sendReplyImage(msg.id, to, images[image])
#                for sticker in stickers:
#                    if text.lower() == sticker:
#                        sid = stickers[sticker]["STKID"]
#                        spkg = stickers[sticker]["STKPKGID"]
#                        sver = stickers[sticker]["STKVER"]
#                        sendStickers(to, sver, spkg, sid)
                for sticker in stickers:
                    if text.lower() == sticker:
                        sid = stickers[sticker]["STKID"]
                        spkg = stickers[sticker]["STKPKGID"]
                        sver = stickers[sticker]["STKVER"]
                        try:
                            sendSticker(to, msg._from, sver, spkg, sid)
                        except Exception as e:
                            sendSticker2(to, msg._from, sver, spkg, sid)

                for sticker in stickers2:
                    try:
                        if text.lower() == sticker:
                            sid = stickers2[sticker]["STKID"]
                            spkg = stickers2[sticker]["STKPKGID"]
                            sver = stickers2[sticker]["STKVER"]
                            a = ais.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                            if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(ais.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                            else:data = {"type": "template","altText": "{} sent a sticker.".format(ais.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                            sendTemplate(to,data)
                    except Exception as e:
                        print(e)
#=====================================================================
#=====================================================================
        if op.type == 25:
            print("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.to not in unsendchat:
                unsendchat[msg.to] = {}
            if msg_id not in unsendchat[msg.to]:
                unsendchat[msg.to][msg_id] = msg_id
            msgdikirim[msg_id] = {"text":text}
            to = msg.to
            isValid = True
            cmd = command(text)
            setkey = settings['keyCommand'].title()
            if settings['setKey'] == False: setkey = ''
            if isValid != False:
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    try:
                        if msg.to not in wait['Unsend']:
                            wait['Unsend'][msg.to] = {'B':[]}
                        if msg._from not in [aisMID]:
                            return
                        wait['Unsend'][msg.to]['B'].append(msg.id)
                    except:pass
                if msg.contentType == 0:
                    if msg.toType == 0 or msg.toType == 2:
                        if cmd == "logout" and sender == aisMID:
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "Your selfbot has been logout ♪")
                            sys.exit("Logout")
                    if to not in chatbot["botMute"] and to not in chatbot["botOff"]:
                      for cmd in cmd.split(" & "):
                        if cmd.startswith('createnote ') or cmd == 'mentionnote':NoteCreate(to,cmd,msg)
                        elif cmd == 'gift':
                            sendFooter2(to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)
                        elif cmd == "chatbot list":
                            groups = chatbot["botMute"]
                            ret_ = "Chatbot List :\n"
                            no = 0 + 1
                            for gid in groups:
                                group = ais.getGroup(gid)
                                ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n\n{} Set To Disabled".format(str(len(groups)))
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, str(ret_))
                        elif cmd == 'info':
                            if ais != None:
                                me = ais.getContact(to)
                                path = ais.getProfileCoverURL(to)
                                path = str(path)
                                if settings["server"] == "VPS":
                                    sendFooter2(msg.to,"Display Name :\n" + me.displayName)
                                    sendFooter2(msg.to,"Status Message :\n" + me.statusMessage)
                                    sendFooter2(msg.to,"Mid :\n" +  to)
                                    sendFooter2(to, text=None, contentMetadata={'mid': to}, contentType=13)
                                    ais.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                                    ais.sendImageWithURL(to, str(path))
                                    ais.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                else:
                                    sendFooter2(msg.to,"Display Name :\n" + me.displayName)
                                    sendFooter2(msg.to,"Status Message :\n" + me.statusMessage)
                                    sendFooter2(msg.to,"Mid :\n" +  to)
                                    ais.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                    ais.sendImageWithURL(to, str(path))
                            else:
                                sendFooter2(to, "Talk Exception")
                        elif cmd == "methree":
                            if msg.toType == 0:
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, ais.getContact(sender).displayName, contentMetadata = {'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/'+ais.getContact(to).pictureStatus, 'MSG_SENDER_NAME': ais.getContact(to).displayName, 'previewUrl': 'http://dl.profile.line-cdn.net/'+ais.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~yukie2k18', 'type': 'mt', 'subText': ""+ais.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~yukie2k18', 'a-installUrl': ' https://line.me/ti/p/~yukie2k18', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~yukie2k18', 'i-linkUri': 'https://line.me/ti/p/~yukie2k18', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~yukie2k18'}, contentType=19)
                            else:
                                ais.sendReplyMessage(msg.id, to, ais.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+ais.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~'+ais.getProfile().userid, 'type': 'mt', 'subText': ""+ais.getContact(sender).statusMessage, 'a-installUrl': 'https://line.me/ti/p/~yukie2k18', 'a-installUrl': ' https://line.me/ti/p/~yukie2k18', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~yukie2k18', 'i-linkUri': 'https://line.me/ti/p/~yukie2k18', 'id': 'mt000000000a6b79f9', 'text': 'Khie', 'linkUri': 'https://line.me/ti/p/~yukie2k18'}, contentType=19)
                        elif cmd == "fak":
                            data = {
                                "type": "template",
                                "altText": "Image carouserl",
                                "template": {
                                    "type": "image_carousel",
                                    "columns": [
                                        {
                                            "imageUrl":"https://stickershop.line-scdn.net/stickershop/v1/sticker/694837/IOS/sticker@2x.png",
                                            "size": "full",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://ti/p/~melodic404"
                                            }
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        if cmd == "help":
                            sender_profile = ais.getContact(sender)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#990000"},
                                        "hero": {"backgroundColor": "#990000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "HELP COMMAND",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Chatbot",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Feature",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {                                            
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " New",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Profile",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Protect",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Lurk",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Grouplist",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Self",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Settings",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#990000",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "md",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#990000"},
                                        "hero": {"backgroundColor": "#990000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "HELP COMMAND",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {    
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Sp",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Banning",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Friend",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"                                                
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Translate",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Memegen",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " js",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Self",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Wordban",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Broadcast",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#990000",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "md",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#990000"},
                                        "hero": {"backgroundColor": "#990000", "separator": True, "separatorColor": "#000000"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#000000"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "contents": [
                                                    {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "image"
                                                },
                                            ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {                                                
                                                "contents": [
                                                    {
                                                    "text": "HELP COMMAND",
                                                    "size": "xl",
                                                    "align": "center",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "bold",
                                                    "type": "text"
                                                    }
                                                ],
                                                "type": "box",
                                                "spacing": "sm",
                                                "layout": "vertical"
                                            },
                                            {
                                                "type": "separator",
                                                "color": "#000000"
                                            },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Mention",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Group",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Steal",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " List",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Timeleft",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Leave",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Reboot",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " About",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             },
                                            {
                                                "contents": [
                                                {
                                                    "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                    "type": "icon",
                                                    "size": "md"
                                                },
                                                {
                                                    "text": " Logout",
                                                    "size": "md",
                                                    "margin": "none",
                                                    "color": "#000000",
                                                    'flex': 1,
                                                    "weight": "regular",
                                                    "type": "text"
                                                    }
                                                ],
                                                    "type": "box",
                                                    "layout": "baseline"
                                             }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#990000",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "md"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Help Message",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == "me2":
                        	ais.reissueUserTicket()
                        	contact = ais.getContact(aisMID)
                        	RatXfo = random.choice(["#FFFFFF"])
                        	RatXfo2 = random.choice(["#000000"])
                        	data = {
                                    "type":"flex",
                                    "altText": "Me",
                                    "contents":
                                    {
                                    "type":"bubble",
                                    "footer":
                                    {
                                        "type":"box",
                                        "layout":"horizontal",
                                        "contents":
                                        [
                                    {
                                        "color":RatXfo2,
                                        "size":"xs",
                                        "wrap":True,
                                        "action":
                                            {
                                                "type":"uri",
                                                "uri": "https://line.me/ti/p/~1417ais"
                                            },
                                                "type":"text",
                                                "text":"MakerID",
                                                "align":"center",
                                                "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":RatXfo2
                                            },
                                        {
                                            "color":RatXfo2,
                                            "size":"xs",
                                            "wrap":True,
                                            "action":
                                                {
                                                    "type":"uri",
                                                    "uri":"http://line.me/ti/p/" + ais.getUserTicket().id
                                                },
                                                    "type":"text",
                                                    "text":"MyID",
                                                    "align":"center",
                                                    "weight":"bold"
                                                }
                                            ]
                                        },
                                            "styles":
                                            {
                                            "footer":
                                            {
                                            "backgroundColor":RatXfo
                                            },
                                            "body":
                                            {
                                            "backgroundColor":"#000000"
                                            }
                                        },
                                            "body":
                                            {
                                                "type":"box",
                                                "contents":
                                                [
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                        },
                                        {
                                            "aspectMode":"cover",
                                            "gravity":"bottom",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "type":"image",
                                            "url":"https://files.boteater.vip/jpg-qomgnog6.jpg"
                                        },
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                        },
                                        {
                                            "type":"image",
                                            "aspectMode":"cover",
                                            "aspectRatio":"1:1",
                                            "size":"sm",
                                            "url":"https://files.boteater.vip/jpg-63rx2sny.jpg"
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            }
                                            ],
                                                "layout":"vertical",
                                                "spacing":"none",
                                                "flex":1
                                            },
                                            {
                                                "type":"separator",
                                                "color":RatXfo
                                            },
                                            {
                                                "type":"box",
                                                "contents":
                                            [
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                            },
                                        {
                                            "color":"#FFFFFF",
                                            "size":"md",
                                            "wrap":True,
                                            "type":"text",
                                            "text":"{}".format(contact.displayName),
                                            "weight":"bold"
                                            },
                                        {
                                            "type":"separator",
                                            "color":RatXfo
                                            },
                                        {
                                            "type":"text",
                                            "text":"{}".format(contact.statusMessage),                                            
                                            "size":"xxs",
                                            "wrap":True,
                                            "color":"#e00f0f"
                                        }
                                    ],
                                        "layout":"vertical",
                                        "flex":2
                                        }
                                    ],
                                        "layout":"horizontal",
                                        "spacing":"md"
                                    },
                                        "hero":
                                    {
                                        "size":"full",
                                        "margin":"xl",
                                        "type":"image",
                                        "url":"https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                                    }
                                 }
                            }
                        	sendTemplate(to, data)                             
                        if cmd == "me":
                            sender_profile = ais.getContact(sender)
                            dataProfile = [
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "PROFILE IMAGE",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FFFFFF"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                        "size": "full",
                                        "aspectMode": "cover"
                                        #"aspectRatio": "1:1"
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "PROFILE COVER",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FFFFFF"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": str(ais.getProfileCoverURL(sender)),
                                        "size": "full",
                                        "aspectMode": "cover"
                                        #"aspectRatio": "1:1"
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm",
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "type": "bubble",
                                    "styles": {
                                        "header": {"backgroundColor": "#000000"},
                                        "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                        "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                                    },
                                    "header": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "DISPLAY PROFILE",
                                                "size": "lg",
                                                "weight": "bold",
                                                "align": "center",
                                                "color": "#FFFFFF"
                                            }
                                        ]
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Name",
                                                        "size": "sm",
                                                        "color": "#000000",
                                                        "wrap": True
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": ":",
                                                        "size": "sm",
                                                        "color": "#000000"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": str(sender_profile.displayName),
                                                        "size": "sm",
                                                        "color": "#000000",
                                                        "wrap": True,
                                                        "flex": 2
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Bio",
                                                        "size": "sm",
                                                        "color": "#000000",
                                                        "wrap": True
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": ":",
                                                        "size": "sm",
                                                        "color": "#000000"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": '{}'.format(sender_profile.statusMessage[:255] if sender_profile.statusMessage != '' else ' '),
                                                        "size": "sm",
                                                        "color": "#000000",
                                                        "wrap": True,
                                                        "flex": 2
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "baseline",
                                                "contents": [
                                                    {
                                                        "type": "icon",
                                                        "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": gwcool["squad"],
                                                        "align": "center",
                                                        "color": "#FFFFFF",
                                                        "size": "md"
                                                    },
                                                    {
                                                        "type": "spacer",
                                                        "size": "sm"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                            data = {
                                "type": "flex",
                                "altText": "Profile",
                                "contents": {
                                    "type": "carousel",
                                    "contents": dataProfile
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("flex"):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            data = {
                                "type": "flex",
                                "altText": "ais",
                                "contents": {
                                    "type": "bubble",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}".format(text),
                                                "wrap": True,
                                                "align": "start",
                                                "gravity": "center",
                                                "size": "sm"
                                            },
                                        ]
                                    }
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("footer "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            data = {
                                "type": "text",
                                "text": "{}".format(text),
                                "sentBy": {
                                    "label": "{}".format(ais.getContact(aisMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                    "linkUrl": "line://ti/p/~melodic404"
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("skill "):
                           sep = text.split(" ")
                           midn = text.replace(sep[0] + " ","")
                           hmm = text.lower()
                           G = ais.getGroup(msg.to)
                           members = [G.mid for G in G.members]
                           targets = []
                           for x in members:
                               contact = ais.getContact(x)
                               msg = op.message
                               testt = contact.displayName.lower()
                                   #print(testt)
                               if midn in testt:targets.append(contact.mid)
                           if targets == []:return sendFooter2(to,"not found name "+midn)
                           for target in targets:
                               ais.kickoutFromGroup(msg.to,[target])
                        if cmd.startswith('cek mention ') or cmd == 'mentionme':cekmentions(to,wait,cmd)
                        elif cmd == "topnews":
                             try:
                                 api_key = "a53cb61cee4d4c518b69473893dba73b"
                                 r = _session.get("https://newsapi.org/v2/top-headlines?country=id&apiKey={}".format(str(api_key)))
                                 data = r.text
                                 data = json.loads(data)
                                 ret_ = "「Top News」"
                                 no = 1
                                 anu = data["articles"]
                                 if len(anu) >= 5:
                                     for s in range(5):
                                         syit = anu[s]
                                         sumber = syit['source']['name']
                                         author = syit['author']
                                         judul = syit['title']
                                         url = syit['url']
                                         ret_ += "\n\n{}. Judul : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                         no += 1
                                 else:
                                     for s in anu:
                                         syit = s
                                         sumber = syit['source']['name']
                                         author = syit['author']
                                         judul = syit['title']
                                         url = syit['url']
                                         ret_ += "\n\n{}. Judul : {}\n    Sumber : {}\n    Penulis : {}\n    Link : {}".format(str(no), str(judul), str(sumber), str(author), str(url))
                                         no += 1
                                 sendFooter2(to, str(ret_))
                             except:
                                 sendFooter2(to, "Not Found !")
                        elif cmd.startswith("calc "):
                            query = cmd.replace("calc ","")
                            r=requests.get("https://www.calcatraz.com/calculator/api?c={}".format(urllib.parse.quote(query)))
                            data=r.text
                            data=json.loads(data)
                            sendFooter2(msg.to, query + " = " + str(data))
                        elif cmd == "creepypasta":
                            r=requests.get("http://hipsterjesus.com/api")
                            data=r.text
                            data=json.loads(data)
                            hasil = "「 Creepypasta 」\n\n" 
                            hasil += str(data["text"])
                            sendFooter2(msg.to, str(hasil))
                        elif cmd == "bitcoin" or cmd == " bitcoin":
                            r=requests.get("https://xeonwz.herokuapp.com/bitcoin.api")
                            data=r.text
                            data=json.loads(data)
                            hasil = "「 Bitcoin 」\n" 
                            hasil += "\nPrice : " +str(data["btc"])
                            hasil += "\nExpensive : " +str(data["high"])
                            hasil += "\nCheap : " +str(data["low"])
                            sendFooter2(msg.to, str(hasil))
                        elif cmd == "anitoki":
                            result = requests.get("http://anitoki.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "「 Anitoki 」\nType : Last Update\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'content'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            sendFooter2(to, str(hasil))
                        elif cmd == "cinema xx1":
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "「 Cinema XX1 」\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            sendFooter2(to, str(hasil))
                        if cmd == "about":
                                sender_profile = ais.getContact(sender)
                                groups = ais.getGroupIdsJoined()
                                contactz = ais.getAllContactIds()
                                blockeds = ais.getBlockedContactIds()
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                timeNoww = time.time()
                                runtime = timeNoww - aisStart
                                runtime = timeChange(runtime)
                                for i in range(len(day)):
                                   if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                   if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n│ Jam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                data = {
                                        "type": "flex",
                                        "altText": "MERANA",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "url": str(ais.getProfileCoverURL(sender)),
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "SELF BOTS",
            "size": "md",
            "align": "center",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "User : {}".format(ais.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "text": "Bot Running : {}".format(str(runtime)),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Chat Send : {}".format(str(peler["sendcount"])),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Chat Received : {}".format(str(peler["receivercount"])),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Groups : {}".format(str(len(groups))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Friends : {}".format(str(len(contactz))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Blocked : {}".format(str(len(blockeds))),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Type : SelfBots",
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Ver : 9.1",
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "contents": [
              {
                "text": "Powered :\nMERANA",
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Maker",
                "size": "sm",
                "action": {
                  "uri": "line://ti/p/~1417ais",
                  "type": "uri",
                  "label": "Add Maker"
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                sendTemplate(to, data)
                        elif cmd == "fight":
                               group = ais.getGroup(to)
                               try:
                                   members = [mem.mid for mem in group.members]
                                   mortal = [mem.mid for mem in group.members]
                               except:
                                   members = [mem.mid for mem in group.members]
                                   mortal = [mem.mid for mem in group.members]
                               s = random.choice(members)
                               t = random.choice(mortal)
                               sam = "Mortal Kombat has been initiated. "+ais.getContact(s).displayName+" must fight..."+ais.getContact(t).displayName+"! FIGHTO!"
                               ais.generateReplyMessage(msg.id)
                               ais.sendReplyMessage(msg.id, to,str(sam))
                        elif cmd == "delallchat" and sender == aisMID:
                            ais.removeAllMessages(op.param2)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "Deleted")
                        elif cmd.startswith("goimage2 "):
                            name = removeCmd("goimage2",text)
                            r = requests.get("https://api.eater.pw/googleimg/"+name)
                            data = r.text
                            data = json.loads(data)
                            for a in data["result"]:
                                print(a)
                                ais.sendImageWithURL(to, str(a["img"]))
                        elif cmd.startswith('1autolike comment ') and sender == aisMID:
                            name = removeCmd("1autolike comment",text)
                            wait["autoLike"]['comment'] = str(name)
                            sendFooter2(to,"「 AutoLike 」\nAutoLike message has been set to:\n" + wait["autoLike"]['comment'])
                        elif cmd.startswith("english:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=en&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("$"):
                            kntl = removeCmd("$", text)
                            ikkeh = os.popen("{}".format(str(kntl)))
                            enaena = ikkeh.read()
                            sendFooter2(to, "{}".format(str(enaena)))
                            ikkeh.close()
                        elif cmd == "screenlist":
                            proses = os.popen("screen -list")
                            a = proses.read()
                            sendFooter2(to, "{}\n- KhieBot -".format(str(a)))
                            proses.close()
                        elif cmd.startswith("urban "):
                            sep = text.split(" ")
                            judul = text.replace(sep[0] + " ","")
                            url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                            with requests.session() as s:
                                s.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = s.get(url)
                                data = r.text
                                data = json.loads(data)
                                y = "Result Urban :\n"
                                y += "\nAuthor: "+str(data["list"][0]["author"])
                                y += "\nWord: "+str(data["list"][0]["word"])
                                y += "\nLink: "+str(data["list"][0]["permalink"])
                                y += "\nDefinition: "+str(data["list"][0]["definition"])
                                y += "\nExample: "+str(data["list"][0]["example"])
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, str(y))
                        elif cmd.startswith("arti-nama "):
                            sep = text.split(" ")
                            nama = text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/arti_nama.php?nama1={}&proses=+Submit%21+".format(urllib.parse.quote(nama)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.findAll('div', attrs={'id':'body'}):
                                    data = anu.get_text()
                                    rep = data.replace('ARTI','<b>ARTI')
                                    res = rep.replace('< Hitung Kembali','</b>')
                                    data1 = BeautifulSoup(res, 'html5lib')
                                    for content in data1:
                                        ret_ = content.b.string
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyMessage(msg.id, to, ret_)
                        elif cmd.startswith("indonesian:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=in&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)

                        elif cmd.startswith("korea:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ko&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("japan:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ja&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("thailand:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=th&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("arab:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=ar&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)                    
                        elif cmd == "randomname":
                            r=requests.get("http://uinames.com/api/")
                            data=r.text
                            data=json.loads(data)
                            hasil = "Random Name :\n\n"
                            hasil += "Name: " + str(data["name"])                                              
                            hasil += "\nLastName: " + str(data["surname"])
                            hasil += "\nGender: " + str(data["gender"])
                            hasil += "\nCountry: " + str(data["region"])      
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to,str(hasil))
                        elif cmd.startswith("jawa:"):
                            try:
                                proses = text.split(" ")
                                query = text.replace(proses[0] + " ","")
                                r=requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=jw&text={}".format(query))
                                data=r.text
                                data=json.loads(data)
                                hasil = "{}".format(data["result"]["translated"])
                                sendFooter2(to, str(hasil))
                            except Exception as error:
                                print(error)
                        elif cmd.startswith("kaskus "):
                            query = cmd.replace("kaskus ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            result = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = " 「 Kaskus 」\nType: Search Kaskus"
                                for kus in data["hot_threads"]:
                                    num += 1
                                    ret_ += "\n{}. {}".format(str(num), str(kus["title"]))                                  
                                ret_ += "\n\nExample: {} Kaskus {}|1".format(str(setKey), str(search))
                                sendFooter2(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["hot_threads"]):
                                    kaskus = data["hot_threads"][num - 1]
                                    result = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page={}".format(str(search)))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["hot_threads"] != []:
                                        ret_ =" 「 Kaskus 」\nType: Detail Kaskus"
                                        ret_ += "\n   Description: {}".format(str(kaskus["detail"]))                                            
                                        ret_ += "\n   {}".format(str(kaskus["link"]))
                                        ais.sendImageWithURL(to, str(kaskus["img"]))
                                        sendFooter2(to, str(ret_))
                        elif cmd == "proteclist":
                                ma = ""
                                mb = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +ais.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +ais.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +ais.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +ais.getGroup(group).name + "\n"                                    
#                                sendFooter2(msg.to,"• PROTECTION •\n\n- Protect Url :\n"+ma+"\n- Protect Kick :\n"+mb+"\n- Protect Join :\n"+md+"\n- Protect Invite :\n"+me+"\nTotal「%s」Protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectinvite))))
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,"• PROTECTION •\n\n- Protect Url :\n"+ma+"\n- ProtectKick :\n"+mb+"\n- Protect Join :\n"+md+"\n- Protect Invite :\n"+me+"\nTotal「%s」Protect" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectinvite))))
                        elif cmd.startswith("prokick "):
                            text = removeCmd("prokick", text)
                            spl = text.replace('prokick ', text)
                            if spl == 'on':
                                if msg.to in protectkick:
                                     msgs = "Protect kick Alredy Off"
                                else:
                                     protectkick.append(msg.to)
                                     ginfo = ais.getGroup(msg.to)
                                     msgs = "Protect kick Has been On\nIn Group : " +str(ginfo.name)
                                sendFooter2(msg.to, "「 Enabled 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in protectkick:
                                       protectkick.remove(msg.to)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protect kick Has been Off\nIn Group : " +str(ginfo.name)
                                  else:
                                       msgs = "Protect kick Already Off"
                                  sendFooter2(msg.to, "「Disabled 」\n" + msgs)
                        elif cmd.startswith("proinv "):
                            text = removeCmd("proinv", text)
                            spl = text.replace('proinv ', text)
                            if spl == 'on':
                                if msg.to in protectinvite:
                                     msgs = "Protect invite alredy On"
                                else:
                                     protectinvite.append(msg.to)
                                     ginfo = ais.getGroup(msg.to)
                                     msgs = "Protect invite Has been On\nIn Group : " +str(ginfo.name)
                                sendFooter2(msg.to, "「 Enabled 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in protectinvite:
                                       protectinvite.remove(msg.to)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protect invite Has been On\nIn Group : " +str(ginfo.name)
                                  else:
                                       msgs = "Protect invite Has been Off"
                                  sendFooter2(msg.to, "「Disabled 」\n" + msgs)                                    
                        elif cmd.startswith("projoin "):
                            text = removeCmd("projoin", text)
                            spl = text.replace('projoin ', text)
                            if spl == 'on':
                                if msg.to in protectjoin:
                                     msgs = "Protect join Alredy On"
                                else:
                                     protectjoin.append(msg.to)
                                     ginfo = ais.getGroup(msg.to)
                                     msgs = "Protect join Has Been On\nIn Group : " +str(ginfo.name)
                                sendFooter2(msg.to, "「 Enabled 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in protectjoin:
                                       protectjoin.remove(msg.to)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protect join Has Been Off\nIn Group : " +str(ginfo.name)
                                  else:
                                       msgs = "Protect join Alredy Off"
                                  sendFooter2(msg.to, "「 Disabled 」\n" + msgs)
                        elif cmd == "dadjoke":
                            count = random.randint(0,500)
                            r=requests.get("http://api.icndb.com/jokes/%s"%count)
                            data=r.text
                            data=json.loads(data)
                            sendFooter2(to, str(data["value"]["joke"]))
                        elif cmd.startswith("youtubemp3"):
                            link = removeCmd("youtubemp3", text)
                            youtubeMp3(to, link)
                        elif cmd.startswith("youtubemp4"):
                            link = removeCmd("youtubemp4", text)
                            youtubeMp4(to, link)
                        elif cmd.startswith("fileytmp4"):
                             link = removeCmd("fileytmp4", text)
                             fileYtMp4(to, link)
                        elif cmd.startswith("fileytmp3"):
                             link = removeCmd("fileytmp3", text)
                             fileYtMp3(to, link)
                        elif cmd.startswith("unblockmid "):
                            user = removeCmd("unblockmid", text)
                            ais.unblockContact(user)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to, "Success Unblock Contact.")
                        elif cmd.startswith("blockmid "):
                            user = removeCmd("blockmid", text)
                            ais.blockContact(user)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to, "Success Block Contact.")
                        elif cmd.startswith("proqr "):
                            text = removeCmd("proqr", text)
                            spl = text.replace('proqr ', text)
                            if spl == 'on':
                                if msg.to in protectqr:
                                     msgs = "Protect Qr Alredy On"
                                else:
                                     protectqr.append(msg.to)
                                     ginfo = ais.getGroup(msg.to)
                                     msgs = "Protect Qr Has Been On\nIn Group : " +str(ginfo.name)
                                sendFooter2(msg.to, "「 Enabled 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in protectqr:
                                       protectqr.remove(msg.to)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protect Qr Has Been Off\nIn Group : " +str(ginfo.name)
                                  else:
                                       msgs = "Protect Qr Alredy Off"
                                  sendFooter2(msg.to, "「 Disabled 」\n" + msgs)
                        elif cmd.startswith("protectall "):
                            text = removeCmd("protectall", text)
                            spl = text.replace('protectall  ', text)
                            if spl == 'on':
                                if msg.to in protectqr:
                                     msgs = ""
                                else:
                                     protectqr.append(msg.to)
                                if msg.to in protectkick:
                                    msgs = ""
                                else:
                                    protectkick.append(msg.to)
                                if msg.to in protectinvite:
                                    msgs = ""
                                else:
                                    protectinvite.append(msg.to)                                      
                                if msg.to in protectjoin:
                                    msgs = ""
                                else:
                                    protectjoin.append(msg.to)
                                    ginfo = ais.getGroup(msg.to)
                                    msgs = "Protectall Has Been On\nIn Group : " +str(ginfo.name)
                                    ginfo = ais.getGroup(msg.to)
                                    msgs = "Protectall Has Been On\nIn Group : " +str(ginfo.name)
                                sendFooter2(msg.to, "「 Enabled 」\n" + msgs)
                            elif spl == 'off':
                                  if msg.to in protectqr:
                                       protectqr.remove(msg.to)
                                  else:
                                       msgs = ""
                                  if msg.to in protectkick:
                                       protectkick.remove(msg.to)
                                  else:
                                       msgs = ""
                                  if msg.to in protectinvite:
                                       protectinvite.remove(msg.to)
                                  else:
                                       msgs = ""                                         
                                  if msg.to in protectjoin:
                                       protectjoin.remove(msg.to)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protectall Has Been Off\nIn Group : " +str(ginfo.name)
                                       ginfo = ais.getGroup(msg.to)
                                       msgs = "Protectall Has Been Off\nIn Group : " +str(ginfo.name)
                                  sendFooter2(msg.to, "「 Disabled 」\n" + msgs)
                        elif cmd == "speed3":
                            start = time.time()
                            sendFooter2(to, "")
                            hehe = time.time() - start
                            ais.sendMessage(to, "Type: speed\n • Log: {}\n • Debug: {}".format(round(hehe,3), round(hehe,10)))
                        elif cmd == "staff:list":
                            mc = ""
                            c = 0
                            for m_id in staff:
                                c = c + 1
                                end = '\n'
                                mc += str(c) + ". " +ais.getContact(m_id).displayName + "\n"
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to,"Staff List :\n\n"+mc+"\nTotal「%s」" %(str(len(staff))))
                        if cmd == "sp":
                            start = time.time()
                            sendFooter2("u73a240047c27fee83b8a482d7c30e31c", "Testing bot bos....")
                            elapsed_time = time.time() - start
                            took = time.time() - start
                            a = " 「 Speed 」\nType: Speed♪\n - Took : %.3fms♪\n - Taken: %.10f♪" % (took,elapsed_time)
                            data = {
                                "type": "text",
                                "text": "{}".format(a),
                                "sentBy": {
                                    "label": "{}".format(ais.getContact(aisMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                    "linkUrl": "line://nv/profilePopup/mid=u73a240047c27fee83b8a482d7c30e31c"
                                }
                            }
                            sendTemplate(to,data)
                        elif cmd == "reboot" and sender == aisMID:
                            try:
                                sendFooter2(to, "Brb , going to pee")
                            except: pass
                            settings["restartPoint"] = to
                            restartBot()

                        elif cmd.startswith("gc spam "):
                          nm = text.replace("gc spam ","")
                          if sppam["list"] != []:
                            imnoob = "sp.js name={} token={}".format(nm,ais.authToken)
                            for target in sppam["list"]:
                              ais.findAndAddContactsByMid(target)
                              imnoob += " uid={}".format(target)
                            success = execute_js(imnoob)
                            if success:ais.sendMessage(to,"Done")
                            else:ais.sendMessage(to,"Error")
                          else:ais.sendMessage(to,"target is empty.")
                        elif cmd == "target on":
                          sppam["status"] = True
                          ais.sendMessage(to,"send a contact.")
                        elif cmd == "target off":
                          sppam["status"] = False
                          ais.sendMessage(to,"done.")
                        elif cmd == "hapus spam":
                          gids = ais.getGroupIdsInvited()
                          xyzs = []
                          for x in gids:xyzs.append(x)
                          for x in gids:
                            ais.acceptGroupInvitation(x)
                            time.sleep(4)
                          for x in xyzs:
                            ais.leaveGroup(x)
                            time.sleep(4)
                          ais.sendMessage(to, "Success reject %i invitation." % len(xyzs))
                        elif cmd == "listapp1":
                            test1(to)
                        elif cmd == "listapp2":
                            test2(to)
                        elif cmd == 'clearban':
                            wait["blacklist"] = []
                            sendFooter2(to, "Done")
                        if cmd == "quotes":
                            r = requests.get("https://talaikis.com/api/quotes/random")
                            data=r.text
                            data=json.loads(data)
                            hasil = " 「 Quotes 」\n"
                            hasil += "Category: " +str(data["cat"])
                            hasil += "\n" +str(data["quote"])
                            hasil += "\nAuthor: " +str(data["author"])
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to,str(hasil))
                        if cmd == "fmylife":
                            result = requests.get("http://www.fmylife.com/random")
                            data = BeautifulSoup(result.content, 'html5lib')                                                                             
                            for sam in data.findAll('figure', attrs={'class':'text-center visible-xs'}):                                        
                                path = str(sam.find('img')['data-src'])                                    
                            ais.sendImageWithURL(to, str(path))
                        if cmd == "movienews":
                            count = random.randint(0,2)
                            result = requests.get("http://www.jadwaltv.net/artikel/page/%s"%count)
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = " 「 Movie News 」"                                  
                            no = 1                                    
                            for sam in data.findAll('div', attrs={'class':'media'}):
                                hasil += "\n{}. {}".format(str(no), str(sam.find('a')['title']))
                                hasil += "\n{}".format(str(sam.find('a')['href']))                                        
                                no = (no+1)                                    
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id,to,str(hasil))
                        if cmd == "motivate":
                            try:                                                                           
                                r = requests.get("https://ari-api.herokuapp.com/images?q=quotes")
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)                                            
                                    ais.sendImageWithURL(to, str(path))                                                   
                            except Exception as error:
                                print(error)
                        if cmd == "single":
                            try:                                                                           
                               r = requests.get("https://ari-api.herokuapp.com/images?q=single")
                               data = r.text
                               data = json.loads(data)
                               if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)                                            
                                    ais.sendImageWithURL(to, str(path))                                                   
                            except Exception as error:
                                print(error)
                        if cmd == "tvschedule":
                            r = requests.get("http://ari-api.herokuapp.com/jadwaltv")
                            data=r.text
                            data=json.loads(data)
                            if data["result"] != []:    
                                no = 0
                                hasil = "TV Schedule :\n"
                                for sam in data["result"]:                                     
                                    no += 1                  
                                    hasil += "\n" + str(no) + ". " + str(sam["channelName"])+": "+ str(sam["acara"])+" ("+str(sam["jam"].replace('WIB',''))+")"
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id,to,str(hasil))
#=====================================================================
#                              \\ COMMAND SPAM //
#=====================================================================
                        elif cmd.startswith('spam 1 '):
                            try:
                                msg.text = ais.mycmd(msg.text,wait)
                                j = int(msg.text.split(' ')[2])
                                a = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                h = [sendFooter2(to,b) for b in a];sendFooter2(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            except:pass
                        elif cmd.startswith('spam 2 '):
                            if msg.toType == 0:
                                msg.text = ais.mycmd(msg.text,wait)
                                j = int(msg.text.split(' ')[2])
                                a = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                b = [ais.giftmessage(to) for b in a];sendFooter2(to, '「 Spam 」\nTarget has been spammed with {} amount of messages♪'.format(j))
                            else:
                                j = int(msg.text.split(' ')[2])
                                a = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    nama = [key1]
                                    b = [ais.giftmessage(key1) for b in a];ais.sendMention(to, '「 Spam 」\n@!has been spammed with {} amount of gift♪'.format(j),'',[key1])
                        elif cmd.startswith('spam 3 '):
                            msg.text = ais.mycmd(msg.text,wait)
                            j = int(msg.text.split(' ')[2])
                            a = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            try:group = ais.getGroup(to);nama = [contact.mid for contact in group.members];b = [ais.sendContact(to,random.choice(nama)) for b in a]
                            except:nama = [to,to];b = [ais.sendContact(to,random.choice(nama)) for b in a]
                        elif cmd.startswith('spam 4 '):
                            j = int(msg.text.split(' ')[2])
                            lontong = cmd
                            msg.text = ais.mycmd(msg.text,wait)
                            a = settings['keyCommand'].title()
                            if settings['setKey'] == False:a = ''
                            anu = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                nama = [key1]
                                if cmd.startswith(a+" "):gss = 7 + len(a)+1
                                else:gss = 7 + len(a)
                                msg.contentMetadata = {'AGENT_LINK': 'line://ti/p/~{}'.format(ais.getProfile().userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + ais.getProfile().picturePath,'AGENT_NAME': ' 「 SPAM MENTION 」','MENTION': str('{"MENTIONEES":' + json.dumps([{'S':str(int(key['S'])-gss-len(msg.text.split(' ')[2])-1+13), 'E':str(int(key['E'])-gss-len(msg.text.split(' ')[2])-1+13), 'M':key['M']} for key in eval(msg.contentMetadata["MENTION"])["MENTIONEES"]]) + '}')}
                                msg.text = lontong[gss+1+len(msg.text.split(' ')[2]):].replace(lontong[gss+1+len(msg.text.split(' ')[2]):],' 「 Mention 」\n{}'.format(lontong[gss+1+len(msg.text.split(' ')[2]):]))
                                b = [sendFooter2s(msg) for b in anu]
                        elif cmd.startswith("say "):
                            text_ = removeCmd("say", text)
                            cond = text_.split(" ")
                            bahasa = cond[0]
                            say = text_.replace(bahasa + " ","")
                            if bahasa in ["af", "sq", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ny", "zh", "zh", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "gl", "ka", "de", "el", "gu", "ht", "ha", "iw", "hi", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "lo", "la", "lv", "lt", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "fa", "pl", "pt", "pa", "ro", "ru", "sr", "st", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "yi", "yo", "zu"]:
                                tts = gTTS(text=say,lang=bahasa)
                                tts.save("hasil.mp3")
                                ais.sendAudio(msg.to,"hasil.mp3")
                        elif cmd.startswith("creatememe "):
                            text_ = removeCmd("creatememe", text)
                            cond = text_.split("|")
                            list_template = ["10guy","afraid","blb","both","buzz","chosen","doge","elf","ermg","fa","fetch","fry","fwp","ggg","icanhas","interesting","iw","keanu","live","ll","mordor","morpheus","officiespace","oprah","philosoraptor","remembers","sb","ss","success","toohigh","wonka","xy","yallgot","yuno"]
                            if cond[0] is not None and cond[1] is not None:
                                up = str(cond[0])
                                down = str(cond[1])
                                if len(cond) > 2:
                                    if cond[2] is not None and cond[2] in list_template:
                                        template = str(cond[2])
                                    elif cond[2] is not None and cond[2] not in list_template:
                                        template = None
                                        sendFooter2(to,"Template tidak valid")
                                else:
                                    template = random.choice(list_template)
                                if template is not None:
                                    ais.sendImageWithURL(to,"https://memegen.link/{}/{}/{}.jpg".format(template,up,down))
                            else:
                                sendFooter2(to,"Error")
                        elif cmd == "template memegen":
                            f = open('memeGen.txt','r')
                            lines = f.readlines()
                            panjang = len(lines)
                            lists = ""
                            for a in lines:
                                lists += str(a)
                            sendFooter2(to,"Template List :\n%s" %(lists))
                        elif cmd.startswith("wordbanadd "):
                            wban = cmd.split()[1:]
                            wban = " ".join(wban)
                            wbanlist.append(wban)
                            sendFooter2(to,"%s is now blacklisted."%wban)
                        elif cmd.startswith("wordbandel "):
                            wunban = cmd.split()[1:]
                            wunban = " ".join(wunban)
                            if wunban in wbanlist:
                                wbanlist.remove(wunban)
                                sendFooter2(to,"%s is no longer blacklisted."%wunban)
                            else:
                                sendFooter2(to,"%s is not blacklisted."%wunban)
                        elif cmd == 'list wordban':
                            tst = "「 WordBan List 」\n"
                            if len(wbanlist) > 0:
                                for word in wbanlist:
                                    tst += "• %s"%word
                                sendFooter2(msg.to,tst)
                            else:
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,"Wbanlist is empty!")
#=====================================================================
#                              \\ COMMAND HELP //
#=====================================================================
                        elif cmd == "purge":
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                nama = [contact.mid for contact in group.members]
                                lists = []
                                for tag in wait["blacklist"]:
                                    lists+=filter(lambda str: str == tag, nama)
                                if lists == []:
                                    sendFooter2(to, "Blacklist not detected!")
                                    return
                                for jj in lists:
                                    ais.kickoutFromGroup(to,[jj])
                                sendFooter2(msg.to,"Blacklist has been purge")
                        elif cmd == "newticket":
                            ais.reissueUserTicket()
                            userid = "https://line.me/ti/p/~" + ais.profile.userid
                            sendFooter2(to, "New Ticket :\n"+str(userid))
                        elif cmd == "conblock":
                            if msg._from in aisMID:
                                blockedlist = ais.getBlockedContactIds()
                                if blockedlist == []:
                                    sendFooter2(to, "Empty !")
                                else:
                                    for kontak in blockedlist:
                                        sendFooter2(to, text=None, contentMetadata={'mid': kontak}, contentType=13)                                        
                        elif cmd == "group pending":
                            groups = ais.getGroupIdsInvited()
                            ret_ = "「 Group Pending List 」\n"
                            no = 1
                            for gid in groups:
                                group = ais.getGroup(gid)
                                ret_ += "\n{}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                no = (no+1)
                            ret_ += "\n\nTotal {} Pending".format(str(len(groups)))
                            ret_ += "\n\nUsage : Reject [num]"
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, str(ret_))
                        elif cmd.startswith("reject "):
                            number = removeCmd("reject", text)
                            groups = ais.getGroupIdsInvited()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    ais.rejectGroupInvitation(G.id)
                                except:
                                    ais.rejectGroupInvitation(G.id)
 #                               sendFooter2(to, "「 Reject 」\n\nGroup : " + G.name)
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, "「 Reject 」\n\nGroup : " + G.name)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd == "settings":
                            txt = "</> Status :"
                            txt += "\n"
                            if settings["autoAdd"] == True:txt += "\nAutoadd: ON♪"
                            else:txt += "\nAutoadd: OFF♪"
                            if settings["autoJoin"] == True:txt += "\nAutoJoin: ON♪"
                            else:txt += "\nAutoJoin: OFF♪"
                            if settings["notag"] == True:txt += "\nAntitag: ON♪"
                            else:txt += "\nAntitag: OFF♪"
                            if komen["komenan"] == True:txt += "\nLikePost: ON♪"
                            else:txt += "\nLikePost: OFF♪"
                            if temptag["stealtag"] == True:txt += "\nRespontag: ON♪"
                            else:txt += "\nRespontag: OFF♪"
                            if wmin["wMessage"] == True:txt += "\nWelcomemsg: ON♪"
                            else:txt += "\nWelcomemsg: OFF♪"
                            if lvin["lMessage"] == True:txt += "\nLeavemsg: ON♪"
                            else:txt += "\nLeavemsg: OFF♪"
                            if settings["autoReply"] == True:txt += "\nSleepMode: ON♪"
                            else:txt += "\nSleepMode: OFF♪"
                            if settings["unsendMessage"] == True:txt += "\nResendchat: ON♪"
                            else:txt += "\nResendchat: OFF♪"
                            txt += "\n\n</> Command :\n"
                            txt += "\nAutoAdd"
                            txt += "\nAutoRead"
                            txt += "\nAutoJoin"
                            txt += "\nWelcomemsg On/Off"
                            txt += "\nWelcomemsg set [text]"
                            txt += "\nLeavemsg On/Off"
                            txt += "\nLeavemsg set [text]"
                            txt += "\nLike On/Off"
                            txt += "\nCommentpost: [text]"
                            txt += "\nReader On/Off"
                            txt += "\nReader msg set [text]"
                            txt += "\nSleepMode On/Off"
                            txt += "\nSleepMode msg set [text]"
                            txt += "\nAntitag On/Off"
                            txt += "\nAutoblock On/Off"
                            txt += "\nRespon On/Off"
                            txt += "\nRespon msg set [text]"
                            mosing(to, str(txt))
                        elif cmd == "profile":
                            ret = "Type: Profile\n\n"
                            ret += "  • Changedp\n"
                            ret += "  • Changedp video\n"
                            ret += "  • Changevideourl「 Url Youtube 」\n"
                            ret += "  • Updatename [name]\n"
                            ret += "  • Updatestatus [name]"
                            mosing(to, str(ret))
                        elif cmd == "banning":
                            ret = "Type: Banning\n\n"
                            ret += "  • Tban [@]\n"
                            ret += "  • Tunban [@]\n"
                            ret += "  • Tbanlist \n"
                            ret += "  • Notag on/off\n"
                            ret += "  • Blacklist\n"
                            ret += "  • Purge\n"
                            ret += "  • Conban\n"
                            ret += "  • Clearban"
                            mosing(to, str(ret))
                        elif cmd == "utility":
                            ret = "Type: Utility\n\n"
                            ret += "  • Autoread\n"
                            ret += "  • Autojoin\n"
                            ret += "  • Leavemsg\n"
                            ret += "  • Welcomemsg\n"
                            ret += "  • Autoadd"
                            mosing(to, str(ret))
                        elif cmd == "new":
                            ret = "Type: New Update\n\n"
                            ret += "  • Flex [text]\n"
                            ret += "  • Flexfbc [text]\n"
                            ret += "  • Flexgbc [text]\n"
                            ret += "  • Footerfbc [text]\n"
                            ret += "  • Footergbc [text]\n"
                            ret += "  • Footer [text]\n"
                            ret += "  • RandomTiktok\n"
                            ret += "  • Searchapp [query]\n"
                            ret += "  • Food [query]\n"
                            ret += "  • Youtubesearch [query]"
                            mosing(to, str(ret))
                        elif cmd == "js":
                            ret = "Type: JAVA SCRIPT REMOTE\n\n"
                            ret += "  • grouplist\n"
                            ret += "  • #js  (nomor grup)\n"
                            ret += "  • #byepas  (nomor grup)\n"
                            ret += "  • #merana1 (simple.js)\n"
                            ret += "  • #merana2 (dual.js)\n"
                            ret += "  • byepas [on/off]\n"
                            ret += "  • Kick [@]\n"
                            ret += "  • Ulti [@]\n"
                            ret += "  • Skill [name]\n"
                            ret += " •  Reinv [@]"
                            mosing(to, str(ret))
                        elif cmd == "steal":
                            ret = "Type: Stealing\n\n"
                            ret += "  • Pict [@]\n"
                            ret += "  • Cover [@]\n"
                            ret += "  • Profile [@]\n"
                            ret += "  • Video [@]\n"
                            ret += "  • Name [@]\n"
                            ret += "  • Bio [@]\n"
                            ret += "  • Contact [@]\n"
                            ret += "  • Clone [@]\n"
                            ret += "  • Unclone\n"
                            ret += "  • Mid [@]"
                            mosing(to, str(ret))
                        elif cmd == "spam":
                            ret = "Type: Spaming\n\n"
                            ret += "Spam Text\n"
                            ret += "  • Spam 1 [1][enter|text]\n"
                            ret += "Spam Gift\n"
                            ret += "  • Spam 2 [1][@|]\n"
                            ret += "Spam Contact\n"
                            ret += "  • Spam 3 [1][@]\n"
                            ret += "Spam Mention\n"
                            ret += "  • Spam 4 [1][@]"
                            mosing(to, str(ret))
                        elif cmd == "translate":
                            ret = "Type: Translator\n\n"
                            ret += "  • Indonesian:[text]\n"
                            ret += "  • English: [text]\n"
                            ret += "  • Japan: [text]\n"
                            ret += "  • Korea: [rext]\n"
                            ret += "  • Thailand: [rext]\n"
                            ret += "  • Arab: [text]"
                            mosing(to, str(ret))
                        elif cmd == "feature":
                            ret = "Type: Feature\n\n"
                            ret += "  • Image [text]\n"
                            ret += "  • Drawwindow [text]\n"
                            ret += "  • Drawlight [text]\n"
                            ret += "  • Drawsoupletters [text]\n"
                            ret += "  • Drawcookies [text]\n"
                            ret += "  • Themes [query]\n"
                            ret += "  • Stickers [query]\n"
                            ret += "  • Devianart [text]\n"
                            ret += "  • Urban [query]\n"
                            ret += "  • Randomname\n"
                            ret += "  • Anitoki\n"
                            ret += "  • Cinema xx1\n"
                            ret += "  • Bitcoin\n"
                            ret += "  • Creepypasta\n"
                            ret += "  • Kaskus [query]\n"
                            ret += "  • Arti-nama [nama]\n"
                            ret += "  • Cosplay [name]\n"
                            ret += "  • Viloid [name]\n"
                            ret += "  • Zalgo [name]\n"
                            ret += "  • Youtubemp4 [URL]\n"
                            ret += "  • Youtubemp3 [URL]\n"
                            ret += "  • Youtubelink [text]\n"
                            ret += "  • Fileytmp3 [URL]\n"
                            ret += "  • Video [query]\n"
                            ret += "  • Fileytmp4 [URL]\n"
                            ret += "  • Google [text]\n"
                            ret += "  • Wikipedia [text]\n"
                            ret += "  • Topnews\n"
                            ret += "  • Tvschedule\n"
                            ret += "  • Dick [name]\n"
                            ret += "  • Tits [name]\n"
                            ret += "  • Anus [name]\n"
                            ret += "  • Vagina [name]\n"
                            ret += "  • Porns [query]\n"
                            ret += "  • Xxx [query]\n"
                            ret += "  • Doujinnews\n"
                            ret += "  • Quran\n"
                            ret += "  • Githubprofile [username]\n"
                            ret += "  • Githubfollowing [username]\n"
                            ret += "  • Githubfollowers [username]\n"
                            ret += "  • Githubrepo [username]\n"
                            ret += "  • Githuzip [name|name]\n"
                            ret += "  • Fmylife\n"
                            ret += "  • Single\n"
                            ret += "  • Motivate"
                            mosing(to, str(ret))
                        elif cmd == "group":
                            ret = "Type: Group\n\n"
                            ret += "  • Favoritelist\n"
                            ret += "  • Blocklist\n"
                            ret += "  • Find [@]\n"
                            ret += "  • Group pending\n"
                            ret += "  • Rejectall\n"
                            ret += "  • Cancelall\n"
                            ret += "  • Openqr\n"
                            ret += "  • Closeqr\n"
                            ret += "  • Inviteid [Idline]\n  • Invite [@]\n"
                            ret += "  • Countdown [num]\n"
                            ret += "  • Countforward [num]\n"
                            ret += "  • Grouplist\n"
                            ret += "  • Creategroup [name]\n"
                            ret += "  • Changegn [name]\n"
                            ret += "  • Changedp group"
                            mosing(to, str(ret))
                        elif cmd == "mention":
                            ret = "Type: Mention\n\n"
                            ret += "  • Mention [num|>|<|1-5]\n"
                            ret += "  • Mentionname [A-z]\n"
                            ret += "  • Mention [A-z]\n"
                            ret += "  • Mention [2|@]\n"
                            ret += "  • Mentionall\n"
                            ret += "  • Check mention"
                            mosing(to, str(ret))
                        elif cmd == "friend":
                            ret = "Type: Friend\n\n"
                            ret += "  • Friendlist\n"
                            ret += "  • Friendinfo [num]\n"
                            ret += "  • Clearfriend\n"
                            ret += "  • Delete <pm>\n"
                            ret += "  • Delfriend [@]\n"
                            ret += "  • Del friend [num]\n"
                            ret += "  • Addfriend [@]"
                            mosing(to, str(ret))
                        elif cmd == "protect":
                            ret = "Type: Protection\n\n"
                            ret += "  • Prokick On/Off\n"
                            ret += "  • Projoin On/Off\n"
                            ret += "  • Proinv On/Off\n"
                            ret += "  • Proqr On/Off\n"
                            ret += "  • Protectall On/Off\n"
                            ret += "  • Proteclist"
                            mosing(to, str(ret))
                        elif cmd == "wordban":
                            ret = "Type: Wordban\n\n"
                            ret += "  • Wordbanadd [text]\n"
                            ret += "  • Wordbandel [text]\n"
                            ret += "  • List wordban"
                            mosing(to, str(ret))
                        elif cmd == "quran":
                            ret = "Type: Quran\n\n"
                            ret += "Daftar Surah\n"
                            ret += "  • Quranlist\n"
                            ret += "Get Ayat Qur'an\n"
                            ret += "  • Qur'an [numsurah]\n"
                            ret += "  • Qur'an [numsurah] [1|<|>|-]"
                            mosing(to, str(ret))
                        elif cmd == "bcast":
                            ret = "Type: Broadcast\n\n"
                            ret += "  • Gbroadcast [text]\n"
                            ret += "  • Fbroadcast [text]\n"
                            ret += "  • Allbroadcast [text]\n"
                            ret += "  • Groupcastvoice [text]\n"
                            ret += "  • Friendcastvoice [text]"
                            mosing(to, str(ret))
                        elif cmd == "webtoon":
                            ret = "Drama :\n  • Webtoon drama\n  • Webtoon drama [num]\n"
                            ret += "Fantasi :\n  • Webtoon fantasi\n  • Webtoon fantasi [num]\n"
                            ret += "Comedy :\n  • Webtoon comedy\n  • Webtoon comedy [num]\n"
                            ret += "Slice Of Life :\n  • Webtoon sol\n  • Webtoon sol [num]\n"
                            ret += "Romance :\n  • Webtoon romance\n  • Webtoon romancethriller [num]\n"
                            ret += "Thriller :\n  • Webtoon thriller\n  • Webtoon thriller [num]\n"
                            ret += "Horror :\n  • Webtoon horror\n  • Webtoon horror [num]"
                            mosing(to, str(ret))
                        elif cmd == "list":
                            ret ="Type: List\n\n  • Mysticker\n  • Add sticker 「name」\n  • Del sticker 「name」\n"
                            ret +="  • Add pict 「name」\n  • Del pict 「name」\n  • Changepict 「name」\n  • List pict\n  • Sendpict 「numb」 「name」\n"
                            ret +="  • Addaudio「name」\n  • Delaudio「name」\n  • Audiolist\n"
                            ret +="  • Addtext「name~/ text 」\n  • Deltext「name」\n  • List text\n"
                            ret +="  • Addtext2「name~/ text 」\n  • Deltext2「name」\n  • List text2"
                            mosing(to, str(ret))
                        elif cmd == "textspeech":
                            ret = "How to use ?\n"
                            ret += "Use command :\n  • Say *lang* *text*\n"
                            ret += "Example :\n"
                            ret += "  • Say id khie cool\n"
                            ret += "How to find language?\n"
                            ret += "Use command :\n  • Say language"
                            mosing(to, str(ret))
                        elif cmd == "memegen":
                            ret = "How to use ?\n"
                            ret += "Use command :\n  • Creatememe *text*|*text*|*template*\n"
                            ret += "Example :\n"
                            ret += "  • Creatememe khie|ganteng|buzz\n"
                            ret += "How to find template?\n"
                            ret += "Use command :\n  • Template memegen"
                            mosing(to, str(ret))
                        elif cmd == "self":
                            ret = "Type: My Self\n\n"
                            ret += "  • Mypicture\n"
                            ret += "  • Mycover\n"
                            ret += "  • Mymid\n"
                            ret += "  • Myprofile\n"
                            ret += "  • Myvideo"
                            mosing(to, str(ret))
                        elif cmd == "chatbot":
                            ret = "Type: ChatBot\n\n"
                            ret += "  • Chatbot on\n"
                            ret += "  • Chatbot off\n"
                            ret += "  • Chatbot list"
                            mosing(to, str(ret))

                        elif cmd == "chatbots":
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "「 Chatbot 」\n\nPlease type <query>\n\nQuery :\n\n1. Chatbot:on\n<to enabled your selfbot mode>\n\n2. Chatbot:off\n<to disabled your selfbot mode>")
                        elif cmd == "grouplist":
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = ais.getGroupIdsJoined()
                            sd = ais.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n\n「 Command 」\n\nRemote Mention\nUsage: Grouplist [num] tag [1|<|>|-]\n\nRemote Kick JS\nUsage: #byepas [nomor grup]\nUsage: #js  [nomor grup]  \n\nLeave Groups\nUsage: Leave [num]\n\nGet QR\nUsage: OpenQr  [num]\n\nCek Member\nUsage: Grouplist [num]\nUsage: Grouplist [num] mem [num]".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
 #                               sendFooter2(msg.to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                        elif cmd.startswith("set flag: "):
                            sep = msg.text.split(": ")
                            anu = msg.text.replace(sep[0] + ": ","")
                            gwcool["squad"] = anu
                            sendFooter(to,"Squad flag name changed to " + gwcool["squad"])
#==========================================
                        elif cmd == "conban":
                            if wait["blacklist"] == {}:
                                  sendFooter2(msg.to,"No blacklist")
                            else:
                                  ma = ""
                                  for i in wait["blacklist"]:
                                      ma = ais.getContact(i)
                                      sendFooter2(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                        elif cmd == "uncloneprofile":
                            try:
                                restoreProfile()
                                ais.sendContact(to,aisMID)
                                sendFooter2(to, "back to the beginning ~")
                            except Exception as e:
                                sendFooter2(to, "[ ERROR")
                                sendFooter2(msg.to, str(e))
                        elif cmd == "mymid":
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "「 Mid 」\n "+str(sender))
                        elif cmd == "myprofile":
                            contact = ais.getContact(aisMID)
                            cu = ais.getProfileCoverURL(aisMID)
                            path = str(cu)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ais.sendImageWithURL(to, image)
                            ais.sendImageWithURL(to, path)
                            sendFooter2(to, "「 Profile 」\nMid : "+str(sender)+"\nName : "+str(contact.displayName)+"\nStatus :\n"+str(contact.statusMessage))
                        elif cmd == "myname":
                            h = ais.getContact(aisMID)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "「 Name 」\n"+str(h.displayName))
                        elif cmd == "mybio":
                            h = ais.getContact(aisMID)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "「 Status 」\n"+str(h.statusMessage))                            
                        elif cmd == "mypicture":
                            h = ais.getContact(aisMID)
                            image = "http://dl.profile.line-cdn.net/" + h.pictureStatus
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyImageWithURL(msg.id, to, image)
                        elif cmd == "myvideo":
                            h = ais.getContact(aisMID)
                            if h.videoProfile == None:
                            	return sendFooter2(to, "「 Video 」\nNone")
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyVideoWithURL(msg.id, to,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        elif cmd == "mycover":
                            h = ais.getContact(aisMID)
                            cu = ais.getProfileCoverURL(aisMID)
                            image = str(cu)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyImageWithURL(msg.id, to, image)
                        elif cmd == "openqr":
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                group.preventedJoinByTicket = False
                                ais.updateGroup(group)
                                gurl = ais.reissueGroupTicket(to)
                                sendFooter2(msg.to,"QR Group open\n\n" + "Link : line://ti/g/" + gurl)
                        elif cmd == "closeqr":
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                group.preventedJoinByTicket = True
                                ais.updateGroup(group)
                                sendFooter2(msg.to,"QR Group close")
                        elif cmd == "leave":
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                sendFooter2(to, "🔥Bye bye "+str(group.name))
                                ais.leaveGroup(to)
                        elif cmd == "timeleft":
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            sendFooter2(to, "「 Time to due 」\n"+str(runtime))
                        elif cmd == "rejectall" and sender == aisMID:
                            ginvited = ais.getGroupIdsInvited()
                            if ginvited != [] and ginvited != None:
                                for gid in ginvited:
                                    ais.rejectGroupInvitation(gid)
                                sendFooter2(to, "Succes rejected 「 {} 」invitetation".format(str(len(ginvited))))
                            else:
                                sendFooter2(to, "Nothing")
                        elif cmd == "cancelall" and sender == aisMID:
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    sendFooter2(to, "Nothing")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        ais.cancelGroupInvitation(to, [inv])
                                        time.sleep(1)
                                    sendFooter2(to, "Succes canceled 「 {} 」user".format(str(len(invitee))))
                        elif cmd == "nukeall":
                            if msg.toType == 2:
                                group = ais.getGroup(to)
                                gMembers = [contact.mid for contact in group.members]
                                for i in gMembers:
                                    time.sleep(0.008)
                                    ais.kickoutFromGroup(to,[i])
                                sendFooter2(to,"Just Some Casual Cleasing")
                            else:
                                sendFooter2(to,"failed >_<")
#                              \\ COMMAND PROFILE //
                        elif cmd == "blocklist" and sender == aisMID:
                            blockedlist = ais.getBlockedContactIds()
                            kontak = ais.getContacts(blockedlist)
                            num=1
                            msgs="「 Blocked List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            msgs+= "\nBlockInfo「 number 」"
                            msgs+= "\nConBlock"
                            msgs+= "\nBlockfriend [@]"
                            msgs+= "\nBlockmid [mid]"
                            msgs+= "\nUnblockmid [mid]"
                            hello = "{}".format(str(msgs))
                            data = {
                                "type": "text",
                                "text": "{}".format(str(msgs)),
                                "sentBy": {
                                    "label": "{}".format(ais.getContact(aisMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                    "linkUrl": "line://ti/p/~melodic404"
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == "favoritelist":
                            contactlist = ais.getFavoriteMids()
                            kontak = ais.getContacts(contactlist)
                            num=1
                            msgs="「 Favorite List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\n「 Total Favoritelist : %i 」" % len(kontak)
                            msgs+= "\nUsage : FavoriteInfo「 number 」"
                            hello = "{}".format(str(msgs))
                            data = {
                                "type": "text",
                                "text": "{}".format(str(msgs)),
                                "sentBy": {
                                    "label": "{}".format(ais.getContact(aisMID).displayName),
                                    "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                    "linkUrl": "line://ti/p/~melodic404"
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd == 'gift':
#.                               sendFooter2(to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, text=None, contentMetadata={'PRDID': '350d37d6-bfc9-44cb-a0d1-cf17ae3657db','PRDTYPE': 'THEME','MSGTPL': '5'}, contentType=9)
#=====================================================================
                        elif cmd == "changedp" and sender == aisMID:
                            settings["changePicture"] = True
                            sendFooter2(to, "Type: Profile\n • Detail: Change Profile Picture\n • Status: Waiting for picture\n Please send a picture...")
                        elif cmd == "change cover" and sender == aisMID:
                            settings["changeCover"] = True
                            sendFooter2(to, "Type: Profile\n • Detail: Change Home Photos\n • Status: Waiting for picture\nPlease send a picture...")
                        elif cmd == "changedp video" and sender == aisMID:
                            settings['changeProfileVideo']['status'] = True
                            settings['changeProfileVideo']['stage'] = 1
                            sendFooter2(to, "Type: Profile\n • Detail: Change Video Profile\n • Status: Waiting for video\nPlease send a video...")
                        elif cmd == "changedp group":
                            if msg.toType == 2:
                                if to not in settings["changeGroupPicture"]:
                                    settings["changeGroupPicture"].append(to)
                                sendFooter2(to, "Type: Group\n • Detail: Change Group Picture\n • Status: Waiting for picture\nPlease send a picture...")
                        elif cmd.startswith("changemy video "):
                            link = removeCmd("changemy video", text)
                            contact = ais.getContact(sender)
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            pict = ais.downloadFileURL(pic)
                            try:
                                r = requests.get("http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q={}".format(link))
                                data = r.text
                                data = json.loads(data)
                                for x in data["result"]["videolist"]:
                                    if x["extension"] == "mp4" and x["resolution"] == "720p":
                                        sendFooter2(to, "Type: Profile\n • Detail: Change video\n • Status: Download...")
                                        vids = ais.downloadFileURL(x['url'])
                                        changeVideoAndPictureProfile(pict, vids)
                                        sendFooter2(to, "Type: Profile\n • Detail: Change video\n • Status: Succes")
                                    else:pass
                            except:pass
                        elif cmd.startswith("vid "):
                            name = removeCmd("vid",text)
                            ais.sendVideo(to, "tmp/{}".format(name))
                        elif cmd.startswith("addtext2 "):
                            	if sender in aisMID:
                                    sep = text.split(" ")
                                    apl = text.replace(sep[0] + " ","")
                                    sam = apl.split("~")
                                    chat1 = sam[0]
                                    chat2 = sam[1]
                                    apk = ""+chat1
                                    tes2["Message2"][apk] = chat2
                                    tes2["msg2"] = chat1
                                    anu = tes2["msg2"]+'.'
                                    sendFooter2(to,"Command %s created."%chat1)
                                    tes2["msg"] = {}
                                    backupData()
                        elif cmd == "list text2":
                            	if sender in aisMID:
                                    backupData()
                                    if tes2["Message2"] == {}:
                                        sendFooter2(to,"You don't have chat message")
                                    else:
                                        mc = ""
                                        jml = 1
                                        for listword in tes2["Message2"]:
                                            mc += "\n"+str(jml)+". "+listword+""
                                            jml += 1
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyMessage(msg.id, to, "List text :\n"+str(mc))
                        elif cmd.startswith("deltext2 "):
                            	if sender in aisMID:
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in tes2["Message2"]:
                                        del tes2["Message2"][xres]                                        
                                        sendFooter2(to,"Command %s has been removed."%tetx)
                                    else:
                                        sendFooter2(to,"Command %s does not exist."%tetx)
                        elif cmd.startswith("addtext "):
                            	if sender in aisMID:
                                    sep = text.split(" ")
                                    apl = text.replace(sep[0] + " ","")
                                    sam = apl.split("~")
                                    chat1 = sam[0]
                                    chat2 = sam[1]
                                    apk = ""+chat1
                                    tes["Message"][apk] = chat2
                                    tes["msg"] = chat1
                                    anu = tes["msg"]+'.'
                                    sendFooter2(to,"Command %s created."%chat1)
                                    tes["msg"] = {}
                                    backupData()
                        elif cmd == "list text":
                            	if sender in aisMID:
                                    backupData()
                                    if tes["Message"] == {}:
                                        sendFooter2(to,"You don't have chat message")
                                    else:
                                        mc = ""
                                        jml = 1
                                        for listword in tes["Message"]:
                                            mc += "\n"+str(jml)+". "+listword+""
                                            jml += 1
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyMessage(msg.id, to, "List text :\n"+str(mc))
                        elif cmd.startswith("getvideo "):
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl=("https://www.youtube.com" + results['href'])
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = "Youtube - Video :\n"
                                    hasil += "\nTitle : {}".format(str(vid.title))
                                    hasil += "\nSubscriber From : {}".format(str(vid.author))
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,hasil)
                                ais.sendVideoWithURL(msg.to,vin)
                                print("[YOUTUBE]MP4 Succes")
                            except Exception as e:
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,str(e))
                        elif cmd.startswith("deltext "):
                            	if sender in aisMID:
                                    sep = text.split(" ")
                                    xres = text.replace(sep[0] + " ","")
                                    tetx = text.replace(sep[0] + " ","")
                                    if xres in tes["Message"]:
                                        del tes["Message"][xres]                                        
                                        sendFooter2(to,"Command %s has been removed."%tetx)
                                    else:
                                        sendFooter2(to,"Command %s does not exist."%tetx)
                        elif cmd.startswith("stickers "):
                            search = removeCmd("stickers", text)        
                            r = requests.get("http://api.zicor.ooo/lstickers.php?search={}".format(str(search)))
                            data=r.text
                            data=json.loads(data)
                            if data["items"] != []:    
                                no = 0
                                hasil = " 「 Line Stickers 」"
                                for sam in data["items"]:                                     
                                    no += 1                  
                                    hasil += "\n    " + str(no) + ". " + str(sam["title"])+"\n"+"line.me/S/sticker/"+str(sam["id"])
                                sendFooter2(to, str(hasil))    
                        elif cmd.startswith("themes "):
                            search = removeCmd("themes", text)        
                            r = requests.get("http://api.zicor.ooo/ltheme.php?search={}".format(str(search)))
                            data=r.text
                            data=json.loads(data)
                            if data["items"] != []:    
                                no = 0
                                hasil = " 「 Line Themes 」"
                                for sam in data["items"]:                                     
                                    no += 1                  
                                    hasil += "\n    " + str(no) + ". " + str(sam["title"])+"\n"+"line://shop/theme/detail?id="+str(sam["id"])
                                sendFooter2(to, str(hasil))    
                        elif cmd.startswith("drawsoupletters "):
                            q = removeCmd("drawsoupletters", text)
                            r = requests.get("http://api.zicor.ooo/sletters.php?text={}".format(str(q)))                                    
                            data=r.text
                            data=json.loads(data)
                            ais.sendImageWithURL(to,str(data["image"]))
                        elif cmd.startswith("drawstreets "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            r = requests.get("http://api.zicor.ooo/streets.php?text="+urllib.parse.quote(txt))
                            data=r.text
                            data=json.loads(data)
                            ais.sendImageWithURL(to,str(data["image"]))
                        elif cmd.startswith("drawwindow "):
                            q = removeCmd("drawwindow", text)
                            r = requests.get("http://api.zicor.ooo/fwindow.php?text={}&btype=3".format(str(q)))
                            data=r.text
                            data=json.loads(data)
                            ais.sendImageWithURL(to,str(data["image"]))
                        elif cmd.startswith("drawcookies "):
                            q = removeCmd("drawcookies", text)
                            r = requests.get("http://api.zicor.ooo/wcookies.php?text={}".format(str(q)))
                            data=r.text
                            data=json.loads(data)
                            ais.sendImageWithURL(to,str(data["image"]))
                        elif cmd.startswith("drawlight "):
                            q = removeCmd("drawlight", text)
                            r = requests.get("http://api.zicor.ooo/graffiti.php?text={}".format(str(q)))
                            data=r.text
                            data=json.loads(data)
                            ais.sendImageWithURL(to,str(data["image"]))
                        elif cmd.startswith("zodiac "):
                            text = removeCmd("zodiac", text)
                            sep = text.split(" ")
                            url = text.replace(sep[0] + " ", text)
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = ""
                                for a in soup.select('div.vml-zodiak-detail'):
                                    ret_ += a.h1.string
                                    ret_ += "\n"+ a.h4.string
                                    ret_ += " : "+ a.span.string +""
                                for b in soup.select('div.col-center'):
                                    ret_ += "\nTanggal : "+ b.string
                                for d in soup.select('div.number-zodiak'):
                                    ret_ += "\nAngka keberuntungan : "+ d.string
                                for c in soup.select('div.paragraph-left'):
                                    ta = c.text
                                    tab = ta.replace("    ", "")
                                    tabs = tab.replace(".", ".\n")
                                    ret_ += "\n"+ tabs
                                    #print (ret_)
                                sendFooter2(msg.to, str(ret_))
                        elif cmd.startswith("cosplay "):
                             sep = text.split(" ")
                             txt = text.replace(sep[0] + " ","")
                             url = "https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=nda12345&text={}".format(txt)
                             ais.sendImageWithURL(to, url)
                        elif cmd.startswith("viloid "):
                             sep = text.split(" ")
                             txt = text.replace(sep[0] + " ","")
                             url = "https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=aguzzzz748474848&beta&text={}".format(txt)
                             ais.sendImageWithURL(to, url)
                        elif cmd.startswith("spamgift "):
                            text = removeCmd("spamgift", text)
                            korban = text.replace('spamgift ', text)
                            korban2 = korban.split()
                            midd = korban2[0]
                            jumlah = int(korban2[1])
                            if jumlah <= 1000:
                                for var in range(0,jumlah):
                                    sendFooter2(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                sendFooter2(to, "Succes ~")
                        elif cmd.startswith("gift "):
                            query = removeCmd("gift", text)
                            text = query.split("-")
                            message = text[0]
                            number = text[1]
                            groups = ais.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    ais.sendGift(group,str(message),'sticker')
                                except:
                                    ais.sendGift(group,str(message),'sticker')
                                sendFooter2(to, "「 Remote Gift 」\n\nGroup : " + G.name)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd.startswith("sendfile"):
                            text = removeCmd("sendfile", text)
                            sep = text.split(" ")
                            file = text.replace(sep[0] + " ", text)
                            time.sleep(1)
                            ais.sendFile(to,file)
                        elif cmd.startswith("xxx "):
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.avgle.com/v1/search/{}/1?limit=10".format(str(search)))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Search video 18+ 」\n"
                                for aa in data["response"]["videos"]:
                                    no += 1
                                    hasil += "\n"+str(no)+". "+str(aa["title"])+"\nDurasi : "+str(aa["duration"])
                                    ret_ = "\n\nXxx {} | Number".format(str(search))
                                sendFooter2(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["response"]["videos"][num - 1]
                                    c = str(b["vid"])
                                    d = requests.get("https://api.avgle.com/v1/video/"+str(c))
                                    data1 = json.loads(d.text)
                                    hasil = "Title : "+str(data1["response"]["video"]["title"])
                                    hasil += "\n\nDurasi : "+str(data1["response"]["video"]["duration"])
                                    hasil += "\nKualitas HD : "+str(data1["response"]["video"]["hd"])
                                    hasil += "\nDitonton "+str(data1["response"]["video"]["viewnumber"])
                                    #e = requests.get("https://api-ssl.bitly.com/v3/shorten?access_token=c52a3ad85f0eeafbb55e680d0fb926a5c4cab823&longUrl="+str(data1["response"]["video"]["video_url"]))
                                    #data2 = json.loads(e.text)
                                    hasil += "\nLink video : "+str(data1["response"]["video"]["video_url"])
                                    hasil += "\nLink embed : "+str(data1["response"]["video"]["embedded_url"])
                                    sendFooter2(msg.to,hasil)
                                    anuanu = str(data1["response"]["video"]["preview_url"])
                                    path = ais.downloadFileURL(anuanu)
                                    ais.sendImage(msg.to,path)
                                    #cl.sendVideoWithURL(msg.to, data["data"]["url"])
                                except Exception as e:
                                    sendFooter2(msg.to," "+str(e))
                        elif cmd.startswith("idline "):
                            a = removeCmd("idline", text)
                            b = ais.findContactsByUserid(a)
                            line = b.mid
                            sendFooter2(msg.to,"http://line.me/ti/p/~" + a)
                            ais.sendContact(to, line)                                                                                           
                            sendFooter2(to,str(hasil))
                        elif cmd.startswith("blockinfo "):
                            number = removeCmd("blockinfo", text)
                            contactlist = ais.getBlockedContactIds()
                            try:
                                contact = contactlist[int(number)-1]
                                friend = ais.getContact(contact)
                                cu = ais.getProfileCoverURL(contact)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + friend.pictureStatus
                                try:
                                    sendFooter2(to,"「 Block Info 」\n\n" + "Name : " + friend.displayName + "\nStatus : " + friend.statusMessage + "\nMid : " + friend.mid)
                                    ais.sendImageWithURL(to,image)
                                    ais.sendImageWithURL(to,path)
                                    ais.sendContact(to, friend.mid)
                                except:
                                    pass
                            except Exception as error:
                                sendFooter2(to, "「 Result Error 」\n" + str(error))
                        elif cmd.startswith("favoriteinfo "):
                            text = removeCmd("favoriteinfo", text)
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ", text)
                            contactlist = ais.getFavoriteMids()
                            try:
                                contact = contactlist[int(number)-1]
                                friend = ais.getContact(contact)
                                cu = ais.getProfileCoverURL(contact)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + friend.pictureStatus
                                try:
                                    sendFooter2(to,"「 Favorite Info」\n\n" + "Name : " + friend.displayName + "\nStatus : " + friend.statusMessage + "\nMid : " + friend.mid)
                                    ais.sendImageWithURL(to,image)
                                    ais.sendImageWithURL(to,path)
                                    ais.sendContact(to, friend.mid)
                                except:
                                    pass
                            except Exception as error:
                                sendFooter2(to, "Result Error\n" + str(error))
                        elif cmd.startswith("savefile"):
                            text = removeCmd("savefile", text)
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ", text)
                            if " " in key:
                                sendFooter2(to, "Failed !")
                            else:
                                hoho["namafile"] = str(key).lower()
                                hoho["savefile"] = True
                                sendFooter2(to, "Send file to save to be「 {} 」".format(str(key).lower()))
                        elif cmd.startswith("imagehd "):
                                query = removeCmd("imagehd", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.eater.pw/wallp/{}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["link"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["link"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Wallpp HD",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)

                        elif cmd.startswith("footergbc"):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = ais.getGroupIdsJoined()
                            for gr in groups:
                                data = {
                                    "type": "text",
                                    "text": "{}".format(text),
                                    "sentBy": {
                                        "label": "{}".format(ais.getContact(aisMID).displayName),
                                        "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                        "linkUrl": "line://ti/p/~melodic404"
                                    }
                                }
                                bcTemplate(gr, data)
                        elif cmd.startswith("flexgbc "):
                            rah = text.split(" ")
                            matt = text.replace(rah[0] + " ","")
                            chat = "{}".format(matt)
                            groups = ais.getGroupIdsJoined()
                            for gr in groups:
                                data = {
                                    "type": "flex",
                                    "altText": "This is flex message",
                                    "contents": {
                                        "type": "bubble",
                                        "body": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "{}".format(chat),
                                                    "wrap": True,
                                                    "align": "start",
                                                    "gravity": "center",
                                                    "size": "xxs"
                                                }
                                            ]
                                        }
                                    }
                                }
                                bcTemplate(gr, data)
                        elif cmd.startswith("flexgbc "):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = ais.getGroupIdsJoined()
                            for gr in groups:
                                data = {
                                        "type": "flex",
                                        "altText": "MERANA",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u8d7744d8ca82d10dc6c986a121a4b0cc").pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact("u8d7744d8ca82d10dc6c986a121a4b0cc").pictureStatus),
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "BROADCAST",
            "size": "md",
            "align": "center",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "{}".format(text),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Click to Order",
                "size": "sm",
                "action": {
                  "uri": "line://ti/p/~1417ais",
                  "type": "uri",
                  "label": "Add Maker"
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                bcTemplate(gr, data)
                        elif cmd.startswith("footerfbc"):
                            khie = text.split(" ")
                            hey = text.replace(khie[0] + " ", "")
                            text = "{}".format(hey)
                            groups = ais.getGroupIdsJoined()
                            for friend in friends:
                                data = {
                                    "type": "text",
                                    "text": "{}".format(text),
                                    "sentBy": {
                                        "label": "{}".format(ais.getContact(aisMID).displayName),
                                        "iconUrl": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
                                        "linkUrl": "line://nv/profilePopup/mid=u73a240047c27fee83b8a482d7c30e31c"
                                    }
                                }
                                bcTemplate2(friend, data)
                        elif cmd.startswith("ig "):
                            bah = msg.text.split(" ")
                            lah = msg.text.replace(bah[0] + " ","")
                            r = requests.get("http://api.farzain.com/ig_profile.php?id={}&apikey=mat404".format(lah))
                            anu = r.text
                            anu = json.loads(anu)
                            data = {
                                "type": "flex",
                                "altText": "Instagram",
                                "contents": {
                                    "type": "bubble",
                                    "header": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Instagram {}".format(str(lah)),
                                                "weight": "bold",
                                                "color": "#aaaaaa",
                                                "size": "sm"
                                            }
                                        ]
                                    },
                                    "hero": {
                                        "type": "image",
                                        "url": "{}".format(str(anu["info"]["profile_pict"])),
                                        "size": "full",
                                        "aspectRatio": "20:13",
                                        "aspectMode": "cover",
                                        "action": {
                                            "type": "uri",
                                            "uri": "line://nv/profilePopup/mid=u73a240047c27fee83b8a482d7c30e31c"
                                        }
                                    },
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "margin": "lg",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Name",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["info"]["full_name"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Username",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["info"]["username"])),
                                                                "color": "#666666",
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Bio",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["info"]["bio"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Url Bio",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["info"]["url_bio"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Followers",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["count"]["followers"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Following",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["count"]["following"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "baseline",
                                                        "spacing": "sm",
                                                        "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "Post",
                                                                "color": "#aaaaaa",
                                                                "size": "sm",
                                                                "flex": 3
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": "{}".format(str(anu["count"]["post"])),
                                                                "color": "#666666",
                                                                "wrap": True,
                                                                "size": "sm",
                                                                "flex": 5
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "style": "link",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Instagram",
                                                    "uri": "https://www.instagram.com/{}".format(str(anu["info"]["username"]))
                                                }                                                   
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 0
                                    }
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("goimage "):
                                query = removeCmd("goimage", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("https://api.eater.pw/googleimg/{}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                        if 'http://' in fn["img"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["img"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(fn["img"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Google_Image",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                        elif cmd.startswith("youtubesearch"):
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            r = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q={}&type=video&key=AIzaSyAF-_5PLCt8DwhYc7LBskesUnsm1gFHSP8".format(str(search)))
                            data = r.text
                            a = json.loads(data)
                            if a["items"] != []:
                                ret_ = []
                                yt = []
                                for music in a["items"]:
                                    ret_.append({
                                        "type": "bubble",
                                        "styles": {
                                            "header": {
                                                "backgroundColor": "#ffffff"
                                            },
                                            "body": {
                                               "backgroundColor": "#ffffff",
                                               "separator": True,
                                               "separatorColor": "#000000"
                                            },
                                            "footer": {
                                                "backgroundColor": "#ffffff",
                                                "separator": True,
                                               "separatorColor": "#000000"
                                           }
                                        },
                                        "header": {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                               {
                                                    "type": "text",
                                                    "text": "Youtube",
                                                    "weight": "bold",
                                                    "color": "#1C1C1C",
                                                    "size": "sm"
                                                }
                                            ]
                                        },
                                        "hero": {
                                            "type": "image",
                                            "url": "https://i.ytimg.com/vi/{}/maxresdefault.jpg".format(music['id']['videoId']),
                                            "size": "full",
                                            "aspectRatio": "20:13",
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": "line://nv/profilePopup/mid=u73a240047c27fee83b8a482d7c30e31c"
                                            }
                                        },
                                        "body": {
                                            "type": "box",
                                            "spacing": "md",
                                            "layout": "horizontal",
                                            "contents": [{
                                                "type": "box",
                                                "spacing": "none",
                                                "flex": 1,
                                                "layout": "vertical",
                                                "contents": [{
                                                    "type": "image",
                                                    "url": "https://cdn2.iconfinder.com/data/icons/social-icons-circular-color/512/youtube-512.png",
                                                    "aspectMode": "cover",
                                                    "gravity": "bottom",
                                                    "size": "sm",
                                                    "aspectRatio": "1:1",
                                                    "action": {
                                                      "type": "uri",
                                                      "uri": "https://www.youtube.com/watch?v=%s" % music['id']['videoId']
                                                    }
                                                }]
                                            }, {
                                                "type": "separator",
                                                "color": "#000000"
                                            }, {
                                                "type": "box",
                                                "contents": [{
                                                    "type": "text",
                                                    "text": "Title",
                                                    "color": "#000000",
                                                    "size": "md",
                                                    "weight": "bold",
                                                    "flex": 1,
                                                    "gravity": "top"
                                                }, {
                                                    "type": "text",
                                                    "text": "%s" % music['snippet']['title'],
                                                    "color": "#000000",
                                                    "size": "sm",
                                                    "weight": "bold",
                                                    "flex": 3,
                                                    "wrap": True,
                                                    "gravity": "top"
                                                }],
                                                "flex": 2,
                                                "layout": "vertical"
                                            }]
                                        },
                                        "footer": {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [{
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [{
                                                    "type": "button",
                                                    "flex": 2,
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Page",
                                                        "uri": "https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }, {
                                                    "flex": 3,
                                                    "type": "button",
                                                    "margin": "sm",
                                                    "style": "primary",
                                                    "color": "#000000",
                                                    "height": "sm",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Mp3",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp3%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                    }
                                                }]
                                            }, {
                                                "type": "button",
                                                "margin": "sm",
                                                "style": "primary",
                                                "color": "#000000",
                                                "height": "sm",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "Mp4",
                                                    "uri": "line://app/1602687308-GXq4Vvk9?type=text&text=youtubemp4%20https://www.youtube.com/watch?v={}".format(str(music['id']['videoId']))
                                                }
                                            }]
                                        }
                                    }
                                )
                                    yt.append('https://www.youtube.com/watch?v=' +music['id']['videoId'])
                                k = len(ret_)//10
                                for aa in range(k+1):
                                    data = {
                                        "type": "flex",
                                        "altText": "Youtube",
                                        "contents": {
                                            "type": "carousel",
                                            "contents": ret_[aa*10 : (aa+1)*10]
                                        }
                                    }
                                    sendTemplate(to, data)
                        elif cmd.startswith("food "):
                                query = removeCmd("food", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/{}".format(str(search)))
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    ret_ = []                                	
                                    for food in data:
                                        if 'http://' in food["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(food["url"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Send Image",
                                                        "uri": "line://app/1602687308-GXq4Vvk9?type=image&img={}".format(str(food["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "I'm hungry",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
#REMOTE DISCO
                        elif cmd.startswith("haha "):
                                number = removeCmd("haha", text)
                                groups = ais.getGroupIdsJoined()
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                ret_ = []
                                ret_.append({"imageUrl":"https://thumbs.gfycat.com/QuaintScornfulAmericanlobster-small.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                k = len(ret_)//1
                                for aa in range(k+1):
                                    data = {
                                        "type": "template",
                                        "altText": "This is image_carousel",
                                        "template": {
                                            "type": "image_carousel",
                                            "columns": ret_[aa*1 : (aa+1)*1]
                                        }
                                    }
                                    sendTemplate(group, data)
                                sendFooter2(to, "Remote Haha\nIn Grup {}".format(G.name))
                        elif cmd.startswith("haha "):
                                number = removeCmd("haha", text)
                                groups = ais.getGroupIdsJoined()
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                ret_ = []
                                ret_.append({"imageUrl":"https://thumbs.gfycat.com/QuaintScornfulAmericanlobster-small.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                k = len(ret_)//1
                                for aa in range(k+1):
                                    data = {
                                        "type": "template",
                                        "altText": "This is image_carousel",
                                        "template": {
                                            "type": "image_carousel",
                                            "columns": ret_[aa*1 : (aa+1)*1]
                                        }
                                    }
                                    sendTemplate(group, data)
                                sendFooter2(to, "Remote Haha\nIn Grup {}".format(G.name))
                        elif cmd.startswith("disco "):
                                number = removeCmd("disco", text)
                                groups = ais.getGroupIdsJoined()
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                ret_ = []
                                ret_.append({"imageUrl":"https://techflourish.com/images/book-clipart-gif-9.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://i.pinimg.com/originals/a1/9a/39/a19a390f4a46f098eec1c8070001b5ad.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://4.bp.blogspot.com/-MifM_HCQjAE/Wnkgxjj-pcI/AAAAAAALEdg/ObmxB3z9aW8DXfVnjwTCUNooO3LfgDsSQCLcBGAs/s1600/AS003630_02.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://media.giphy.com/media/fvOKZ1hETl5L2/giphy.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://steamusercontent-a.akamaihd.net/ugc/269469010840327100/309EC530780F049E3FAC757C4B2A75A008D2667E/","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://media.giphy.com/media/lnd8s1O9mV61O/giphy.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                ret_.append({"imageUrl":"https://s.kaskus.id/images/2013/06/05/5534212_20130605075951.gif","size": "full","action": {"type": "uri","uri": "line://ti/p/~melodic404"}})
                                k = len(ret_)//5
                                for aa in range(k+1):
                                    data = {
                                        "type": "template",
                                        "altText": "DiscoDance",
                                        "template": {
                                            "type": "image_carousel",
                                            "columns": ret_[aa*5 : (aa+1)*5]
                                        }
                                    }
                                    sendTemplate(group, data)
                                sendFooter2(to, "Success Remote Template Disco in\nGrup {}".format(G.name))
#YT REMOTE
                        elif cmd.startswith("searchapp "):
                                query = removeCmd("searchapp", text)
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.farzain.com/playstore.php?id={}&apikey=KJaOT94NCD1bP1veQoJ7uXc9M".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if data != []:
                                    ret_ = []
                                    for music in data:
                                        if 'http://' in music["url"]:
                                            pass
                                        else:
                                            if len(ret_) >= 10:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(music["icon"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Download",
                                                        "uri": "{}".format(str(music["url"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                            "type": "template",
                                            "altText": "Searching App",
                                            "template": {
                                                "type": "image_carousel",
                                                "columns": ret_[aa*10 : (aa+1)*10]
                                            }
                                        }
                                        sendTemplate(to, data)
                        elif cmd.startswith("xvideos "):
                            sep = text.split(" ")
                            txt = msg.text.replace(sep[0] + " ", "")
                            url = requests.get("https://api.eater.pw/xvideos/{}".format(txt))
                            tae = url.json()
                            anu = tae
                            data = {
                                "type": "template",
                                "altText": "XxX",
                                "template": {
                                    "type": "carousel",
                                    "columns": [
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][0]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][0]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][0]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][1]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][1]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][1]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][2]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][2]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][2]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][3]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][3]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][3]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][4]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][4]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][4]["link"])
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("redtube "):
                            sep = text.split(" ")
                            txt = msg.text.replace(sep[0] + " ", "")
                            url = requests.get("https://api.eater.pw/redtube/{}".format(txt))
                            tae = url.json()
                            anu = tae
                            data = {
                                "type": "template",
                                "altText": "XxX",
                                "template": {
                                    "type": "carousel",
                                    "columns": [
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][0]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][0]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][0]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][1]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][1]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][1]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][2]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][2]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][2]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][3]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][3]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][3]["link"])
                                                }
                                            ]
                                        },
                                        {
                                            "thumbnailImageUrl": "{}".format(anu["result"][4]["img"]),
                                            "imageBackgroundColor": "#FFFFFF",
                                            "title": "Page {}".format(txt),
                                            "text": "source: xvideos",
                                            "actions": [
                                                {
                                                    "type": "uri",
                                                    "label": "Download",
                                                    "uri": "line://app/1487085176-lP805wzy?text={}".format(anu["result"][4]["dl"])
                                                },
                                                {
                                                    "type": "uri",
                                                    "label": "Go",
                                                    "uri": "{}".format(anu["result"][4]["link"])
                                                }
                                            ]
                                        }
                                    ]
                                }
                            }
                            sendTemplate(to, data)
                        elif cmd.startswith("spaminvite"):
                            key = eval(msg.contentMetadata["MENTION"])
                            tar = key["MENTIONEES"][0]["M"]
                            dan = text.split("|")
                            nam = dan[1]
                            jlh = int(dan[2])
                            grr = ais.groups
                            ais.findAndAddContactsByMid(tar)
                            if jlh <= 101:
                                for var in range(0,jlh):
                                    gcr = ais.createGroup(nam, [tar])
                                    ais.inviteIntoGroup(gcr.id, [tar])
                                    time.sleep(2)
                                    ais.leaveGroup(gcr.id)
                                ais.sendMention(to, "Succesfully Spam Invite @! to Group {}".format(gcr.name), [tar])
                        elif cmd.startswith("flood ") and sender == aisMID:
                            dzin = removeCmd("flood", text)
                            line = dzin.split("|")
                            count = int(line[1])
                            text1 = removeCmd("flood"+str(line[0])+"|"+str(count)+"|", text)
                            text2 = count * (text1+"\n")
                            if line[0] == "on":
                                if count <= 1000:
                                    for a in range(count):
#                                        ais.sendMessage(to, str(text1))
                                        data = {
                                                "type": "flex",
                                                "altText": "MERANA",
                                                "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFFFF"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": "https://obs.line-scdn.net/{}".format(ais.getContact(aisMID).pictureStatus),
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "url": str(ais.getProfileCoverURL(sender)),
            "type": "image"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "text": "FLOODING",
            "size": "md",
            "align": "center",
            "color": "#FFFFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "vertical"
      },
      {
        "type": "separator",
        "color": "#FFFFFF"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": "User : {}".format(ais.getProfile().displayName),
                "size": "xs",
                "margin": "none",
                "color": "#FFFFFF",
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          },
          {
            "type": "separator",
            "color": "#FFFFFF"
          },
          {
            "contents": [
              {
                "text": str(text1),
                "size": "sm",
                "margin": "none",
                "color": "#FFFFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "Maker",
                "size": "sm",
                "action": {
                  "uri": "line://ti/p/~1417ais",
                  "type": "uri",
                  "label": "Add Maker"
                },
                "margin": "xl",
                "align": "center",
                "color": "#000000",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                        sendTemplate(to, data)
                                else:
                                    ais.sendMessage(to, "Max 1000.")
                            if line[0] == "off":
                                if count <= 1000:
                                    ais.sendMessage(to, str(text2))
                                else:
                                    ais.sendMessage(to, "Max 1000.")
                        elif cmd.startswith("examplee"):
                            try:
                                proses = text.split("|")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "❂➣ Penyanyi: "+str(d)
                                hasil += "\n❂➣ Judul : "+str(c)
                                data = {                               
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#00FFFF"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "「THE PEOPLE」\n      「TEAM」\n\n       「MP3」",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "              PLAY",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": e,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                sendTemplate(to, data)
                            except Exception as error:
                                sendFooter2(to, "404\n " + str(error))
                                logError(error)
#=====================================================================
#                              \\ COMMAND Kick //
                        elif cmd.startswith("ulti "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        ais.kickoutFromGroup(to, [ls])
                                        ais.findAndAddContactsByMid(ls)
                                        ais.inviteIntoGroup(to, [ls])
                                        ais.cancelGroupInvitation(to, [ls])
                                    except:
                                       sendFooter2(to, "Limited !")
                        elif cmd.startswith("cloneprofile "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                if len(lists) != []:
                                    ls = random.choice(lists)
                                    cloneProfile(ls)
                                    ais.sendContact(to,aisMID)
                                    sendFooter2(to, "Has been Clone ~")
                        elif cmd.startswith("staff:add "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        staff[ls] = True
                                        f=codecs.open('staff.json','w','utf-8')
                                        json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        sendFooter2(to, 'Added to staff')
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyMessage(msg.id, to, 'Added to staff')
                                    except:
                                        pass
                        elif cmd.startswith("staff:del "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del staff[ls]
                                        f=codecs.open('staff.json','w','utf-8')
                                        json.dump(staff, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyMessage(msg.id, to, 'Deleted from staff')
                                    except:
                                        pass
                        elif cmd.startswith("tban "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        apalo["Talkblacklist"][ls] = True
                                        sendFooter2(to, 'Add to TalkBan')
                                    except:
                                        pass
                        elif cmd.startswith("tunban "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del apalo["Talkblacklist"][ls]
                                        sendFooter2(to, 'Deleted from TalkBan')
                                    except:
                                        pass
                        elif cmd.startswith("mentionmid "):
                            contact = removeCmd("mentionmid", text)
                            sendMention(to, contact)
                        elif cmd.startswith("slain "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        ais.kickoutFromGroup(to, [ls])
                                        ais.findAndAddContactsByMid(ls)
                                        ais.inviteIntoGroup(to, [ls])
                                        ais.cancelGroupInvitation(to, [ls])
                                        time.sleep(5)
                                        ais.inviteIntoGroup(to, [ls])
                                    except:
                                       sendFooter2(to, "Limited !")
                        elif cmd.startswith("reinv "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        ais.findAndAddContactsByMid(ls)
                                        ais.kickoutFromGroup(to, [ls])
                                        time.sleep(5)
                                        ais.inviteIntoGroup(to, [ls])
                                    except:
                                       sendFooter2(to, "Limited !")
                        elif cmd.startswith("invite "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                       ais.findAndAddContactsByMid(ls)
                                       ais.inviteIntoGroup(to, [ls])
                                    except:
                                       sendFooter2(to, "Limited !")
                        elif cmd.startswith("tes "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    try:
                                	    rename = contact.displayNameOverridden
                                    except:
                                	    rename = "「 Display Rename 」\nERROR"
                                    sendFooter2(to, "「 Display Name 」\n" + contact.displayName + "\n\n「 Display Rename 」\n{}".format(rename))
                        elif cmd.startswith("clone "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                clone = ast.literal_eval(msg.contentMetadata['MENTION'])
                                clones = clone['MENTIONEES']
                                target = []
                                for clone in clones:
                                    if clone["M"] not in target:
                                        target.append(clone["M"])
                                for she in target:
                                    BackupProfile = ais.getContact(sender)
                                    Save1 = "http://dl.profile.line-cdn.net/{}".format(BackupProfile.pictureStatus);Save2 = "{}".format(BackupProfile.displayName);ProfileMe["PictureMe"] = Save1;ProfileMe["NameMe"] = Save2
                                    contact = ais.getContact(she);ClonerV2(she)
                                    sendMention(to, contact.mid, "「 Clone Profile 」\n", "\nStatus : Success");ais.sendContact(to, str(BackupProfile.mid));ais.sendContact(to, str(contact.mid))
                        elif cmd == "unclone":
                            try:
                                aisProfile = ais.getProfile()
                                aisName = ais.getProfile()
                                aisProfile.statusMessage = str(ProfileMe["myProfile"]["statusMessage"])
                                aisProfile.pictureStatus = str(ProfileMe["myProfile"]["pictureStatus"])
                                aisName.displayName = ProfileMe["NameMe"]
                                ais.updateProfile(aisName)
                                path = ais.downloadFileURL(ProfileMe["PictureMe"])
                                ais.updateProfilePicture(path)
                                coverId = str(ProfileMe["myProfile"]["coverId"])
                                ais.updateProfileCoverById(coverId)
                                BackupProfile = ais.getContact(sender)
                                sendMention(to, BackupProfile.mid, "「 Unclone Profile 」\n", "\nStatus : Success");ais.sendContact(to, str(BackupProfile.mid))
                            except Exception as error:
                                sendFooter2(to, "Failed to Backup")

                        elif cmd.startswith("creategroup "):
                            text = removeCmd("creategroup", text)
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ", text)
                            ais.createGroup(name, [aisMID])
                            gids = ais.getGroupIdsByName(name)
                            for gid in gids:
                	            try:
                		            x = ais.getGroup(gid)
                		            x.preventedJoinByTicket = False
                		            ais.updateGroup(x)
                	            except Exception as e:
                		            sendFooter2(to, str(e))
                            sendFooter2(to, "Create Group {}\n\nQR : http://line.me/R/ti/g/{}".format(str(name), str(ais.reissueGroupTicket(x.id))))

                        elif cmd.startswith('addbl') or cmd.startswith('delbl') or cmd.startswith('addwl') or cmd.startswith('delwl') or cmd.startswith('del block '):
                            to = msg.to
                            msg.text = ais.mycmd(msg.text,wait)
                            cmd = msg.text.lower()
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                if cmd.startswith('addbl '):ais.datamentions(to,'Blacklist',targets,'ADDBL',wait,ps='\n├ Type: Add Blacklist')
                                elif cmd.startswith('delbl '):ais.datamentions(to,'Blacklist',targets,'DELBL',wait,ps='\n├ Type: Delete Blacklist')
                                elif cmd.startswith('addwl '):ais.datamentions(to,'Whitelist',targets,'ADDWL',wait,ps='\n├ Type: Add Whitelist')
                                elif cmd.startswith('delwl '):ais.datamentions(to,'Whitelist',targets,'DELWL',wait,ps='\n├ Type: Delete Whitelist')
                                elif cmd.startswith('addml '):ais.datamentions(to,'Mimiclist',targets,'ADDML',wait,ps='\n├ Type: Add Mimiclist')
                                elif cmd.startswith('delml '):ais.datamentions(to,'Mimiclist',targets,'DELML',wait,ps='\n├ Type: Delete Mimiclist')
                                elif cmd.startswith('delfriend '):ais.datamentions(to,'Friendlist',targets,'DELFL',wait,ps='\n├ Type: Delete Friendlist')
                            else:
                                if cmd.startswith('delbl '):ais.adityaarchi(wait,'Blacklist','delbl',to,ais.adityasplittext(cmd),to,'\n├ Type: Delete Blacklist',nama=wait['blacklist'])
                                if cmd.startswith('delwl '):ais.adityaarchi(wait,'Whitelist','delwl',to,ais.adityasplittext(cmd),to,'\n├ Type: Delete Whitelist',nama=wait['bots'])
                                if cmd.startswith('delml '):ais.adityaarchi(wait,'Mimiclist','delml',to,ais.adityasplittext(cmd),to,'\n├ Type: Delete Mimiclist',nama=wait['target'])
                                if cmd.startswith('del block '):sendFooter2(to,' 「 Blocklist 」\nWaiting.....');ais.adityaarchi(wait,'Blocklist','delblock',to,ais.adityasplittext(cmd,'s'),to,'\n├ Type: Delete Blocklist',nama=ais.getBlockedRecommendationIds())
                            if msg.toType == 0:
                                if cmd == 'addbl':ais.datamentions(to,'Blacklist',[to],'ADDBL',wait,ps='\n├ Type: Add Blacklist')
                                elif cmd == 'delbl':ais.datamentions(to,'Blacklist',[to],'DELBL',wait,ps='\n├ Type: Delete Blacklist')
                                elif cmd == 'addwl':ais.datamentions(to,'Whitelist',[to],'ADDWL',wait,ps='\n├ Type: Add Whitelist')
                                elif cmd == 'delwl':ais.datamentions(to,'Whitelist',[to],'DELWL',wait,ps='\n├ Type: Delete Whitelist')
                                elif cmd == 'addml':ais.datamentions(to,'Mimiclist',[to],'ADDML',wait,ps='\n├ Type: Add Mimiclist')
                                elif cmd == 'delml':ais.datamentions(to,'Mimiclist',[to],'DELML',wait,ps='\n├ Type: Delete Mimiclist')
#=====================================================================
#                              \\ COMMAND Steal //
                        elif cmd.startswith("locate "):
                            if 'MENTION' in msg.contentMetadata.keys() != None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                userid = "https://line.me/ti/p/~" + ais.profile.userid
                                G = ais.getGroupIdsJoined()
                                cgroup = ais.getGroups(G)
                                groups = ais.groups
                                ngroup = ""
                                ngroup += "「 Locate 」\n"
                                no = 0 + 1
                                num = 0
                                for mention in mentionees:
                                    for x in range(len(cgroup)):
                                        gMembMids = [contact.mid for contact in cgroup[x].members]
                                        if mention['M'] in gMembMids:
                                            ngroup += "\n{}. {} | {}".format(str(no), str(cgroup[x].name), str(len(cgroup[x].members)))
                                            no += 1
                                            num += 1
                                    ngroup += "\n\n{} groups".format(str(num))
                                    sendFooter2(to, str(ngroup))
                                if ngroup == "":
                                    sendFooter2(to, "「 Locate 」\nNot found")
                        elif cmd.startswith("mid "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = "「 Mid User 」"
                                for ls in lists:
                                    ret_ += "\n{}".format(str(ls))
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, str(ret_))
                        elif cmd.startswith("pict "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.line.naver.jp/" + ais.getContact(ls).pictureStatus
                                    ais.generateReplyMessage(msg.id)
                                    ais.sendReplyImageWithURL(msg.id, to, str(path))
                        elif cmd.startswith("video "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    if contact.videoProfile == None:
                                    	continue
                                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "/vp"
                                    ais.generateReplyMessage(msg.id)
                                    ais.sendReplyVideoWithURL(msg.id, to, str(path))
                        elif cmd.startswith("cover "):
                            if ais != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = ais.getProfileCoverURL(ls)
                                        path = str(path)
                                        ais.generateReplyMessage(msg.id)
                                        ais.sendReplyImageWithURL(msg.id, to, str(path))
                        elif cmd.startswith("name "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    ais.generateReplyMessage(msg.id)
                                    ais.sendReplyMessage(msg.id, to, "{}".format(str(contact.displayName)))
                        elif cmd.startswith("bio "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    ais.generateReplyMessage(msg.id)
                                    ais.sendReplyMessage(msg.id, to, "{}".format(str(contact.statusMessage)))
                        elif cmd.startswith("profile "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    cu = ais.getProfileCoverURL(ls)
                                    path = str(cu)
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                    sendFooter2(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                    ais.sendImageWithURL(msg.to,image)
                                    ais.sendImageWithURL(msg.to,path)
                        elif cmd.startswith("contact "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    mi_d = contact.mid
                                    ais.sendContact(to, mi_d)
                        elif cmd.startswith("changevideourl"):
                            link = removeCmd("changevideourl", text)
                            contact = ais.getContact(sender)
                            sendFooter2(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = ais.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            sendFooter2(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")
#=====================================================================
                        elif cmd == "autojoin":
                            if settings["autoJoin"] == True:a = "Enabled"
                            else:a = "Disabled"
                            if wait["Members"]:
                                b = "{}".format(int(wait["Members"]))
                            else:b = "0"
                            key = settings['keyCommand']
                            key = key.title()
                            if settings['setKey'] == False:key = ""
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "「 Auto Join 」\nEvent Trigger:\n Autojoin: "+a+"\n Stage: "+b+"\n\nCommand:\n Autojoin\n • Usage: "+key+" autojoin on|off\n • Usage: "+key+" autojoin set 「numb」")
                        elif cmd.startswith("autojoin set "):
                            msg.text = ais.mycmd(msg.text,wait)
                            wait["Members"] = int(msg.text.split(" ")[2])
                            sendFooter2(msg.to, " 「 Autojoin 」\nType: Minim Members\nStatus: Success Set\nTo: {} Members".format(wait["Members"]))
                        elif cmd == "autojoin on":
                            if settings['autoJoin'] == True:
                                msgs=" 「 Auto Join 」\nAuto Join already set to ENABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to ENABLED♪"
                                settings['autoJoin']=True
                            sendFooter2(msg.to, msgs)
                        elif cmd == "autojoin off":
                            if settings['autoJoin'] == False:
                                msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
                                settings['autoJoin']=False
                            sendFooter2(msg.to, msgs)
                        elif cmd == "mc on":
                            if mcroom['leaveMC'] == True:
                                msgs=" 「 Auto Join 」\nAuto Join already set to ENABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to ENABLED♪"
                                mcroom['leaveMC']=True
                            sendFooter2(msg.to, msgs)
                        elif cmd == "mc off":
                            if mcroom['leaveMC'] == False:
                                msgs=" 「 Auto Join 」\nAuto Join already set to DISABLED♪"
                            else:
                                msgs=" 「 Auto Join 」\nAuto Join has been set to DISABLED♪"
                                mcroom['leaveMC']=False
                            sendFooter2(msg.to, msgs)
#=====================================================================
                        elif cmd == "tbanlist":
                            if apalo["Talkblacklist"] == {}:
                              sendFooter2(to,"Nothing Talkban user")
                            else:
                              ma = ""
                              a = 0
                              for m_id in apalo["Talkblacklist"]:
                                  a = a + 1
                                  end = '\n'
                                  ma += str(a) + ". " +ais.getContact(m_id).displayName + "\n"
                              sendFooter2(to,"List TalkBan :\n\n"+ma+"\nTotal %s Talkban User" %(str(len(apalo["Talkblacklist"]))))
#=====================================================================
                        elif cmd == "autoread":
                            if settings["autoRead"] == True:a = "Enabled"
                            else:a = "Disabled"
                            if settings["autoRead1"] == True:b = "Enabled"
                            else:b = "Disabled"
                            key = settings['keyCommand']
                            key = key.title()
                            if settings['setKey'] == False:key = ""
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, " 「 Auto Read 」\nEvent Trigger:\n1 on Personal: "+a+"\n2 on Group: "+b+"\n\nCommand:\n Autoread\n  Usage: "+key+" autoread on 1|2 or off 1|2")
                        elif cmd == "autoread on 1":
                            if settings["autoRead"] == True:
                                msgs=" 「 Auto Read 」\nAutoread in Private message set to ENABLED♪\nMessage will not Affected.."
                            else:
                                msgs=" 「 Auto Read 」\nAutoread in Private message already set to ENABLED♪\nMessage will not Affected.."
                                settings["autoRead"]=True
                            sendFooter2(msg.to, msgs)
                        elif cmd == "autoread off 1":
                            if settings["autoRead"] == False:
                                msgs=" 「 Auto Read 」\nAutoread in Private message set to DISABLED♪\nMessage will Affected.."
                            else:
                                msgs=" 「 Auto Read 」\nAutoread in Private message already set to DISABLED♪\nMessage will Affected.."
                                settings["autoRead"]=False
                            sendFooter2(msg.to, msgs)
                        elif cmd == "autoread on 2":
                            if settings["autoRead1"] == True:
                                msgs =" 「 Auto Read 」\nAutoread in Group set to ENABLED♪\nMessage will not Affected.."
                            else:
                                msgs=" 「 Auto Read 」\nAutoread in Group already set to ENABLED♪\nMessage will not Affected.."
                                settings["autoRead1"]=True
                            sendFooter2(msg.to, msgs)
                        elif cmd == "autoread off 2":
                            if settings["autoRead1"] == False:
                                msgs=" 「 Auto Read 」\nAutoread in Group set to DISABLED♪\nMessage will Affected.."
                            else:
                                msgs=" 「 Auto Read 」\nAutoread in Group set to DISABLED♪\nMessage will Affected.."
                                settings["autoRead1"]=False
                            sendFooter2(msg.to, msgs)
                        elif cmd == "sleepmode" and sender == aisMID:
                            if settings["replyPesan"] is not None:
                                sendFooter2(to,"「 Sleep Mode 」\nSet Sleep Mode : " + str(settings["replyPesan"]))
                                msgSticker = settings["messageSticker"]["listSticker"]["replySticker"]
                                if msgSticker != None:
                                    sid = msgSticker["STKID"]
                                    spkg = msgSticker["STKPKGID"]
                                    sver = msgSticker["STKVER"]
                                    sendSticker(to, sver, spkg, sid)
                            else:
                                sendFooter2(to,"Set Sleep Mode  : No messages are set")
                        elif cmd.startswith("sleepmode msg set ") and sender == aisMID:
                            text_ = removeCmd("sleepmode msg set", text)
                            try:
                                settings["replyPesan"] = text_
                                sendFooter2(to,"「 Sleep Mode 」\nChanged to : " + text_)
                            except:
                                sendFooter2(to,"「 Sleep Mode 」\nFailed to replace message")
                        elif cmd == "temp off":
                            if norak["detectTemplate"] == False:
                                msgs=" 「 Detect Template 」\nDetect Template already DISABLED♪\nNote: Detect Template message is not affected♪"
                            else:
                                msgs=" 「 Detect Template 」\nDetect Template set to DISABLED♪\nNote: Detect Template message is not affected♪"
                                norak['detectTemplate']=False
                            sendFooter2(to, msgs)
                        elif cmd == "temp on":
                            if norak["detectTemplate"] == True:
                                msgs=" 「 Detect Template 」\nDetect Template Enable♪\nNote: Detect Template message is not affected♪"
                            else:
                                msgs=" 「 Detect Template 」\nDetect Template set to Enable♪\nNote: Detect Template message is not affected♪"
                                norak["detectTemplate"]=True
                            sendFooter2(to, msgs)
                        elif cmd == "antitag on":
                            if settings["notag"] == True:
                                msgs=" 「 Anti Tag 」\nAnti Tag already Enable♪"
                            else:
                                msgs=" 「 Anti Tag 」\nAnti Tag set to Enable♪"
                                settings["notag"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "antitag off":
                            if settings["notag"] == False:
                                msgs=" 「 Anti Tag 」\nAnti Tag already DISABLED♪"
                            else:
                                msgs=" 「 Anti Tag 」\nAnti Tag set to DISABLED♪"
                                settings["notag"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "sleepmode on":
                            if settings["autoReply"] == True:
                                msgs=" 「 Sleep Mode 」\nSleep Mode already Enable♪"
                            else:
                                msgs=" 「 Sleep Mode 」\nSleep Mode set to Enable♪"
                                settings["autoReply"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "sleepmode off":
                            if settings["autoReply"] == False:
                                msgs=" 「 Sleep Mode 」\nSleep Mode already DISABLED♪"
                            else:
                                msgs=" 「 Sleep Mode 」\nSleep Mode set to DISABLED♪"
                                settings["autoReply"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "resendchat on":
                            if settings["unsendMessage"] == True:
                                msgs=" 「 Resend Chat 」\nResend Chat already Enable♪"
                            else:
                                msgs=" 「 Resend Chat 」\nResend Chat set to Enable♪"
                                settings["unsendMessage"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "resendchat off":
                            if settings["unsendMessage"] == False:
                                msgs=" 「 Resend Chat 」\nResend Chat already DISABLED♪"
                            else:
                                msgs=" 「 Resend Chat 」\nResend Chat set to DISABLED♪"
                                settings["unsendMessage"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "respon on":
                            if temptag["stealtag"] == True:
                                msgs=" 「 Respon 」\nRespon Tag already Enable♪"
                            else:
                                msgs=" 「 Respon 」\nRespon  Tag set to Enable♪"
                                temptag["stealtag"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "respon off":
                            if temptag["stealtag"] == False:
                                msgs=" 「 Respon 」\nRespon Tag already DISABLED♪"
                            else:
                                msgs=" 「 Respon 」\nRespon Tag set to DISABLED♪"
                                temptag["stealtag"] = False
                            sendFooter2(to, msgs)
                        elif cmd.startswith("respon msg set "):
                            text_ = removeCmd("respon msg set", text)
                            try:
                                temptag["pesanya"] = text_
                                sendFooter2(to,"「 Respon Tag 」\nChanged to : " + text_)
                            except:
                                sendFooter2(to,"「 Respon Tag 」\nFailed to replace message")
                        elif cmd == "welcomemsg on":
                            if wmin["wMessage"] == True:
                                msgs=" 「 Welcome 」\nWelcomemsg already Enable♪"
                            else:
                                msgs=" 「 Welcome 」\nWelcomemsg set to Enable♪"
                                wmin["wMessage"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "welcomemsg off":
                            if wmin["wMessage"] == False:
                                msgs=" 「 wMessage 」\nWelcomemsg already DISABLED♪"
                            else:
                                msgs=" 「 Welcome 」\nWelcomemsg set to DISABLED♪"
                                wmin["wMessage"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "leavemsg on":
                            if lvin["lMessage"] == True:
                                msgs=" 「 Leave 」\nLeavemsg already Enable♪"
                            else:
                                msgs=" 「 Leave 」\nLeavemsg set to Enable♪"
                                lvin["lMessage"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "leavemsg off":
                            if lvin["lMessage"] == False:
                                msgs=" 「  Leave 」\nLeavemsg already DISABLED♪"
                            else:
                                msgs=" 「  Leave  」\nLeavemsg set to DISABLED♪"
                                lvin["lMessage"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "byepas on":
                            if itil["cancel"] == True:
                                msgs=" 「 Leave 」\nAnti byepas already Enable♪"
                            else:
                                msgs=" 「 Leave 」\nAnti byepas set to Enable♪"
                                itil["cancel"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "byepas off":
                            if itil["cancel"] == False:
                                msgs=" 「  Leave 」\nAnti byepas already DISABLED♪"
                            else:
                                msgs=" 「  Leave  」\nAnti byepas set to DISABLED♪"
                                itil["cancel"] = False
                            sendFooter2(to, msgs)
                        elif cmd == "like on":
                            if komen["komenan"] == True:
                                msgs=" 「 Like Post 」\nAuto Like Post already Enable♪"
                            else:
                                msgs=" 「 Like Post 」\nAuto Like Post set to Enable♪"
                                komen["komenan"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "like off":
                            if komen["komenan"] == False:
                                msgs=" 「 Like Post 」\nAuto Like Post already DISABLED♪"
                            else:
                                msgs=" 「 Like Post 」\nAuto Like Post set to DISABLED♪"
                                komen["komenan"] = False
                            sendFooter2(to, msgs)
                        elif cmd.startswith("leavemsg set ") and sender == aisMID:
                            text_ = removeCmd("leavemsg set", text)
                            try:
                                lvin["textnya"] = text_
                                sendFooter2(to,"「 LeaveMsg 」\nChanged to : " + text_)
                            except:
                                sendFooter2(to,"「 LeaveMsg 」\nFailed to replace message")
                        elif cmd.startswith("welcomemsg set ") and sender == aisMID:
                            text_ = removeCmd("welcomemsg set", text)
                            try:
                                wmin["textnya"] = text_
                                sendFooter2(to,"「 WelcomeMsg 」\nChanged to : " + text_)
                            except:
                                sendFooter2(to,"「 WelcomeMsg 」\nFailed to replace message")
                        elif cmd == "reader on" and sender == aisMID:
                            tailah["siderTemp"][receiver] = []
                            #settings['siderTemp'][receiver]['status'] = True
                            sendFooter2(to, "Getreader set to on.")
                        elif cmd == "reader off" and sender == aisMID:
                            if receiver in tailah["siderTemp"]:
                                del tailah["siderTemp"][receiver]
                                #settings['siderTemp'][receiver]['status'] = False
                                sendFooter2(to, "Getreader set to off.")
                        elif cmd.startswith("reader msg set ") and sender == aisMID:
                            text_ = removeCmd("reader msg set", text)
                            try:
                                tailah["siderPesan"] = text_
                                sendFooter2(to,"「 Get Reader 」\nChanged to : " + text_)
                            except:
                                sendFooter2(to,"「Get Reader 」\nFailed to replace message")
                        elif cmd == "autoblock on":
                            if wtf["autoBlock"] == True:
                                msgs=" 「 Block 」\nAutoBlock already Enable♪"
                            else:
                                msgs=" 「 Block 」\nAutoBlock set to Enable♪"
                                wtf["autoBlock"] = True
                            sendFooter2(to, msgs)
                        elif cmd == "autoblock off":
                            if wtf["autoBlock"] == False:
                                msgs=" 「  Block 」\nAutoBlock already DISABLED♪"
                            else:
                                msgs=" 「  Block  」\nAutoBlock set to DISABLED♪"
                                wtf["autoBlock"] = False
                            sendFooter2(to, msgs)
#=====================================================================
                        elif cmd == "autoadd": 
                            key = settings['keyCommand']
                            key = key.title()
                            b = settings['messageSticker']['listSticker']['addSticker']
                            a = b['STKPKGID']
                            z = ais.shop.getProduct(packageID=int(a), language='ID', country='ID')
                            if settings["messageSticker"]["listSticker"]["addSticker"]["status"] == True:c = z.title
                            else:c = 'None'
                            if settings['setKey'] == False:key = ""
                            if settings["autoAdd"] == True:
                                if settings["addPesan"] == '':
                                    msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Sticker: "+c+"\nAdd Message: False♪\n\n\n"
                                else:
                                    msgs=" 「 Auto Add 」\nAdd Back: True♪\nAdd Sticker: "+c+"\nAdd Message: True♪"
                                    msgs+="\n" + settings["addPesan"] + "\n\n"
                            else:
                                if settings["addPesan"] == '':
                                    msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Sticker: "+c+"\nAdd Message: False♪\n\n\n"
                                else:
                                    msgs=" 「 Auto Add 」\nAdd Back: False♪\nAdd Sticker: "+c+"\nAdd Message: True♪"
                                    msgs+="\n" + settings["addPesan"] + "\n"
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, msgs+"\nType: Autoadd friend\n  Usage:"+key+" autoadd [on|off]\nType: Autoadd msg setting\n  Usage:"+key+" autoadd msg set <text>\nType: Autoadd Sticker\n  Usage:"+key+" add autoaddsticker\n  Usage:"+key+" del autoaddsticker")
                        elif cmd == "autoadd off":
                            if settings["autoAdd"] == False:
                                msgs=" 「 Auto Add 」\nAuto Add already DISABLED♪\nNote: Auto add message is not affected♪"
                            else:
                                msgs=" 「 Auto Add 」\nAuto Add set to DISABLED♪\nNote: Auto add message is not affected♪"
                                settings['autoAdd']=False
                            sendFooter2(to, msgs)
                        elif cmd == "autoadd on":
                            if settings["autoAdd"] == True:
                                msgs=" 「 Auto Add 」\nAuto Add already Enable♪\nNote: Auto add message is not affected♪"
                            else:
                                msgs=" 「 Auto Add 」\nAuto Add set to Enable♪\nNote: Auto add message is not affected♪"
                                settings["autoAdd"]=True
                            sendFooter2(to, msgs)
                        elif cmd.startswith('autoadd msg set'):
                            msg.text = ais.mycmd(msg.text,wait)
                            if len(msg.text.split("\n")) >= 2:
                                settings["addPesan"] = msg.text.replace(msg.text.split("\n")[0]+"\n","").replace('|','@!')
                                sendFooter2(msg.to," 「 Auto Add 」\nAuto add message has been set to:\n" + settings["addPesan"])
                        elif cmd == "add autoaddsticker" and sender == aisMID:
                            settings["messageSticker"]["addStatus"] = True
                            settings["messageSticker"]["addName"] = "addSticker"
                            sendFooter2(to, " 「 Auto Add 」\nType: Auto add\n • Detail: Add autoadd sticker\n • Status: Send sticker")
                        elif cmd == "del autoaddsticker" and sender == aisMID:
                            settings["messageSticker"]["listSticker"]["addSticker"]["status"] = False
                            sendFooter2(to, " 「 Auto Add 」\nType: Auto add\n • Detail: Del autoadd sticket\n • Status: Succes")
#=====================================================================
                        elif cmd.startswith('unsend '):
                            ais.unsendMessage(msg.id)
                            j = int(msg.text.split(' ')[1])
                            a = [ais.adityasplittext(msg.text,'s').replace('{} '.format(j),'')]*j
                            if len(msg.text.split(' ')) == 2:
                                h = wait['Unsend'][msg.to]['B']
                                n = len(wait['Unsend'][msg.to]['B'])
                                for b in h[:j]:
                                    try:
                                        ais.unsendMessage(b)
                                        wait['Unsend'][msg.to]['B'].remove(b)
                                    except:pass
                                t = len(wait['Unsend'][msg.to]['B'])
  #                              ais.generateReplyMessage(msg.id)
  #                              ais.sendReplyMessage(msg.id, to," 「 Unsend 」\nUnsend {} message".format((n-t)))
                            if len(msg.text.split(' ')) >= 3:h = [ais.unsendMessage(sendFooter2(to,ais.adityasplittext(msg.text,'s')).id) for b in a]
#=====================================================================
#=====================================================================
                        elif cmd == "friends":
                            sendFooter2(to, " 「 Friend 」\nType: List contact\n • Usage: Friendlist\n • Usage: Friend info 「numb」\n\nType: Delete friend\n • Usage: Clearfriend\n • Usage: Delete\n • Usage: Delfriend 「 @ 」\n • Usage: Del friend 「numb」")
                        elif cmd == 'friendlist':a = ais.refreshContacts();ais.datamention(msg.to,'List Friend',a)
                        elif cmd.startswith('getid'):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                ais.getinformation(msg.to,key1,wait)
                            else:
                                if len(cmd.split(' ')) == 2:
                                    a = ais.getGroupIdsJoined()
                                    ais.getinformation(msg.to,a[int(cmd.split(' ')[1])-1],wait)
                                if cmd == 'getid':ais.getinformation(msg.to,msg.to,wait)
                        elif cmd.startswith("friend info "):
                            msg.text = msg.text = ais.mycmd(msg.text,wait)
                            if len(msg.text.split(' ')) == 3:
                                b = ais.refreshContacts()
                                ais.getinformation(to,b[int(msg.text.split(' ')[2])-1],wait)
                        elif cmd == "clearfriend":
                            n = len(ais.getAllContactIds())
                            try:
                                ais.clearContacts()
                            except: 
                                pass
                            t = len(ais.getAllContactIds())
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to,"Type: Friendlist\n • Detail: Clear Contact\n • Before: %s Friendlist\n • After: %s Friendlist\n • Total removed: %s Friendlist\n • Status: Succes.."%(n,t,(n-t)))
                        elif cmd == "delete":
                            n = len(ais.getAllContactIds())
                            try:
                                ais.deleteContact(to)
                            except:pass
                            t = len(ais.getAllContactIds())
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                        elif cmd.startswith("delfriend "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    n = len(ais.getAllContactIds())
                                    try:
                                        ais.deleteContact(ls)
                                    except:pass
                                    t = len(ais.getAllContactIds())
                                    ais.generateReplyMessage(msg.id)
                                    ais.sendReplyMessage(msg.id, to, "Type: Friendlist\n • Detail: Delete friend\n • Status: Succes..\n • Before: %s Friendlist\n • After: %s Friendlist"%(n,t))
                        elif cmd.startswith("addfriend "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    ais.findAndAddContactsByMid(ls)
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Friendlist")
                        elif cmd.startswith("blockfriend "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = ais.getContact(ls)
                                    ais.blockContact(ls)
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to, "Success add " + str(contact.displayName) + " to Blocklist")
                        elif cmd.startswith("del friend "):
                            anu = ais.refreshContacts()
                            ais.deletefriendnum(to, wait, cmd)
                        elif cmd.startswith("dick "):
                            khie = removeCmd("dick", text)
                            s = urllib.parse.quote(khie)
                            sendFooter2(to,"http://en.inkei.net/dick/"+s)
                        elif cmd.startswith("anus "):
                            khie = removeCmd("anus", text)
                            s = urllib.parse.quote(khie)
                            sendFooter2(to,"http://en.inkei.net/anus/"+s)
                        elif cmd.startswith("tits "):
                            khie = removeCmd("tits", text)
                            s = urllib.parse.quote(khie)
                            sendFooter2(to,"http://en.inkei.net/tits/"+s)
                        elif cmd.startswith("vagina "):
                            khie = removeCmd("vagina", text)
                            s = urllib.parse.quote(khie)
                            sendFooter2(to,"http://en.inkei.net/vagina/"+s)
                        elif cmd.startswith("countdown "):
                           number = removeCmd("countdown", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 500:                                             
                                       sendFooter2(to,"invalid >_< ! Max: 100.")
                                   else:
                                       for i in range(0,number):
                                           sendFooter2(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  sendFooter2(to,"Please specify a valid number.")
                        elif cmd.startswith("countforward "):
                           number = removeCmd("countforward", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 500:                                             
                                       sendFooter2(to,"Invalid >_< ! Max 100.")
                                   else:
                                       for i in range(0,number):
                                           sendFooter2(to,str(i+1))
                                           i += 1+1
                                           time.sleep(0.008)
                               else:
                                  sendFooter2(to,"Please input count number.")

                        if text.startswith("b64encode "):
        	                de_str = msg.text.replace("b64encode ","")
        	                hasil = base64.b64encode(de_str.encode())
        	                sendFooter2(to,str(hasil.decode('utf-8')))
                        if text.startswith("b64decode "):
                	        de_str = msg.text.replace("b64decode ","")
                	        hasil = base64.b64decode(de_str.encode())
                	        sendFooter2(to,str(hasil.decode('utf-8')))
                        elif cmd.startswith("fuck "):
                           number = removeCmd("fuck", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 1000000:                                             
                                       ais.sendMessage(to,"invalid >_< ! Max: 1000000.")
                                   else:
                                       for i in range(0,number):
                                           ais.sendMessage(to,str(number))
                                           number -= 1
                                           ais.sendMessage(to,str(i+1))
                                           i += 1+1
                               else:
                                  ais.sendMessage(to,"Please input count number.")
#=====================================================================
#=====================================================================
                        elif cmd == "mentionall -s":
                            ais.unsendMessage(msg_id)
                            try:group = ais.getGroup(msg.to);nama = [contact.mid for contact in group.members];nama.remove(ais.getProfile().mid)
                            except:group = ais.getRoom(msg.to);nama = [contact.mid for contact in group.contacts]
                            k = len(nama)//20
                            for a in range(k+1):
                                if a == 0:ais.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[:20],pl=0,ps='╭「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                                else:ais.mentionmention(to=msg.to,wait=wait,text='',dataMid=nama[a*20 : (a+1)*20],pl=a*20,ps='├「 Mention 」─',pg='MENTIONALLUNSED',pt=nama)
                        elif cmd == "mentionall":
                            group = ais.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(ais.getProfile().mid)
                            ais.datamention(to,'Mention',nama)
                        elif cmd.startswith('mention '):
                            msg.text = ais.mycmd(msg.text,wait)
                            if msg.toType == 0:
                                ais.datamention(to,'Spam',[to]*int(cmd.split(" ")[1]))
                            elif msg.toType == 2:
                                gs = ais.getGroup(to)
                                nama = [contact.mid for contact in gs.members]
                                try:
                                    if 'MENTION' in msg.contentMetadata.keys()!=None:ais.datamention(to,'Spam',[eval(msg.contentMetadata["MENTION"])["MENTIONEES"][0]["M"]]*int(cmd.split(" ")[1]))
                                    else:texst = ais.adityasplittext(cmd)
                                    gs = ais.getGroup(to)
                                    nama = [contact.mid for contact in gs.members];nama.remove(ais.getProfile().mid)
                                    c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                                    c.sort()
                                    b = []
                                    for s in c:
                                        if len(texst) == 1:dd = s[len(texst)-1].lower()
                                        else:dd = s[:len(texst)].lower()
                                        if texst in dd:b.append(s.split(':-:')[1])
                                    ais.datamention(to,'Mention By Abjad',b)
                                except:ais.adityaarchi(wait,'Mention','',to,ais.adityasplittext(msg.text),msg,'\n├Group: '+gs.name[:20],nama=nama)
                        elif cmd.startswith('mentionname '):
                            texst = ais.adityasplittext(cmd)
                            gs = ais.getGroup(to)
                            c = ['{}:-:{}'.format(a.displayName,a.mid) for a in gs.members]
                            c.sort()
                            b = []
                            for s in c:
                                if texst in s.split(':-:')[0].lower():b.append(s.split(':-:')[1])
                            ais.datamention(to,'Mention By Name',b)
                        elif cmd == "check mention":
                            if to in wait['ROM']:
                                moneys = {}
                                msgas = ''
                                for a in wait['ROM'][to].items():
                                    moneys[a[0]] = [a[1]['msg.id'],a[1]['waktu']] if a[1] is not None else idnya
                                sort = sorted(moneys)
                                sort.reverse()
                                sort = sort[0:]
                                msgas = ' 「 Mention Me 」'
                                h = []
                                no = 0
                                for m in sort:
                                    has = ''
                                    nol = -1
                                    for kucing in moneys[m][0]:
                                        nol+=1
                                        has+= '\nline://nv/chatMsg?chatId={}&messageId={} {}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[m][1][nol]/1000)))
                                    h.append(m)
                                    no+=1
                                    if m == sort[0]:
                                        msgas+= '\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                                    else:
                                        msgas+= '\n\n{}. @!{}x{}'.format(no,len(moneys[m][0]),has)
                                mentions(to, msgas, h)
                                del wait['ROM'][to]
                            else:
                                try:
                                    mids = ["u3e941ed98d2a98e04ad01784b7baacf6"]
                                    msgas = 'Sorry @!In {} nothink get a mention'.format(ais.getGroup(to).name)
                                    mentions(to, msgas, [aisMID])
                                except:
                                    mids = ["u3e941ed98d2a98e04ad01784b7baacf6"]
                                    msgas = 'Sorry @!In Chat @!nothink get a mention'
                                    mentions(to, msgas, [aisMID])
                        elif cmd.startswith("ginfo "):
                            number = removeCmd("ginfo",text)
                            groups = ais.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                path = "http://dl.profile.line-cdn.net/" + G.pictureStatus
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ais.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "「 Group Info 」\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ais.sendImageWithURL(to, path)
                                sendFooter2(to, str(ret_))
                                ais.sendContact(to, G.creator.mid)
                            except:
                                pass
                        elif cmd.startswith("changegn"):
                            if msg.toType == 2:
                                X = ais.getGroup(to)
                                X.name = removeCmd("changegn", text)
                                ais.updateGroup(X)
                            
                        elif cmd.startswith("leave ") and sender == aisMID:
                            number = removeCmd("leave", text)
                            groups = ais.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    ais.leaveGroup(G.id)
                                except:
                                    ais.leaveGroup(G.id)
                                sendFooter2(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd.startswith("commentpost: "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            try:
                                settings["commentPost"] = txt
                                sendFooter2(to, "Comment changed to :\n{}".format(txt))
                            except:
                                ais.sendMessage(to, "Failed")
#=====================================================================
#=====================================================================
                        elif cmd == "lurk":
                            if 'lurkauto' not in wait:wait['lurkauto'] = False
                            if wait['lurkauto'] == False:sd = "\n│Lurk Auto: OFF"
                            else:sd = "\n│Lurk Auto: ON"
                            if to in wait['readPoint']:
                                a = "\n│Lurk State: ON"+sd
                            else:
                                a = "\n│Lurk State: OFF"+sd
                            if to in wait["lurkp"]:
                                if wait["lurkp"][to] == {}:
                                    b='\n╰Lurk People: None'
                                    h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurtk Point\n│  Usage: lurk on\n│  Usage: lurk auto on\n│Lurk Del\n│  Usage: lurk off\n│  Usage: lurk auto off\n│Lurk Cek\n│  Usage: lurk result"
                                    sendFooter2(to,h+b)
                                else:
                                    h= "╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Usage: lurk on\n│  Usage: lurk auto on\n│Lurk Del\n│  Usage: lurk off\n│  Usage: lurk auto off\n│Lurk Cek\n│  Usage: lurk result\n│Lurk People: {}".format(len(wait["lurkp"][to]))
                                    no=0
                                    hh = []
                                    for c in wait["lurkp"][to]:
                                        no+=1
                                        hh.append(c)
                                        if no == len(wait["lurkp"][to]):h+= '\n╰ {}. @!'.format(no)
                                        else:h+= '\n│ {}. @!'.format(no)
                                    mentions(to,h,hh)
                            else:
                                b='\n╰Lurk People: None'
                                h="╭「 Lurk 」─"+a+"\n│    | Command |  \n│Lurk Point\n│  Usage: lurk on\n│  Usage: lurk auto on\n│Lurk Del\n│  Usage: lurk off\n│  Usage: lurk auto off\n│Lurk Cek\n│  Usage: lurk result"
                                sendFooter2(to,h+b)
                        elif cmd == "lurk on":
                            if to in wait['readPoint']:
                                sendFooter2(to, " 「 Lurk 」\nLurk already set♪")
                            else:
                                try:
                                    del wait['readPoint'][to];del wait['setTime'][to]
                                except:
                                    pass
                                wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                                sendFooter2(to, " 「 Lurk 」\nLurk point set♪")
                        elif cmd == "lurk off":
                            if msg.to not in wait['readPoint']:
                                sendFooter2(to, " 「 Lurk 」\nLurk already off♪")
                            else:
                                try:
                                   del wait['readPoint'][to];wait['setTime'][to] = {};wait['ROM1'][to] = {}
                                except:
                                   pass
                                sendFooter2(to, " 「 Lurk 」\nLurk point off♪")
                        elif cmd == "lurk result":
                            if to in wait['readPoint']:
                                try:
                                    anulurk(to,wait)
                                    wait['setTime'][to]  = {}
                                except:sendFooter2(to,'╭「 Lurkers 」─\n╰ None')
                            else:sendFooter2(to, " 「 Lurk 」\nLurk point not on♪")
                        elif cmd == "lurk auto on":
                            if to in wait['readPoint']:
                                if wait['lurkauto'] == True:sendFooter2(to, " 「 Lurk 」\nLurk already set♪")
                            else:
                                try:
                                    del wait['readPoint'][to];del wait['setTime'][to]
                                except:
                                    pass
                                wait['readPoint'][to] = msg.id;wait['setTime'][to]  = {};wait['ROM1'][to] = {}
                                wait['lurkauto'] = True
                                sendFooter2(to, " 「 Lurk 」\nLurk point set♪")
                        elif cmd == "lurk auto off":
                            if wait['lurkauto'] == False:
                                sendFooter2(to, " 「 Lurk 」\nLurk auto already off♪")
                            else:
                                wait['lurkauto'] = False
                                sendFooter2(to, " 「 Lurk 」\nLurk auto point off♪")
                        elif cmd.startswith("lurk on "):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                targets = key["MENTIONEES"][0]["M"]
                                if targets in wait['readPoints']:
                                    ais.sendMention(to, " 「 Lurk 」\nLurk in @! already active",'',[targets])
                                else:
                                    try:
                                        del wait['readPoints'][targets];del wait['lurkt'][to];del wait['lurkp'][to][targets]
                                    except:
                                        pass
                                    wait['readPoints'][targets] = msg.id
                                    if to not in wait['lurkt']:
                                        wait['lurkt'][to] = {}
                                        wait['lurkp'][to] = {}
                                    if targets not in wait['lurkp'][to]:
                                        wait['lurkp'][to][targets] = {}
                                        wait['lurkt'][to][targets] = {}
                                    ais.sendMention(to, " 「 Lurk 」\nLurk in @! set to active",'',[targets])
                        elif cmd.startswith("lurk off "):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                targets = key["MENTIONEES"][0]["M"]
                                if targets not in wait['readPoints']:
                                    ais.sendMention(to, " 「 Lurk 」\nLurk in @! already mute",'',[targets])
                                else:
                                    try:
                                        del wait['readPoints'][targets];del wait['lurkp'][to];del wait["lurkt"][to]
                                    except:
                                        pass
                                    ais.sendMention(to, " 「 Lurk 」\nLurk in @! set to mute",'',[targets])
                        elif cmd.startswith("lurk result "):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                targets = key["MENTIONEES"][0]["M"]
                                if targets in wait['readPoints']:
                                    chiya = []
                                    for rom in wait["lurkp"][to][targets].items():
                                        chiya.append(rom[1])
                                        print(rom[1])
                                    k = len(chiya)//100
                                    for a in range(k+1):
                                        if a == 0:ais.mentionmention(to=to,wait=wait,text='',dataMid=chiya[:100],pl=0,ps='╭「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                                        else:ais.mentionmention(to=to,wait=wait,text='',dataMid=chiya[a*100 : (a+1)*100],pl=a*100,ps='├「 Lurkers 」─',pg='SIDERMES',pt=chiya)
                                    wait['lurkt'][to][targets]  = {};wait['lurkp'][to][targets] = {}
                                else:ais.sendMention(to, " 「 Lurk 」\nLurk in @! not active",'',[targets])
#=====================================================================
#=====================================================================
                        elif cmd.startswith("add pict ") and sender == aisMID:
                            load()
                            name = removeCmd("add pict", text)
                            name = name.lower()
                            if name not in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendFooter2(to, "Type: Picture\n • Detail: Add picture\n • Statud: Send pict...")
                            else:
                                sendFooter2(to, "Type: Picture\n • Detail: Add picture\n • Status: Failed, Picture already in list...")
                        elif cmd.startswith("del pict ") and sender == aisMID:
                            load()
                            name = removeCmd("del pict", text)
                            name = name.lower()
                            if name in images:
                                ais.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendFooter2(to, "Type: Picture\n • Detail: Delete list picture\n • Status: Succes delete Picture {}".format(str(name.lower())))
                            else:
                                sendFooter2(to, "Type: Picture\n • Detail: Delete list picture\n • Status: Failed, Picture not in list...")
                        elif cmd.startswith("changepict ") and sender == aisMID:
                            load()
                            name = removeCmd("changepict", text)
                            name = name.lower()
                            if name in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendFooter2(to, "Type: Picture\n • Detail: Change picture\n • Status: Send pict...")
                            else:
                                sendFooter2(to, "Type: Picture\n • Detail: Change picture\n • Status: Failed, Picture not in list...")
                        elif cmd == "list pict":
                            load()
                            no = 0
                            ret_ = " 「 List Picture 」"
                            for image in images:
                                no += 1
                                ret_ += "\n{}. {}".format(int(no), image.title())
                            ret_ += "\n\nTotal {} Picture".format(str(len(images)))
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyMessage(msg.id, to, ret_)
                        elif cmd.startswith("sendpict ") and sender == aisMID:
                            load()
                            text = removeCmd("sendpict", text)
                            cond = text.split(" ")
                            jml = int(cond[0])
                            imagename = text.replace(cond[0] + " ","").lower()
                            if imagename in images:
                                imgURL = images[imagename]
                            else:
                                sendFooter2(to, "Type: Picture\n • Detail: Send picture\n • Status: Failed, Picture name not in list...")
                                return
                            for x in range(jml):
                                ais.sendImage(to, imgURL)
#=====================================================================
                        elif cmd.startswith("add sticker ") and sender == aisMID:
                            load()
                            name = removeCmd("add sticker", text)
                            name = name.lower()
                            if name not in stickers2:
                                anyun["addTikel"]["status"] = True
                                anyun["addTikel"]["name"] = name.lower()
                                stickers2[name.lower()] = {}
                                f = codecs.open('sticker2.json','w','utf-8')
                                json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendFooter2(to, "Send stickers to save as {} ".format(name.lower()))
                            else:
                                sendFooter2(to, "Stickers {} already in list.".format(name.lower()))
                        elif cmd.startswith("del sticker ") and sender == aisMID:
                            name = removeCmd("del sticker", text)
                            name = name.lower()
                            if name in stickers2:
                                del stickers2[name.lower()]
                                f = codecs.open('sticker2.json','w','utf-8')
                                json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                                sendFooter2(to, "Success delete stickers {} ".format(name.lower()))
                            else:
                                sendFooter2(to, "Stickers {} not found in list.".format(name.lower())) 
                        elif cmd == "list sticker":
                            load()
                            ret_ = "「 Sticker List 」\n"
                            for sticker in stickers2:
                                ret_ += "\n" + sticker.title()
                            ret_ += "\n\nTotal {} Stickers".format(str(len(stickers2)))
                            sendFooter2(to, ret_)
                        elif cmd.startswith("lyrics "):
                            anu = removeCmd("lyrics", text)
                            slyric(to, text)
                        elif cmd.startswith("searchlyric "):
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            cond = txt.split("|")
                            query = cond[0]
                            key = settings["keyCommand"].title()
                            if settings["setKey"] == False:key = ''
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0"
                                url = web.get("https://www.musixmatch.com/search/{}".format(urllib.parse.quote(query)))
                                data = BeautifulSoup(url.content, "html.parser")
                                result = []
                                for trackList in data.findAll("ul", {"class":"tracks list"}):
                                    for urlList in trackList.findAll("a"):
                                        title = urlList.text
                                        url = urlList["href"]
                                        result.append({"title": title, "url": url})
                                if len(cond) == 1:
                                    ret_ = "Lyric  Result :\n"
                                    num = 0
                                    for title in result:
                                        num += 1
                                        ret_ += "\n{}. {}".format(str(num), str(title["title"]))
                                    ret_ += "\n\nTotal {} Lyric".format(str(len(result)))
                                    ret_ += "\n\nSearchLyric {}|「number」".format(str(query))
                                    sendFooter2(to, ret_)
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(result):
                                        data = result[num - 1]
                                        with requests.session() as web:
                                            web.headers["user-agent"] = "Mozilla/5.0"
                                            url = web.get("https://www.musixmatch.com{}".format(urllib.parse.quote(data["url"])))
                                            data = BeautifulSoup(url.content, "html5lib")
                                            for lyricContent in data.findAll("p", {"class":"mxm-lyrics__content "}):
                                                lyric = lyricContent.text
                                                sendFooter2(to, lyric)
                        elif cmd.startswith("play "):
                            name = removeCmd("play",text)
                            path = ais.downloadFileURL(name)
                            ais.sendAudio(to, path)
                            os.remove(path)
#=====================================================================
#=====================================================================
#=====================================================================
#=====================================================================
                        elif cmd == "get announ":
                            msg.text = ais.mycmd(msg.text,wait)
                            to = msg.to
                            a = ais.getChatRoomAnnouncements(msg.to)
                            if a == []:
                                ais.sendMention(to, 'Sorry @!In {} nothink get a Announcements'.format(self.getGroup(to).name),' 「 Announcements 」\n', [self.getProfile().mid])
                                return
                            no = 0
                            c = ' 「 Announcements 」'
                            h = []
                            ds = [a[b].creatorMid for b in range(len(a)) if a[b].creatorMid not in h]
                            for b in a:
                                if b.creatorMid not in h:
                                    h.append(b.creatorMid)
                                    no += 1
                                    c += "\n{}. @! #{}x".format(no,str(a).count(b.creatorMid))
                                ais.sendMention(msg.to,c,'',h)
                        elif cmd.startswith("get announ "):
                            msg.text = ais.mycmd(msg.text,wait)
                            to = msg.to
                            a = ais.getChatRoomAnnouncements(msg.to)
                            if a == []:
                                ais.sendMention(to, 'Sorry @!In {} nothink get a Announcements'.format(ais.getGroup(to).name),' 「 Announcements 」\n', [ais.getProfile().mid])
                                return
                            c = ' 「 Announcements 」'
                            no = 0
                            h = []
                            ds = [a[b].creatorMid for b in range(len(a)) if a[b].creatorMid not in h]
                            if len(msg.text.split(' ')) == 3:
                                sd = ds[int(msg.text.split(' ')[2])-1]
                            c+= '\nCreate by: @!'
                            no=0
                            for b in a:
                                if b.contents.link != None:
                                    if b.creatorMid in sd:
                                        no+=1
                                if 'line://nv/chatMsg?chatId=' in b.contents.link:sdg = '{}'.format(b.contents.link)
                                else:sdg = '{}'.format(b.contents.text)
                                if no == 1:c+= '\n{}. 「 {} 」\n{}'.format(no,humanize.naturaltime(datetime.fromtimestamp(b.createdTime/1000)),sdg)
                                else:c+= '\n\n{}. 「 {} 」\n{}'.format(no,humanize.naturaltime(datetime.fromtimestamp(b.createdTime/1000)),sdg)
                            ais.sendMention(msg.to,c,'',[sd])
                        elif cmd.startswith("weather "):
                            try:
                                region = removeCmd("weather", text)
                                r = requests.get("https://api.eater.site/api/weather/?apikey=beta&region=%s"%region)
                                data = json.loads(r.text)
                                result = "「 Weather 」\n"
                                result += "\nRegion : %s"%data["result"]["name"]
                                result += "\nLatitude : %s"%data["result"]["coord"]["lat"]
                                result += "\nLongitude : %s"%data["result"]["coord"]["lon"]
                                result += "\nCountry : %s"%data["result"]["sys"]["country"]
                                for anuan in data["result"]["weather"]:
                                    result += "\nDescription : %s"%anuan["description"]
                                result += "\nTemp : %s"%data["result"]["main"]["temp"]
                                result += "\nHumidity : %s"%data["result"]["main"]["humidity"]
                                result += "\nPressure : %s"%data["result"]["main"]["pressure"]
                                result += "\nWind speed: %s"%data["result"]["wind"]["speed"]
                                sendFooter2(receiver, str(result))
                            except Exception as e:
                                sendFooter2(receiver, str(e))
                        elif cmd.startswith("anime "):
                            judul = removeCmd("anime", text)
                            with _session as web:
                                try:
                                    r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(str(judul)))
                                    data = r.text
                                    data = json.loads(data)
                                    anu = data["data"][0]
                                    title = anu["attributes"]["titles"]["en_jp"]
                                    synopsis = anu["attributes"]["synopsis"]
                                    id = anu["id"]
                                    link = anu["links"]["self"]
                                    ret_ = "「About Anime」"
                                    ret_ += "\n\nTitle : {}\nSynopsis : {}\nId : {}\nLink : {}".format(str(title), str(synopsis), str(id), str(link))
                                    sendFooter2(to, str(ret_))
                                except:
                                    sendFooter2(to, "Tidak ada hasil ditemukan")
                        elif cmd.startswith("asking "):
                            kata = removeCmd("asking", text)
                            sch = kata.replace(" ","+")
                            with _session as web:
                                urlz = "http://lmgtfy.com/?q={}".format(str(sch))
                                r = _session.get("http://tiny-url.info/api/v1/create?apikey=A942F93B8B88C698786A&provider=cut_by&format=json&url={}".format(str(urlz)))
                                data = r.text
                                data = json.loads(data)
                                url = data["shorturl"]
                                ret_ = "「Ask」"
                                ret_ += "\n\nLink : {}".format(str(url))
                                sendFooter2(to, str(ret_))
                        elif cmd == "crash":
                            ais.sendContact(to, "ub621484bd88d2486744123db00551d5e',")
                            sendFooter2(to, "Chat related.")
                        elif cmd == "doujinnews":
                            result = requests.get("https://nhentai.net")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "[ Doujin News ]"                                  
                            no = 1
                            for sam in data.findAll('div', attrs={'class':'gallery'}):
                                hasil += "\n{}. {}".format(str(no), str(sam.find('a').text))
                                hasil += "\nhttps://nhentai.net{}".format(str(sam.find('a')['href']))                                        
                                no = (no+1)                                    
                            sendFooter2(to, str(hasil))                      
                        elif cmd == "announ clear":
                            a = ais.getChatRoomAnnouncements(msg.to)
                            try:
                                for b in a:
                                    ais.removeChatRoomAnnouncement(msg.to,b.announcementSeq)
                                    sendFooter2(msg.to, 'Done')
                            except Exception as e:
                                ee = traceback.format_exc()
                                sendFooter2(msg.to, '{}'.format(e))
                        elif cmd == "chatbot off":
                            if sender in aisMID or sender in chatbot["admin"]:
                                if to not in chatbot["botMute"]:
                                    chatbot["botMute"].append(to)
                                    sendFooter2(to, "I'll be here when you need me")
                            else:
                                if to not in chatbot["botOff"]:
                                    chatbot["botOff"].append(to)
                                    sendFooter2(to, "I'll be here when you need me")
                        elif cmd == "banlist":
                            if bl["blacklist"] == []:
                                sendFooter2(to,"「 BlackList 」")
                            else:
                                num = 1
                                mc = "「 BlackList 」\n"
                                for me in bl["blacklist"]:
                                    mc += "\n- %i.  %s" % (num, ais.getContact(me).displayName)
                                    num = (num+1)
                                mc += "\n\nTotaL %i BlackList" % len(bl["blacklist"])
                                sendFooter2(to, mc)
                        elif cmd == "mysticker":
                            a = ais.shop.getActivePurchases(start=0, size=1000, language='ID', country='ID').productList
                            c = "List Download Sticker:"
                            no = 0
                            for b in a:
                                no +=1
                                c += "\n"+str(no)+". "+b.title[:21]+" ID:"+str(b.packageId)
                            k = len(c)//10000
                            for aa in range(k+1):
                                sendFooter2(msg.to,'{}'.format(c[aa*10000 : (aa+1)*10000]))
                        elif cmd.startswith('find '):
                            if 'MENTION' in msg.contentMetadata.keys()!=None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                a = ais.getGroupIdsJoined();i = ais.getGroups(a)
                                c = []
                                for h in i:
                                    g = [c.append(h.name[0:20]+',.s/'+str(len(h.members))) for d in h.members if key1 in d.mid]
                                h = "╭「 Find Contact 」─"
                                no = 0
                                for group in c:
                                    no += 1
                                    h+= "\n│{}. {} | {}".format(no, group.split(',.s/')[0], group.split(',.s/')[1])
                                sendFooter2(msg.to,h+"\n╰─「 {} Groups I Found it 」".format(len(c)))
                        elif cmd.startswith("inviteid "):
                            text = removeCmd("inviteid", text)
                            sep = text.split(" ")
                            idnya = text.replace(sep[0] + " ", text)
                            conn = ais.findContactsByUserid(idnya)
                            ais.findAndAddContactsByMid(conn.mid)
                            ais.inviteIntoGroup(msg.to,[conn.mid])
                            group = ais.getGroup(msg.to)
                            xname = ais.getContact(conn.mid)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '「 Invited from Id 」\nName '
                            khie = str(xname.displayName)
                            pesan = ''
                            pesan2 = pesan+"@a\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                            zx2.append(zx)
                            zxc += pesan2
                            text = xpesan+ zxc + "To group " + str(group.name) +""
                            sendFooter2(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        elif cmd.startswith("gbroadcast ") and sender == aisMID:
                            txt = removeCmd("gbroadcast", text)
                            groups = ais.getGroupIdsJoined()
                            for group in groups:
                                sendFooter2(group, "「 Group Broadcast 」\n\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter2(to, "Succes broadcast to {} group".format(str(len(groups))))
                        elif cmd.startswith("fbroadcast ") and sender == aisMID:
                            txt = removeCmd("fbroadcast", text)
                            friends = ais.getAllContactIds()
                            for friend in friends:
                                sendFooter2(friend, "「 Friend Broadcast 」\n\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter2(to, "Succes friend cast to {} friend ".format(str(len(friends))))
                        elif cmd.startswith("allbroadcast ") and sender == aisMID:
                            txt = removeCmd("allbroadcast", text)
                            friends = ais.getAllContactIds()
                            groups = ais.getGroupIdsJoined()
                            for group in groups:
                                sendFooter2(group, "「 Group Broadcast 」\n\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter2(to, "Succes broadcast to {} group".format(str(len(groups))))
                            for friend in friends:
                                sendFooter2(friend, "「 Friend Broadcast 」\n\n{}".format(str(txt)))
                                time.sleep(1)
                            sendFooter2(to, "Succes broadcast to {} friend".format(str(len(friends))))
                        elif cmd.startswith("closeqr "):
                            number = removeCmd("closeqr", text)
                            groups = ais.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = True
                                    ais.updateGroup(G)
                                except:
                                    G.preventedJoinByTicket = True
                                    ais.updateGroup(G)
                                sendFooter2(to, "「 Close Qr 」\n\nGroup : " + G.name)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd.startswith("openqr "):
                            number = removeCmd("openqr", text)
                            groups = ais.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    ais.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(ais.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    ais.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(ais.reissueGroupTicket(G.id)))
                                sendFooter2(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd.startswith("groupcastvoice ") and sender == aisMID:
                                bctxt = removeCmd("groupcastvoice", text)
                                bc = ("Broadcast voice")
                                cb = (bctxt + bc)
                                tts = gTTS(cb, lang='id', slow=False)
                                tts.save('tts.mp3')
                                n = ais.getGroupIdsJoined()
                                for manusia in n:
                                    ais.sendAudio(manusia, 'tts.mp3')
                        elif cmd.startswith("friendcastvoice ") and sender == aisMID:
                                bctxt = removeCmd("friendcastvoice", text)
                                bc = ("Broadcast voice")
                                cb = (bctxt + bc)
                                tts = gTTS(cb, lang='id', slow=False)
                                tts.save('tts.mp3')
                                n = ais.getAllContactIdsJoined()
                                for manusia in n:
                                    ais.sendAudio(manusia, 'tts.mp3')
                        elif cmd.startswith("updatename "):
                            string = removeCmd("updatename", text)
                            if len(string) <= 10000000000:
                                pname = ais.getContact(sender).displayName
                                profile = ais.getProfile()
                                profile.displayName = string
                                ais.updateProfile(profile)
                                sendFooter2(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                        elif cmd.startswith("updatestatus "):
                            string = removeCmd("updatestatus", text)
                            if len(string) <= 10000000000:
                                pname = ais.getContact(sender).statusMessage
                                profile = ais.getProfile()
                                profile.statusMessage = string
                                ais.updateProfile(profile)
                                sendFooter2(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                        elif cmd.startswith("crash "):
                            number = removeCmd("crash", text)
                            groups = ais.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = ais.getGroup(group)
                                try:
                                    ais.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                except:
                                    ais.sendContact(group, "uc7d319b7d2d38c35ef2b808e3a2aeed9',")
                                sendFooter2(to, "「 Crash 」\n\nGroup : " + G.name)
                            except Exception as error:
                                sendFooter2(to, str(error))
                        elif cmd.startswith('grouplist'):
                            to = msg.to
                            gid = ais.getGroupIdsJoined()
                            group = ais.getGroup(gid[int(cmd.split(' ')[1])-1])
                            nama = [a.mid for a in group.members]
                            if len(cmd.split(" ")) == 2:
                                total = "Local ID: {}".format(int(cmd.split(' ')[1]))
                                ais.datamention(to,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
                            if len(cmd.split(" ")) == 4:
                                if cmd.startswith('grouplist '+cmd.split(' ')[1]+' mem '):ais.getinformation(to,nama[int(cmd.split(' ')[3])-1],wait)
                                if cmd.startswith('grouplist '+cmd.split(' ')[1]+' tag'):ais.adityaarchi(wait,'Mention','tag',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                                if cmd.startswith('grouplist '+cmd.split(' ')[1]+' kick'):ais.adityaarchi(wait,'Kick Member','kick',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
#                     \\ MEDIA //
#=========================================================
                        elif cmd.startswith('webtoon '):
                            msg.text = ais.mycmd(msg.text,wait)
                            drama = msg.text.split(' ')[1].lower()
                            try:
                                if drama == 'drama':aa = 0
                                if drama == 'fantasi':aa = 1
                                if drama == 'comedy':aa = 2
                                if drama == 'sol':aa = 3
                                if drama == 'romance':aa = 4
                                if drama == 'thriller':aa = 5
                                if drama == 'horror':aa = 6
                                a = ais.blekedok(aa,'data')
                                try:
                                    if int(msg.text.split(' ')[2]) > len(a):
                                        sendFooter2(msg.to,' 「 Webtoon 」\nDaftar Webtoon {} urutan ke {} tidak ditemukan'.format(drama.title(),msg.text.split(' ')[2]))
                                    gd = ais.blekedok(aa)[int(msg.text.split(' ')[2])-1].get('href')
                                    b = requests.get(gd)
                                    soup1 = BeautifulSoup(b.text,'html5lib')
                                    data11 = soup1.find_all(class_='subj')
                                    data1 = soup1.find_all(class_='date')
                                    data2 = soup1.find_all(id='_listUl')
                                    data3 = data2[0].find_all('a')
                                    A = ' 「 Webtoon 」\n    | {} |'.format(a[int(msg.text.split(' ')[2])-1].find_all('p')[0].text)
                                    for c in range(0,10):
                                        if c+1 == 1:AA = '\n'
                                        else:AA = '\n\n'
                                        A+= '{}{}. {} | {}\n    {}'.format(AA,c+1,data11[c+1].text,data1[c].text.strip(),data3[c].get('href'))
                                    sendFooter2(msg.to,A)
                                except:
                                    A = ' 「 Webtoon 」\n    | {} |'.format(drama.replace('sol','slice of life').title())
                                    no=0
                                    for b in a:
                                        no+=1
                                        if no == 1:AA = '\n'
                                        else:AA = '\n\n'
                                        if len(str(no)) == 1:cdd = '\n     Author: {}'.format(b.find_all('p')[1].text)
                                        if len(str(no)) == 2:cdd = '\n      Author: {}'.format(b.find_all('p')[1].text)
                                        A+= '{}{}. {} | {} Like{}'.format(AA,no,b.find_all('p')[0].text[:20],b.find_all('p')[2].find_all('em')[0].text,cdd)
                                    sendFooter2(msg.to,A)
                            except Exception as e:sendFooter2(msg.to,str(e))
                        elif cmd == "quranlist":
                            data = ais.adityarequestweb("http://api.alquran.cloud/surah")
                            if data["data"] != []:
                                no = 0
                                ret_ = "╭──「 Al-Qur'an 」"
                                for music in data["data"]:
                                    no += 1
                                    if no == len(data['data']):ret_ += "\n╰{}. {}".format(no,music['englishName'])
                                    else:ret_ += "\n│{}. {}".format(no,music['englishName'])
                                ais.generateReplyMessage(msg.id)
                                ais.sendReplyMessage(msg.id, to,ret_)
                        elif cmd.startswith("qur'an "):
                            msg.text = ais.mycmd(msg.text,wait)
                            data = ais.adityarequestweb("http://api.alquran.cloud/surah/{}".format(ais.adityasplittext(msg.text)))
                            if len(msg.text.split(' ')) == 1:
                                if data["data"] != []:
                                    no = 0
                                    ret_ = "╭──「 Al-Qur'an 」"
                                    for music in data["data"]:
                                        no += 1
                                        if no == len(data['data']):ret_ += "\n╰{}. {}".format(no,music['englishName'])
                                        else:ret_ += "\n│{}. {}".format(no,music['englishName'])
                                    sendFooter2(msg.to,ret_)
                            if len(msg.text.split(' ')) == 2:
                                try:
                                    no = 0
                                    ret_ = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                                    for music in data["data"]["ayahs"]:
                                        no += 1
                                        ret_ += "\n{}. {}".format(no,music['text'])
                                    k = len(ret_)//10000
                                    for aa in range(k+1):
                                        sendFooter2(msg.to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                                except:sendFooter2(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(ais.adityasplittext(msg.text)))
                            if len(msg.text.split(' ')) == 3:
                                try:
                                    nama = data["data"]["ayahs"]
                                    selection = ais.MySplit(ais.adityasplittext(msg.text.lower(),'s'),range(1,len(nama)+1))
                                    k = len(nama)//100
                                    text = " 「 Al-Qur'an 」\nSurah: {}".format(data['data']['englishName'])
                                    no = 0
                                    for i in selection.parse():
                                        no+= 1
                                        text+= "\n{}. {}".format(i,nama[i-1]['text'])
                                    k = len(text)//10000
                                    for aa in range(k+1):
                                        sendFooter2(msg.to,'{}'.format(text[aa*10000 : (aa+1)*10000]))
                                except:
                                    sendFooter2(msg.to," 「 Al-Qur'an 」\nI can't found surah number {}".format(ais.adityasplittext(msg.text)))
                        elif cmd == 'blacklist':ais.adityasuperdata(to,wait,'Blacklist','bl',wait['blacklist'])
                        elif cmd == 'whitelist':ais.adityasuperdata(to,wait,'Whitelist','wl',wait['bots'])
                        elif cmd.startswith("ytdl "):
                            anu = removeCmd("ytdl",text)
                            a = ais.adityarequestweb("https://rest.farzain.com/api/yt_download.php?id={}&apikey=Q7I7o74ss7NrVm9QV0Gfr93fr".format(anu))
                            print(a)
                            #sendFooter2(to, str(a))
                            ais.sendVideoWithURL(to, a["urls"][0]["id"])
                        elif cmd.startswith("porns "):
                            kata = removeCmd("porns", text)
                            with _session as web:
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "「Porn」"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 5:
                                        for s in range(5):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n\n{}. Title : {}\n    Duration : {}\n    Views : {}\n    Link : {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n\n{}. Title : {}\n    Duration : {}\n    Views : {}\n    Link : {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    sendFooter2(to, str(ret_))
                                except:
                                    sendFooter2(to, "Porn Not Found !")
                        elif cmd.startswith("image "):
                            start = time.time()
                            search = removeCmd("image", text)
                            url = "https://xeonwz.herokuapp.com/images/google.api?q=" + urllib.parse.quote(search)
                            with _session as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["status"] == True:
                                    items = data["content"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    ais.sendImageWithURL(to, str(path))
                                    elapsed_time = time.time() - start
                                    sendFooter2(to,"Got image in %s seconds" %(elapsed_time))
                        elif cmd.startswith("devianart "):
                            start = time.time()
                            search = removeCmd("devianart", text)
                            with _session as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://xeonwz.herokuapp.com/images/deviantart.api?q={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                if data["status"] == True:
                                    path = random.choice(data["content"])
                                    ais.sendImageWithURL(to, str(path))
                                    elapsed_time = time.time() - start
                                    sendFooter2(to,"[Image Result]\nGot image in %s seconds" %(elapsed_time))
                                else:
                                    sendFooter2(to, "Hasil pencarian tidak ditemukan")
                        elif cmd.startswith("food2 "):
                                text = removeCmd("food2", text)
                                query = text.replace("food2 ", text)
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        ais.sendImageWithURL(msg.to, str(food["url"]))
                        elif cmd.startswith("google "):
                            spl = re.split("google ",msg.text,flags=re.IGNORECASE)
                            if spl[0] == "":
                                if spl[1] != "":
                                    try:
                                        sendFooter2(to,"Searching ..")
                                        resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                                        text = "Google:\n\n"
                                        for el in resp.findAll("h3",attrs={"class":"r"}):
                                            try:
                                                tmp = el.a["class"]
                                                continue
                                            except:
                                                pass
                                            try:
                                                if el.a["href"].startswith("/search?q="):
                                                    continue
                                            except:
                                                continue
                                            text += el.a.text+"\n"
                                            text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                                        text = text[:-2]
                                        sendFooter2(to,str(text))
                                    except Exception as e:
                                        print(e)
                        elif cmd.startswith("wikipedia "):
                            search = removeCmd("wikipedia", text)
                            wiki = WikiApi({'locale':'id'})
                            results = wiki.find(search)
                            for a in results:
                                ret_ = "Wikipedia :\n"
                                article = wiki.get_article(a)
                                if article.image is not None: ais.sendImageWithURL(to,str(article.image))
                                ret_ += "\nTitle : {}".format(str(article.heading))
                                ret_ += "\nURL : {}".format(str(article.url))
                                ret_ += "\nSummary\n{}".format(str(article.summary.replace("^","")))
                                sendFooter2(to,ret_)
                        elif cmd.startswith("githubprofile "):
                            username = removeCmd("githubprofile", text)
                            r = _session.get("https://api.github.com/users/" + username)
                            data = r.text
                            profile = json.loads(data)
                            if profile != [] and "message" not in profile:
                                ret_ = "「 Github 」\n"
                                ret_ += "\nType : Profile"
                                ret_ += "\nUsername : " + str(profile["login"])
                                ret_ += "\nFull Name : " + str(profile["name"])
                                ret_ += "\nType : " + str(profile["type"])
                                if profile["company"] is None:
                                    ret_ += "\nCompany : None"
                                else:
                                    ret_ += "\nCompany : " + str(profile["company"])
                                if profile["blog"] is None:
                                    ret_ += "\nWebsite : None"
                                else:
                                    ret_ += "\nWebsite : " + str(profile["blog"])
                                if profile["location"] is None:
                                    ret_ += "\nLocation : None"
                                else:
                                    ret_ += "\nLocation : " + str(profile["location"])
                                if profile["email"] is None:
                                    ret_ += "\nEmail : None"
                                else:
                                    ret_ += "\nEmail : " + str(profile["email"])
                                if profile["bio"] is None:
                                    ret_ += "\nBiography : None"
                                else:
                                    ret_ += "\nBiography : " + str(profile["bio"])
                                ret_ += "\nPublic Repository : " + format_number(str(profile["public_repos"]))
                                ret_ += "\nPublic Gists : " + format_number(str(profile["public_gists"]))
                                ret_ += "\nFollowers : " + format_number(str(profile["followers"]))
                                ret_ += "\nFollowing : " + format_number(str(profile["following"]))
                                ret_ += "\nCreated At : " + str(profile["created_at"])
                                ret_ += "\nUpdated At : " + str(profile["updated_at"])
                                links = "https://github.com/" + username
                                ais.sendImageWithURL(to, str(profile["avatar_url"]))
                                sendFooter2(to, str(ret_))
                            elif "message" in profile:
                                sendFooter2(to, "╭─「 Github 」\n╰ Username not found")
                        elif cmd.startswith("githubfollowers "):
                            text = removeCmd("githubfollowers", text)
                            cond = text.split("|")
                            username = cond[0]
                            r = requests.get("https://api.github.com/users/{}/followers".format(username))
                            data = r.text
                            data = json.loads(data)
                            no = 0
                            if len(cond) == 1:
                                if data != [] and "message" not in data:
                                    ret_ = "「 Github Followers 」\n"
                                    for followers in data:
                                        no += 1
                                        ret_ += "\n" + str(no) + ". " + str(followers["login"])
                                    ret_ += "\n\n「 Total {} User 」".format(str(len(data)))
                                    ret_ += "\n\nUsage : GithubFollowers {}|「number」".format(text)
                                    sendFooter2(to,ret_)
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User didn't have followers")
                            elif len(cond) == 2:
                                if data != [] and "message" not in data:
                                    if int(cond[1]) <= len(data):
                                        followers = data[int(cond[1])-1]
                                        ret_ = "「 Github Followers 」\n"
                                        ret_ += "\nUsername : " + str(followers["login"])
                                        ret_ += "\n\n「 https://github.com/{} 」".format(followers["login"])
                                        ais.sendImageWithURL(to,str(followers["avatar_url"]))
                                        sendFooter2(to,ret_)
                                    else:
                                        sendFooter2(to,"Index out of range")
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User didn't have followers")
                        elif cmd.startswith("githubzip "):
                            try:
                                query = removeCmd("githubzip", text)
                                cond = query.split("|")
                                username = str(cond[0])
                                repository = str(cond[1])
                                r = requests.get("https://api.github.com/repos/{}/{}".format(str(username), str(repository)))
                                data = r.text
                                data = json.loads(data)
                                ret_ = "「 Github Zip 」\n"
                                ret_ += "\nName Owner : {}".format(str(data["owner"]["login"]))
                                ret_ += "\nId Owner : {}".format(str(data["owner"]["id"]))
                                ret_ += "\nLink Repo {} : {}".format(str(data["name"]), str(data["clone_url"]))
                                ret_ += "\nId Repo {} : {}".format(str(data["name"]), str(data["id"]))
                                ret_ += "\nProgramming Language : {}".format(str(data["language"]))
                                sendFooter2(to, str(ret_))
                                ais.sendImageWithURL(to, str(data["owner"]["avatar_url"]))
                                os.system("git clone {}".format(str(data["clone_url"])))
                                os.system("zip -r {}.zip {}".format(str(repository), str(repository)))
                                ais.sendFile(to, "{}.zip".format(str(repository)))
                                time.sleep(2)
                                os.remove('{}.zip'.format(repository))
                                os.system('rm -r {}'.format(repository))
                            except Exception as error:
                                print("[ ERROR ] {} ~".format(error))
                                sendFooter2(to, ' 「 ERROR 」')
                        elif cmd.startswith("githubrepo "):
                            text = removeCmd("githubrepo", text)
                            cond = text.split("|")
                            username = cond[0]
                            r = requests.get("https://api.github.com/users/{}/repos".format(username))
                            data = r.text
                            data = json.loads(data)
                            no = 0
                            if len(cond) == 1:
                                if data != [] and "message" not in data:
                                    ret_ = "「 Github RepoSitory 」\n"
                                    for repo in data:
                                        no += 1
                                        ret_ += "\n" + str(no) + ". " + str(repo["name"])
                                    ret_ += "\n\n「 Total {} User 」".format(str(len(data)))
                                    ret_ += "\n\nUsage : GithubRepo {}|「number」".format(text)
                                    sendFooter2(to,ret_)
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User doesn't have any repository")
                            elif len(cond) == 2:
                                if data != [] and "message" not in data:
                                    if int(cond[1]) <= len(data):
                                        repo = data[int(cond[1])-1]
                                        ret_ = "「 Github RepoSitory 」\n"
                                        ret_ += "\nName Repository : " + str(repo["name"])
                                        ret_ += "\nOwner : " + str(repo["owner"]["login"])
                                        if repo["private"] == True:
                                            ret_ += "\nPrivate : Yes"
                                        else:
                                            ret_ += "\nPrivate : No"
                                        if repo["description"] is None:
                                            ret_ += "\nDescription : None"
                                        else:
                                            ret_ += "\nDescription : " + str(repo["description"])
                                        if repo["fork"] == True:
                                            ret_ += "\nFork : Yes"
                                        else:
                                            ret_ += "\nFork : No"
                                        ret_ += "\n URL : " + str(repo["svn_url"])
                                        ret_ += "\nGit URL : " + str(repo["git_url"])
                                        ret_ += "\nSSH URL : " + str(repo["ssh_url"])
                                        ret_ += "\nCreated On : " + str(repo["created_at"])
                                        ret_ += "\nUpdated On : " + str(repo["updated_at"])
                                        ret_ += "\nPushed On : " + str(repo["pushed_at"])
                                        ret_ += "\nSize Repository : ".format(str(repo["size"]))
                                        ret_ += "\nLanguage : " + str(repo["language"])
                                        ret_ += "\nTotal Forked : ".format(str(repo["forks_count"]))
                                        ret_ += "\nTotal Issues : ".format(str(repo["open_issues_count"]))
                                        ret_ += "\n\n「 https://github.com/{} 」".format(str(repo["owner"]["login"]))
                                        ret_ += "\n\nUsage : GithubFollowing {}".format(username)
                                        ret_ += "\nUsage : GithubFollowers {}".format(username)
                                        sendFooter2(to, str(ret_))
                                    else:
                                        sendFooter2(to,"Index out of range")
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User doesn't have any repository")
                        elif cmd.startswith("githubfollowing "):
                            text = removeCmd("githubfollowing", text)
                            cond = text.split("|")
                            username = cond[0]
                            r = requests.get("https://api.github.com/users/{}/following".format(username))
                            data = r.text
                            data = json.loads(data)
                            no = 0
                            if len(cond) == 1:
                                if data != [] and "message" not in data:
                                    ret_ = "「 Github Following 」\n"
                                    for following in data:
                                        no += 1
                                        ret_ += "\n " + str(no) + ". " + str(following["login"])
                                    ret_ += "\n\n「 Total {} User 」".format(str(len(data)))
                                    ret_ += "\n\nUsage : GithubFollowing {}|「number」".format(text)
                                    sendFooter2(to,ret_)
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User didn't following anybody")
                            elif len(cond) == 2:
                                if data != [] and "message" not in data:
                                    if int(cond[1]) <= len(data):
                                        following = data[int(cond[1])-1]
                                        ret_ = "「 Github Following 」\n"
                                        ret_ += "\nUsername : " + str(following["login"])
                                        ret_ += "\n\n「 https://github.com/{} 」".format(following["login"])
                                        ais.sendImageWithURL(to,str(following["avatar_url"]))
                                        sendFooter2(to,ret_)
                                    else:
                                        sendFooter2(to,"Index out of range")
                                elif "message" in data:
                                    sendFooter2(to,"User not found")
                                elif data == []:
                                    sendFooter2(to,"User didn't following anybody")
#=====================================================================
                    if text.lower().startswith("change:me "):
                        anu = text.lower().replace("change:me ","")
                        itu = str(settings["me"])
                        settings["me"] = str(anu).lower()
                        sendFooter2(to, "Key me has been change...")
                    if cmd == "chatbot on":
                        if sender in aisMID or sender in chatbot["admin"]:
                            if to in chatbot["botMute"] or to in chatbot["botOff"]:
                                if to in chatbot["botMute"]:
                                    chatbot["botMute"].remove(to)
                                if to in chatbot["botOff"]:
                                    chatbot["botOff"].remove(to)
                                sendFooter2(to, "Switched to normal mode")
                            else:
                                sendFooter2(to, "bots is already actived")
                        else:
                            if to in chatbot["botOff"] and to not in chatbot["botMute"]:
                                chatbot["botOff"].remove(to)
                                sendFooter2(to, "Switched to normal mode")
                            else:
                                sendFooter2(to, "Failed !")
                    if "/ti/g/" in msg.text.lower():
                        if settings["autoJoin"] == True or settings["autoJoin"] == False:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = ais.findGroupByTicket(ticket_id)
                                ais.acceptGroupInvitationByTicket(group.id,ticket_id)
                    for image in images:
                        if msg.text.lower() == image:
                            ais.generateReplyMessage(msg.id)
                            ais.sendReplyImage(msg.id, to, images[image])
#                    for sticker in stickers:
#                        if text.lower() == sticker:
#                            sid = stickers[sticker]["STKID"]
#                            spkg = stickers[sticker]["STKPKGID"]
#                            sver = stickers[sticker]["STKVER"]
#                            sendStickers(to, sver, spkg, sid)
                    for sticker in stickers:
                        if text.lower() == sticker:
                            sid = stickers[sticker]["STKID"]
                            spkg = stickers[sticker]["STKPKGID"]
                            sver = stickers[sticker]["STKVER"]
                            try:
                                sendSticker(to, msg._from, sver, spkg, sid)
                            except Exception as e:
                                sendSticker2(to, msg._from, sver, spkg, sid)
                    
                    for sticker in stickers2:
                        try:
                            if text.lower() == sticker:
                                sid = stickers2[sticker]["STKID"]
                                spkg = stickers2[sticker]["STKPKGID"]
                                sver = stickers2[sticker]["STKVER"]
                                a = ais.shop.getProduct(packageID=int(spkg), language='ID', country='ID')
                                if a.hasAnimation == True:data = {"type": "template","altText": "{} sent a sticker.".format(ais.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker_animation@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                                else:data = {"type": "template","altText": "{} sent a sticker.".format(ais.getProfile().displayName),"template": {"type": "image_carousel","columns": [{"imageUrl": "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(sid),"size": "full","action": {"type": "uri","uri": "http://line.me/S/sticker/{}".format(spkg)}}]}}
                                sendTemplate(to,data)
                        except Exception as e:
                            print(e)
#=====================================================================
#=====================================================================
                elif msg.contentType == 1:
                    if settings["changePicture"] == True and sender == aisMID:
                        path = ais.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        settings["changePicture"] = False
                        ais.updateProfilePicture(path)
                        sendFooter2(to, "Type: Profile\n • Detail: Change Profile Picture\n • Status: Succes..")
                    if settings["changeCover"] == True and sender == aisMID:
                        path = ais.downloadObjectMsg(msg_id, saveAs="tmp/cover.bin")
                        settings['changeProfileCover'] = path
                        settings["changeCover"] = False
                        cover = str(settings["changeProfileCover"])
                        ais.updateProfileCoverById(cover)
                        sendFooter2(to, "Type:Profile\n • Detail: Change Home Photos\n • Status: Succes..")
                    if settings['changeProfileVideo']['status'] == True and sender == aisMID:
                        path = ais.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        if settings['changeProfileVideo']['stage'] == 1:
                            settings['changeProfileVideo']['picture'] = path
                            sendFooter2(to, "Silahkan kirimkan video yang ingin anda jadikan profile")
                            settings['changeProfileVideo']['stage'] = 2
                        elif settings['changeProfileVideo']['stage'] == 2:
                            settings['changeProfileVideo']['picture'] = path
                            changeProfileVideo(to)
                            sendFooter2(to, "Type: Profile\n • Detail: Change Video Profile\n • Status: Succes..")
                    if settings["addImage"]["status"] == True and sender == aisMID:
                        path = ais.downloadObjectMsg(msg_id)
                        images[settings["addImage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendFooter2(to, " 「 Picture 」\n • Detail: Add picture\n • Status: Succes added picture {} in list".format(str(settings["addImage"]["name"])))
                        settings["addImage"]["status"] = False
                        settings["addImage"]["name"] = ""
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = ais.downloadObjectMsg(msg_id, saveAs="tmp/video.bin")
                            settings["changeGroupPicture"].remove(to)
                            ais.updateGroupPicture(to, path)
                            sendFooter2(to, "Type: Group\n • Detail: Update Group Picture\n • Status: Succes..")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = ais.downloadObjectMsg(msg_id, saveAs="tmp/video.bin")
                            settings["changeGroupPicture"].remove(to)
                            ais.updateGroupPicture(to, path)
                            sendFooter2(to, "Type: Group\n • Detail: Update Group Picture\n • Status: Succes..")
                elif msg.contentType == 2:
                    if settings['changeProfileVideo']['status'] == True and sender == aisMID:
                        path = ais.downloadObjectMsg(msg_id)
                        if settings['changeProfileVideo']['stage'] == 1:
                            settings['changeProfileVideo']['video'] = path
                            sendFooter2(to, "Type: Profile\n • Detail: Change Video Profile\n • Status: Send picture ~")
                            settings['changeProfileVideo']['stage'] = 2
                        elif settings['changeProfileVideo']['stage'] == 2:
                            settings['changeProfileVideo']['video'] = path
                            changeProfileVideo(to)
                elif msg.contentType == 7:
                    a = ais.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                    if settings["messageSticker"]["addStatus"] == True and sender == aisMID:
                        name = settings["messageSticker"]["addName"]
                        if name != None and name in settings["messageSticker"]["listSticker"]:
                            settings["messageSticker"]["listSticker"][name] = {
                                "STKID": msg.contentMetadata["STKID"],
                                "STKVER": msg.contentMetadata["STKVER"],
                                "STKPKGID": msg.contentMetadata["STKPKGID"]
                            }
                            sendFooter2(msg.to, " 「 Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                        settings["messageSticker"]["addStatus"] = False
                        settings["messageSticker"]["addName"] = None
                        settings["messageSticker"]["listSticker"]["addSticker"]["status"] = True
                        settings['messageSticker']['listSticker']['readerSticker']['status'] = True
                        settings['messageSticker']['listSticker']['replySticker']['status'] = True
                    if settings["addSticker"]["status"] == True and sender == aisMID:
                        stickers[settings["addSticker"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        stickers[settings["addSticker"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers[settings["addSticker"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        f = codecs.open('sticker.json','w','utf-8')
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendFooter2(to, "Succes Add Sticker {}".format(str(settings["addSticker"]["name"])))
                        settings["addSticker"]["status"] = False
                        settings["addSticker"]["name"] = ""
                if msg.contentType == 7:
                    if anyun["addTikel"]["status"] == True:
                        stickers2[anyun["addTikel"]["name"]]["STKID"] = msg.contentMetadata["STKID"]
                        stickers2[anyun["addTikel"]["name"]]["STKPKGID"] = msg.contentMetadata["STKPKGID"]
                        stickers2[anyun["addTikel"]["name"]]["STKVER"] = msg.contentMetadata["STKVER"]
                        f = codecs.open('sticker2.json','w','utf-8')
                        json.dump(stickers2, f, sort_keys=True, indent=4, ensure_ascii=False)
                        sendFooter2(to, "Success add sticker {}".format(str(anyun["addTikel"]["name"])))
                        anyun["addTikel"]["status"] = False
                        anyun["addTikel"]["name"] = ""
                if msg.contentType == 7:
                    a = ais.shop.getProduct(packageID=int(msg.contentMetadata['STKPKGID']), language='ID', country='ID')
                    if msg.to in wait["GROUP"]['AR']['S']:
                        if wait["GROUP"]['AR']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['AR']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            sendFooter2(msg.to, " 「 Autorespon Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['AR']['S'][msg.to]['AP'] = False
                    if msg.to in wait["GROUP"]['WM']['S']:
                        if wait["GROUP"]['WM']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['WM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            sendFooter2(msg.to, " 「 Welcome Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['WM']['S'][msg.to]['AP'] = False
                    if msg.to in wait["GROUP"]['LM']['S']:
                        if wait["GROUP"]['LM']['S'][msg.to]['AP'] == True:
                            wait["GROUP"]['LM']['S'][msg.to]['Sticker'] = msg.contentMetadata
                            sendFooter2(msg.to, " 「 Leave Sticker 」\nName: "+a.title+"\nSTKID: "+msg.contentMetadata['STKID']+"\nSTKPKGID: "+msg.contentMetadata['STKPKGID']+"\nSTKVER: "+msg.contentMetadata['STKVER'])
                            wait["GROUP"]['LM']['S'][msg.to]['AP'] = False
                elif msg.contentType == 13:
                    if settings["addContact"]["status"] == True:
                        contacts[settings["addContact"]["name"]]["mid"] = msg.contentMetadata["mid"]
                        backupData()
                        sendFooter2(to,"Contact successfully added to command {}.".format(str(settings["addContact"]["name"])))
                        settings["addContact"]["status"] = False
                        settings["addContact"]["name"] = ""
                if msg.contentType == 13 and sppam["status"] == True:
                  if msg.contentMetadata["mid"] not in sppam["list"]:
                    sppam["list"].append(msg.contentMetadata["mid"])
                    ais.sendMessage(to,"user added spam success bos...")
                  else:
                    ais.sendMessage(to,"user already in list.")

                elif msg.contentType == 14:
                    if hoho["savefile"] == True and sender == aisMID:
                        try:
                             namafile = hoho["namafile"]
                             ais.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             sendFooter2(to, "Successful, the file has been uploaded")
                        except Exception as e:
                         	sendFooter2(to, str(e))
                elif msg.contentType == 15:
                    if msg.location != None:                           
                        yun = msg.location.latitude
                        yun2 = msg.location.longitude
                        sam1 = "https://maps.googleapis.com/maps/api/streetview?location={},{}&size=600x400&heading=0&key=AIzaSyCTxOiGYGTCJH0PXkhTPRwBvooBaKdcD74".format(str(yun),str(yun2))
                        sam2 = "https://maps.googleapis.com/maps/api/streetview?location={},{}&size=600x400&heading=90&key=AIzaSyCTxOiGYGTCJH0PXkhTPRwBvooBaKdcD74".format(str(yun),str(yun2))
                        sam3 = "https://maps.googleapis.com/maps/api/streetview?location={},{}&size=600x400&heading=100&key=AIzaSyCTxOiGYGTCJH0PXkhTPRwBvooBaKdcD74".format(str(yun),str(yun2))
                        sam4 = "https://maps.googleapis.com/maps/api/streetview?location={},{}&size=600x400&heading=270&key=AIzaSyCTxOiGYGTCJH0PXkhTPRwBvooBaKdcD74".format(str(yun),str(yun2))
                        sam5 = "https://maps.googleapis.com/maps/api/streetview?location={},{}&size=600x400&heading=370&key=AIzaSyCTxOiGYGTCJH0PXkhTPRwBvooBaKdcD74".format(str(yun),str(yun2))                           
                        ais.sendImageWithURL(to, str(sam1))
                        ais.sendImageWithURL(to, str(sam2))
                        ais.sendImageWithURL(to, str(sam3))
                        ais.sendImageWithURL(to, str(sam4))
                        ais.sendImageWithURL(to, str(sam5))

        if op.type == 55:
            if op.param1 in tailah["siderTemp"] and op.param2 not in tailah["siderTemp"][op.param1]:
                tailah["siderTemp"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = ais.getContact(op.param2)
                    pesan = tailah["siderPesan"]
                    data = {
                        "type": "flex",
                        "altText": "{} Send Flex".format(ais.getProfile().displayName),
                        "contents": {
                            "type": "bubble",
                            "styles": {
                                "header": {"backgroundColor": "#000000"},
                                "hero": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"},
                                "footer": {"backgroundColor": "#000000", "separator": True, "separatorColor": "#FFFFFF"}
                            },
                            "header": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "THIS IS GROUP READER",
                                        "align": "center",
                                        "weight": "bold",
                                        "color": "#FFFFFF",
                                        "size": "sm"
                                    }
                                ]
                            },
                            "hero": {
                                "type": "image",
                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                "size": "full",
                                "margin":"xl",
                                "action": {
                                    "type": "uri",
                                    "uri": "line://ti/p/~melodic404"
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "margin": "lg",
                                        "spacing": "sm",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Reader : {}".format(contact.displayName),
                                                        "align": "center",
                                                        "weight": "bold",
                                                        "color": "#000000",
                                                        "size": "sm",
                                                        "flex": 0
                                                    }
                                                ]
                                            },
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "spacing": "sm",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "Message : {}".format(pesan),
                                                        "align": "center",
                                                        "weight": "bold",
                                                        "color": "#000000",
                                                        "size": "sm",
                                                        "flex": 0
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [
                                            {
                                                "type": "icon",
                                                "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus),
                                                "size": "md"
                                            },
                                            {
                                                "type": "text",
                                                "text": gwcool["squad"],
                                                "align": "center",
                                                "color": "#FFFFFF",
                                                "size": "md"
                                            },
                                            {
                                                "type": "spacer",
                                                "size": "sm",
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                    sendTemplate(op.param1, data)
                
            if op.param1 in read["readPoint"]:
                _name = ais.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
        if op.type == 55:
            print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != aisMID: to = sender
                else: to = receiver
                if msg.contentType == 0 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            if msg.location != None:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"location":msg.location,"from":msg._from,"waktu":unsendmsg}
                            else:
                                unsendmsg = time.time()
                                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"waktu":unsendmsg}
                        except Exception as e:
                            print (e)
                if msg.contentType == 1 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg1 = time.time()
                            path = ais.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"image":path,"waktu":unsendmsg1}
                        except Exception as e:
                            print (e)
                if msg.contentType == 2 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg2 = time.time()
                            path = ais.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"video":path,"waktu":unsendmsg2}
                        except Exception as e:
                            print (e)
                if msg.contentType == 3 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg3 = time.time()
                            path = ais.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"audio":path,"waktu":unsendmsg3}
                        except Exception as e:
                            print (e)
                if msg.contentType == 7 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg7 = time.time()
                            sticker = msg.contentMetadata["STKID"]
                            link = "http://dl.stickershop.line.naver.jp/stickershop/v1/sticker/{}/android/sticker.png".format(sticker)
                            msg_dict[msg.id] = {"from":msg._from,"sticker":link,"waktu":unsendmsg7}
                        except Exception as e:
                            print (e)
                if msg.contentType == 13 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg13 = time.time()
                            mid = msg.contentMetadata["mid"]
                            msg_dict[msg.id] = {"from":msg._from,"mid":mid,"waktu":unsendmsg13}
                        except Exception as e:
                            print (e)
                if msg.contentType == 14 and to not in chatbot["botMute"]:
                    if settings["unsendMessage"] == True:
                        try:
                            unsendmsg14 = time.time()
                            path = ais.downloadObjectMsg(msg_id)
                            msg_dict[msg.id] = {"from":msg._from,"file":path,"waktu":unsendmsg14}
                        except Exception as e:
                            print (e)
        if op.type == 65:
            if op.param1 not in chatbot["botMute"]:
                if settings["unsendMessage"] == True:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        ah = time.time()
                        ikkeh = ais.getContact(msg_dict[msg_id]["from"])
                        if "text" in msg_dict[msg_id]:
                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                            waktumsg = format_timespan(waktumsg)
                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                            rat_ += "\nText :\n{}".format(msg_dict[msg_id]["text"])
                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                            del msg_dict[msg_id]
                        else:
                            if "image" in msg_dict[msg_id]:
                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                waktumsg = format_timespan(waktumsg)
                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                rat_ += "\nImage :\nBelow"
                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                ais.sendImage(at, msg_dict[msg_id]["image"])
                                del msg_dict[msg_id]
                            else:
                                if "video" in msg_dict[msg_id]:
                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                    waktumsg = format_timespan(waktumsg)
                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                    rat_ += "\nVideo :\nBelow"
                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                    ais.sendVideo(at, msg_dict[msg_id]["video"])
                                    del msg_dict[msg_id]
                                else:
                                    if "audio" in msg_dict[msg_id]:
                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                        waktumsg = format_timespan(waktumsg)
                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                        rat_ += "\nAudio :\nBelow"
                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                        ais.sendAudio(at, msg_dict[msg_id]["audio"])
                                        del msg_dict[msg_id]
                                    else:
                                        if "sticker" in msg_dict[msg_id]:
                                            waktumsg = ah - msg_dict[msg_id]["waktu"]
                                            waktumsg = format_timespan(waktumsg)
                                            rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                            rat_ += "\nSticker :\nBelow"
                                            sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                            ais.sendImageWithURL(at, msg_dict[msg_id]["sticker"])
                                            del msg_dict[msg_id]
                                        else:
                                            if "mid" in msg_dict[msg_id]:
                                                waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                waktumsg = format_timespan(waktumsg)
                                                rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                rat_ += "\nContact :\nBelow"
                                                sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                ais.sendContact(at, msg_dict[msg_id]["mid"])
                                                del msg_dict[msg_id]
                                            else:
                                                if "location" in msg_dict[msg_id]:
                                                    waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                    waktumsg = format_timespan(waktumsg)
                                                    rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                    rat_ += "\nLocation :\nBelow"
                                                    sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                    ais.sendLocation(at, msg_dict[msg_id]["location"])
                                                    del msg_dict[msg_id]
                                                else:
                                                    if "file" in msg_dict[msg_id]:
                                                        waktumsg = ah - msg_dict[msg_id]["waktu"]
                                                        waktumsg = format_timespan(waktumsg)
                                                        rat_ = "\nSend At :\n{} ago".format(waktumsg)
                                                        rat_ += "\nFile :\nBelow"
                                                        sendMentionFooter(at, ikkeh.mid, "# Resend Message\n\nMaker :\n", str(rat_))
                                                        ais.sendFile(at, msg_dict[msg_id]["file"])
                                                        del msg_dict[msg_id]
                else:
                    print ("[ ERROR ] Terjadi Error Karena Tidak Ada Data Chat Tersebut~")

        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
   

def run():
    while True:
        try:
 #           delExpire()
            ops = aisPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(aisBot(op))
                   #aisBot(op)
                   aisPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()
