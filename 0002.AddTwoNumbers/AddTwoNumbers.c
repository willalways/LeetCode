/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
        int start, end, carry = 0;
        struct ListNode *ret = (struct ListNode *)malloc(sizeof(struct ListNode) * 4096);
        struct ListNode tmp = {0};

        start = end = 0;
        int x;
        while (l1 || l2 || carry)
        {
                if (!l1)
                        l1 = &tmp;
                if (!l2)
                        l2 = &tmp;
                x = l1->val + l2->val + carry;
                carry = x / 10;
                ret[end + 1].val = x % 10;
                ret[end + 1].next = NULL;
                ret[end].next = &ret[end + 1];
                l1 = l1->next;
                l2 = l2->next;
                end++;
        }

        return ret + 1;
}