class Book:
  def __init__(self, title, autor, ISBN, genero):
    self.title = title
    self.autor = autor
    self.ISBN = ISBN
    self.genero = genero
    self.status = True

  def __str__(self):
    status = "Disponível" if self.status else "Indisponível"
    return f"{self.title}, {self.autor} - {status}"

class Client:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.borrowed_books = []

  def borrow_book(self, book):
    if book not in self.borrowed_books:
      self.borrowed_books.append(book)
      print(f"{self.name} pegou o livro {book.title}.")
    else:
      print(f"{self.name} já pegou {book.title}!")

  def return_book(self, book):
    if book in self.borrowed_books:
      self.borrowed_books.remove(book)
      print(f"{self.name} devolveu o livro {book.title}")
    else:
      print(f"O livro {book.title} não foi emprestado para {self.name}")

  def show_books(self, book):
    if book in self.borrowed_books:
      print(f"{self.name} pegou os livros:")
      for book in self.borrowed_books:
        print(f"- {book.title}")
    else:
      print(f"{self.name} ainda não pegou nenhum livro!")

class Librarian:
  def __init__(self, name):
    self.name = name
    self.collection = []
    self.clients = []

  def add_to_collection(self, book):
    if book not in self.collection:
      self.collection.append(book)
      print(f"O livro {book.title} foi adicionado ao acervo!")
    else:
      print(f"O livro {book.title} já se encontra no acervo!")

  def show_collection(self):
    print("Acervo da biblioteca:")
    for book in self.collection:
      print(f"- {book.title}")

  def add_clients(self, client):
    self.clients.append(client)
    print(f"Novo usuário adicionado: {client.name}")

  def show_clients(self):
    print("Clientes ativos:")
    for client in self.clients:
      print(f"- {client.name}")

  def lent_book(self, client, book_title):
    found_book = None
    for book in self.collection:
      if book_title == book.title:
        found_book = book
        break
      else:
        print(f"O livro '{book_title}' não está disponível ou não existe.")
        break
    if found_book and found_book.status:
      client.borrow_book(found_book)
      found_book.status = False
      print(f"{self.name} realizou o empréstimo com sucesso.")

  def collect_book(self, client, book_title):
    found_book = None
    for book in self.collection:
      if book_title == book.title:
        found_book = book
        break
      else:
        print(f"O livro '{book_title}' não está disponível ou não existe.")
        break
    if found_book:
      client.return_book(found_book)
      found_book.status = True
    else:
      print(f"O cliente {client.name} não possui este livro.")
