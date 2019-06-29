// Time: O(n), space: O(1)
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MAX;
        int profit = 0;
        for (int price : prices) {
            buy = min(buy, price);
            profit = max(profit, price - buy);
        }
        
        return profit;
    }
};

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int current = 0;
        for (int i = 1; i < prices.size(); ++i) {
            current = max(0, current + prices[i] - prices[i - 1]);
            maxprofit = max(maxprofit, current);
        }

        return maxprofit;
    }
};
