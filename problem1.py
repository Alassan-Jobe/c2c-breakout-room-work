def reverse_string(s: str) -> str:
    if s == '':
        return ''
    result = ''
    for letter in s:
        result = s + result
    return result
