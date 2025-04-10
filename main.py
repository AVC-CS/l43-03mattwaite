def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    count = 0 
    
    while count < 5:
        number = int(input(f"Enter a number{count + 1}:"))
        total += number 
        count += 1
        
    print("Total:",total)
        
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
