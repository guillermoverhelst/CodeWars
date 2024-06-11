#First solution
def pick_peaks(arr):
    peaks = {'pos': [], 'peaks': []}
    pos = None

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1]:
            pos = i
        if pos is not None and arr[i] > arr[i + 1]:
            peaks['pos'].append(pos)
            peaks['peaks'].append(arr[pos])
            pos = None

    return peaks

print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))