#include <vector>
#include <map>
#include <iostream>
#include <stdio.h>

using namespace std;

class Solution
{
public:
        vector<int> twoSum(vector<int> &nums, int target)
        {
                map<int, int> hashmap;

                for (int i = 0; i < nums.size(); i++)
                {
                        if (hashmap.find(target - nums[i]) != hashmap.end())
                                return vector<int>{hashmap[target - nums[i]], i};
                        hashmap[nums[i]] = i;
                }
        }
};