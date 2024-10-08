import enum


class InvalidFormatError(Exception):
    pass


class RespEnum(enum.Enum):
    SIMPLE = "SIMPLE_STRING"
    ERROR = "ERROR"
    INTEGER = "INTEGER"
    BULK = "BULK_STRING"
    ARRAY = "ARRAY"
    NULL = "NULL"
    BOOLEAN = "BOOLEAN"


class RespHandler:
    def determine_first_byte(input: bytes) -> str:
        if input[:1] == b"+":
            return RespEnum.SIMPLE.value
        if input[:1] == b"-":
            return RespEnum.ERROR.value
        if input[:1] == b":":
            return RespEnum.INTEGER.value
        if input[:1] == b"$":
            return RespEnum.BULK.value
        if input[:1] == b"*":
            return RespEnum.ARRAY.value
        if input[:1] == b"_":
            return RespEnum.NULL.value
        if input[:1] == b"#":
            return RespEnum.BOOLEAN.value

        raise InvalidFormatError("Invalid message. Cannot define data type.")
