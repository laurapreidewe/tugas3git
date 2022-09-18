from math_function import add, mul, div


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
<<<<<<< HEAD
        result = add(data_1, data_2)      
=======
        result = add(data_1, data_2)
    elif operator == "*":
        result = mul(data_1, data_2)
    elif operator == "/":
        result = div(data_1, data_2)

>>>>>>> feature/add_mul_div

    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()
