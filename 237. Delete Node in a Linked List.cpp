/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode *next = node -> next;
        *node = *next;
        delete next;
    }
};

class Solution {
public:
    void deleteNode(ListNode* node) {
        ListNode *pre;
        while (node) {
            if (node -> next) {
                node -> val = node -> next -> val;
                pre = node;
                node = node -> next;
            } else {
                if (pre) pre -> next = NULL; // ATTENTION
                node = NULL; // attention
            }
        }
    }
};
