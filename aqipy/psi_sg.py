# coding: utf-8

"""
    Singapore PSI
    Source: https://www.haze.gov.sg/docs/default-source/faq/computation-of-the-pollutant-standards-index-(psi).pdf
            https://www.nea.gov.sg/our-services/pollution-control/air-pollution/faqs#chapterA
            https://www-haze-gov-sg-admin.cwp.sg/docs/default-source/default-document-library/how-to-plan-your-outdoor-activities-during-haze.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula_texts

SG_PSI = ((0, 50), (51, 100), (101, 200), (201, 300), (301, 400), (401, 500))
SG_PM25_24H = ((0, 12), (13, 55), (56, 150), (151, 250), (251, 350), (351, 500))
SG_PM10_24H = ((0, 50), (51, 150), (151, 350), (351, 420), (421, 500), (501, 600))
SG_SO2_24H = ((0, 30), (31, 139), (140, 304), (305, 610), (611, 801), (802, 1000))
SG_CO_8H = ((0.0, 4.4), (4.5, 8.7), (8.8, 14.8), (14.9, 29.7), (29.8, 40.1), (40.2, 50.2))
SG_O3_8H = ((0, 59), (60, 78), (79, 117), (118, 392), (393, 490), (491, 590))
SG_NO2_1H = ((0, 0), (0, 0), (0, 601), (602, 1202), (1203, 1595), (1596, 1995))

SG_AQI_GENERAL = (
    "Normal activities",
    "Normal activities",
    "Reduce prolonged or strenuous outdoor physical exertion",
    "Avoid prolonged or strenuous outdoor physical exertion",
    "Minimise outdoor activity",
    "Healthy people may experience adverse symptoms that affect normal activity."
)
# Vulnerable persons include the elderly, pregnant women, children, and persons with chronic lung disease or heart disease
SG_AQI_RISK = (
    "Normal activities",
    "Normal activities",
    "Avoid prolonged or strenuous outdoor physical exertion",
    "Avoid outdoor activity",
    "Avoid outdoor activity",
    "PSI levels above 400 may be life-threatening to ill and elderly persons"
)


def get_psi_o3_8h(o3_8h: float) -> (int, str, str):
    """
    Calculates O3 Singapore PSI

    :param o3_8h: O3 average (1h), ppm
    :return: Singapore PSI, General message, Risk message
    """
    cp = __round_down(o3_8h * 1000)
    return __get_aqi_general_formula_texts(cp, SG_O3_8H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_psi_no2_1h(no2_1h: float) -> (int, str, str):
    """
    Calculates NO2 Singapore PSI

    :param no2_1h: NO2 average (1h), ppm
    :return: Singapore PSI, General message, Risk message
    """
    cp = __round_down(no2_1h * 1000)
    return __get_aqi_general_formula_texts(cp, SG_NO2_1H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_psi_so2_24h(so2_24h: float) -> (int, str, str):
    """
    Calculates SO2 Singapore PSI

    :param so2_24h: SO2 average (24h), ppm
    :return: Singapore PSI, General message, Risk message
    """
    cp = __round_down(so2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, SG_SO2_24H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_psi_co_8h(co_8h: float) -> (int, str, str):
    """
    Calculates CO Singapore PSI

    :param co_8h: CO average (8h), ppm
    :return: Singapore PSI, General message, Risk message
    """
    cp = __round_down(co_8h, 1)
    return __get_aqi_general_formula_texts(cp, SG_CO_8H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_psi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) Singapore PSI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 Singapore PSI,  General message, Risk message
    """
    cp = __round_down(pm25_24h)
    return __get_aqi_general_formula_texts(cp, SG_PM25_24H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_psi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) Singapore PSI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 Singapore PSI,  General message, Risk message
    """
    cp = __round_down(pm10_24h)
    return __get_aqi_general_formula_texts(cp, SG_PM10_24H, SG_AQI_GENERAL, SG_AQI_RISK, SG_PSI)


def get_aqi(o3_8h: float = None, no2_1h: float = None, so2_24h: float = None,
            co_8h: float = None, pm25_24h: float = None, pm10_24h: float = None, ) -> (int, {}):
    """
    Calculates Singapore PSI (Maximum from individual indexes)

    :param o3_8h: O3 average (8h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param so2_24h: SO2 average (24h), ppm
    :param co_8h: CO average (8h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :return: Singapore PSI, dict with tuples (Individual PSI, General message, Risk message)
            keys are: o3_8h, no2_1h, so2_24h, co_8h, pm25_24h, pm10_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if o3_8h:
        aqi_data['o3_8h'] = get_psi_o3_8h(o3_8h)
    if no2_1h:
        aqi_data['no2_1h'] = get_psi_no2_1h(no2_1h)
    if so2_24h:
        aqi_data['so2_24h'] = get_psi_so2_24h(so2_24h)
    if co_8h:
        aqi_data['co_8h'] = get_psi_co_8h(co_8h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_psi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_psi_pm10_24h(pm10_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
