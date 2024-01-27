
def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    if len(numbers) == 0:
        return 0
    
    largest = ""
    
    for _ in range(len(numbers)):
        biggest = "0"
        for number in numbers:
            if int(number[0]) > int(biggest[0]):
                biggest = number
            elif int(number[0]) == int(biggest[0]):
                if number + biggest > biggest + number:
                    biggest = number
            
        largest += biggest
        numbers.remove(biggest)
                    
            
    return (largest)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))
