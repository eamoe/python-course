from user_interface import temperature_view
from user_interface import pressure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '   <p {}>Temperature: {} °C</p>\n'\
            .format(style, temperature_view(device))
    html += '   <p {}>Pressure: {} mmHg</p>\n'\
            .format(style, pressure_view(device))
    html += '   <p {}>Wind Speed: {} m/s</p>\n'\
            .format(style, wind_speed_view(device))
    html += '   </body>\n</html>'

    with open('join_job/index.html', 'w') as page:
        page.write(html)
    
    return html