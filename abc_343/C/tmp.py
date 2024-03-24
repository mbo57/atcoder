def is_palindrome(n):
    return str(n) == str(n)[::-1]


def find_palindrome_cubes(start, end):
    palindrome_cubes = []
    for num in range(start, end + 1):
        cube = num ** 3
        if is_palindrome(cube):
            palindrome_cubes.append(cube)
    return palindrome_cubes


# 例: 1から100000までの範囲で回文立方数を求める
start_range = 1
end_range = 100000
result = find_palindrome_cubes(start_range, end_range)

print("回文立方数:", result)
