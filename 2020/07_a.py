import re
from functools import lru_cache

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
    @lru_cache(maxsize=None)
    def contains_shiny_bag(bag_color):
        return any(
            child_bag_color == SHINY_BAG or contains_shiny_bag(child_bag_color)
            for child_bag_color in content_rules[bag_color].keys()
        )

    return len([
        bag_color
        for bag_color
        in content_rules.keys()
        if contains_shiny_bag(bag_color)
    ])


file_name = '07.txt'
bag_rules = parse_input(file_name)
solution = solve(bag_rules)
print(solution)
