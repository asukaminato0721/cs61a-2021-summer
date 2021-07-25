test = {
  'name': 'Problem 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 3]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
          [['What', 'luck'], ['great']]
          >>> p2 = [4, 3, 1]
          >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
          [['What'], ['great'], ['luck']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p0 = [5, 1, 3]
          >>> p1 = [4, 1, 6]
          >>> fastest_words(game(['Just', 'have', 'fun'], [p0, p1]))
          [['have', 'fun'], ['Just']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 5, 1]]
          >>> fastest_words(game(['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly'], p))
          [['newsstand', 'stereochromy', 'quinaldine', 'invalidate', 'japingly']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1], [2, 5, 5]]
          >>> fastest_words(game(['unstatesmanlike', 'median', 'cueca'], p))
          [['median', 'cueca'], ['unstatesmanlike']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2, 4, 3]]
          >>> fastest_words(game(['introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene'], p))
          [['introspectional', 'squamigerous', 'sair', 'heterodromy', 'butylene']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 5, 2, 1, 5], [3, 5, 3, 5, 4, 1], [2, 1, 3, 1, 2, 3]]
          >>> fastest_words(game(['musiclike', 'nonregarding', 'oxypropionic', 'postvide', 'muncheel', 'reburial'], p))
          [['musiclike', 'muncheel'], ['oxypropionic', 'reburial'], ['nonregarding', 'postvide']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 1, 1, 5, 2], [1, 4, 5, 4, 2], [5, 3, 2, 2, 3]]
          >>> fastest_words(game(['nuggety', 'phlegmatous', 'doomsman', 'butterfingered', 'scouse'], p))
          [['phlegmatous', 'doomsman', 'scouse'], ['nuggety'], ['butterfingered']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5], [3], [3]]
          >>> fastest_words(game(['cixiid'], p))
          [[], ['cixiid'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(game(['accredit'], p))
          [['accredit']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1]]
          >>> fastest_words(game(['electroextraction'], p))
          [['electroextraction']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 5, 4], [1, 3, 2, 1], [4, 2, 5, 1]]
          >>> fastest_words(game(['termolecular', 'unbeatably', 'unamenable', 'ratio'], p))
          [['unbeatably'], ['termolecular', 'unamenable', 'ratio'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 3, 1], [2, 1, 3, 1, 5]]
          >>> fastest_words(game(['interlardment', 'supercargo', 'inquilinity', 'mackenboy', 'trauma'], p))
          [['interlardment', 'supercargo', 'inquilinity', 'trauma'], ['mackenboy']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 2, 3], [4, 3, 1, 1, 5], [3, 2, 4, 5, 4]]
          >>> fastest_words(game(['chromo', 'casson', 'unpliableness', 'overweeningly', 'unsquandered'], p))
          [['chromo', 'casson', 'unsquandered'], ['unpliableness', 'overweeningly'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 1, 1]]
          >>> fastest_words(game(['negotiatrix', 'attaintment', 'concurringly', 'glyoxaline'], p))
          [['negotiatrix', 'attaintment', 'concurringly', 'glyoxaline']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 4, 2, 1, 3]]
          >>> fastest_words(game(['marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity'], p))
          [['marble', 'undeleted', 'subrogation', 'lownly', 'nebulosity']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 1, 1, 1, 3], [3, 5, 1, 2, 3, 3]]
          >>> fastest_words(game(['pectous', 'kathal', 'supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber'], p))
          [['kathal', 'supercargoship', 'keelblock', 'celiosalpingectomy', 'pronumber'], ['pectous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2, 2, 1, 3], [3, 4, 4, 4, 2, 2]]
          >>> fastest_words(game(['coalhole', 'osmotic', 'barnard', 'irreligiousness', 'nitrobacteria', 'cellarless'], p))
          [['osmotic', 'barnard', 'irreligiousness', 'nitrobacteria'], ['coalhole', 'cellarless']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 3, 3], [1, 1, 3], [2, 3, 3]]
          >>> fastest_words(game(['incendiarism', 'carbamide', 'families'], p))
          [['families'], ['incendiarism', 'carbamide'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 3, 2, 3, 3], [5, 1, 2, 4, 2, 5]]
          >>> fastest_words(game(['heaps', 'kitling', 'workhouse', 'scriver', 'chilicothe', 'anteprandial'], p))
          [['heaps', 'kitling', 'scriver', 'anteprandial'], ['workhouse', 'chilicothe']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 1, 3], [3, 4, 4, 1], [1, 2, 3, 3]]
          >>> fastest_words(game(['brat', 'structureless', 'opacous', 'successfully'], p))
          [['structureless', 'opacous'], ['successfully'], ['brat']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 5], [3, 5, 1, 3]]
          >>> fastest_words(game(['saponify', 'bakerless', 'nonluminous', 'zonesthesia'], p))
          [['bakerless', 'nonluminous'], ['saponify', 'zonesthesia']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 5, 4], [5, 4, 3], [4, 4, 4]]
          >>> fastest_words(game(['uranophane', 'whereso', 'toolmaking'], p))
          [['uranophane'], ['whereso', 'toolmaking'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 1, 5, 5, 2, 5]]
          >>> fastest_words(game(['ali', 'indult', 'palmitic', 'carbon', 'scudder', 'novaculite'], p))
          [['ali', 'indult', 'palmitic', 'carbon', 'scudder', 'novaculite']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 3, 2, 4, 2], [5, 1, 3, 4, 1, 3]]
          >>> fastest_words(game(['telangiectasy', 'unratable', 'dissolvableness', 'redheadedly', 'recluse', 'galloon'], p))
          [['telangiectasy', 'dissolvableness', 'redheadedly', 'galloon'], ['unratable', 'recluse']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5], [1]]
          >>> fastest_words(game(['incorporable'], p))
          [[], ['incorporable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4], [2, 1, 2]]
          >>> fastest_words(game(['accresce', 'during', 'unreproachableness'], p))
          [['accresce', 'during'], ['unreproachableness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 4, 2, 2], [2, 4, 3, 3, 5]]
          >>> fastest_words(game(['counterprotection', 'karyolysis', 'contuse', 'esophagomalacia', 'investigatorial'], p))
          [['karyolysis', 'esophagomalacia', 'investigatorial'], ['counterprotection', 'contuse']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 3, 2, 5, 4], [2, 4, 2, 3, 4, 1]]
          >>> fastest_words(game(['driftpiece', 'archaic', 'oreotragine', 'nystagmic', 'refute', 'wellhole'], p))
          [['driftpiece', 'archaic', 'nystagmic'], ['oreotragine', 'refute', 'wellhole']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 4], [4, 3]]
          >>> fastest_words(game(['colly', 'ransackle'], p))
          [[], ['colly', 'ransackle']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 1, 4], [4, 1, 1, 2]]
          >>> fastest_words(game(['clodpated', 'subcouncil', 'digestment', 'hierocratic'], p))
          [['clodpated', 'digestment'], ['subcouncil', 'hierocratic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 3], [5, 2]]
          >>> fastest_words(game(['swearingly', 'pimple'], p))
          [['swearingly'], ['pimple']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 4]]
          >>> fastest_words(game(['unbungling', 'rizzle', 'undistinguishableness'], p))
          [['unbungling', 'rizzle', 'undistinguishableness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 3, 2], [2, 5, 1]]
          >>> fastest_words(game(['nonassortment', 'gowan', 'uneducable'], p))
          [['gowan'], ['nonassortment', 'uneducable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [5]]
          >>> fastest_words(game(['uninterlocked'], p))
          [['uninterlocked'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 3, 4], [3, 4, 4]]
          >>> fastest_words(game(['boldness', 'uraniid', 'inherently'], p))
          [['boldness', 'uraniid', 'inherently'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3]]
          >>> fastest_words(game(['eartab', 'wileful', 'manioc'], p))
          [['eartab', 'wileful', 'manioc']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [3, 3, 3], [5, 4, 3]]
          >>> fastest_words(game(['pargeboard', 'liquidly', 'nongentile'], p))
          [['nongentile'], ['pargeboard', 'liquidly'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 5, 4]]
          >>> fastest_words(game(['remonetize', 'crustation', 'syntypicism'], p))
          [['remonetize', 'crustation', 'syntypicism']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 2], [1, 2, 2], [1, 1, 5]]
          >>> fastest_words(game(['photomezzotype', 'durian', 'precompletion'], p))
          [['precompletion'], ['photomezzotype'], ['durian']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 4, 1, 4], [3, 1, 1, 3, 4]]
          >>> fastest_words(game(['bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal', 'heading'], p))
          [['supraseptal', 'heading'], ['bloodstroke', 'dioestrous', 'heterochthonous']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 1]]
          >>> fastest_words(game(['podgily', 'collectivism', 'mitotically'], p))
          [['podgily', 'collectivism', 'mitotically']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 3, 5, 5], [1, 3, 4, 3, 4], [2, 5, 5, 1, 4]]
          >>> fastest_words(game(['haematosepsis', 'apomecometry', 'yrs', 'briefly', 'urinometric'], p))
          [['apomecometry', 'yrs'], ['haematosepsis', 'urinometric'], ['briefly']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [2], [1]]
          >>> fastest_words(game(['prophasis'], p))
          [['prophasis'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 4, 4], [3, 4, 4, 2]]
          >>> fastest_words(game(['diploglossate', 'fatalistic', 'ow', 'disquietedness'], p))
          [['diploglossate', 'fatalistic', 'ow'], ['disquietedness']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 3, 5], [2, 3, 3, 3, 2]]
          >>> fastest_words(game(['carbomethoxyl', 'dianilid', 'strack', 'whacky', 'stationery'], p))
          [['dianilid', 'strack', 'whacky'], ['carbomethoxyl', 'stationery']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1], [1, 2]]
          >>> fastest_words(game(['dysmetria', 'cl'], p))
          [['cl'], ['dysmetria']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [1, 4]]
          >>> fastest_words(game(['rippable', 'hectical'], p))
          [['hectical'], ['rippable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4, 5, 2], [3, 2, 1, 5]]
          >>> fastest_words(game(['scleranth', 'perdricide', 'renably', 'sorn'], p))
          [['scleranth', 'sorn'], ['perdricide', 'renably']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 2, 1, 4, 1], [2, 3, 2, 3, 1], [2, 5, 2, 3, 1]]
          >>> fastest_words(game(['mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous'], p))
          [['mien', 'wellness', 'antitobacconist', 'sarcogenous'], ['zoosporangiophore'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4]]
          >>> fastest_words(game(['nonactinic'], p))
          [['nonactinic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 1], [4, 2, 1, 2]]
          >>> fastest_words(game(['prefacer', 'parasynetic', 'podogyne', 'ravissant'], p))
          [['prefacer', 'parasynetic', 'ravissant'], ['podogyne']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4], [1]]
          >>> fastest_words(game(['toxic'], p))
          [[], ['toxic']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4], [3, 2], [5, 4]]
          >>> fastest_words(game(['orchiocatabasis', 'brangling'], p))
          [['orchiocatabasis'], ['brangling'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 4, 3]]
          >>> fastest_words(game(['brushed', 'removedness', 'peenge', 'equid'], p))
          [['brushed', 'removedness', 'peenge', 'equid']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 1, 3, 1, 3, 1]]
          >>> fastest_words(game(['hyperdulic', 'crimple', 'soother', 'overkind', 'cinnamaldehyde', 'veretilliform'], p))
          [['hyperdulic', 'crimple', 'soother', 'overkind', 'cinnamaldehyde', 'veretilliform']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 2, 1, 2], [2, 3, 5, 3, 3], [3, 3, 1, 4, 1]]
          >>> fastest_words(game(['parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind'], p))
          [['parapsidal', 'unattendance', 'wheelwright'], [], ['expirable', 'rind']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 4, 3, 1]]
          >>> fastest_words(game(['plethoretical', 'plantlike', 'electrotechnology', 'superioress'], p))
          [['plethoretical', 'plantlike', 'electrotechnology', 'superioress']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 4], [4, 2]]
          >>> fastest_words(game(['spermatophore', 'sapping'], p))
          [['spermatophore'], ['sapping']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 5, 4], [4, 4, 1, 4], [4, 2, 2, 1]]
          >>> fastest_words(game(['gangrenous', 'lostness', 'doctrinarian', 'nonphosphorized'], p))
          [[], ['gangrenous', 'doctrinarian'], ['lostness', 'nonphosphorized']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 2], [1, 2, 1], [1, 5, 3]]
          >>> fastest_words(game(['undisparaged', 'polarly', 'baldachino'], p))
          [['polarly'], ['undisparaged', 'baldachino'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 1, 1, 5, 2, 5], [3, 2, 1, 5, 2, 3], [1, 5, 3, 3, 3, 4]]
          >>> fastest_words(game(['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly'], p))
          [['renominate', 'quondam', 'staysail'], ['unfleshly'], ['wraprascal', 'gullibility']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 2, 1], [3, 2, 4]]
          >>> fastest_words(game(['tarsoplasty', 'unprincipal', 'myrmicoid'], p))
          [['tarsoplasty', 'unprincipal', 'myrmicoid'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 1]]
          >>> fastest_words(game(['fibrinate', 'pillarlet', 'widdendream'], p))
          [['fibrinate', 'pillarlet', 'widdendream']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 1], [4, 2], [3, 2]]
          >>> fastest_words(game(['undisinfected', 'unnapkined'], p))
          [['undisinfected', 'unnapkined'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2, 5], [3, 4, 2], [4, 4, 1]]
          >>> fastest_words(game(['gmbh', 'toothy', 'achromatism'], p))
          [['toothy'], ['gmbh'], ['achromatism']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 4]]
          >>> fastest_words(game(['wapp', 'matrix', 'pitfall', 'bardel'], p))
          [['wapp', 'matrix', 'pitfall', 'bardel']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5, 1, 4, 5, 5], [1, 4, 5, 2, 3, 5]]
          >>> fastest_words(game(['yoven', 'lovably', 'sheepmonger', 'molave', 'hate', 'walloon'], p))
          [['sheepmonger', 'walloon'], ['yoven', 'lovably', 'molave', 'hate']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3], [1, 2]]
          >>> fastest_words(game(['ferrohydrocyanic', 'wambly'], p))
          [['ferrohydrocyanic'], ['wambly']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2, 3, 5, 1, 2]]
          >>> fastest_words(game(['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry'], p))
          [['lactase', 'pleionian', 'guige', 'tellureted', 'magistratically', 'playwrightry']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], []]
          >>> fastest_words(game([], p))
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 2], [5, 2, 4], [4, 4, 2]]
          >>> fastest_words(game(['apparent', 'natron', 'mazopathia'], p))
          [['apparent', 'mazopathia'], ['natron'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1], [5], [1]]
          >>> fastest_words(game(['agamid'], p))
          [['agamid'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 2, 5, 1, 3], [1, 4, 4, 1, 4], [1, 4, 3, 4, 2]]
          >>> fastest_words(game(['belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry'], p))
          [['belord', 'vermeology', 'phellodermal'], [], ['wrive', 'weaponry']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[]]
          >>> fastest_words(game([], p))
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 5, 2], [3, 4, 1, 1], [5, 2, 1, 2]]
          >>> fastest_words(game(['swarfer', 'threap', 'philosophistical', 'pushwainling'], p))
          [['swarfer'], ['philosophistical', 'pushwainling'], ['threap']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 3], [3, 3]]
          >>> fastest_words(game(['unilocularity', 'fumigant'], p))
          [['fumigant'], ['unilocularity']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3, 5, 3, 5, 2, 2], [1, 3, 2, 3, 5, 1], [2, 3, 5, 2, 4, 4]]
          >>> fastest_words(game(['stageably', 'rattlejack', 'corium', 'crumbable', 'coelialgia', 'agape'], p))
          [['coelialgia'], ['stageably', 'rattlejack', 'corium', 'agape'], ['crumbable']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5], [3, 3], [3, 2]]
          >>> fastest_words(game(['boycottism', 'yo'], p))
          [[], ['boycottism'], ['yo']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[2, 1, 5], [5, 2, 4]]
          >>> fastest_words(game(['spry', 'agrobiological', 'zaphara'], p))
          [['spry', 'agrobiological'], ['zaphara']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[], [], []]
          >>> fastest_words(game([], p))
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[3], [5], [3]]
          >>> fastest_words(game(['durational'], p))
          [['durational'], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 2]]
          >>> fastest_words(game(['fungous', 'script'], p))
          [['fungous', 'script']]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 4, 5], [1, 3, 4], [5, 5, 5]]
          >>> fastest_words(game(['immusical', 'azimine', 'commentarialism'], p))
          [[], ['immusical', 'azimine', 'commentarialism'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 2], [2, 5], [2, 3]]
          >>> fastest_words(game(['wettish', 'carthame'], p))
          [['carthame'], ['wettish'], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[5, 5, 2], [4, 2, 2]]
          >>> fastest_words(game(['stilted', 'sensorivascular', 'disadvantageously'], p))
          [['disadvantageously'], ['stilted', 'sensorivascular']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import game, fastest_words
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats)
          >>> p0 = [2, 2, 3]
          >>> p1 = [6, 1, 2]
          >>> cats.fastest_words(cats.game(['What', 'great', 'luck'], [p0, p1]))
          [['What'], ['great', 'luck']]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import cats
      >>> import tests.abstraction_check as test # make sure the abstraction barrier isn't crossed!
      """,
      'teardown': r"""
      >>> test.restore_implementations(cats)
      """,
      'type': 'doctest'
    }
  ]
}
