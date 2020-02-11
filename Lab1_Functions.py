def coefficients(N=1000):
    sum_odd = 0
    sum_even = 0
    a1 = a2 = a3 = a4 = 0.0
    b1 = b2 = b3 = b4 = 0.0
    for n in range(1, N):
        sum_odd += (2 * n - 1) ** 2
        sum_even += (2 * n) ** 2
        a1 = sum_odd / n ** 3
        b1 = sum_even / n ** 3
        a2 = (sum_odd / n ** 2) - (a1 * n)
        b2 = (sum_even / n ** 2) - (b1 * n)
        a3 = (sum_odd / n) - (a1 * n ** 2) - (a2 * n)
        b3 = (sum_even / n) - (b1 * n ** 2) - (b2 * n)
        a4 = sum_odd - (a1 * n ** 3) - (a2 * n ** 2) - (a3 * n)
        b4 = sum_even - (b1 * n ** 3) - (b2 * n ** 2) - (b3 * n)
    print("Polynomial of the sum of odd numbers: ", a1, "n^3 + ", a2, "n^2 + ", a3, "n +", a4)
    print("Polynomial of the sum of even numbers: ", b1, "n^3 + ", b2, "n^2 + ", b3, "n +", b4)


def shiftList(l, n):
    return l[n:] + l[:n]


def main():
    coefficients(1000)
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    list_shifted = shiftList(l,2)
    print(list_shifted)


if __name__ == "__main__":
    main()