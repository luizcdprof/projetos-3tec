def fizzbuzz(num:int):
    if num % 3 == 0:
        return 'fizz'    
    elif num % 5 == 0:
        return 'buzz'
    elif num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    else:
        return num