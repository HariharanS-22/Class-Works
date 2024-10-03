
nums=[1,2,3,4,5,6]
with open("numbers.txt","w") as file:
    for num in nums:
        file.write(f"{num}.\n")
