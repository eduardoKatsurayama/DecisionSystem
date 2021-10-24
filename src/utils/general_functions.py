def approve_customer(flow, mis, to_approve, aa_code):
    index_to_drop = flow[flow['cpf'].isin(to_approve)].index
    flow.drop(index_to_drop, inplace=True)
    mis.loc[
        mis['cpf'].isin(to_approve),
        ['decision', 'approved']
    ] = aa_code, 1


def deny_customer(flow, mis, to_deny, na_code):
    index_to_drop = flow[flow['id'].isin(to_deny)].index
    flow.drop(index_to_drop, inplace=True)
    mis.loc[
        mis['id'].isin(to_deny),
        ['decision', 'approved']
    ] = na_code, 0
