# AOC-2023-Day1-Part2

```python
initial_strings = [] #Put strings in this list

string_numbers = ['1','2','3','4','5','6','7','8','9','one','two','three','four','five','six','seven','eight','nine']

def make_correct_split():
    correct_list = []
    for string in initial_strings:
        indices = {}
        temp_list = []
        for number in string_numbers:
            for m in re.finditer(number,string):
                indices[m.start()] = number

        sorted_dict = dict(sorted(indices.items()))
        # print(sorted_dict)

        for value in sorted_dict.values():
            if value == 'one':
                temp_list.append('1')
            elif value == 'two':
                temp_list.append('2')
            elif value == 'three':
                temp_list.append('3')
            elif value == 'four':
                temp_list.append('4')
            elif value == 'five':
                temp_list.append('5')
            elif value == 'six':
                temp_list.append('6')
            elif value == 'seven':
                temp_list.append('7')
            elif value == 'eight':
                temp_list.append('8')
            elif value == 'nine':
                temp_list.append('9')
            else:
                temp_list.append(value)
        # print(temp_list)
        correct_list.append(temp_list)
    return correct_list


def calculate_sum(fixed_list):
    total = 0
    for item in fixed_list:
        two_digit = int(f'{item[0]}{item[-1]}')
        total += two_digit
    return total


fixed_list = make_correct_split()
total_sum = calculate_sum(fixed_list)
```
