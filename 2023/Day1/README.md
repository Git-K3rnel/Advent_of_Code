# AOC-2023-Day1-Part1

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
  <summary><b>Stabilize Shell</b></summary>

  ```text
56397
  ```
</details>
