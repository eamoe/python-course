import data_provider as provider
import logger

def temperature_view(sensor):
    data = provider.get_temperature(sensor)
    logger.temperature_logger(data)
    return data


def pressure_view(sensor):
    data = provider.get_pressure(sensor)
    logger.pressure_logger(data)
    return data


def wind_speed_view(sensor):
    data = provider.get_wind_speed(sensor)
    logger.wind_speed_logger(data)
    return data