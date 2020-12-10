import re

import common

def _parse_bag_color_rule(bag_color_rule_string):
    bag_color, bag_contents_string = re.search(
        rf'^([\w ]+) bags contain (.*)\.$',
        bag_color_rule_string
    ).groups()
    content_rules = {}
    if bag_contents_string != 'no other bags':
        content_rules = {
            child_bag_color: int(num_bags)
            for num_bags, child_bag_color
            in re.findall(r'(?:(\d+) ([\w ]+) bags?)+', bag_contents_string)
        }
    return bag_color, content_rules


def parse_input(file_name):
    return {
        parent_bag_color: content_rules
        for parent_bag_color, content_rules
        in (
            _parse_bag_color_rule(bag_color_rule_string)
            for bag_color_rule_string in common.get_input_lines(file_name)
        )
    }


def solve(content_rules):
    SHINY_BAG = 'shiny gold'
    def child_bag_count(bag_color):
        return sum(
            num_child_bags * (1 + child_bag_count(child_bag_color))
            for child_bag_color, num_child_bags
            in content_rules[bag_color].items()
        )
    return child_bag_count(SHINY_BAG)


file_name = '7.txt'
bag_rules = parse_input(file_name)
solution = solve(bag_rules)
print(solution)
