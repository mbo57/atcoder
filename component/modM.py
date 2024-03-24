
def find_unique_z(x, y, m):
    # 逆元を計算
    x_inv = pow(x, m - 2, m)
    # z = y * x_inv (mod m) で解を計算
    z = (y * x_inv) % m
    return z
