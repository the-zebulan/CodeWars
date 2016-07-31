from collections import defaultdict


def generate_report(records):
    group_id_output = 'Group: {}'.format
    group_total_output = '    Group total: {:>21}\n'.format
    product_id_value_output = '    Product: {} Value: {:>6}'.format
    products = defaultdict(lambda: defaultdict(int))
    result = []
    total = 0
    for product_id, group_id, value in records:
        products[group_id][product_id] += value
    for group_id, group_products in sorted(products.iteritems()):
        group_total = 0
        result.append(group_id_output(group_id))
        for product_id, product_value in sorted(group_products.iteritems()):
            group_total += product_value
            result.append(product_id_value_output(product_id, product_value))
        result.append(group_total_output(group_total))
        total += group_total
    result.append('Total: {:>31}'.format(total))
    return '\n'.join(result)
