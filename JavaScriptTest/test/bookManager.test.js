const Book = require('../book');
const BookManager = require('../bookManager');

describe('BookManager', () => {
  let bookManager;

  beforeEach(() => {
    bookManager = new BookManager();
  });

  test('Test menambahkan buku', () => {
    const book = new Book("Bumi", "Tere Liye", 2014);
    bookManager.addBook(book);
    expect(bookManager.getBookCount()).toBe(1);
  });

  test('Test menghapus buku yang ada', () => {
    const book = new Book("Bumi", "Tere Liye", 2014);
    bookManager.addBook(book);

    const removed = bookManager.removeBook("Bumi");
    expect(removed).toBe(true);
    expect(bookManager.getBookCount()).toBe(0);
  });

  // Unit Test: menghapus buku yang tidak ada di list
  test('Test menghapus buku yang tidak ada', () => {
    const book = new Book("Bumi", "Tere Liye", 2014);
    bookManager.addBook(book);

    const removed = bookManager.removeBook("Matahari");
    expect(removed).toBe(false);
    expect(bookManager.getBookCount()).toBe(0);
  });

  // Unit Test: mencari buku berdasarkan penulis
  test('Test mencari buku berdasarkan author', () => {
    const book1 = new Book("Bumi", "Tere Liye", 2014);
    const book2 = new Book("Laskar Pelangi", "Andrea Hirata", 2005);
    bookManager.addBook(book1);
    bookManager.addBook(book2);

    const result = bookManager.findBooksByAuthor("Tere Liye");
    expect(result).toContainEqual(book1);
    expect(result).not.toContainEqual(book2);
  });

  // Unit Test: mendapatkan semua buku
  test('Test mendapatkan semua buku', () => {
    const book1 = new Book("Bumi", "Tere Liye", 2014);
    const book2 = new Book("Matahari", "Tere Liye", 2016);
    bookManager.addBook(book1);
    bookManager.addBook(book2);

    const allBooks = bookManager.getAllBooks();
    expect(allBooks.length).toBe(2);
    expect(allBooks).toContainEqual(book1);
    expect(allBooks).toContainEqual(book2);
  });
});