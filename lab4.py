import random
global result

class Stock_find:
    def __init__(self):
        self.max_sum_idx = None
        self.correction = None
        self.flag = 0
        self.global_max = 0

    def maxCrossingSum(self,arr, l, m, h):

        summ = 0
        left_sum = -10000

        for i in range(m, l - 1, -1):
            summ += arr[i]
            if summ > left_sum:
                left_sum = summ
                idx_left = (m, i)

        summ = 0
        right_sum = -1000

        for i in range(m + 1, h + 1):
            summ += arr[i]
            if summ > right_sum:
                right_sum = summ
                idx_right = (m+1, i)

        maxx = max(left_sum + right_sum, left_sum, right_sum)
        if maxx == left_sum + right_sum and maxx > self.global_max:
            self.correction = (idx_left[1], idx_right[1] + 1)
            self.global_max = maxx
        if maxx == left_sum and maxx > self.global_max:
            self.correction = idx_left
            self.global_max = maxx
        if maxx == right_sum and maxx > self.global_max:
            self.correction = idx_right
            self.global_max = maxx
        return maxx

    def maxSubArraySum(self,arr, l, h,):
        if (l == h):
            return arr[l]
        m = (l + h) // 2

        res_left = self.maxSubArraySum(arr, l, m)
        res_right = self.maxSubArraySum(arr, m + 1, h)
        res_union = self.maxCrossingSum(arr, l, m, h)
        if max(res_left, res_right, res_union) == res_left:
            self.max_sum_idx = (l-1, m)
        elif max(res_left, res_right, res_union) == res_right:
            self.max_sum_idx = (m, h+1)
        elif max(res_left, res_right, res_union) == res_union:
            self.max_sum_idx = self.correction
        else:
            self.max_sum_idx = None
        return max(res_left, res_right, res_union)
    @property
    def get_max_sum_idx(self):
        return self.max_sum_idx

    @property
    def max_sum(self):
        return sum(arr[self.max_sum_idx[0]:self.max_sum_idx[1]])





def quicksort(arr, left, right):
    if left >= right:
        return

    i, j = left, right
    sep = arr[random.randint(left, right)]

    while i <= j:
        while arr[i] < sep:
            i += 1
        while arr[j] > sep:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1

    quicksort(arr, left, j)
    quicksort(arr, i, right)

if __name__ == "__main__":
    arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    find = Stock_find()
    find.maxSubArraySum(arr, 0, len(arr) - 1)
    print(f"Maximum drop range:{find.get_max_sum_idx}")
    print(f"The largest price difference {find.max_sum}")


    arr = [*reversed(range(9))]
    print(f"Start quick sort: {arr}")
    quicksort(arr, 0, len(arr) - 1)
    print(f"Finish Quick sort: {arr}")