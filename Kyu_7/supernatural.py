drunkenDoodling = {
    'ghost': "Salt and iron, and don't forget to burn the corpse",
    'wendigo': 'Burn it to death',
    'phoenix': 'Use the colt',
    'angel': 'Use the angelic blade',
    'werewolf': 'Silver knife or bullet to the heart',
    'shapeshifter': 'Silver knife or bullet to the heart',
    'rugaru': 'Burn it alive',
    'reaper': "If it's nasty, you should gank who controls it",
    'demon': "Use Ruby's knife, or some Jesus-juice",
    'vampire': 'Behead it with a machete',
    'dragon': 'You have to find the excalibur for that',
    'leviathan': 'Use some Borax, then kill Dick',
    'witch': 'They are humans',
    'djinn': "Stab it with silver knife dipped in a lamb's blood",
    'pagan god': 'It depends on which one it is',
    'skinwalker': 'A silver bullet will do it',
    'jefferson starship': 'Behead it with a silver blade',
    'ghoul': 'Behead it'
}


def bob(what):
    return '{}, idjits!'.format(drunkenDoodling.get(
        what, 'I have friggin no idea yet'))
