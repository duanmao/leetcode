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
    ListNode* reverseList(ListNode* head) {
        ListNode *rhead = head;
        ListNode *node = head;
        while (node) {
            ListNode *next = node -> next;
            if (node != head) node -> next = rhead;
            else node -> next = NULL; // ATTENTION!
            rhead = node;
            node = next;
        }
        
        return rhead;
    }
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *rhead = NULL;
        reverse(head, rhead);
        return rhead;
    }
    
    ListNode *reverse(ListNode *node, ListNode *&rhead) {
        if (!node) return NULL;
        ListNode *tail = reverse(node -> next, rhead);
        if (tail) tail -> next = node;
        else rhead = node; // ATTENTION..._(:з」∠)_
        node -> next = NULL;
        return node;
    }
};
