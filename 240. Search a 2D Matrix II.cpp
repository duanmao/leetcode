// 以矩阵左下角为起点，向上所有的元素都比它小，向右所有的元素都比它大
// 因此若target比它小则向上走，比它大则向右走，若走出了矩阵边界则说明不存在

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0) return false;
        int m = matrix.size();
        int n = matrix[0].size();
        int row = m - 1, column = 0;
        while (row >= 0 && column < n) {
            if (matrix[row][column] == target) return true;
            else if (matrix[row][column] < target) ++column;
            else --row;
        }
        
        return false;
    }
};
