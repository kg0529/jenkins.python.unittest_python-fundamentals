# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"
        # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add)
        # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index+1]
        # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index+1:ending_index]
        # TODO - Implement solution

    def compare(self, first_value, second_value):
        if first_value == None or False:
            first_value = 0
            return first_value == second_value
        elif first_value == True:
            first_value = 1
            return first_value == second_value
        else:
            return first_value == second_value
        # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        mid_index = len(string_to_fetch_from) / 2 - 1
        return string_to_fetch_from[mid_index]
        # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        temp_string_first = string_to_fetch_from.split(" ")
        return temp_string_first[0]
        # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        temp_string_second = string_to_fetch_from.split(" ")
        return temp_string_second[1]
        # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]
        # TODO - Implement solution