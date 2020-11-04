import math

AQI_NOT_AVAILABLE = -1
AQI_MIN = -1


def __get_aqi_texts(aqi: int, aqi_a: [], a1: [], a2: []) -> (str, str):
    for i in range(len(aqi_a)):
        if aqi_a[i][0] <= aqi <= aqi_a[i][1]:
            return a1[i], a2[i]
    return "", ""


def __round_down(n, decimals=0) -> float:
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def __get_index_data(val: float, array: [[]], max_aqi: int, aqi_a: []) -> (int, [], []):
    for i in range(len(array)):
        if array[i][0] <= val <= array[i][1]:
            if max_aqi <= aqi_a[i][1]:
                return len(aqi_a), aqi_a[i], array[i]
            return i, aqi_a[i], array[i]
        elif val < array[i][0]:
            return AQI_MIN, aqi_a[0], array[0]
    return len(aqi_a), aqi_a[-1], array[-1]


def __get_aqi_general_formula(cp: float, av: [], aqi_a: [], max_aqi: int = 0) -> int:
    if max_aqi == 0:
        max_aqi = aqi_a[-1][1]
    t, i, bp = __get_index_data(cp, av, max_aqi, aqi_a)
    if t == len(aqi_a):
        return max_aqi
    elif t == AQI_MIN:
        return 0
    aqi = round((i[1] - i[0]) / (bp[1] - bp[0]) * (cp - bp[0]) + i[0])
    return aqi


def __get_aqi_general_formula_texts(cp: float, av: [], a1: [], a2: [], aqi_a: [], max_aqi: int = 0) -> (int, str, str):
    if max_aqi == 0:
        max_aqi = aqi_a[-1][1]
    t, i, bp = __get_index_data(cp, av, max_aqi, aqi_a)
    if t == len(aqi_a):
        text1, text2 = __get_aqi_texts(max_aqi, aqi_a, a1, a2)
        return max_aqi, text1, text2
    elif t == AQI_MIN:
        return 0, a1[0], a2[0]
    aqi = round((i[1] - i[0]) / (bp[1] - bp[0]) * (cp - bp[0]) + i[0])
    text1, text2 = __get_aqi_texts(aqi, aqi_a, a1, a2)
    return aqi, text1, text2


def __added_risk(beta, c):
    ar = math.expm1(beta * float(c)) * 100.0
    return ar
