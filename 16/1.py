#!/usr/bin/python3

class Packet:
    def __init__(self, str, is_hex=False, do_parse=True):
        if is_hex:
            self.hex = str
            self.bin = self.lpad(bin(int('1' + self.hex, 16))[3:])
        else:
            self.bin = str
            self.hex = hex(int(str, 2))[2:]

        self.version = None
        self.type_id = None
        self.value = None
        self.subs = None

        if do_parse:
            self.version, self.type_id, self.value, self.subs, _, _ = self.parse(self.bin)

    def __str__(self):
        return self.bin

    def __eq__(self, other):
        return self.bin == other.bin

    def __bool__(self):
        return len(self.hex) > 0

    def lpad(self, b):
        while len(b) % 4 != 0:
            b = '0' + b
        return b

    def parse(self, b):
        version = int(b[:3], 2)
        type_id = int(b[3:6], 2)
        value = None
        subs = None

        cp = 6  # current pointer, after header
        if type_id == 4:
            value = ""
            while True:
                group_indicator = b[cp:cp + 1]
                value += b[cp + 1:cp + 5]
                cp += 5
                if group_indicator == '0': break

            value = int(value, 2)
        else:
            subs = []
            length_type_id = int(b[cp:cp + 1], 2)
            cp = 7

            sub_packets_length = None
            sub_packets_count = None
            packets_read = 0

            if length_type_id == 0:
                sub_packets_length = int(b[cp:cp + 15] or '0', 2)
                if sub_packets_length <= 0: return None, None, None, None, None, None
                cp += 15
            elif length_type_id == 1:
                sub_packets_count = int(b[cp:cp + 11], 2)
                if sub_packets_count <= 0: return None, None, None, None, None, None
                cp += 11

            while True:
                if length_type_id == 0 and sub_packets_length is not None:
                    if cp >= 7 + 15 + sub_packets_length:
                        break
                elif length_type_id == 1 and packets_read is not None and sub_packets_count is not None:
                    if packets_read >= sub_packets_count:
                        break

                sub_version, sub_type_id, sub_value, sub_subs, sub_cp, sub_b = self.parse(b[cp:])
                cp += sub_cp if sub_cp is not None else 0
                packets_read += 1

                if sub_b:
                    np = Packet(sub_b, False, False)
                    np.version = sub_version
                    np.type_id = sub_type_id
                    np.value = sub_value
                    np.subs = sub_subs
                    subs.append(np)

        return version, type_id, value, subs, cp, b

    def version_sum(self):
        return self.version if self.subs is None else self.version + sum([s.version_sum() for s in self.subs])


def test():
    examples = [(line.strip().split(":")[0], int(line.strip().split(":")[1])) for line in
                open("input_example").readlines()]

    for example, version_sum in examples:
        p = Packet(example, True)
        print("Test %s\n%s: Expected: %s - Got: %s" % (
            example,
            f"\033[1m\033[92mPASS\033[0m" if version_sum == p.version_sum() else f"\033[1m\033[91mFAIL\033[0m",
            version_sum,
            p.version_sum()
        ), end="\n\n")


# test()

p = Packet(open("input").read().strip(), True)
print(p.version_sum())