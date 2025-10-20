# Print only the odd numbers

for i in range(1, 11):
    # checking the number is even
    if i % 2 == 0: # condition
        continue # skipping the iteration
    print(f"Found an odd number: {i}")

print("Loop Finished.")