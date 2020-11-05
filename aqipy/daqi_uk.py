# coding: utf-8

"""
    DAQI UK
    Source: https://uk-air.defra.gov.uk/air-pollution/daqi
            https://uk-air.defra.gov.uk/assets/documents/reports/cat14/1304251155_Update_on_Implementation_of_the_DAQI_April_2013_Final.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula, __get_aqi_general_formula_texts

UK_O3_1H = ((0, 16), (17, 33), (34, 50), (51, 60), (61, 70), (71, 80), (81, 93), (94, 106), (107, 120), (121, 121))
UK_NO2_1H = (
    (0, 35), (36, 71), (72, 106), (107, 142), (143, 177), (178, 212), (213, 248), (249, 284), (285, 319), (320, 320))
UK_SO2_15M = (
    (0, 33), (34, 67), (68, 101), (102, 134), (135, 168), (169, 202), (203, 270), (271, 338), (339, 405), (406, 406))
UK_PM25_24H = ((0, 11), (12, 23), (24, 35), (36, 41), (42, 47), (48, 53), (54, 58), (59, 64), (65, 70), (71, 71))
UK_PM10_24H = ((0, 16), (17, 33), (34, 50), (51, 58), (59, 66), (67, 75), (76, 83), (84, 91), (92, 100), (101, 101))

UK_DAQI_GENERAL = (
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Anyone experiencing discomfort such as sore eyes, cough or sore throat should consider reducing activity, particularly outdoors.",
    "Anyone experiencing discomfort such as sore eyes, cough or sore throat should consider reducing activity, particularly outdoors.",
    "Anyone experiencing discomfort such as sore eyes, cough or sore throat should consider reducing activity, particularly outdoors.",
    "Reduce physical exertion, particularly outdoors, especially if you experience symptoms such as cough or sore throat."
)
# Adults and children with heart or lung problems are at greater risk of symptoms. Follow your doctor's usual advice about exercising and managing your condition. It is possible that very sensitive individuals may experience health effects even on Low air pollution days. Anyone experiencing symptoms should follow the guidance provided below.
UK_DAQI_RISK = (
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Enjoy your usual outdoor activities.",
    "Adults and children with lung problems, and adults with heart problems, who experience symptoms, should consider reducing strenuous physical activity, particularly outdoors.",
    "Adults and children with lung problems, and adults with heart problems, who experience symptoms, should consider reducing strenuous physical activity, particularly outdoors.",
    "Adults and children with lung problems, and adults with heart problems, who experience symptoms, should consider reducing strenuous physical activity, particularly outdoors.",
    "Adults and children with lung problems, and adults with heart problems, should reduce strenuous physical exertion, particularly outdoors, and particularly if they experience symptoms. People with asthma may find they need to use their reliever inhaler more often. Older people should also reduce physical exertion.",
    "Adults and children with lung problems, and adults with heart problems, should reduce strenuous physical exertion, particularly outdoors, and particularly if they experience symptoms. People with asthma may find they need to use their reliever inhaler more often. Older people should also reduce physical exertion.",
    "Adults and children with lung problems, and adults with heart problems, should reduce strenuous physical exertion, particularly outdoors, and particularly if they experience symptoms. People with asthma may find they need to use their reliever inhaler more often. Older people should also reduce physical exertion.",
    "Adults and children with lung problems, adults with heart problems, and older people, should avoid strenuous physical activity. People with asthma may find they need to use their reliever inhaler more often."
)


def __get_daqi(val: float, array: [[]]) -> (int, str, str):
    for i in range(len(array)):
        if array[i][0] <= val <= array[i][1]:
            return i + 1, UK_DAQI_GENERAL[i], UK_DAQI_RISK[i]
    return len(array), UK_DAQI_GENERAL[-1], UK_DAQI_RISK[-1]


def get_daqi_o3_1h(o3_1h: float) -> (int, str, str):
    """
    Calculates O3 (1h) UK DAQI

    :param o3_1h: O3 average (1h), ppm
    :return: O3 UK DAQI, Effect message, Caution message
    """
    cp = __round_down(o3_1h * 1000)
    return __get_daqi(cp, UK_O3_1H)


def get_daqi_no2_1h(no2_1h: float) -> (int, str, str):
    """
    Calculates NO2 (1h) UK DAQI

    :param no2_1h: NO2 average (1h), ppm
    :return: NO2 UK DAQI, Effect message, Caution message
    """
    cp = __round_down(no2_1h * 1000)
    return __get_daqi(cp, UK_NO2_1H)


def get_daqi_so2_15m(so2_15m: float) -> (int, str, str):
    """
    Calculates SO2 (15m) UK DAQI

    :param so2_15m: SO2 average (15m), ppm
    :return: SO2 UK DAQI, Effect message, Caution message
    """
    cp = __round_down(so2_15m * 1000)
    return __get_daqi(cp, UK_NO2_1H)


def get_aqi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) UK DAQI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 UK DAQI, Effect message, Caution message
    """
    cp = __round_down(pm25_24h)
    return __get_daqi(cp, UK_PM25_24H)


def get_aqi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) UK DAQI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 UK DAQI, Effect message, Caution message
    """
    cp = __round_down(pm10_24h)
    return __get_daqi(cp, UK_PM10_24H)


def get_daqi(o3_1h: float = None, no2_1h: float = None, so2_15m: float = None,
            pm25_24h: float = None, pm10_24h: float = None) -> (int, {}):
    """
    Calculates DAQI UK (Maximum from individual indexes)

    :param o3_1h: O3 average (1h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param so2_15m: SO3 average (15m), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :return: DAQI UK, dict with tuples (Individual aqi, Effect message, Caution message)
             keys are: o3_1h, no2_1h, so2_15m, pm25_24h, pm10_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_1h:
        aqi_data['o3_1h'] = get_daqi_o3_1h(o3_1h)
    if no2_1h:
        aqi_data['no2_1h'] = get_daqi_no2_1h(no2_1h)
    if so2_15m:
        aqi_data['so2_15m'] = get_daqi_so2_15m(so2_15m)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_aqi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_aqi_pm10_24h(pm10_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
