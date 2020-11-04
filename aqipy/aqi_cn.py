# coding: utf-8

"""
    Mainland China AQI
    Source: https://core.ac.uk/download/pdf/38094372.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula_texts

CN_AQI = ((0, 50), (51, 100), (101, 150), (151, 200), (201, 299), (300, 300))
CN_AQI_EFFECTS = (
    "No health implications.",
    "Some pollutants may slightly affect very few hypersensitive individuals.",
    "Healthy people may experience slight irritations and sensitive individuals will be slightly affected to a larger extent.",
    "Sensitive individuals will experience more serious conditions. The hearts and respiratory systems of healthy people may be affected.",
    "Healthy people will commonly show symptoms. People with respiratory or heart diseases will be significantly affected and will experience reduced endurance in activities.",
    "Healthy people will experience reduced endurance in activities and may also show noticeably strong symptoms. Other illnesses may be triggered in healthy people. Elders and the sick should remain indoors and avoid exercise. Healthy individuals should avoid outdoor activities."
)
CN_AQI_CAUTIONS = (
    "Everyone can continue their outdoor activities normally.",
    "Only very few hypersensitive people should reduce outdoor activities.",
    "Children, seniors and individuals with respiratory or heart diseases should reduce sustained and high-intensity outdoor exercises.",
    "Children, seniors and individuals with respiratory or heart diseases should avoid sustained and high-intensity outdoor exercises. General population should moderately reduce outdoor activities.",
    "Children, seniors and individuals with heart or lung diseases should stay indoors and avoid outdoor activities. General population should reduce outdoor activities.",
    "Children, seniors and the sick should stay indoors and avoid physical exertion. General population should avoid outdoor activities."
)
CN_SO2_24H = ((0, 18), (19, 57), (58, 181), (182, 305), (306, 610), (611, 1000))
CN_NO2_24H = ((0, 21), (22, 42), (43, 95), (96, 148), (149, 300), (301, 500))
CN_CO_24H = ((0.0, 1.6), (1.7, 3.4), (3.5, 12.1), (12.2, 20.8), (20.9, 31.3), (31.4, 52.4))
CN_O3_1H = ((0, 80), (81, 100), (101, 150), (151, 200), (201, 400), (401, 600))
CN_O3_8H = ((0, 50), (51, 80), (81, 107), (108, 132), (133, 400))
CN_PM25_24H = ((0, 50), (51, 150), (151, 250), (251, 350), (351, 420), (421, 600))
CN_PM10_24H = ((0, 35), (36, 75), (76, 115), (116, 150), (151, 250), (251, 500))


def get_aqi_o3_1h(o3_1h: float) -> (int, str, str):
    """
    Calculates O3 CN AQI

    :param o3_1h: O3 average (1h), ppm
    :return: O3 CN AQI, Effect message, Caution message
    """
    cp = __round_down(o3_1h * 1000)
    return __get_aqi_general_formula_texts(cp, CN_O3_1H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_o3_8h(o3_8h: float) -> (int, str, str):
    """
    Calculates O3 CN AQI

    :param o3_8h: O3 average (8h), ppm
    :return: O3 CN AQI, Effect message, Caution message
    """
    cp = __round_down(o3_8h * 1000)
    return __get_aqi_general_formula_texts(cp, CN_O3_8H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_co_24h(co_24h: float) -> (int, str, str):
    """
    Calculates CO (24h) CN AQI

    :param co_24h: CO average (24h), ppm
    :return: CO CN AQI, Effect message, Caution message
    """
    cp = __round_down(co_24h, 1)
    return __get_aqi_general_formula_texts(cp, CN_CO_24H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) CN AQI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 CN AQI, Effect message, Caution message
    """
    cp = __round_down(pm25_24h, 1)
    return __get_aqi_general_formula_texts(cp, CN_PM25_24H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) CN AQI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 CN AQI, Effect message, Caution message
    """
    cp = round(pm10_24h)
    return __get_aqi_general_formula_texts(cp, CN_PM10_24H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_so2_24h(so2_24h: float) -> (int, str, str):
    """
    Calculates SO2 (24h) CN AQI

    :param so2_24h: SO2 average (24h), ppm
    :return: SO2 CN AQI, Effect message, Caution message
    """
    cp = round(so2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, CN_SO2_24H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi_no2_24h(no2_24h: float) -> (int, str, str):
    """
    Calculates NO2 (24h) CN AQI

    :param no2_24h: NO2 average (24h), ppm
    :return: NO2 CN AQI, Effect message, Caution message
    """
    cp = round(no2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, CN_NO2_24H, CN_AQI_EFFECTS, CN_AQI_CAUTIONS, CN_AQI)


def get_aqi(o3_1h: float = None, o3_8h: float = None, co_24h: float = None, pm25_24h: float = None,
            pm10_24h: float = None, so2_24h: float = None, no2_24h: float = None) -> (int, {}):
    """
    Calculates US AQI (Maximum from individual indexes)

    :param o3_1h: O3 average (1h), ppm
    :param o3_8h: O3 average (8h), ppm
    :param co_24h: CO average (24h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :param so2_24h: SO2 average (24h), ppm
    :param no2_24h: NO2 average (24h), ppm
    :return: US AQI, dict with tuples (Individual aqi, Effect message, Caution message)
            keys are: o3_1h, o3_8h, co_24h, pm25_24h, pm10_24h, so2_24h, no2_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_1h:
        aqi_data['o3_1h'] = get_aqi_o3_1h(o3_1h)
    if o3_8h:
        aqi_data['o3_8h'] = get_aqi_o3_8h(o3_8h)
    if co_24h:
        aqi_data['co_24h'] = get_aqi_co_24h(co_24h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_aqi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_aqi_pm10_24h(pm10_24h)
    if so2_24h:
        aqi_data['so2_24h'] = get_aqi_so2_24h(so2_24h)
    if no2_24h:
        aqi_data['no2_24h'] = get_aqi_no2_24h(no2_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
