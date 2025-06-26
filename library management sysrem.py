class LibraryBook:
    def _init_(self, title , price, author ,pages):
        self._title = title
        self._price = price
        self._author = author
        self._pages = pages

    # GET METHOD FOR BOOK NAME
    def title(self):
        return self._title
    
    # SET METHOD FOR BOOK NAME
    def set_book_name(self, name):
        self._title = name

    # GET METHOD FOR PRICE 
    def get_price(self):
        return self._price

    # SET METHOD FOR PRICE
    def set_price(self, price):
        self._price = price

    # GET METHOD FOR AUTHOR
    def get_author(self):
        return self._author

    # GET METHOD FOR AUTHOR
    def set_author(self, author):
        self._author = author

    # GET METHOD FOR PAGES
    def get_pages(self):
        return self._pages

    #SET METHOD FOR PAGES
    def set_pages(self, pages):
        self._pages = pages

    # METHOD TO DISPLAY ALL INFO 
    def display(self):
        print("Book Details:")
        print(" Name  :", self._title)
        print(" Author:", self._author)
        print(" Price :", self._price)
        print(" Pages :", self._pages)