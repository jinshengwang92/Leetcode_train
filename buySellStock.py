#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
#-*-coding:utf-8-*-

# this is test of leetcode solutions
'''
Given a list as prices of stock, find the index to buy and sell that results in
the highest profit and print them out.
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        lowest_p = prices[0]
        lowest_ind = 0
        highest_p = prices[0]
        highest_ind = 0
        buy_p = prices[0]
        buy_ind = 0
        sell_p = prices[0]
        sell_ind = 0
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < lowest_p:
                lowest_p = prices[i]
                lowest_ind = i
            if prices[i] > highest_p:
                highest_p = prices[i]
                highest_ind = i

            if prices[i] - lowest_p > maxprofit:
                sell_p = prices[i]
                sell_ind = i
                maxprofit = prices[i] - lowest_p
                buy_p = lowest_p
                buy_ind = lowest_ind
        print('--- Max profit is {0}\n--- Buy at Day {1}\n--- Sell at Day {2}'.format(maxprofit,buy_ind+1,sell_ind+1))
        print('--- Highest price is {0} at day {1}'.format(highest_p,highest_ind+1))
        print('--- Lowest price is {0} at day {1}'.format(lowest_p,lowest_ind+1))
        return buy_ind+1,sell_ind+1,maxprofit,

def main():
    case = Solution()
    ans = case.maxProfit([10,2,5,6,3,6,9,3,5,6,0.5,10,11])
    print(ans)

if __name__ == "__main__":
    main()
