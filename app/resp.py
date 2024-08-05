import enum


class InvalidFormatError(Exception):
    pass


class RespEnum(enum.Enum):
    SIMPLE = "SIMPLE_STRING"
    ERROR = "ERROR"
    INTEGER = "INTEGER"
    BULK = "BULK_STRING"
    ARRAY = "ARRAY"


class RespHandler:
    def deserialize(input: str) -> str:
        pass

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

        raise InvalidFormatError("Byte array should start by +, -, :, $ or *.")
