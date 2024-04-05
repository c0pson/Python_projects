from enum import Enum

class Color(str, Enum):
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def _01d():
    # clear sky
    ascii_clear = r'''
│╭───────────────╮
││     \   /     │
││      .-.      │
││  -- (   ) --  │
││      `-'      │
││     /   \     │
│╰───────────────╯
'''
    return ascii_clear

def _02d():
    # few clouds
    ascii_few_clouds = r'''
│╭───────────────╮
││    \  /       │
││  _`/"".-.     │
││   ,\_(   ).   │
││    /(___(__)  │
││               │
│╰───────────────╯
'''
    return ascii_few_clouds

def _03d():
    # scattered clouds
    ascii_scattered_clouds = r'''
│╭───────────────╮
││               │
││      .--.     │
││   .-(    ).   │
││  (___.__)__)  │
││               │
│╰───────────────╯
'''
    return ascii_scattered_clouds

def _04d():
    # broken clouds
    ascii_broken_clouds = r'''
│╭───────────────╮
││       .--.    │
││    .-(    ).  │
││  .(___.__)__) │
││ (_.__)__)     │
││               │
│╰───────────────╯
'''
    return ascii_broken_clouds

def _09d():
    # shower rain
    ascii_shower_rain = r'''
│╭───────────────╮
││      .--.     │
││   .-(    ).   │
││  (___.__)__)  │
││   ' ' ' ' '   │
││  ' ' ' ' '    │
│╰───────────────╯
'''
    return ascii_shower_rain

def _10d():
    # rain
    ascii_rain = r'''
│╭───────────────╮
││  `/"".--.     │
││  ,\_(   _).   │
││   /(__._(__)  │
││     ' ' ' '   │
││    ' ' ' '    │
│╰───────────────╯
'''
    return ascii_rain

def _11d():
    # thunderstorm
    ascii_thunderstorm = r'''
│╭───────────────╮    
││      .--.-.   │
││   .-(    )_)  │
││  (___.__)__)  │
││   ϟ   ϟ   ϟ   │
││     ϟ   ϟ     │
│╰───────────────╯
'''
    return ascii_thunderstorm

def _13d():
    # snow
    ascii_snow = r'''
│╭───────────────╮  
││      .--.     │
││   .-(    ).   │
││  (___.__)__)  │
││   * * * * *   │
││  * * * * *    │
│╰───────────────╯
'''
    return ascii_snow

def _50d():
    # mist
    ascii_mist = r'''
│╭───────────────╮
││   --- ___ =   │
││ ___ ==== ===  │
││  ==== ====    │
││ ==   --- ==== │
││  __ == ==-=   │
│╰───────────────╯
'''
    return ascii_mist

def _01n():
    # clear sky
    ascii_clear_sky = r'''
│╭───────────────╮
││      _..      │
││    ,'.`       │
││    | |        │
││    \ `._;     │
││     '.__/     │
│╰───────────────╯
'''
    return ascii_clear_sky

def _02n():
    # few clods
    ascii_few_clouds = r'''
│╭───────────────╮
││               │
││   /"".--.     │
││   \_(   _).   │
││    (__._(__)  │
││               │
│╰───────────────╯
'''
    return ascii_few_clouds

def _03n():
    # scattered_clouds
    ascii_scattered_clouds = r'''
│╭───────────────╮
││               │
││      .--.-.   │
││   .-(    )_)  │
││  (___.__)__)  │
││               │
│╰───────────────╯
'''
    return ascii_scattered_clouds

def _04n():
    ascii_broken_clouds = r'''
│╭───────────────╮
││       .--.    │
││    .-(    ).  │
││  .(___.__)__) │
││ (_.__)__)     │
││               │
│╰───────────────╯
'''
    return ascii_broken_clouds

def _09n():
    ascii_shower_rain = r'''
│╭───────────────╮
││      .--.     │
││   .-(    ).   │
││  (___.__)__)  │
││   ' ' ' ' '   │
││  ' ' ' ' '    │
│╰───────────────╯
'''
    return ascii_shower_rain

def _10n():
    ascii_rain = r'''
│╭───────────────╮
││   /"".--.     │
││   \_(   _).   │
││    (__._(__)  │
││     ' ' ' '   │
││    ' ' ' '    │
│╰───────────────╯
'''
    return ascii_rain

def _11n():
    # thunderstorm
    ascii_thunderstorm = r'''
│╭───────────────╮
││      .--.-.   │
││   .-(    )_)  │
││  (___.__)__)  │
││   ϟ   ϟ   ϟ   │
││     ϟ   ϟ     │
│╰───────────────╯   
'''
    return ascii_thunderstorm

def _13n():
    # snow
    ascii_snow = r'''
│╭───────────────╮
││      .--.     │
││   .-(    ).   │
││  (___.__)__)  │
││   * * * * *   │
││  * * * * *    │
│╰───────────────╯
'''
    return ascii_snow

def _50n():
    # mist
    ascii_mist = r'''
│╭───────────────╮
││   --- ___ =   │
││ ___ ==== ===  │
││  ==== ====    │
││ ==   --- ==== │
││  __ == ==-=   │
│╰───────────────╯
'''
    return ascii_mist
