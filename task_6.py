types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_dupes(data):
    uniques = set()
    new_data = {}
    for key, value in data.items():
        result = []
        for ticket in value:
            if ticket not in uniques:
                uniques.add(ticket)
                result.append(ticket)
        new_data[key] = result
    return new_data



def apply_types(keys, vals):
    new_tickets = {}
    for index, v in enumerate(vals.values()):
        key = keys.get(index+1)
        new_tickets[key] = v
    return new_tickets

deduped = remove_dupes(tickets)
typed = apply_types(types, deduped)
