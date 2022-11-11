import re,requests,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()
no,surat,nama_surat=0,[],[]

url = parser(ses.get("https://litequran.net/").text,"html.parser")
for data in url.find_all("a",href=True):
	nama_surat.append(data.text)
	if "https://Litequran.net/" in data.get("href"):
		pass
	else:
		if "Kebijakan Privasi" in data.text:
			pass
		else:
			no +=1
			print(f"{no}. {data.text}")
			surat.append(data.get("href"))

ask = input("\n masukan nomer : ")
urel = parser(ses.get(f"https://litequran.net/{surat[int(ask)-1]}").text,"html.parser")
for det in urel.find_all("p",{"class": ["arabic","translate"]}):
	print(det.text)
		
		
		
		