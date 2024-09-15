def maqsum_alaih(n):
    sum_numbers = 0
    count_numbers = 0

    for a in range(1, n + 1):
        for b in range(1, a + 1):
            if a % b == 0:
                sum_numbers += b
                count_numbers += 1

    return count_numbers, sum_numbers


n = int(input())
count, sum_factors = maqsum_alaih(n)

print(count, sum_factors)
