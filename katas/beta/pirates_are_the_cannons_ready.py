def cannons_ready(gunners):
    return 'Fire!' if all(a == 'aye' for a in gunners.itervalues()) else \
        'Shiver me timbers!'
