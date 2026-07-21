class Solution {
    public int findDuplicate(int[] nums) {
        List<Integer> list = new LinkedList<>();
        for(int i=0;i<nums.length;i++)
        {
            if(list.contains(nums[i]))
                return nums[i];
            else
                list.add(nums[i]);
        }
        return 0;
    }
}
