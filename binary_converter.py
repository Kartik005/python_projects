your_number = input("Enter binary code: ")
digits = [int(integer) for integer in str(your_number)]
digits.reverse()
n=int(len(digits))
bin_no = 0
sum = 0
i =0
while(i<= n-1):
    for num in digits:
        multiplier= 2**i
        bin_no = num * multiplier
        if i== 0:
            position = "1st"
        elif i == 1:
            position = "2nd"
        elif i == 2:
            position = "3rd"
        else:
            position = f"{i}th"
        
        i+=1
        
        print(f"    Value of {position} digits is: {bin_no}")
        sum = sum + bin_no
    print(f"\n Value in decimal system is: {sum}")
    
