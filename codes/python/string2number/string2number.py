from constants import EN_NUMBERS_DICT, FA_NUMBERS_DICT


def string2number(string, numbers_dict):
    if not string or string == '':
        return 'string is empty'
    result = 0
    current_number = 0
    for word in [i for i in string.lower().split() if i not in ['and', 'و']]:
        if word not in numbers_dict:
            return None
        value = numbers_dict[word]
        if value >= 1000:
            result += current_number * value
            current_number = 0
        elif word in ['hundred', 'صد']:
            current_number = 1 if current_number == 0 else current_number
            current_number *= numbers_dict[word]
        else:
            current_number += value
    result += current_number
    return result


def main():
    while True:
        string = input('please enter a string (q to quit): ')
        if string.lower().strip().startswith('q'):
            break
        result = string2number(string, EN_NUMBERS_DICT)
        if result is None:
            result = string2number(string, FA_NUMBERS_DICT)
        if result is None:
            print('invalid string')
        print(result)


if __name__ == '__main__':
    main()
