// !!!!!OMG I DID IT!!!!! I CANNOT BELIEVE I DID IT!!!
// I ACed at the very first try!!!!! UNBELIEVABLE!!!
// It's a linked list involving so many operations!!!
// I'm on a roll right now...
// Time: O(n), space: O(1)
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
    ListNode* oddEvenList(ListNode* head) {
        if (!head || !(head->next)) return head;
        ListNode *odd = head, *even = head -> next;
        ListNode *cur = even -> next;
        while (cur) {
            ListNode *oddnext = odd -> next;
            odd -> next = cur;
            even -> next = cur -> next;
            even = even -> next;
            cur -> next = oddnext;
            odd = cur;
            if (even) cur = even -> next;
            else break;
        }
        
        return head;
    }
};
