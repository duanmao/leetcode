// Time: O(n), space: O(1)
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        random_shuffle(nums.begin(), nums.end());
        int n = nums.size();
        int low = 0, high = n - 1;
        while (low < high) {
            int pos = split(nums, low, high);
            if (pos == k - 1) break; // attention k - 1 here
            else if (pos < k) low = pos + 1;
            else high = pos - 1;
        }
        
        return nums[k - 1]; // attention k - 1 here
    }
    
    int split(vector<int> &nums, int low, int high) {
        int target = nums[low];
        int ptr = low;
        for (int i = low + 1; i <= high; ++i) {
            if (nums[i] > target) swap(nums[i], nums[++ptr]);
        }
        
        swap(nums[low], nums[ptr]);
        return ptr;
    }
};

// Time: O(nlogk), space: O(k)
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> heap;
        for (int num : nums) {
            heap.push(num);
            if (heap.size() > k) heap.pop();
        }
        
        return heap.top();
    }
};

// Time: O(nlogk), space: O(k)
// This implements priority_queue, or say heap, manually
// instead of using the library
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        vector<int> heap;
        for (int num : nums) {
            push(heap, num);
            // print(heap);
            if (heap.size() > k) pop(heap);
            // print(heap);
        }
        
        return heap[0];
    }
    
    void print(vector<int> &nums) {
        for (int num : nums) cout << num << " ";
        cout << endl;
    }
    
    void push(vector<int> &heap, int num) {
        heap.push_back(num);
        sift_up(heap);
    }
    
    void sift_up(vector<int> &heap) {
        int n = heap.size();
        int cur = n - 1;
        int prt = (cur - 1) / 2;
        while (cur > 0 && heap[cur] < heap[prt]) {
            swap(heap[cur], heap[prt]);
            cur = prt;
            prt = (cur - 1) / 2;
        }
    }
    
    void pop(vector<int> &heap) {
        if (heap.empty()) return;
        int n = heap.size();
        swap(heap[0], heap[n - 1]);
        heap.pop_back();
        sift_down(heap);
    }
    
    void sift_down(vector<int> &heap) {
        int n = heap.size();
        int cur = 0;
        int left = cur * 2 + 1, right = (cur + 1) * 2;
        while ((left < n && heap[cur] > heap[left]) || (right < n && heap[cur] > heap[right])) {
            if (right < n && heap[right] < heap[left]) { // attention check right here
                swap(heap[cur], heap[right]);
                cur = right;
            } else { // here handles more conditions than you may have thought
                swap(heap[cur], heap[left]);
                cur = left;
            }
            
            left = cur * 2 + 1;
            right = (cur + 1) * 2;
        }
    }
};
