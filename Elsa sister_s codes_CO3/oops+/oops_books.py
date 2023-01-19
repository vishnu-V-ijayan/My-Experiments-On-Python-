
class Publisher:
    def __init__(self,Pubname):
        self.Pubname=Pubname
    def dispaly(self):
        print("Publisher name is:,self.Pubname")
class Book(Publisher):
    def __init__(self,Pubname,Title,author):
        Publisher. __init__(self,Pubname)
        self.Title=Title
        self.author=author
    def dispaly(self):
        print("Title is:,self.Title")
        print("author name is:,self.author")
class Python(Book):
    def __init__(self,Pubname,Title,author,Price,Page):
        Book. __init__(self,Pubname,Title,author)
        self.Price=Price
        self.Page=Page


    def display(self):
        print("Title:",self.Title)
        print("Author:",self.author)
        print("Publisher:",self.Pubname)
        print("Pages:",self.Page)
        print("Price:",self.Price)


b=Python("New India","Python For freshers","mark leo",600,900)
b.display()

