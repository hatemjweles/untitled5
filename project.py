class LibraryMethod:
    def __init__(self,id,title):
        self.id=id
        self.title=title
    def print_info(self):
        print("-----libraryMethod-----")
        print("The id is :" + str(self.id))
        print("the title is :" + self.title)

class Book(LibraryMethod):
    def __init__(self,id,title,author,ISBN):
        LibraryMethod.__init__(self,id,title)
        self.author=author
        self.ISBN = ISBN

    def print_info(self):
        super().print_info()
        print("-----Book Info-----")
        print("the author name:" + self.author)
        print("the ISBN is :" +self.ISBN)

class Audio(LibraryMethod):
    def __init__(self,id,title,singer,year):
        LibraryMethod.__init__(self,id,title)
        self.singer=singer
        self.year=year
    def print_info(self):
        super().print_info()
        print("-----Audio-----")
        print("Singer Name:"+self.singer)
        print("Year is:"+str(self.year))

class AudioBook(Book,Audio):
    def __init__(self,id,title,author,singer,ISBN,year):
        Book.__init__(self,id,title,author,ISBN)
        Audio.__init__(self,id,title,singer,year)


ab1 = AudioBook(10,"show me the meaning","Hatem","Qusai","10-2202-5",1995)
ab1.print_info()
