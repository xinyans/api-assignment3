from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FANTASY: Genre
HORROR: Genre
MYSTERY: Genre
SCIFI: Genre
UNDEFINED: Genre

class BookInfo(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishingYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    publishingYear: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishingYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    publishingYear: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class CreateBookResponse(_message.Message):
    __slots__ = ["created", "message"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    created: bool
    message: str
    def __init__(self, created: bool = ..., message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["bookInfo", "found", "message"]
    BOOKINFO_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    bookInfo: BookInfo
    found: bool
    message: str
    def __init__(self, found: bool = ..., message: _Optional[str] = ..., bookInfo: _Optional[_Union[BookInfo, _Mapping]] = ...) -> None: ...

class GetInventoryRequest(_message.Message):
    __slots__ = ["inventoryNumber"]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    inventoryNumber: int
    def __init__(self, inventoryNumber: _Optional[int] = ...) -> None: ...

class GetInventoryResponse(_message.Message):
    __slots__ = ["found", "inventoryItem", "message"]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    INVENTORYITEM_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    found: bool
    inventoryItem: InventoryItem
    message: str
    def __init__(self, found: bool = ..., message: _Optional[str] = ..., inventoryItem: _Optional[_Union[InventoryItem, _Mapping]] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNumber"]
    class status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.status
    book: BookInfo
    inventoryNumber: int
    def __init__(self, inventoryNumber: _Optional[int] = ..., book: _Optional[_Union[BookInfo, _Mapping]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
