```python
import json
red_cubes = 12
green_cubes = 13
blue_cubes = 14

# read input file
with open('input.txt','r') as file:
    mydata = file.readlines()


# make a json data out of input file
myDictionary = {}
for data in mydata:
    game_data_split = data.split(':')
    game = game_data_split[0].strip()
    game_number = game.split(' ')[1]
    all_sets = game_data_split[1].strip()
    each_set_list = all_sets.split(';')
    temp_list = []
    for each_set in each_set_list:
        cubes_in_each_set = each_set.split(',')  
        temp_dict ={}
        for single_cube in cubes_in_each_set:    
            cube_count = single_cube.strip().split(' ')
            temp_dict[cube_count[1]] = cube_count[0]
        temp_list.append(temp_dict)
    myDictionary[game_number] = temp_list

# turn dictionary to json
json_dump = json.dumps(myDictionary)
final_json = json.loads(json_dump)




def part1():
    # find games that violate the number of cubes allowed
    games_to_remove = []
    for key in final_json.keys():
        game_sets = final_json[key]
        for each_set in game_sets:
            for color in each_set.keys():
                if (color == 'red' and int(each_set[color]) > 12) or (color == 'green' and int(each_set[color]) > 13) or (color == 'blue' and int(each_set[color]) > 14):
                    if key not in games_to_remove:
                        games_to_remove.append(key)

    # remove games that violate the rule from all games
    for game_number in games_to_remove:
        del final_json[game_number]

    # calculate rest of the games number
    total_sum = 0
    for key in final_json.keys():
        total_sum += int(key)
    print(total_sum)


def part2():
    # Find lowest possible cube color count
    total_sum = 0
    for key in final_json.keys():
        game_sets = final_json[key]
        red = 0
        blue = 0
        green = 0
        for each_set in game_sets:
            for color in each_set.keys():
                if color == 'red':
                    if int(each_set[color]) > int(red):
                        red = each_set[color]
                elif color == 'blue':
                    if int(each_set[color]) > int(blue):
                        blue = each_set[color]
                elif color == 'green':
                    if int(each_set[color]) > int(green):
                        green = each_set[color]
        power = int(red) * int(blue) * int(green)
        total_sum += power
    print(total_sum)        


part1()
part2()
```
