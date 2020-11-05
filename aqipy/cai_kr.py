# coding: utf-8

"""
    South Korea CAI
    Source: http://www.airkorea.or.kr/eng/khaiInfo?pMENU_NO=166
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula_texts

KR_CAI = ((0, 50), (51, 100), (101, 250), (251, 500))
KR_O3_1H = ((0, 0.03), (0.031, 0.09), (0.091, 0.15), (0.151, 0.6))
KR_CO_1H = ((0, 2), (2.01, 9), (9.01, 15), (15.01, 50))
KR_SO2_1H = ((0, 0.02), (0.021, 0.05), (0.051, 0.15), (0.151, 1))
KR_NO2_1H = ((0, 0.03), (0.031, 0.06), (0.061, 0.2), (0.201, 2))
KR_PM25_24H = ((0, 15), (16, 35), (36, 75), (76, 500))
KR_PM10_24H = ((0, 30), (31, 80), (81, 150), (151, 600))

KR_AQI_GENERAL = (
    "A level that will not impact patients suffering from diseases related to air pollution",
    "A level which may have a meager impact on patients in case of chronic exposure",
    "A level that may have harmful impacts on patients and members of sensitive groups (children, aged or weak people), and also cause the general public unpleasant feelings",
    "A level which may need to take emergency measures for patients and members of sensitive groups and have harmful impacts on the general public"
)


def get_cai_o3_1h(o3_1h: float) -> (int, str, str):
    """
    Calculates O3 (1h) South Korea CAI

    :param o3_1h: O3 average (1h), ppm
    :return: O3 South Korea CAI, General message, Risk message
    """
    cp = __round_down(o3_1h, 3)
    return __get_aqi_general_formula_texts(cp, KR_O3_1H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_cai_co_1h(co_1h: float) -> (int, str, str):
    """
    Calculates CO (1h) South Korea CAI

    :param co_1h: CO average (1h), ppm
    :return: CO South Korea CAI, General message, Risk message
    """
    cp = __round_down(co_1h, 2)
    return __get_aqi_general_formula_texts(cp, KR_CO_1H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_cai_so2_1h(so2_1h: float) -> (int, str, str):
    """
    Calculates SO2 (1h) South Korea CAI

    :param so2_1h: SO2 average (1h), ppm
    :return: SO2 South Korea CAI, General message, Risk message
    """
    cp = __round_down(so2_1h, 3)
    return __get_aqi_general_formula_texts(cp, KR_SO2_1H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_cai_no2_1h(no2_1h: float) -> (int, str, str):
    """
    Calculates NO2 (1h) South Korea CAI

    :param no2_1h: NO2 average (1h), ppm
    :return: NO2 South Korea CAI, General message, Risk message
    """
    cp = __round_down(no2_1h, 3)
    return __get_aqi_general_formula_texts(cp, KR_NO2_1H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_cai_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) South Korea CAI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 South Korea CAI, General message, Risk message
    """
    cp = __round_down(pm25_24h)
    return __get_aqi_general_formula_texts(cp, KR_PM25_24H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_cai_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) South Korea CAI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 South Korea CAI, General message, Risk message
    """
    cp = __round_down(pm10_24h)
    return __get_aqi_general_formula_texts(cp, KR_PM10_24H, KR_AQI_GENERAL, KR_AQI_GENERAL, KR_CAI)


def get_aqi(o3_1h: float = None, co_1h: float = None, so2_1h: float = None, no2_1h: float = None,
            pm25_24h: float = None, pm10_24h: float = None) -> (int, {}):
    """
    Calculates South Korea CAI (Maximum from individual indexes)

    :param o3_1h: O3 average (1h), ppm
    :param co_1h: CO average (1h), ppm
    :param so2_1h: SO2 average (1h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :return: South Korea CAI, dict with tuples (Individual aqi, General message, Risk message)
             keys are: o3_1h, co_1h, so2_1h, no2_1h, pm25_24h, pm10_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_1h:
        aqi_data['o3_1h'] = get_cai_o3_1h(o3_1h)
    if co_1h:
        aqi_data['co_1h'] = get_cai_co_1h(co_1h)
    if so2_1h:
        aqi_data['so2_1h'] = get_cai_so2_1h(so2_1h)
    if no2_1h:
        aqi_data['no2_1h'] = get_cai_no2_1h(no2_1h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_cai_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_cai_pm10_24h(pm10_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
