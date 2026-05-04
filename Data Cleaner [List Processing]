data = [10,None,20,10,"",30,None,40]

clean_list = []
removed_count = 0

for item in data:
    if item is None or item == "":
        removed_count  += 1
    elif item in clean_list:
        removed_count += 1
    else:
        clean_list.append(item)

        clean_list.sort()

print("Clean List:",clean_list)
print("Removed Values:",removed_count)        



