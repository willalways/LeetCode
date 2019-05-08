/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution
{
public:
        ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
        {
                ListNode *ret = NULL, *first = NULL;

                int carry = 0;
                while (l1 || l2)
                {
                        ListNode *node = (ListNode *)malloc(sizeof(ListNode));
                        if (l1 && l2)
                                node->val = l1->val + l2->val + carry;
                        else if (l1)
                                node->val = l1->val + carry;
                        else if (l2)
                                node->val = l2->val + carry;

                        carry = node->val / 10;
                        node->val %= 10;
                        node->next = NULL;
                        if (!ret)
                                first = ret = node;
                        else
                                ret->next = node, ret = ret->next;

                        if (l1)
                                l1 = l1->next;
                        if (l2)
                                l2 = l2->next;
                }
                if (carry)
                {
                        ListNode *node = (ListNode *)malloc(sizeof(ListNode));
                        node->val = 1;
                        node->next = NULL;
                        ret->next = node;
                }
                return first;
        }
};

static auto x = []() {
        // turn off sync
        std::ios::sync_with_stdio(false);
        // untie in/out streams
        std::cin.tie(NULL);
        return 0;
}();