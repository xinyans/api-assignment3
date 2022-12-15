import unittest
from unittest.mock import MagicMock

import grpc

import book_pb2
import book_pb2_grpc
from get_book_titles import get_book_titles
from inventory_client import InventoryClient


class TestMockGetBookTitles(unittest.TestCase):

    def setUp(self) -> None:
        channel = grpc.insecure_channel('localhost:50051')
        mock_stub = book_pb2_grpc.BookStub(channel)
        self.mock_client = InventoryClient.instance_from_predefined_stub(mock_stub)
        self.mock_client.create_book = MagicMock(return_value=True)
        self.mock_client.get_book = MagicMock(return_value=book_pb2.BookInfo(title="mock_title"))

    def testValidInput(self):
        get_result = get_book_titles(self.mock_client, ["a1", "a2"])
        assert len(get_result) == 2

    def testNoInput(self):
        get_result = get_book_titles(self.mock_client, [])
        assert len(get_result) == 0


class TestLiveGetBookTitles(unittest.TestCase):
    def setUp(self) -> None:
        self.client = InventoryClient.instance_by_default()

    def testValidInput(self):
        get_result = get_book_titles(self.client, ["ab12", "ef56"])
        assert len(get_result) == 2

    def testNoInput(self):
        get_result = get_book_titles(self.client, [])
        assert len(get_result) == 0


if __name__ == '__main__':
    unittest.main()
