import org.example.Book;
import org.example.BookManager;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class BookManagerTest {
    private BookManager bookManager;

    @BeforeEach
    void setUp() {
        bookManager = new BookManager();
    }

    @Test
    @DisplayName("Test menambahkan buku")
    void testAddBook() {
        Book book = new Book("Pemrograman", "Andi", 2020);
        bookManager.addBook(book);
        assertEquals(1, bookManager.getBookCount());
    }

    @Test
    @DisplayName("Test menghapus buku yang ada")
    void testRemoveBook() {
        Book book = new Book("Database", "Erlangga", 2021);
        bookManager.addBook(book);
        bookManager.removeBook("Basis Data");
        assertEquals(0, bookManager.getBookCount());
    }

    // Menguji unit test untuk buku yang tidak ada/tidak terdapat pada list
    @Test
    @DisplayName("Test menghapus buku yang tidak ada")
    void testRemoveNonExistingBook() {
        bookManager.removeBook("Matematika");
        assertEquals(0, bookManager.getBookCount());
    }

    // Menguji Unit Test dibawah untuk mencari buku berdasarkan penulis
    @Test
    @DisplayName("Test mencari buku berdasarkan author")
    void testFindBooksByAuthor() {
    }

    // Menguji Unit Test dibawah untuk seluruh buku yang ada di dalam list
    @Test
    @DisplayName("Test mendapatkan semua buku")
    void testGetAllBooks() {
    }
}
