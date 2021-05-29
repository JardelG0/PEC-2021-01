def soma(num):
    s = sum(num)
    print("A soma desses números é", s)


def multiplic(nums):
    mult = 1
    for i in nums:
        mult *= i
    print("O produto desses números é", mult, end="")


def main():
    numbers = []
    for i in range(10):
        nums = int(input("Digite aqui um número: "))
        numbers.append(nums)
    
    print(f'Os números digitados foram: {numbers}')
    soma(numbers)
    multiplic(numbers)


if __name__ == "__main__":
    main()
