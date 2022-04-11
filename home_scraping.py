try:
    from bs4 import BeautifulSoup
    import requests
    import pypyodbc
    from pub import publisher
except:
    print('[!] libraries not importing')
else:
    con = pypyodbc.connect(
        '''
        Driver={SQL Server};
        Server=serverName;
        Database=databaseName;
        UID=username;
        PWD=password;
        '''
    )

    class Main:
        def __init__(self,url):
            self.url = url
            self.links = []
            self.ctitle = ""
            self.idata = ""
            self.ititle = ""
            self.create = True
            self.cursor = con.cursor()
        
        def find(self):
            menu = requests.get(self.url)
            self.soup = BeautifulSoup(menu.text,'lxml')
            ads = self.soup.find_all("div", class_ = "links")
            for ad in ads: self.links.append("https://www.hepsiemlak.com" + ad.a.get('href'))
        
        
        def save(self):
            for link in self.links:
                self.ctitle = ""
                self.idata = ""
                self.ititle = ""
                home = requests.get(link)
                self.soup = BeautifulSoup(home.text,'lxml')
                item = self.soup.find_all("li", class_ = "spec-item")
                item_price = self.soup.find("div", class_="right").text.replace(' ','')
                item_title = self.soup.find("h1", class_="fontRB").text

                for info in item:

                    gen_title = "Başlık"
                    price_title  = "Fiyat"
                    data = info.text.replace(info.span.text,"").strip() #45835-323567
                    title = info.span.text.replace(" ", "")

                    self.ctitle += f"{title} text, " #"IlanNo text, "
                    self.ititle += f"{title}, " #"IlanNo, "
                    self.idata += f"'{data}', " #"'45835-323567', "
                
                item_title = item_title.strip().replace("'","")
                self.ctitle = f"{gen_title} text, " + f"{price_title} text, " + publisher(self.ctitle.strip().strip(','))
                self.idata = f"'{item_title}', " + f"'{item_price}', " + self.idata.strip().strip(',')
                self.ititle = f"{gen_title}, " + f"{price_title}, " + publisher(self.ititle.strip().strip(','))

                try:
                    if self.create == True: self.cursor.execute(f"create table x0house ({self.ctitle})"); self.create = False
                except: print('[!] Table already exists.')
                finally:
                    try: self.cursor.execute(f"insert into x0house({self.ititle}) values({self.idata})")
                    except: pass
                
                con.commit()

    hepsiemlak = Main('https://www.hepsiemlak.com/istanbul-satilik')
    hepsiemlak.find()
    hepsiemlak.save()