/**
 *  * Definition for singly-linked list.
 *   * struct ListNode {
 *    *     int val;
 *     *     ListNode *next;
 *      *     ListNode(int x) : val(x), next(NULL) {}
 *       * };
 *        */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
                if (headA == NULL || headB == NULL)
                    return NULL;
                int lA = length(headA);
                int lB = length(headB);
                int par = abs(lA - lB);
                
                if(lA > lB)
                    for(int i=0; i<par; i++)
                        headA = headA->next;
                else
                    for(int i=0; i<par; i++)
                        headB = headB->next;
                while (headA != NULL) {
                    if (headA->val == headB->val) 
                        return headA;
                    headA = headA->next;
                    headB = headB->next;
                }
        return NULL;
    }
    
    int length(ListNode *n) {
        if (n == NULL) 
            return 0;
        int length = 0;
        while (n != NULL) {
            length++;
            n = n->next;
        }
        return length;
    }
};
