from __future__ import print_function

import logging

import grpc
import book_pb2 as book_pb2
import book_pb2_grpc as book_pb2_grpc


def run():
    print("Will try to get a book ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookStub(channel)
        client = InventoryClient(stub)
        tryCreateBook(client)
        tryGetBook(client)


def tryCreateBook(client):
    created = client.create_book("ab123", "testBook", "testAuthor", book_pb2.HORROR, 2023)
    if not created:
        print("Book is not created.")
    else:
        print("Book creation success!")


def tryGetBook(client):
    book_info = client.get_book("ab123")
    if book_info:
        print("Found book with title %s and author %s." % (book_info.title, book_info.author))
        print(book_info.genre)
    else:
        print("Book not found!")


class InventoryClient:
    def __init__(self, stub):
        self.stub = stub

    @classmethod
    def instance_from_predefined_stub(cls, stub):
        return cls(stub)

    @classmethod
    def instance_by_default(cls):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = book_pb2_grpc.BookStub(channel)
            return cls(stub)

    def get_book(self, isbn):
        response = self.stub.GetBook(book_pb2.GetBookRequest(isbn=isbn))
        if response.found:
            return response.bookInfo
        else:
            return None

    def create_book(self, isbn, title, author, genre, pub_year):
        response = self.stub.CreateBook(book_pb2.CreateBookRequest(isbn=isbn, title=title, author=author,
                                                                   genre=genre, publishingYear=pub_year))
        return response.created


if __name__ == '__main__':
    logging.basicConfig()
    run()
