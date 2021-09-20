def display_odd_numbers(first_number, second_number):
    while first_number < second_number:
        first_number+=1
        if first_number % 2 != 0:
            print(first_number)

display_odd_numbers(10,20)