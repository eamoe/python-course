from datetime import datetime as dt

def data_logger(input_data, output_data):
    date = dt.now().date()
    time = dt.now().strftime('%H:%M')
    with open('calc/log.csv', 'a') as file:
        file.write('{};{};expression;{};result;{}\n'
                    .format(date, time, input_data, output_data))