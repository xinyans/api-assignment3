import grpc
import book_pb2
import book_pb2_grpc
from book_db import BookDB, Book, Genre

import logging
from concurrent import futures


def genre_enum_to_proto_enum(genre):
    if genre == Genre.SCIFI:
        return book_pb2.SCIFI
    elif genre == Genre.HORROR:
        return book_pb2.HORROR
    elif genre == Genre.UNDEFINED:
        return book_pb2.UNDEFINED
    elif genre == Genre.FANTASY:
        return book_pb2.FANTASY
    elif genre == Genre.MYSTERY:
        return book_pb2.MYSTERY
    else:
        return None


def proto_enum_to_genre_enum(genre):
    if genre == book_pb2.SCIFI:
        return Genre.SCIFI
    elif genre == book_pb2.HORROR:
        return Genre.HORROR
    elif genre == book_pb2.UNDEFINED:
        return Genre.UNDEFINED
    elif genre == book_pb2.FANTASY:
        return Genre.FANTASY
    elif genre == book_pb2.MYSTERY:
        return Genre.MYSTERY
    else:
        return None


class InventoryServer(book_pb2_grpc.BookServicer):
    def __init__(self):
        super().__init__()
        self.book_db = BookDB()

    def GetBook(self, request, context):
        print("Received request for book %s." % request.isbn)
        book = self.book_db.get_book_by_isbn(request.isbn)
        if not book:
            print("Book not found. Returning false result.")
            return book_pb2.GetBookResponse(found=False)
        else:
            print("Book found. Returning the book.")
            genre_proto = genre_enum_to_proto_enum(book.genre)
            book_info = book_pb2.BookInfo(isbn=book.isbn, title=book.title, author=book.author, genre=genre_proto,
                                          publishingYear=book.pub_year)
            return book_pb2.GetBookResponse(found=True, bookInfo=book_info)

    def CreateBook(self, request, context):
        print("Received request to create book %s by %s." % (request.title, request.author))
        if not request.isbn:
            return book_pb2.CreateBookResponse(created=False, message="You need to provide an isbn.")
        book = self.book_db.get_book_by_isbn(request.isbn)
        if book:
            return book_pb2.CreateBookResponse(created=False, message="A book with this isbn already exists.")
        new_book = Book(request.isbn, request.title, request.author,
                        proto_enum_to_genre_enum(request.genre), request.publishingYear)
        self.book_db.add_book(new_book)
        return book_pb2.CreateBookResponse(created=True)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServicer_to_server(InventoryServer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
