from device import Device
from pytest_mock.plugin import MockerFixture

# TODO: SYS


def test_cls(mocker: MockerFixture):
    mock_display = mocker.Mock()
    device = Device(display=mock_display)
    device.run(program=b"\x00\xe0", instruction_limit=1)
    assert mock_display.clear.called


def test_ret(mocker: MockerFixture):
    device = Device(display=mocker.Mock())
    device.run(program=b"\x22\x02\x00\xee", instruction_limit=2)
    assert device._program_counter == b"\x02\x00"
    assert device._stack_pointer == b"\x00"


def test_jp(mocker: MockerFixture):
    device = Device(display=mocker.Mock())
    device.run(program=b"\x11\x23", instruction_limit=1)
    assert device._program_counter == b"\x01\x23"


def test_call(mocker: MockerFixture):
    device = Device(display=mocker.Mock())
    device.run(program=b"\x21\x23", instruction_limit=1)
    assert device._stack_pointer == b"\x01"
    assert device._stack[device._stack_pointer[0]] == b"\x02\x00"
    assert device._program_counter == b"\x01\x23"


def test_se_equals(mocker: MockerFixture):
    device = Device(display=mocker.Mock())
    device.run(program=b"\x32\x00", instruction_limit=1)
    assert device._program_counter == b"\x02\x02"


def test_se_not_equals(mocker: MockerFixture):
    device = Device(display=mocker.Mock())
    device.run(program=b"\x32\x01", instruction_limit=1)
    assert device._program_counter == b"\x02\x00"
