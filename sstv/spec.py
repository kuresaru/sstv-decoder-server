"""Constants for SSTV specification and each supported mode"""

from enum import Enum


class COL_FMT(Enum):
    RGB = 1
    GBR = 2
    YUV = 3
    BW = 4


class M1(object):
    NAME = "Martin 1"

    COLOR = COL_FMT.GBR
    LINE_WIDTH = 320
    LINE_COUNT = 256
    SCAN_TIME = 0.146432
    SYNC_PULSE = 0.004862
    SYNC_PORCH = 0.000572
    SEP_PULSE = 0.000572

    CHAN_COUNT = 3
    CHAN_SYNC = 0
    CHAN_TIME = SEP_PULSE + SCAN_TIME

    CHAN_OFFSETS = [SYNC_PULSE + SYNC_PORCH]
    CHAN_OFFSETS.append(CHAN_OFFSETS[0] + CHAN_TIME)
    CHAN_OFFSETS.append(CHAN_OFFSETS[1] + CHAN_TIME)

    LINE_TIME = SYNC_PULSE + SYNC_PORCH + 3 * CHAN_TIME
    PIXEL_TIME = SCAN_TIME / LINE_WIDTH
    WINDOW_FACTOR = 2.34

    HAS_START_SYNC = False
    HAS_MERGE_SCAN = False


class S1(object):
    NAME = "Scottie 1"

    COLOR = COL_FMT.GBR
    LINE_WIDTH = 320
    LINE_COUNT = 256
    SCAN_TIME = 0.138240
    SYNC_PULSE = 0.009000
    SYNC_PORCH = 0.001500
    SEP_PULSE = 0.001500

    CHAN_COUNT = 3
    CHAN_SYNC = 2
    CHAN_TIME = SEP_PULSE + SCAN_TIME

    CHAN_OFFSETS = [SYNC_PULSE + SYNC_PORCH + CHAN_TIME]
    CHAN_OFFSETS.append(CHAN_OFFSETS[0] + CHAN_TIME)
    CHAN_OFFSETS.append(SYNC_PULSE + SYNC_PORCH)

    LINE_TIME = SYNC_PULSE + 3 * CHAN_TIME
    PIXEL_TIME = SCAN_TIME / LINE_WIDTH
    WINDOW_FACTOR = 2.48

    HAS_START_SYNC = True
    HAS_MERGE_SCAN = False


class R36(object):
    NAME = "Robot 36"

    COLOR = COL_FMT.YUV
    LINE_WIDTH = 320
    LINE_COUNT = 240
    SCAN_TIME = 0.088000
    MERGE_SCAN_TIME = 0.044000
    SYNC_PULSE = 0.009000
    SYNC_PORCH = 0.003000
    SEP_PULSE = 0.004500
    SEP_PORCH = 0.001500

    CHAN_COUNT = 2
    CHAN_SYNC = 0
    CHAN_TIME = SEP_PULSE + SCAN_TIME

    CHAN_OFFSETS = [SYNC_PULSE + SYNC_PORCH]
    CHAN_OFFSETS.append(CHAN_OFFSETS[0] + CHAN_TIME + SEP_PORCH)

    LINE_TIME = CHAN_OFFSETS[1] + MERGE_SCAN_TIME
    PIXEL_TIME = SCAN_TIME / LINE_WIDTH
    MERGE_PIXEL_TIME = MERGE_SCAN_TIME / LINE_WIDTH
    WINDOW_FACTOR = 7.83

    HAS_START_SYNC = False
    HAS_MERGE_SCAN = True


VIS_MAP = {44: M1, 60: S1, 8: R36}

BREAK_OFFSET = 0.300
LEADER_OFFSET = 0.010 + BREAK_OFFSET
VIS_START_OFFSET = 0.300 + LEADER_OFFSET

HDR_SIZE = 0.030 + VIS_START_OFFSET
HDR_WINDOW_SIZE = 0.010

VIS_BIT_SIZE = 0.030