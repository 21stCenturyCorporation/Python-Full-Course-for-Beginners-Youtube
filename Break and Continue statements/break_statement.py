numbers = [1, 8, 3, 7, 5, 2, 9] # list of numbers

found_it = False # flag variable

for num in numbers: 
    print(f"Checking {num}.. ")
    if num == 5:
        found_it = True
        print("Found it! Breaking the Loop")
        break

print("Loop Finished.")
