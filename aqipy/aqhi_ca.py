# coding: utf-8

"""
    Canada AQHI
    Source: https://www.tandfonline.com/doi/pdf/10.3155/1047-3289.58.3.435?needAccess=true
            https://en.wikipedia.org/wiki/Air_Quality_Health_Index_(Canada)
"""

from typing import Union, Tuple
from aqipy.utils import __get_aqi_texts, __added_risk, __get_aqi_level, AQI_NOT_AVAILABLE

CA_AQHI = ((1, 3), (4, 6), (7, 10), (11, 11))
CA_AQHI_LEVELS = ('low', 'moderate', 'high', 'very high')

CA_AQHI_GENERAL = (
    "Ideal air quality for outdoor activities.",
    "No need to modify your usual outdoor activities unless you experience symptoms such as coughing and throat irritation.",
    "Consider reducing or rescheduling strenuous activities outdoors if you experience symptoms such as coughing and throat irritation.",
    "Reduce or reschedule strenuous activities outdoors, especially if you experience symptoms such as coughing and throat irritation."
)
# People with heart or breathing problems are at greater risk. Follow your doctor's usual advice about exercising and managing your condition.
CA_AQHI_RISK = (
    "Enjoy your usual outdoor activities.",
    "Consider reducing or rescheduling strenuous activities outdoors if you are experiencing symptoms.",
    "Reduce or reschedule strenuous activities outdoors. Children and the elderly should also take it easy.",
    "Avoid strenuous activities outdoors. Children and the elderly should also avoid outdoor physical exertion."
)


def get_aqhi(o3_3h: float, no2_3h: float, pm25_3h: float, pm10_3h: float, with_level: bool = False) -> Union[
    Tuple[float, str, str], Tuple[float, dict]]:
    """
    Calculates Canada AQHI

    :param o3_3h: O3 average (3h), ppm
    :param no2_3h: NO2 average (3h), ppm
    :param pm25_3h: PM2.5 average (3h), μg/m3
    :param pm10_3h: PM10 average (3h), μg/m3
    :param with_level: Boolean distinguishing whether to print AQI level such as 'good' or 'hazardous'
    :return: CA AQHI, General message, Risk message
    """
    if any(value is None for value in (o3_3h, no2_3h, pm10_3h, pm25_3h)):
        return AQI_NOT_AVAILABLE, "", ""
    betas = [0.000537, 0.000871, 0.000487, 0.000297]
    c = [o3_3h * 1000, no2_3h * 1000, pm25_3h, pm10_3h]
    ars = list(map(__added_risk, betas, c))
    ar_pm25 = sum(ars[0:2]) + ars[2]
    pm25 = max(1, min(CA_AQHI[-1][1], round(ar_pm25)))
    ar_pm10 = sum(ars[0:2]) + ars[3]
    pm10 = max(1, min(CA_AQHI[-1][1], round(ar_pm10)))
    aqhi = max(pm25, pm10)
    text1, text2 = __get_aqi_texts(aqhi, CA_AQHI, CA_AQHI_GENERAL, CA_AQHI_RISK)
    if not with_level:
        return aqhi, text1, text2
    return aqhi, {'level': __get_aqi_level(aqhi, CA_AQHI, CA_AQHI_LEVELS)}
