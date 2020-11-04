# coding: utf-8

"""
    CAQI Europe
    Source: https://www.airqualitynow.eu/download/CITEAIR-Comparing_Urban_Air_Quality_across_Borders.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula

EU_CAQI = ((0, 24), (25, 49), (50, 74), (75, 99), (100, 100))
EU_NO2_1H = ((0, 26), (27, 52), (53, 105), (106, 212), (213, 213))
EU_PM10_1H = ((0, 24), (25, 49), (50, 89), (90, 179), (180, 180))
EU_PM10_24H = ((0, 14), (15, 29), (30, 49), (50, 99), (100, 100))
EU_PM25_1H = ((0, 14), (15, 29), (30, 54), (55, 109), (110, 110))
EU_PM25_24H = ((0, 9), (10, 19), (20, 29), (30, 59), (60, 60))
EU_O3_1H = ((0, 29), (30, 59), (60, 89), (90, 119), (120, 120))
EU_CO_8H = ((0.0, 4.3), (4.4, 6.5), (6.6, 8.6), (8.7, 17.4), (17.5, 17.5))
EU_SO2_1H = ((0, 18), (19, 37), (38, 133), (134, 190), (191, 191))


def get_caqi_no2_1h(no2_1h: float) -> float:
    """
    Calculates NO2 (1h) CAQI Europe

    :param no2_1h: NO2 (1h), ppm
    :return: NO2 CAQI Europe
    """
    cp = __round_down(no2_1h * 1000)
    return __get_aqi_general_formula(cp, EU_NO2_1H, EU_CAQI)


def get_caqi_so2_1h(so2_1h: float) -> float:
    """
    Calculates SO2 (1h) CAQI Europe

    :param so2_1h: SO2 (1h), ppm
    :return: SO2 CAQI Europe
    """
    cp = __round_down(so2_1h * 1000)
    return __get_aqi_general_formula(cp, EU_SO2_1H, EU_CAQI)


def get_caqi_o3_1h(o3_1h: float) -> float:
    """
    Calculates O3 (1h) CAQI Europe

    :param o3_1h: O3 (1h), ppm
    :return: O3 CAQI Europe
    """
    cp = __round_down(o3_1h * 1000)
    return __get_aqi_general_formula(cp, EU_O3_1H, EU_CAQI)


def get_caqi_co_1h(co_8h: float) -> float:
    """
    Calculates CO (8h) CAQI Europe

    :param co_8h: CO (8h), ppm
    :return: CO CAQI Europe
    """
    cp = __round_down(co_8h, 1)
    return __get_aqi_general_formula(cp, EU_CO_8H, EU_CAQI)


def get_caqi_pm25_1h(pm25_1h: float) -> float:
    """
    Calculates PM2.5 (1h) CAQI Europe

    :param pm25_1h: PM2.5 (1h), µg/m3
    :return: PM2.5 CAQI Europe
    """
    cp = __round_down(pm25_1h)
    return __get_aqi_general_formula(cp, EU_PM25_1H, EU_CAQI)


def get_caqi_pm25_24h(pm25_24h: float) -> float:
    """
    Calculates PM2.5 (24h) CAQI Europe

    :param pm25_24h: PM2.5 (24h), µg/m3
    :return: PM2.5 CAQI Europe
    """
    cp = __round_down(pm25_24h)
    return __get_aqi_general_formula(cp, EU_PM25_24H, EU_CAQI)


def get_caqi_pm10_1h(pm10_1h: float) -> float:
    """
    Calculates PM10 (1h) CAQI Europe

    :param pm10_1h: PM10 (1h), µg/m3
    :return: PM10 CAQI Europe
    """
    cp = __round_down(pm10_1h)
    return __get_aqi_general_formula(cp, EU_PM10_1H, EU_CAQI)


def get_caqi_pm10_24h(pm10_24h: float) -> float:
    """
    Calculates PM10 (24h) CAQI Europe

    :param pm10_24h: PM10 (24h), µg/m3
    :return: PM10 CAQI Europe
    """
    cp = __round_down(pm10_24h)
    return __get_aqi_general_formula(cp, EU_PM10_24H, EU_CAQI)


def get_caqi(co_1h: float = None, o3_1h: float = None, no2_1h: float = None, pm25_24h: float = None,
             pm25_1h: float = None, pm10_1h: float = None, pm10_24h: float = None, so2_1h: float = None) -> (int, {}):
    """
    Calculates CAQI Europe (Maximum from individual indexes)

    :param co_1h: CO average (1h), ppm
    :param o3_1h: O3 average (1h), ppm
    :param o3_8h: O3 average (8h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param pm25_1h: PM2.5 average (1h), μg/m3
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_1h: PM10 average (1h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :param so2_1h: SO2 average (1h), ppm
    :return: US AQI, dict with aqi values
            keys are: no2_1h, so2_1h, o3_1h, co_1h, pm25_1h, pm25_24h, pm10_1h, pm10_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if no2_1h:
        aqi_data['no2_1h'] = get_caqi_no2_1h(no2_1h)
    if so2_1h:
        aqi_data['so2_1h'] = get_caqi_so2_1h(so2_1h)
    if o3_1h:
        aqi_data['o3_1h'] = get_caqi_o3_1h(o3_1h)
    if co_1h:
        aqi_data['co_1h'] = get_caqi_co_1h(co_1h)
    if pm25_1h:
        aqi_data['pm25_1h'] = get_caqi_pm25_1h(pm25_1h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_caqi_pm25_24h(pm25_24h)
    if pm10_1h:
        aqi_data['pm10_1h'] = get_caqi_pm10_1h(pm10_1h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_caqi_pm10_24h(pm10_24h)
    if so2_1h:
        aqi_data['so2_1h'] = get_caqi_so2_1h(so2_1h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x, aqi_data.values()))), aqi_data
