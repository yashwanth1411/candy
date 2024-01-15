def distribute_candies(A):
    n = len(A)

    # Initialize an array to store the number of candies each child receives
    candies = [1] * n

    # Traverse from left to right, ensuring that a child with a higher rating gets more candies
    for i in range(1, n):
        if A[i] > A[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse from right to left, ensuring that a child with a higher rating still gets more candies
    for i in range(n - 2, -1, -1):
        if A[i] > A[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Sum up the total number of candies
    total_candies = sum(candies)

    return total_candies


ratings = []
a = int(input())
for i in range(a):
    j = int(input())
    ratings.append(j)
result = distribute_candies(ratings)
print(result)
