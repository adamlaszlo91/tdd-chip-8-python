from ram import Ram
from pytest import raises
from pytest_mock.plugin import MockerFixture


def test_initialization(mocker: MockerFixture):
    size_in_bytes = 5000
    ram = Ram(size_in_bytes=size_in_bytes)
    assert ram.dump() == bytes(size_in_bytes)


def test_write(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    ram.write(address=1, data=b"\x01\x02")
    assert ram.dump() == b"\x00\x01\x02\x00\x00"


def test_write_too_long_data(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="The data does not fit into memory."):
        ram.write(address=1, data=b"\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02")


def test_write_too_small_address(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="Invalid address."):
        ram.write(address=-1, data=b"\x01\x02")


def test_write_too_large_address(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="Invalid address."):
        ram.write(address=100, data=b"\x01\x02")


def test_write_empty(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    ram.write(address=1, data=b"")
    assert ram.dump() == b"\x00\x00\x00\x00\x00"


def test_write_on_read_only_area(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes, read_only_area=range(3))
    with raises(ValueError, match="Cannot write to read only area."):
        ram.write(address=1, data=b"\x01\x02")


def test_write_on_read_only_area_partially(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes, read_only_area=range(1))
    with raises(ValueError, match="Cannot write to read only area."):
        ram.write(address=0, data=b"\x01\x02")


def test_write_outside_of_read_only_area(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes, read_only_area=range(1))
    ram.write(address=2, data=b"\x01\x02")


def test_read(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    ram.write(address=1, data=b"\x01\x02")
    assert ram.read(address=1, count=2) == b"\x01\x02"


def test_read_too_long_data(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="Cannot read data; too long."):
        ram.read(address=1, count=200)


def test_read_too_small_address(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="Invalid address."):
        ram.read(address=-1, count=1)


def test_read_too_large_address(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    with raises(ValueError, match="Invalid address."):
        ram.read(address=100, count=1)


def test_read_empty(mocker: MockerFixture):
    size_in_bytes = 5
    ram = Ram(size_in_bytes=size_in_bytes)
    assert ram.read(address=0, count=0) == b""
