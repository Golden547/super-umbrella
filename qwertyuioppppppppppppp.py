# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:32:59 2022

@author: shn99
"""

class book:
    def __init__(self,name,published,id_number):    
        self.book_name = name
        self.book_published = published
        self.book_id = id_number    
    def add_book(self):
        print("Name: "+self.book_name)
        print("published: "+str(self.book_published))
        print("book ID" +self.book_id)
        print("book Added")
        
book1 = book("harry potter","19th october 2012","0198")
book1.add_book()
book2 = book("Hatchet",  "19th october 2010", "0199")
book2.add_book()              