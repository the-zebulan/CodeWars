def any_arrows(arrows):
    return any(not arrow.get('damaged', False) for arrow in arrows)

assert any_arrows([]) is False
assert any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]) is True
assert any_arrows([{'range': 10, 'damaged': True}, {'damaged': True}]) is False
assert any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]) is True
