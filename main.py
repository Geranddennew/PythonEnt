def string_count(string):
    count_nums = []
    count = 0

    letter = string[0]
    for i in range(len(string)):
        if string[i] == letter:
            count += 1
        elif string[i] != letter and count > 1:
            count_nums.append(letter)
            count_nums.append(str(count))
            count = 1
            letter = string[i]
    count_nums.append(letter)
    count_nums.append(str(count))
    result = ''.join(count_nums)
    return result

string = "AAAAAABBBBBCCCCDDDDDEEEFFFFAAA" #А6B5C4D5E3F4A3
print(string_count(string))
