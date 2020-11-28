## Leetcode

### 1. 栈、队列、堆

例题1. 用队列实现栈（栈、队列）[[link]](https://leetcode-cn.com/problems/implement-stack-using-queues/)

例题2. 用栈实现队列（栈、队列）[[link]](https://leetcode-cn.com/problems/implement-queue-using-stacks/)

例题3. 最小栈（栈）[[link]](https://leetcode-cn.com/problems/min-stack/)

例题4. 验证栈序列（栈、队列）[[link]](https://leetcode-cn.com/problems/validate-stack-sequences/)

例题5. 基本计算器（栈）[[link]](https://leetcode-cn.com/problems/basic-calculator/)

例题6. 数组中的第K个最大元素（堆）[[link]](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

例题7. 数据流的中位数（堆）[[link]](https://leetcode-cn.com/problems/find-median-from-data-stream/)

------------------------

### 2. 链表

例题1-a. 反转链表[[link]](https://leetcode-cn.com/problems/reverse-linked-list/)

例题1-b. 反转链表II[[link]](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

例题2. 相交链表[[link]](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)

例题3-a. 环形链表[[link]](https://leetcode-cn.com/problems/linked-list-cycle/)

例题3-b. 环形链表 II[[link]](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

例题4. 分隔链表[[link]](https://leetcode-cn.com/problems/partition-list/)

例题5. 复制带随机指针的链表[[link]](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)

例题6-a. 合并两个有序链表[[link]](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

例题6-b. 合并K个升序链表[[link]](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

------------

### 3. 贪心

例题1. 分发饼干[[link]](https://leetcode-cn.com/problems/assign-cookies/)（排序、贪心）

例题2. 摆动序列[[link]](https://leetcode-cn.com/problems/wiggle-subsequence/)（贪心）

例题3. 移掉K位数字[[link]](https://leetcode-cn.com/problems/remove-k-digits/)（栈、贪心）

例题4-a. 跳跃游戏[[link]](https://leetcode-cn.com/problems/jump-game/)（贪心）

例题4-b. 跳跃游戏 II[[link]](https://leetcode-cn.com/problems/jump-game-ii/)（贪心）

例题5. 用最少数量的箭引爆气球[[link]](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)（排序、贪心）

例题6. 最低加油次数[[link]](https://leetcode-cn.com/problems/minimum-number-of-refueling-stops/)（堆、贪心）

-------------------

### 4. 递归、回溯与分治

例题1-a. 子集[[link]](https://leetcode-cn.com/problems/subsets/)（回溯法、位运算法）

例题1-b. 子集 II[[link]](https://leetcode-cn.com/problems/subsets-ii/)（回溯法）

例题1-c. 组合总和[[link]](https://leetcode-cn.com/problems/combination-sum/)（回溯、剪枝）

例题1-d. 组合总和 II[[link]](https://leetcode-cn.com/problems/combination-sum-ii/)（回溯法、剪枝）

例题1-e. 全排列[[link]](https://leetcode-cn.com/problems/permutations/)（回溯法）

例题1-f. 全排列 II[[link]](https://leetcode-cn.com/problems/permutations-ii/)（回溯法）

例题2. 生成括号（递归设计）

例题3. N皇后（回溯法）

预备知识：分治算法与归并排序

例题4. 逆序数（分治法、归并排序应用）

--------------

### 5. 二叉树与图

----------------

### 6. 二分查找与二叉排序树

-----------

### 7. 哈希表与字符串

--------------

### 8. 搜索

------------------

### 9. 动态规划

例题1. 爬楼梯[[link]](https://leetcode-cn.com/problems/climbing-stairs/)

1. 确认原问题与子问题

   原问题为求n阶台阶所有走法的数量，子问题是求1阶台阶、2阶台阶、...、n-1阶台阶的走法。

2. 确认状态

   爬楼梯的动态规划状态单一，第i个状态即为i阶台阶的所有走法数量。

3. 确认边界状态的值

   边界状态为1阶台阶与2阶台阶的走法，1阶台阶有1种走法，2阶台阶有2种走法，即dp[1]=1，dp[2]=2。

4. 确定状态转移方程

   将求第i个状态的值转移为求第i-1个状态值与第i-2个状态的值，动态规划转移方程，dp[i]=dp[i-1]+dp[i-2]; (i>=3)

例题2. 打家劫舍[[link]](https://leetcode-cn.com/problems/house-robber/)

1. 确认原问题与子问题

   原问题为求n个房间的最优解，子问题为求前1个房间、前2个房间、...、前n-1个房间的最优解。

2. 确认状态

   第i个状态即为前i个房间能够获得的最大财宝（最优解）。

3. 确认边界状态的值

   前一个房间的最优解，第1个房间的财宝；

   前2个房间的最优解，第1、2个房间中较大的财宝。

4. 确定状态转移方程

   a. 选择第i个房间：第i个房间+前i-2个房间的最优解

   b. 不选择第i个房间：前i-1个房间的最优解

   动态规划转移方程：dp[i]=max(dp[i-1], dp[i-2]+nums[i]); (i>=3)

例题3. 最大子序和[[link]](https://leetcode-cn.com/problems/maximum-subarray/)

例题4. 零钱兑换[[link]](https://leetcode-cn.com/problems/coin-change/)

例题5. 三角形最小路径和[[link]](https://leetcode-cn.com/problems/triangle/)

例题6. 最长上升子序列[[link]](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

例题7. 最小路径和[[link]](https://leetcode-cn.com/problems/minimum-path-sum/)

例题8. 地下城游戏[[link]](https://leetcode-cn.com/problems/dungeon-game/)

---------------

### 10. 复杂数据结构











