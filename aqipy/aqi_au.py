# coding: utf-8

"""
    Australia AQI
    Source: https://www.legislation.gov.au/Details/F2016C00215
            https://www.environment.nsw.gov.au/topics/air/understanding-air-quality-data/air-quality-index
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __get_aqi_texts, __round_down

AU_AQI = ((0, 33), (34, 66), (67, 99), (100, 149), (150, 200), (201, 201))

AU_AQI_GENERAL = (
    "Enjoy normal activities",
    "Enjoy normal activities",
    "Adults are not likely to be affected when the AQI is in this range.",
    "Adults are not likely to be affected. Anyone who experiences symptoms should reduce outdoor activities.",
    "Adults should reduce or reschedule strenuous outdoor activities.",
    "Adults should avoid strenuous outdoor activities."
)
AU_AQI_RISK = (
    "Enjoy normal activities",
    "Enjoy normal activities",
    "People unusually sensitive to air pollution should reduce or reschedule strenuous outdoor activities.",
    "Sensitive groups should reduce strenuous outdoor activities.",
    "Sensitive groups should avoid strenuous outdoor activities.",
    "Sensitive groups should avoid all outdoor activities."
)
AU_CO_NEPM_STANDARD_8H = 9.0
AU_NO2_NEPM_STANDARD_1H = 0.12
AU_O3_NEPM_STANDARD_1H = 0.10
AU_O3_NEPM_STANDARD_4H = 0.08
AU_SO2_NEPM_STANDARD_24H = 0.20
AU_PM25_NEPM_STANDARD_24H = 25
AU_PM10_NEPM_STANDARD_24H = 50


def __get_aqi(cp: float, standard:float) -> (int, str, str):
    aqi = round(cp / standard * 100)
    if aqi > AU_AQI[-1][1]:
        aqi = AU_AQI[-1][1]
    text1, text2 = __get_aqi_texts(aqi, AU_AQI, AU_AQI_GENERAL, AU_AQI_RISK)
    return aqi, text1, text2


def get_aqi_o3_1h(o3_1h: float) -> (int, str, str):
    """
    Calculates O3 (1h) AU AQI

    :param o3_1h: O3 average (1h), ppm
    :return: O3 AU AQI, General message, Risk message
    """
    cp = __round_down(o3_1h, 2)
    return __get_aqi(cp, AU_O3_NEPM_STANDARD_1H)


def get_aqi_co_8h(co_8h: float) -> (int, str, str):
    """
    Calculates CO (8h) AU AQI

    :param co_8h: CO average (8h), ppm
    :return: CO AU AQI, General message, Risk message
    """
    cp = __round_down(co_8h, 1)
    return __get_aqi(cp, AU_CO_NEPM_STANDARD_8H)


def get_aqi_o3_4h(o3_4h: float) -> (int, str, str):
    """
    Calculates O3 (4h) AU AQI

    :param o3_4h: O3 average (4h), ppm
    :return: O3 AU AQI, General message, Risk message
    """
    cp = __round_down(o3_4h, 2)
    return __get_aqi(cp, AU_O3_NEPM_STANDARD_4H)


def get_aqi_no2_1h(no2_1h: float) -> (int, str, str):
    """
    Calculates NO2 (1h) AU AQI

    :param no2_1h: NO2 average (1h), ppm
    :return: NO2 AU AQI, General message, Risk message
    """
    cp = __round_down(no2_1h, 2)
    return __get_aqi(cp, AU_NO2_NEPM_STANDARD_1H)


def get_aqi_so2_24h(so2_24h: float) -> (int, str, str):
    """
    Calculates SO2 (24h) AU AQI

    :param so2_24h: SO2 average (1h), ppm
    :return: SO2 AU AQI, General message, Risk message
    """
    cp = __round_down(so2_24h, 2)
    return __get_aqi(cp, AU_SO2_NEPM_STANDARD_24H)


def get_aqi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) AU AQI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 AU AQI, General message, Risk message
    """
    cp = __round_down(pm25_24h)
    return __get_aqi(cp, AU_PM25_NEPM_STANDARD_24H)


def get_aqi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) AU AQI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 AU AQI, General message, Risk message
    """
    cp = __round_down(pm10_24h)
    return __get_aqi(cp, AU_PM10_NEPM_STANDARD_24H)


def get_aqi(o3_1h: float = None, o3_4h: float = None, co_8h: float = None,
            no2_1h: float = None, so2_24h: float = None, pm25_24h: float = None, pm10_24h: float = None) -> (int, {}):
    """
    Calculates AU AQI (Maximum from individual indexes)

    :param o3_1h: O3 average (1h), ppm
    :param o3_4h: O3 average (4h), ppm
    :param co_8h: CO average (8h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param so2_24h: SO2 average (24h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :return: AU AQI, dict with tuples (Individual aqi, General message, Risk message)
             keys are: o3_1h, o3_4h, co_8h, no2_1h, so2_24h, pm25_24h, pm10_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_1h:
        aqi_data['o3_1h'] = get_aqi_o3_1h(o3_1h)
    if o3_4h:
        aqi_data['o3_4h'] = get_aqi_o3_4h(o3_4h)
    if co_8h:
        aqi_data['co_8h'] = get_aqi_co_8h(co_8h)
    if no2_1h:
        aqi_data['no2_1h'] = get_aqi_no2_1h(no2_1h)
    if so2_24h:
        aqi_data['so2_24h'] = get_aqi_so2_24h(so2_24h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_aqi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_aqi_pm10_24h(pm10_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
