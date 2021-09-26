print("Hello World")

print("This is a git tutorialfor data1050 hw")

def odd_number_and_mean_finder(l):
    #function that detects even numbers in a given list input 
    odd_numbers = []
    counter = 0
    for x in l:
        counter += x
        if (x % 2)!= 0:
            odd_numbers.append(x)
            mean  = counter/len(l)
    print(odd_numbers)
    print(mean)

odd_number_and_mean_finder([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Hi")