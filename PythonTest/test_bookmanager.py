import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

    def test_add_book(self):
        """Test menambahkan buku"""
        book = Book("Pemrograman", "Andi", 2020)
        self.book_manager.add_book(book)
        self.assertEqual(1, self.book_manager.get_book_count())

    def test_remove_existing_book(self):
        """Test menghapus buku yang ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Basis Data")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())

    #Lengkapi Unit Test dibawah untuk buku yang memang tidak terdapat pada list
    def test_remove_non_existing_book(self):
        """Test menghapus buku yang tidak ada"""
        book = Book("Basis Data", "Erlangga", 2021)
        self.book_manager.add_book(book)

        removed = self.book_manager.remove_book("Matematika")
        self.assertTrue(removed)
        self.assertEqual(0, self.book_manager.get_book_count())


    #Lengkapi Unit Test dibawah untuk mencari buku berdasarkan penulis
    def test_find_books_by_author(self):
        """Test mencari buku berdasarkan author"""
        book1 = Book("Bumi", "Tere Liye", 2014)
        book2 = Book("Matahari", "Tere Liye", 2016)
        book3 = Book("Laskar Pelangi", "Andrea Hirata", 2005)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)

        result = self.book_manager.find_books_by_author("Tere Liye")
        self.assertIn(book1, result)
        self.assertIn(book2, result)
        self.assertNotIn(book3, result)
        self.assertEqual(len(result), 2)
        

    #Lengkapi Unit Test dibawah untuk seluruh buku yang ada di dalam list
    def test_get_all_books(self):
        """Test mendapatkan semua buku"""
        book1 = Book("Bumi", "Tere Liye", 2014)
        book2 = Book("Matahari", "Tere Liye", 2016)
        book3 = Book("Laskar Pelangi", "Andrea Hirata", 2005)

        self.book_manager.add_book(book1)
        self.book_manager.add_book(book2)
        self.book_manager.add_book(book3)
        
        result = self.book_manager.get_all_books()
        self.assertEqual(len(self.book_manager), 3)

        # Pastikan semua buku ada dalam hasil
        self.assertIn(book1, result)
        self.assertIn(book2, result)
        self.assertIn(book3, result)
        

if __name__ == '__main__':
    unittest.main()
