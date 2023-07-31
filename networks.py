"""
Networks helpers
"""


def bit_stuffing(to_stuff):
    stuffing = ' 0 '
    stuffed = ''
    stuffing_count = 0
    for bit in to_stuff:
        if bit == '1':
            stuffing_count += 1
        else:
            stuffing_count = 0

        stuffed = stuffed + bit

        if stuffing_count == 5:
            stuffed = stuffed + stuffing
            stuffing_count = 0
    return stuffed


def ip_to_dotted_decimal(no_1):
    print(no_1, end='\t')
    ip = ''
    for _ in range(1, 32):
        if no_1 > 0:
            if _ % 8 == 0:
                ip += '1 '
            else:
                ip += '1'
        else:
            if _ % 8 == 0:
                ip += '0 '
            else:
                ip += '0'
        no_1 = no_1 - 1

    block = ip.split(' ')
    for blk in block:
        print(binaryToDecimal(int(blk)), end='.')
    print()
    print(block, type(block))


def ip_bin_to_dec(bin_ip):
    bin_ip = bin_ip.split(' . ')
    for bin_no in bin_ip:
        print(binaryToDecimal(int(bin_no)), end='.')
    print()


def binaryToDecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def not_vertex_set(vset, start=1, end=20):
    vset = sorted(vset)
    not_vset = []
    for i in range(start, end):
        if i not in vset:
            not_vset.append(i)
    return not_vset


if __name__ == '__main__':
    print(not_vertex_set([1, 20, 14, 7, 10, 13, 12]))
