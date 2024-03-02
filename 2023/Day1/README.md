# Part1

```python

initial_strings = [] #Put strings in this list

natural_numbers = ['1','2','3','4','5','6','7','8','9']

def extract_numbers():
    extracted_numbers = []
    for string in initial_strings:
        temp_list = []
        for char in string:
            if char in natural_numbers:
                temp_list.append(char)
        extracted_numbers.append(temp_list)
    return extracted_numbers


def check_single_array(extracted_numbers_list):
    for item in extracted_numbers_list:
        for number in item:
            if len(item) == 1:
                item.append(number)
    return extracted_numbers_list


def calculate_sum(fixed_list):
    total = 0
    for item in fixed_list:
        two_digit = int(f'{item[0]}{item[-1]}')
        total += two_digit
    return total

ext_number = extract_numbers()
fixed_list = check_single_array(ext_number)
total_sum = calculate_sum(fixed_list)

print(total_sum)
```


<details>
  <summary><b>Answer</b></summary>

  ```text
56397
  ```
</details>


# Part2

```python
import re

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

<details>
  <summary><b>Answer</b></summary>
    
```text
55701
```

</details>
