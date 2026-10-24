from display import Display
from ram import Ram


class Device:

    _ram = Ram(size_in_bytes=4096, read_only_area=range(512))
    _stack: list[bytes] = [bytes(2)] * 16
    _register_v_list: list[bytes] = [bytes(1)] * 16
    _register_i: bytes = bytes(2)
    _register_delay_timer: bytes = bytes(1)
    _register_sound_timer: bytes = bytes(1)
    _program_counter: bytes = bytes(2)
    _stack_pointer: bytes = bytes(1)

    def __init__(self, display: Display) -> None:
        self._display = display
        self._program_counter = b"\x02\x00"

    def run(self, program: bytes, instruction_limit: int | None = None):
        self._ram.write(512, program)

        instruction_count = 0
        while True:
            if instruction_limit:
                if instruction_count >= instruction_limit:
                    return
                else:
                    instruction_count += 1

            instruction = self._ram.read(
                self._program_counter[0] * 256 + self._program_counter[1], 2
            )
            print(instruction)

            if (instruction[0] >> 4).to_bytes() == b"\x00":
                if instruction == b"\x00\xe0":
                    # CLS
                    self._display.clear()
                elif instruction == b"\x00\xee":
                    self._program_counter = self._stack[self._stack_pointer[0]]
                    self._stack_pointer = (self._stack_pointer[0] - 1).to_bytes()
                else:
                    # TODO
                    # SYS
                    pass
            elif (instruction[0] >> 4).to_bytes() == b"\x01":
                # JP
                self._program_counter = (instruction[0] % 16).to_bytes() + instruction[
                    1
                ].to_bytes()
            elif (instruction[0] >> 4).to_bytes() == b"\x02":
                # CALL
                self._stack_pointer = (self._stack_pointer[0] + 1).to_bytes()
                self._stack[self._stack_pointer[0]] = self._program_counter
                self._program_counter = (instruction[0] % 16).to_bytes() + instruction[
                    1
                ].to_bytes()
            elif (instruction[0] >> 4).to_bytes() == b"\x03":
                # SE
                vx = instruction[0] % 16
                if self._register_v_list[vx][0] == instruction[1]:
                    self._program_counter = (
                        (self._program_counter[0] * 256) + self._program_counter[1] + 2
                    ).to_bytes(2)
            else:
                return
