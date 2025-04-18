# class Car:
#     #speed = 110
#     #model = "BMW"
#     def __init__(self, speed, model):
#         self.speed = speed
#         self.m=model
#         Car.count += 1
#
#
# def info(self):
#     print("Швидкість авто", self.speed)
#     print("Модель Авто", self.model)
# auto = Car(speed=125, model='Audi')
# auto.info()
# speed = int(input(">"))
# model = int(input(">"))
# auto2 = Car(speed, model)
# auto2.info()
# print(auto2.count)
# auto3 = Car(speed=225, model='Volkswagen golf gti')
# auto3.info()
# print(Car.count)
# auto2=Car()
#print("Швидкість авто", auto.speed)

#print("Модель Авто", auto2.model)

class Zm:
    def __init__(self, id=111, name="Максим", heigh="170"):
        self.id = id
        self.name = name
        self.heigh=heigh
    def __str__(self):
        print("Інформація учасника:")
        print("Номер:", str(self.id), "Ім'я:", str(self.name), "Зріст:", str(self.heigh))
    def __bool__(self):

       return self.id!=None
p1 =Zm()
#print(p1.name)
p2=Zm(id=112, name="Поліна", heigh=170)
#print(p2.heigh)
p1.__str__()
#print(str(p2))
print(bool(p1))
print(p2.__bool__())


class Books:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        self.soup = None

    def auditsite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
        else:
            print(f"Error: {response.status_code}")
            return

    def getinfo(self):
        tablet = []
        books = self.soup.find_all('article', class_="product_pod")

        if not books:
            print("Не вдалося знайти необхідну інформацію")
            return

        for i in books[:4]:
            name_tag = i.find("h3").find("a")
            price_tag = i.find("p", class_="price_color")

            name = name_tag["title"].strip() if name_tag else "Назва відсутня"
            price = price_tag.text.strip() if price_tag else "Ціна відсутня"

            tablet.append({
                "Назва": name,
                "Ціна": price,
            })

        return tablet

    def showinfo(self, txt):
        print("№\t", "Назва", "\t"*3, "Ціна")
        print("-"*80)
        num = 1
        for i in txt:
            print(f"{num}\t{i['Назва']}\t{i['Ціна']}")
            num += 1

obj = Books("http://books.toscrape.com/")
obj.auditsite()
txt = obj.getinfo()
obj.showinfo(txt) if txt else print("Жодної інформації не знайдено")











import requests as r
from bs4 import BeautifulSoup as bs

class News:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        self.soup = None

    def auditsite(self):
        response = r.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = bs(response.text, 'html.parser')
        else:
            print(f"Error: {response.status_code}")
            return

    def getinfo(self):
        tablet = []
        tablettag = self.soup.find_all('div', class_="sc-41044fee-1 eIoIcv")

        if not tablettag:
            print("Не вдалося знайти необхідну інформацію")
            return

        for i in tablettag[:4]:
            name_tag = i.find("div", class_="sc-87075214-0 jvGDZA")
            price_tag = i.find("p", class_="sc-530fb3d6-0 gJqLcg")

            name = name_tag.text.strip() if name_tag else "Назва відсутня"
            price = price_tag.text.strip() if price_tag else "Текст відсутень"

            tablet.append({
                "Назва": name,
                "Текст": price,
            })

        return tablet

    def showinfo(self, txt):
        print("№\t", "Назва", "\t"*3, "Текст")
        print("-"*80)
        num = 1
        for i in txt:
            print(f"{num}\t{i['Назва']}\t{i['Текст']}")
            num += 1

obj = News("https://www.bbc.com/news")
obj.auditsite()
txt = obj.getinfo()
obj.showinfo(txt) if txt else print("Жодної інформації не знайдено")
