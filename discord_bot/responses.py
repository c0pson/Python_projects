from random import randint

def get_response(user_message):
    lowered = user_message.lower()
    if lowered == 'hihi':
        return 'hihi'
    elif 'hello' in lowered:
        return 'hello'
    else:
        return randint(1 ,10)
