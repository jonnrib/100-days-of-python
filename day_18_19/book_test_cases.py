from day_17.library_class import *

# Registrtar livro
tolkien = Book("The Lord of the Rings", "J. R. R. Tolkien", "9780007527617", "Fantasy")
austen = Book("Pride and Prejudice", "Jane Austen", "9780140439516", "Classic Fiction")

# Registrar usuário
john = Client(1, "John")

# Registrar bibliotecária
biblioteca = Librarian("Maria")

# Adicionar clientes
biblioteca.add_clients(john)

# Ver clientes
biblioteca.show_clients()

# Adicionar livro ao acervo
biblioteca.add_to_collection(tolkien)
biblioteca.add_to_collection(austen)

# Ver acervo
biblioteca.show_collection()

# Emprestar pela biblioteca
biblioteca.lent_book(john, "The Lord of the Rings")

# Ver status do livro
print(tolkien)

# Mostrar livro
john.show_books(tolkien)

# Remover o livro
biblioteca.collect_book(john, "The Lord of the Rings")
