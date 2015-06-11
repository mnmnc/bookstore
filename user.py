__author__ = 'Dawid'

import book

class User:

	def __init__(self, name):
		self.name = name
		self.card_valid = True
		self.rent_counter = 0
		self.book_list = []

	def rent_book(self, book):
		if self.card_valid is True and self.rent_counter < 5 and book.available is True:
			self.book_list.append(book)
			self.rent_counter += 1
			book.return_date = 14
