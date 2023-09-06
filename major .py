import tkinter as tk
from tkinter import messagebox

class BookshopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Store  App")

        self.books = [
            {"title": "ikagai", "author": " Francesc Miralles and Hector Garcia ", "price": 13.29},
            {"title": "Rich Dad and Poor Dad", "author": "Robert Kiyosaki and Sharon Lechter", "price": 11.95},
            {"title": "Think Big and Grow Rich ", "author": "Napoleon Hill", "price": 8.99},
        ] 
        self.book_listbox = tk.Listbox(root)
        self.populate_books()

        self.details_label = tk.Label(root, text="Book Details:")
        self.details_text = tk.Text(root, height=13, width=50)

        self.purchase_button = tk.Button(root, text="Purchase", command=self.purchase_book)

        self.book_listbox.pack(padx=20,pady=20)
        self.details_label.pack(pady=15)
        self.details_text.pack(padx=15)
        self.purchase_button.pack(pady=10)

        self.book_listbox.bind('<<ListboxSelect>>', self.display_selected_book)

    def populate_books(self):
        for book in self.books:
            self.book_listbox.insert(tk.END, f"{book['title']} by {book['author']} (${book['price']:.2f}")

    def display_selected_book(self, event):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            book = self.books[selected_index[0]]
            self.details_text.delete(1.0, tk.END)
            self.details_text.insert(tk.END, f"Title: {book['title']}\nAuthor: {book['author']}\nPrice: ${book['price']:.2f}")

    def purchase_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            selected_book = self.books[selected_index[0]]
            messagebox.showinfo("Purchase", f"You purchased {selected_book['title']} for ${selected_book['price']:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    root["bg"]= "grey"
    root.geometry("850x550")
    app = BookshopApp(root)
    root.mainloop()


