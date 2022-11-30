import statistics
def display_main_menu():
    print("Displaying main menu")

def get_user_input():
    print("Enter some values separated by commas (e.g. 5, 6, 7, 9)")
    user_input = input()
    split_inp = user_input.split(", ")
    list_inp = list(map(float,split_inp))
    print("The list of strings converted into floats : ",list_inp)
    return list_inp

def cal_average(x):
    length = len(x)
    total = 0
    for i in range(0,length):
        total = total + x[i]
    average = total/length
    print("The average is : ",average)
    return average

def find_min_max(y):
    minimum = min(y)
    maximum = max(y)
    mylist = [minimum,maximum]
    return mylist

def sort_temperature(z):
    z.sort()
    print("Floats in ascending order : ", z)
    z.sort(reverse=True)
    print("Floats in descending order : ", z)

def calc_median_temperature(a):
    median = statistics.median(a)
    print("The median temperature is : ",median)

def main():
    print("This is main\n")
    display_main_menu()
    list_inp = get_user_input()
    cal_average(list_inp)
    print(find_min_max(list_inp))
    sort_temperature(list_inp)
    calc_median_temperature(list_inp)
    print("Program finish")

if __name__ == "__main__" :
    main()