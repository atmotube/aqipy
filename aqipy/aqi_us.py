# coding: utf-8

"""
    US AQI
    Source: https://www.airnow.gov/sites/default/files/2018-05/aqi-technical-assistance-document-may2016.pdf
"""

from aqipy.utils import AQI_NOT_AVAILABLE, __round_down, __get_aqi_general_formula_texts

US_AQI = ((0, 50), (51, 100), (101, 150), (151, 200), (201, 300), (301, 500))
US_OZONE_8H = ((0, 0.054), (0.055, 0.070), (0.071, 0.085), (0.086, 0.105), (0.106, 0.200))
US_OZONE_1H = ((0, 0), (0, 0), (0.125, 0.164), (0.165, 0.204), (0.205, 0.404), (0.405, 0.604))
US_OZONE_EFFECTS = (
    "",
    "Unusually sensitive individuals may experience respiratory symptoms.",
    "Increasing likelihood of respiratory symptoms and breathing discomfort in people with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients.",
    "Greater likelihood of respiratory symptoms and breathing in people with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients; possible respiratory effects in general population.",
    "Increasingly severe symptoms and impaired breathing likely in people with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients; increasing likelihood of respiratory effects in general population.",
    "Severe respiratory effects and impaired breathing likely in people with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients; increasingly severe respiratory effects likely in general population."
)
US_OZONE_CAUTIONS = (
    "",
    "Unusually sensitive people should consider reducing prolonged or heavy outdoor exertion.",
    "People with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients should reduce prolonged or heavy outdoor exertion.",
    "People with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients should avoid prolonged or heavy outdoor exertion; everyone else should reduce prolonged or heavy outdoor exertion",
    "People with lung disease (such as asthma), children, older adults, people who are active outdoors (including outdoor workers), people with certain genetic variants, and people with diets limited in certain nutrients should avoid all outdoor exertion; everyone else should reduce outdoor exertion.",
    "Everyone should avoid all outdoor exertion."
)
US_PM25_24H = ((0.0, 12.0), (12.1, 35.4), (35.5, 55.4), (55.5, 150.4), (150.5, 250.4), (250.5, 500.4))
US_PM10_24H = ((0, 54), (55, 154), (155, 254), (255, 354), (355, 424), (425, 604))
US_PM_EFFECTS = (
    "",
    "Respiratory symptoms possible in unusually sensitive individuals; possible aggravation of heart or lung disease in people with cardiopulmonary disease and older adults.",
    "Increasing likelihood of respiratory symptoms in sensitive groups including older adults, children, and people of lower socioeconomic status; aggravation of heart or lung disease and premature mortality in people with heart or lung disease.",
    "Increased aggravation of respiratory symptoms in sensitive groups including older adults, children, and people of lower socioeconomic status; increased aggravation of heart or lung disease and premature mortality in people with heart or lung disease; increased respiratory effects in general population.",
    "Significant aggravation of respiratory symptoms in sensitive groups including older adults, children, and people of lower socioeconomic status; significant aggravation of heart or lung disease and premature mortality in people with heart or lung disease; significant increase in respiratory effects in general population.",
    "Serious aggravation of respiratory symptoms in sensitive groups including older adults, children, and people of lower socioeconomic status; serious aggravation of heart or lung disease and premature mortality in people with heart or lung disease; serious risk of respiratory effects in general population."
)
US_PM_CAUTIONS = (
    "",
    "Unusually sensitive people should consider reducing prolonged or heavy exertion.",
    "People with heart or lung disease, older adults, children, and people of lower socioeconomic status should reduce prolonged or heavy exertion",
    "People with heart or lung disease, older adults, children, and people of lower socioeconomic status should avoid prolonged or heavy exertion; everyone else should reduce prolonged or heavy exertion.",
    "People with heart or lung disease, older adults, children, and people of lower socioeconomic status should avoid all physical activity outdoors. Everyone else should avoid prolonged or heavy exertion.",
    "Everyone should avoid all physical activity outdoors; people with heart or lung disease, older adults, children, and people of lower socioeconomic status should remain indoors and keep activity levels low."
)
US_CO_8H = ((0.0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, 50.4))
US_CO_EFFECTS = (
    "",
    "",
    "Increasing likelihood of reduced exercise tolerance due to increased cardiovascular symptoms, such as chest pain, in people with heart disease.",
    "Reduced exercise tolerance due to increased cardiovascular symptoms, such as chest pain, in people with heart disease.",
    "Significant aggravation of cardiovascular symptoms, such as chest pain, in people with heart disease.",
    "Serious aggravation of cardiovascular symptoms, such as chest pain, in people with heart disease; impairment of strenuous activities in general population."
)
US_CO_CAUTIONS = (
    "",
    "",
    "People with heart disease, such as angina, should limit heavy exertion and avoid sources of CO, such as heavy traffic.",
    "People with heart disease, such as angina, should limit moderate exertion and avoid sources of CO, such as heavy traffic.",
    "People with heart disease, such as angina, should avoid exertion and sources of CO, such as heavy traffic.",
    "People with heart disease, such as angina, should avoid exertion and sources of CO, such as heavy traffic; everyone else should limit heavy exertion."
)
US_SO2_1H = ((0, 35), (36, 75), (76, 185), (186, 304))
US_SO2_24H = ((0, 35), (36, 75), (76, 185), (186, 304), (305, 604), (605, 1004))
US_SO2_EFFECTS = (
    "",
    "",
    "Increasing likelihood of respiratory symptoms, such as chest tightness and breathing discomfort, in people with asthma.",
    "Increased respiratory symptoms, such as chest tightness and wheezing in people with asthma; possible aggravation of other lung diseases.",
    "Significant increase in respiratory symptoms, such as wheezing and shortness of breath, in people with asthma; aggravation of other lung diseases.",
    "Severe respiratory symptoms, such as wheezing and shortness of breath, in people with asthma; increased aggravation of other lung diseases; possible respiratory effects in general population."
)
US_SO2_CAUTIONS = (
    "",
    "",
    "People with asthma should consider limiting outdoor exertion.",
    "Children, people with asthma, or other lung diseases, should limit outdoor exertion.",
    "Children, people with asthma, or other lung diseases should avoid outdoor exertion; everyone else should reduce outdoor exertion.",
    "Children, people with asthma, or other lung diseases, should remain indoors; everyone else should avoid outdoor exertion."
)
US_NO2_1H = ((0, 53), (54, 100), (101, 360), (361, 649), (650, 1249), (1250, 2049))
US_NO2_EFFECTS = (
    "",
    "",
    "Increasing likelihood of respiratory symptoms, such as chest tightness and breathing discomfort, in people with asthma.",
    "Increased respiratory symptoms, such as chest tightness and wheezing in people with asthma; possible aggravation of other lung diseases.",
    "Significant increase in respiratory symptoms, such as wheezing and shortness of breath, in people with asthma; aggravation of other lung diseases.",
    "Severe respiratory symptoms, such as wheezing and shortness of breath, in people with asthma; increased aggravation of other lung diseases; possible respiratory effects in general population."
)
US_NO2_CAUTIONS = (
    "",
    "Unusually sensitive individuals should consider limiting prolonged exertion especially near busy roads.",
    "People with asthma, children and older adults should limit prolonged exertion especially near busy roads.",
    "People with asthma, children and older adults should avoid prolonged exertion near roadways; everyone else should limit prolonged exertion especially near busy roads.",
    "People with asthma, children and older adults should avoid all outdoor exertion; everyone else should avoid prolonged exertion especially near busy roads.",
    "People with asthma, children and older adults should remain indoors; everyone else should avoid all outdoor exertion."
)


def get_aqi_o3_1h(o3_1h: float) -> (int, str, str):
    """
    Calculates O3 US AQI

    :param o3_1h: O3 average (1h), ppm
    :return: O3 US AQI, Effect message, Caution message
    """
    cp = __round_down(o3_1h, 3)
    return __get_aqi_general_formula_texts(cp, US_OZONE_1H, US_OZONE_EFFECTS, US_OZONE_CAUTIONS, US_AQI)


def get_aqi_o3_8h(o3_8h: float) -> (int, str, str):
    """
    Calculates O3 US AQI

    :param o3_8h: O3 average (8h), ppm
    :return: O3 US AQI, Effect message, Caution message
    """
    cp = __round_down(o3_8h, 3)
    # 8-hour O3 values do not define higher AQI values (≥ 301)
    return __get_aqi_general_formula_texts(cp, US_OZONE_8H, US_OZONE_EFFECTS, US_OZONE_CAUTIONS, US_AQI, 300)


def get_aqi_co_8h(co_8h: float) -> (int, str, str):
    """
    Calculates CO (8h) US AQI

    :param co_8h: CO average (8h), ppm
    :return: CO US AQI, Effect message, Caution message
    """
    cp = __round_down(co_8h, 1)
    return __get_aqi_general_formula_texts(cp, US_CO_8H, US_CO_EFFECTS, US_CO_CAUTIONS, US_AQI)


def get_aqi_pm25_24h(pm25_24h: float) -> (int, str, str):
    """
    Calculates PM2.5 (24h) US AQI

    :param pm25_24h: PM2.5 average (24h), μg/m3
    :return: PM2.5 US AQI, Effect message, Caution message
    """
    cp = __round_down(pm25_24h, 1)
    return __get_aqi_general_formula_texts(cp, US_PM25_24H, US_PM_EFFECTS, US_PM_CAUTIONS, US_AQI)


def get_aqi_pm10_24h(pm10_24h: float) -> (int, str, str):
    """
    Calculates PM10 (24h) US AQI

    :param pm10_24h: PM10 average (24h), μg/m3
    :return: PM10 US AQI, Effect message, Caution message
    """
    cp = round(pm10_24h)
    return __get_aqi_general_formula_texts(cp, US_PM10_24H, US_PM_EFFECTS, US_PM_CAUTIONS, US_AQI)


def get_aqi_so2_1h(so2_1h: float) -> (int, str, str):
    """
    Calculates SO2 (1h) US AQI

    :param so2_1h: SO2 average (1h), ppm
    :return: SO2 US AQI, Effect message, Caution message
    """
    cp = round(so2_1h * 1000)
    # 1-hour SO2 values do not define higher AQI values (≥ 200)
    return __get_aqi_general_formula_texts(cp, US_SO2_1H, US_SO2_EFFECTS, US_SO2_CAUTIONS, US_AQI, 200)


def get_aqi_so2_24h(so2_24h: float) -> (int, str, str):
    """
    Calculates SO2 (24h) US AQI

    :param so2_24h: SO2 average (24h), ppm
    :return: SO2 US AQI, Effect message, Caution message
    """
    cp = round(so2_24h * 1000)
    return __get_aqi_general_formula_texts(cp, US_SO2_24H, US_SO2_EFFECTS, US_SO2_CAUTIONS, US_AQI)


def get_aqi_no2_1h(no2_1h: float) -> (int, str, str):
    """
    Calculates NO2 (1h) US AQI

    :param no2_1h: NO2 average (1h), ppm
    :return: NO2 US AQI, Effect message, Caution message
    """
    cp = round(no2_1h * 1000)
    return __get_aqi_general_formula_texts(cp, US_NO2_1H, US_NO2_EFFECTS, US_NO2_CAUTIONS, US_AQI)


def get_aqi(co_8h: float = None, o3_1h: float = None, o3_8h: float = None, no2_1h: float = None, pm25_24h: float = None,
            pm10_24h: float = None, so2_1h: float = None, so2_24h: float = None) -> (int, {}):
    """
    Calculates US AQI (Maximum from individual indexes)

    :param co_8h: CO average (8h), ppm
    :param o3_1h: O3 average (1h), ppm
    :param o3_8h: O3 average (8h), ppm
    :param no2_1h: NO2 average (1h), ppm
    :param pm25_24h: PM2.5 average (24h), μg/m3
    :param pm10_24h: PM10 average (24h), μg/m3
    :param so2_1h: SO2 average (1h), ppm
    :param so2_24h: SO2 average (24h), ppm
    :return: US AQI, dict with tuples (Individual aqi, Effect message, Caution message)
            keys are: co_8h, o3_1h, o3_8h, no2_1h, pm25_24h, pm10_24h, so2_1h, so2_24h
             -1 means AQI is not available
    """
    aqi_data = {}
    if co_8h:
        aqi_data['co_8h'] = get_aqi_co_8h(co_8h)
    if o3_1h:
        aqi_data['o3_1h'] = get_aqi_o3_1h(o3_1h)
    if o3_8h:
        aqi_data['o3_8h'] = get_aqi_o3_8h(o3_8h)
    if no2_1h:
        aqi_data['no2_1h'] = get_aqi_no2_1h(no2_1h)
    if pm25_24h:
        aqi_data['pm25_24h'] = get_aqi_pm25_24h(pm25_24h)
    if pm10_24h:
        aqi_data['pm10_24h'] = get_aqi_pm10_24h(pm10_24h)
    if so2_1h:
        aqi_data['so2_1h'] = get_aqi_so2_1h(so2_1h)
    if so2_24h:
        aqi_data['so2_24h'] = get_aqi_so2_24h(so2_24h)
    if len(aqi_data) == 0:
        return AQI_NOT_AVAILABLE, aqi_data
    return max(list(map(lambda x: x[0], aqi_data.values()))), aqi_data
