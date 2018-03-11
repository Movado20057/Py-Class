item_list = ["person", "school", {"number":10, "position": "md"}, ("mango", "fruit", "church"), ["school", "mosque"]]

def extract_items(item_sequence):
    if type(item_sequence) == dict:
        for item in item_sequence:
            if type(item_sequence[item]) == dict:
                print (item_sequence[item])

            elif type(item_sequence[item]) == list or type(item_sequence[item]) == tuple:
                for inneritem in item_sequence[item]:
                    extract_items(inner_item)
            else:
                print (item_sequence[item])

    elif type(item_sequence) == list or type(item_sequence) == tuple:
        for item in item_sequence:
            extract_items(item)

    else:
        print (item_sequence)

extract_items(item_list)

exit()
