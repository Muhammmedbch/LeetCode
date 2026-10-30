# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        def reverse_list(o_list):
            r_list = []

            ptr = o_list
            while ptr is not None:
                r_list.append(ptr.val)
                ptr = ptr.next

            return r_list[::-1]

        def convert_list_to_number(n_list):
            converted_number = 0
            num = 1

            for value in n_list:
                converted_number += value * (10 ** (len(n_list) - num))
                num += 1

            return converted_number

        def convert_number_to_list(num):
            digits = []

            for letter in str(num):
                digits.append(int(letter))

            return digits[::-1]

        # Convert linked lists into reversed lists
        r_list1 = reverse_list(l1)
        r_list2 = reverse_list(l2)

        # Convert lists into numbers
        c_num1 = convert_list_to_number(r_list1)
        c_num2 = convert_list_to_number(r_list2)

        # Add the numbers
        result_num = c_num1 + c_num2

        # Convert result into a reversed list
        result_list = convert_number_to_list(result_num)

        # Convert the result list into a linked list
        head = ListNode(result_list[0])
        ptr = head

        for digit in result_list[1:]:
            ptr.next = ListNode(digit)
            ptr = ptr.next

        return head