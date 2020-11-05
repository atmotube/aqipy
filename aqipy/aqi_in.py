# coding: utf-8

"""
    India AQI
    Source: http://www.indiaenvironmentportal.org.in/files/file/Air%20Quality%20Index.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula_texts

IN_AQI = ((0, 50), (51, 100), (101, 250), (251, 350), (351, 400), (401, 500))
IN_AQI_EFFECTS = (
    "Minimal impact",
    "May cause minor breathing discomfort to sensitive people.",
    "May cause breathing discomfort to people with lung disease such as asthma, and discomfort to people with heart disease, children and older adults.",
    "May cause breathing discomfort to people on prolonged exposure, and discomfort to people with heart disease.",
    "May cause respiratory illness to the people on prolonged exposure. Effect may be more pronounced in people with lung and heart diseases.",
    "May cause respiratory impact even on healthy people, and serious health impacts on people with lung/heart disease. The health impacts may be experienced even during light physical activity."
)

IN_PM10_24H = ((0, 50), (51, 100), (101, 250), (251, 350), (351, 429), (430, 430))
IN_PM25_24H = ((0, 30), (31, 60), (61, 90), (91, 120), (121, 249), (250, 250))
IN_NO2_24H = ((0, 21), (22, 42), (43, 95), (96, 148), (149, 212), (213, 213))
IN_O3_8H = ((0, 25), (26, 50), (51, 84), (85, 104), (105, 373), (374, 374))
IN_CO_8H = ((0.0, 0.9), (1.0, 1.7), (1.8, 8.6), (8.7, 14.7), (14.8, 29.6), (29.7, 29.7))
IN_SO2_24H = ((0, 15), (16, 30), (31, 144), (145, 305), (306, 610), (611, 611))
IN_NH3_24H = ((0, 287), (288, 574), (575, 1148), (1149, 1721), (1722, 2581), (2582, 2582))
IN_PB_24H = ((0.000, 0.058), (0.059, 0.129), (0.130, 0.247), (0.248, 0.365), (0.366, 0.412), (0.413, 0.413))


def get_aqi_o3_8h(o3_8h: float) -> (int, str, str):
    """
    Calculates O3 India AQI

    :param o3_8h: O3 average (8h), ppm
    :return: O3 India AQI, Effect message, Caution message
    """
    cp = __round_down(o3_8h * 1000)
    return __get_aqi_general_formula_texts(cp, IN_O3_8H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_co_8h(co_8h: float) -> (int, str, str):
    """
    Calculates CO India AQI

    :param co_8h: CO average (8h), ppm
    :return: CO India AQI, Effect message, Caution message
    """
    cp = __round_down(co_8h, 1)
    return __get_aqi_general_formula_texts(cp, IN_CO_8H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_no2_24h(no2_24h: float) -> (int, str, str):
    """
    Calculates NO2 India AQI

    :param no2_24h: NO2 average (24h), ppm
    :return: NO2 India AQI, Effect message, Caution message
    """
    cp = __round_down(no2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, IN_NO2_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_so2_24h(so2_24h: float) -> (int, str, str):
    """
    Calculates SO2 India AQI

    :param so2_24h: SO2 average (24h), ppm
    :return: SO2 India AQI, Effect message, Caution message
    """
    cp = __round_down(so2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, IN_SO2_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_nh3_24h(nh3_24h: float) -> (int, str, str):
    """
    Calculates NH3 India AQI

    :param nh3_24h: NH3 average (24h), ppm
    :return: NH3 India AQI, Effect message, Caution message
    """
    cp = __round_down(nh3_24h * 1000)
    return __get_aqi_general_formula_texts(cp, IN_NH3_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_pb_24h(pb_24h: float) -> (int, str, str):
    """
    Calculates Pb India AQI

    :param pb_24h: Pb average (24h), ppm
    :return: Pb India AQI, Effect message, Caution message
    """
    cp = __round_down(pb_24h * 1000, 3)
    return __get_aqi_general_formula_texts(cp, IN_PB_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 India AQI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 India AQI, Effect message, Caution message
    """
    cp = __round_down(pm25_24h)
    return __get_aqi_general_formula_texts(cp, IN_PM25_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 India AQI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 India AQI, Effect message, Caution message
    """
    cp = __round_down(pm10_24h)
    return __get_aqi_general_formula_texts(cp, IN_PM10_24H, IN_AQI_EFFECTS, IN_AQI_EFFECTS, IN_AQI)


def get_aqi(o3_8h: float = None, co_8h: float = None, pm25_24h: float = None,
            pm10_24h: float = None, so2_24h: float = None, no2_24h: float = None,
            nh3_24h: float = None, pb_24h: float = None) -> (int, {}):
    """
    Calculates India AQI (Maximum from individual indexes)

    :param o3_8h: O3 average (8h), ppm
    :param co_8h: CO average (8h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :param so2_24h: SO2 average (24h), ppm
    :param no2_24h: NO2 average (24h), ppm
    :param nh3_24h: HN3 average (24h), ppm
    :param pb_24h: Pb average (24h), ppm
    :return: US AQI, dict with tuples (Individual aqi, Effect message, Caution message)
             keys are: o3_8h, co_8h, pm25_24h, pm10_24h, so2_24h, no2_24h, nh3_24h, pb_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_8h:
        aqi_data['o3_8h'] = get_aqi_o3_8h(o3_8h)
    if co_8h:
        aqi_data['co_8h'] = get_aqi_co_8h(co_8h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_aqi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_aqi_pm10_24h(pm10_24h)
    if so2_24h:
        aqi_data['so2_24h'] = get_aqi_so2_24h(so2_24h)
    if no2_24h:
        aqi_data['no2_24h'] = get_aqi_no2_24h(no2_24h)
    if nh3_24h:
        aqi_data['nh3_24h'] = get_aqi_nh3_24h(nh3_24h)
    if pb_24h:
        aqi_data['pb_24h'] = get_aqi_pb_24h(pb_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
