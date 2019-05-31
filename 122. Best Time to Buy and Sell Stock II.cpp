class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int bought = -1;
        int n = prices.size();
        for (int i = 0; i < n; ++i) {
            if (bought == -1 && i < n - 1 && prices[i] < prices[i + 1]) {
                bought = i;
            } else if (bought != -1 && (i == n - 1 || prices[i] > prices[i + 1])) {
                // remember to handle i == n - 1 case
                profit += prices[i] - prices[bought];
                bought = -1;
            }
        }
        
        return profit;
    }
};
