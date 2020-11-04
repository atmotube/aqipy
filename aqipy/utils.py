AQI_NOT_AVAILABLE = -1


def __get_aqi_texts(aqi: int, aqi_a: [], a1: [], a2: []) -> (str, str):
    for i in range(len(aqi_a)):
        if aqi_a[i][0] <= aqi <= aqi_a[i][1]:
            return a1[i], a2[i]
    return "", ""
