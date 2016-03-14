def any_arrows(arrows):
    return any(not arrow.get('damaged', False) for arrow in arrows)
