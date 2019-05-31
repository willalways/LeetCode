/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *mergeKLists(struct ListNode **lists, int listsSize)
{
        int finish = 1, i, j;
        struct ListNode *start, *cur, *min;
        start = cur = min = NULL;

        while (1)
        {
                min = NULL;
                for (i = 0; i < listsSize; i++)
                {
                        if (lists[i] != NULL)
                        {
                                if (min == NULL)
                                {
                                        min = lists[i];
                                        j = i;
                                }
                                else if (lists[i]->val < min->val)
                                {
                                        min = lists[i];
                                        j = i;
                                }
                        }
                }
                if (!min)
                        break;
                if (start == NULL)
                {
                        start = cur = min;
                }
                else
                {
                        cur->next = min;
                        cur = cur->next;
                }
                lists[j] = lists[j]->next;
        }

        return start;
}