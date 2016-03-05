def rotate(arr, n):
    dex = -(n % len(arr))
    return arr[dex:] + arr[:dex]
