class Solution:
    def mergeTwoLists(self, list1, list2):

        def LinkedListToArray(linked_list):
            array = []
            i = linked_list

            while i:
                array.append(i.val)
                i = i.next

            return array

        merged_array = LinkedListToArray(list1)
        merged_array += LinkedListToArray(list2)

        merged_array.sort()

        dummy = ListNode()
        current = dummy

        for value in merged_array:
            current.next = ListNode(value)
            current = current.next

        return dummy.next