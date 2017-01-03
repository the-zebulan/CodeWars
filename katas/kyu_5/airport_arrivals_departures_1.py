def flap_display(lines, rotors):
    az = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
    result = []
    for line, rotor_moves in zip(lines, rotors):
        new_line = list(line)
        for i, rotor in enumerate(rotor_moves):
            new_line[i:] = [az[(az.index(a) + rotor) % len(az)]
                            for a in new_line[i:]]
        result.append(''.join(new_line))
    return result
