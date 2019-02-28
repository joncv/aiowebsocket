from itertools import cycle

DATA_CODE = CONT, TEXT, BINARY = 0x00, 0x01, 0x02
CTRL_CODE = CLOSE, PING, PONG = 0x08, 0x09, 0x0A


def apply_mask(data, mask):
    """Apply masking to websocket message.
    """
    if len(mask) != 4:
        raise ValueError("mask must contain 4 bytes")
    return bytes(b ^ m for b, m in zip(data, cycle(mask)))
