from __future__ import print_function

import logging

import grpc
import book_pb2
import book_pb2_grpc


def run():
    print("Will try to get a book ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookStub(channel)
        tryCreateBook(stub)
        tryGetBook(stub)


def tryCreateBook(book_stub):
    response = book_stub.CreateBook(book_pb2.CreateBookRequest(isbn="ab123", title="testBook", author="testAuthor",
                                                               genre=book_pb2.HORROR, publishingYear=2023))
    if not response.created:
        print("Book is not created. Reason: %s." % response.message)
    else:
        print("Book creation success!")


def tryGetBook(book_stub):
    response = book_stub.GetBook(book_pb2.GetBookRequest(isbn="ab123"))
    if response.found:
        book_info = response.bookInfo
        print("Found book with title %s and author %s." % (book_info.title, book_info.author))
        print(book_info.genre)
    else:
        print("Book not found!")


if __name__ == '__main__':
    logging.basicConfig()
    run()
