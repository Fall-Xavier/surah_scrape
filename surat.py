import re,requests,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

class ScrapeSurah:
	
	def __init__(self):
		self.no,self.num = 0,0
		self.user_surah = []
		self.nama_surah = []
		self.ayat = []
		self.surah_fatihah = []
		self.angka = []
		self.url = "https://litequran.net/"
		
	def Get_Kelipatan(self,angka):
		kelipatan = angka
		while kelipatan < 9999:
			self.angka.append(kelipatan)
			kelipatan = kelipatan + angka
	
	def Menu(self):
		url = parser(ses.get(self.url).text,"html.parser")
		for data in url.find_all("a",href=True):
			self.nama_surah.append(data.text)
			if "https://Litequran.net/" in data.get("href"):
				pass
			else:
				if "Kebijakan Privasi" in data.text:
					pass
				else:
					self.no +=1
					print(f"{self.no}. {data.text}")
					self.user_surah.append(data.get("href"))
		ask = input("\n masukan nomer : ")
		self.Get_Surah(self.user_surah[int(ask)-1])
		
	def Get_Surah(self,nama):
		url = parser(ses.get(self.url+nama).text,"html.parser")
		if nama == "al-fatihah":
			self.Al_Fatihah(url)
		self.Get_Kelipatan(4)
		for data in url.find_all("p"):
			if len(self.ayat) in self.angka:
				self.ayat.append("<>")
			self.ayat.append(f"{data.text}|")
		for isi in "".join(self.ayat).split("<>"):
			self.num +=1
			nanya = isi.split("|")
			print(f"""
Ayat Ke {self.num}
{nanya[0]}
{nanya[1]}

Artinya : {nanya[2]}""")
		exit()
			
	def Al_Fatihah(self,url):
		self.Get_Kelipatan(4)
		for data in url.find_all("p"):
			if len(self.surah_fatihah) in self.angka:
				#self.angka.clear()
				self.surah_fatihah.append("<>")
				#self.Get_Kelipatan(4)
			self.surah_fatihah.append(f"{data.text}|")
		for isi in "".join(self.surah_fatihah).split("<>"):
			self.num +=1
			nanya = isi.split("|")
			print(f"""
Ayat Ke {self.num}
{nanya[0]}
{nanya[1]}

Artinya : {nanya[2]}""")
		exit()
		
ScrapeSurah().Menu()
