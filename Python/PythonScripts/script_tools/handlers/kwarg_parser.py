class KwargsParser:
    def __init__(self, rules):
        self.rules = rules

    def update_priority(self, rule_name, new_priority):
        """Update the priority of a rule."""
        if rule_name in self.rules:
            self.rules[rule_name]['priority'] = new_priority
        else:
            raise KeyError(f"Rule '{rule_name}' not found.")

    def parse(self, **kwargs):
        results = {}

        # Sorting rules based on priority
        sorted_rules = sorted(self.rules.items(), key=lambda x: x[1]['priority'])

        for key, rule in sorted_rules:
            value = kwargs.get(key, rule.get('default'))

            if 'expected_type' in rule and not isinstance(value, rule['expected_type']):
                raise TypeError(f"{key} should be of type {rule['expected_type']}")

            results[key] = rule['action'](value) if 'action' in rule else value

        return results


