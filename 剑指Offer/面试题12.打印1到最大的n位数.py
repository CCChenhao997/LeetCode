'''
descrption: 打印从1到最大的n位数
题目：输入数字n，按顺序打印出1到最大的n位十进制数
这里需要考虑n很大时用int甚至long long都无法表示，因为python的字符串是不可变对象，这里我们采用数组的方式并用在最左边加一个空间来判断是否最大值
'''
 
class Solution:
    def print_until_max_n(self, n):
        '''
        1。 这里创建的数组的位数比要求的多一位，最左边的一位是标志位，类如n=3，那么999下一个数就是1000，那么我只要输出最左边一位不为1时的所有的数
        2。 这里有一个从左到右遍历数组的过程碰到9就继续往左移位，然后碰到第一个不为9就加一，右边的置0
        3.  这里给出一个return值，0代表ok，1代表有问题
        '''
        if n<=0:
            print('something Wrong')
            return 1
        arr = [0] * (n+1)   # 如n=3，申请了4个列表空间，且初始化为0
        arr[n] = 1          # 最右边初始化为1
        while not arr[0]:   # arr[0] = 0 时进入while循环，arr[0] = 1 时退出循环
            print(''.join(map(str, arr[1:]))) # 因为a[0]作为判断位，所以只输出arr[1:]
            i = n+1         # i = 3 + 1 =4
            # 从左到右遍历数组的过程碰到9就继续往左移位
            while i > 1 and arr[i-1] == 9:
                i -= 1
            # 碰到第一个不为9就加一，右边的置0
            arr[i-1] += 1   # a[3] = a[3] + 1 = 1
            for j in range(i, n+1):  # range(4, 4) ，i没有向左移动，就不用把右边置0
                arr[j] = 0
        return 0
 
s = Solution()
flag=s.print_until_max_n(2)
flag=s.print_until_max_n(-1)