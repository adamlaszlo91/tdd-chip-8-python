class Ram:

    def __init__(self, size_in_bytes: int, read_only_area: range | None = None) -> None:
        self._bytes: bytes = bytes(size_in_bytes)
        self.read_only_area = read_only_area

    def write(self, address: int, data: bytes):
        if address < 0 or address >= len(self._bytes):
            raise ValueError("Invalid address.")
        if address + len(data) > len(self._bytes):
            raise ValueError("The data does not fit into memory.")

        if self.read_only_area:
            write_range = range(address, len(data))
            # De Morgan
            if (
                self.read_only_area.stop - 1 >= write_range.start
                and write_range.stop - 1 >= self.read_only_area.start
            ):
                raise ValueError("Cannot write to read only area.")
        self._bytes = self._bytes[0:address] + data + self._bytes[address + len(data) :]

    def read(self, address: int, count: int) -> bytes:
        if address < 0 or address >= len(self._bytes):
            raise ValueError("Invalid address.")
        if address + count > len(self._bytes):
            raise ValueError("Cannot read data; too long.")

        return self._bytes[address : address + count]

    def dump(self) -> bytes:
        return bytes(self._bytes)
