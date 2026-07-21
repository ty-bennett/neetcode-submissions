/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0,head);
        ListNode prevgroup = dummy;

        while(true)
        {
            ListNode kth = getKth(prevgroup, k);
            if(kth == null) { break; }
            ListNode groupNext = kth.next;

            ListNode prev = kth.next;
            ListNode curr = prevgroup.next;
            while(curr != groupNext) {
                ListNode tmp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = tmp;
            } 

            ListNode tmp = prevgroup.next;
            prevgroup.next = kth;
            prevgroup = tmp;
        }
        return dummy.next;
    }

    private ListNode getKth(ListNode curr, int k)
    {
        while(curr != null && k > 0)
        {
            curr = curr.next;
            k--;
        }
        return curr;
    }
}
