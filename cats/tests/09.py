test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = time_per_word(p, words)
          >>> get_words(game)
          ['This', 'is', 'fun']
          >>> get_times(game)
          [[3, 2, 1], [4, 2, 3]]
          >>> p = [[0, 2, 3], [2, 4, 7]]
          >>> game = time_per_word(p, ['hello', 'world'])
          >>> word_at(game, word_index=1)
          'world'
          >>> get_times(game)
          [[2, 1], [2, 3]]
          >>> time(game, player_num=0, word_index=1)
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 86, 87, 92, 94], [21, 26, 27, 30, 31]]
          >>> game = time_per_word(p, ['colophonium', 'spatangoid', 'newsstand', 'stereochromy'])
          >>> get_words(game)
          ['colophonium', 'spatangoid', 'newsstand', 'stereochromy']
          >>> get_times(game)
          [[3, 1, 5, 2], [5, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[16, 18, 23, 28, 30, 33]]
          >>> game = time_per_word(p, ['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk'])
          >>> get_words(game)
          ['unstatesmanlike', 'median', 'cueca', 'meroplankton', 'foremilk']
          >>> get_times(game)
          [[2, 5, 5, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[72], [22]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[72, 73, 77]]
          >>> game = time_per_word(p, ['uncommixed', 'gentlewomanly'])
          >>> get_words(game)
          ['uncommixed', 'gentlewomanly']
          >>> get_times(game)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[87, 90, 93], [72, 74, 79]]
          >>> game = time_per_word(p, ['unmistakableness', 'musiclike'])
          >>> get_words(game)
          ['unmistakableness', 'musiclike']
          >>> get_times(game)
          [[3, 3], [2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[16, 21, 22, 23], [73, 77, 82, 86], [8, 9, 11, 16]]
          >>> game = time_per_word(p, ['antinoise', 'archcupbearer', 'opisthotonoid'])
          >>> get_words(game)
          ['antinoise', 'archcupbearer', 'opisthotonoid']
          >>> get_times(game)
          [[5, 1, 1], [4, 5, 4], [1, 2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79, 82, 83]]
          >>> game = time_per_word(p, ['nephros', 'cixiid'])
          >>> get_words(game)
          ['nephros', 'cixiid']
          >>> get_times(game)
          [[3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 58, 60, 63, 66]]
          >>> game = time_per_word(p, ['crural', 'accredit', 'deltation', 'esophagomalacia'])
          >>> get_words(game)
          ['crural', 'accredit', 'deltation', 'esophagomalacia']
          >>> get_times(game)
          [[1, 2, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 85, 90]]
          >>> game = time_per_word(p, ['basiradial', 'pseudoliterary', 'electroextraction'])
          >>> get_words(game)
          ['basiradial', 'pseudoliterary', 'electroextraction']
          >>> get_times(game)
          [[1, 1, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 69, 71, 73, 78, 81, 86], [22, 23, 24, 29, 33, 34, 35], [52, 55, 59, 60, 61, 64, 69]]
          >>> game = time_per_word(p, ['horde', 'termolecular', 'unbeatably', 'unamenable', 'ratio', 'speciology'])
          >>> get_words(game)
          ['horde', 'termolecular', 'unbeatably', 'unamenable', 'ratio', 'speciology']
          >>> get_times(game)
          [[4, 2, 2, 5, 3, 5], [1, 1, 5, 4, 1, 1], [3, 4, 1, 1, 3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 30]]
          >>> game = time_per_word(p, ['interlardment'])
          >>> get_words(game)
          ['interlardment']
          >>> get_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[91, 93]]
          >>> game = time_per_word(p, ['casual'])
          >>> get_words(game)
          ['casual']
          >>> get_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[48, 50, 55, 57]]
          >>> game = time_per_word(p, ['purblindly', 'chromo', 'casson'])
          >>> get_words(game)
          ['purblindly', 'chromo', 'casson']
          >>> get_times(game)
          [[2, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[25, 30, 33]]
          >>> game = time_per_word(p, ['strigal', 'scrawler'])
          >>> get_words(game)
          ['strigal', 'scrawler']
          >>> get_times(game)
          [[5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 29, 32, 36], [10, 11, 13, 14]]
          >>> game = time_per_word(p, ['gormandize', 'pochay', 'negotiatrix'])
          >>> get_words(game)
          ['gormandize', 'pochay', 'negotiatrix']
          >>> get_times(game)
          [[1, 3, 4], [1, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12], [5]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 70], [68, 70]]
          >>> game = time_per_word(p, ['pectous'])
          >>> get_words(game)
          ['pectous']
          >>> get_times(game)
          [[5], [2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 27], [57, 62], [45, 50]]
          >>> game = time_per_word(p, ['campylometer'])
          >>> get_words(game)
          ['campylometer']
          >>> get_times(game)
          [[5], [5], [5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[62, 65, 66], [49, 52, 53]]
          >>> game = time_per_word(p, ['intercrescence', 'incendiarism'])
          >>> get_words(game)
          ['intercrescence', 'incendiarism']
          >>> get_times(game)
          [[3, 1], [3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[74, 77, 78, 81, 83, 86]]
          >>> game = time_per_word(p, ['unrioting', 'heaps', 'kitling', 'workhouse', 'scriver'])
          >>> get_words(game)
          ['unrioting', 'heaps', 'kitling', 'workhouse', 'scriver']
          >>> get_times(game)
          [[3, 1, 3, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[90, 92, 97, 101]]
          >>> game = time_per_word(p, ['infanglement', 'cavern', 'autotriploid'])
          >>> get_words(game)
          ['infanglement', 'cavern', 'autotriploid']
          >>> get_times(game)
          [[2, 5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[4, 5]]
          >>> game = time_per_word(p, ['fiddley'])
          >>> get_words(game)
          ['fiddley']
          >>> get_times(game)
          [[1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[8, 13, 16, 21, 22, 25]]
          >>> game = time_per_word(p, ['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively'])
          >>> get_words(game)
          ['saponify', 'bakerless', 'nonluminous', 'zonesthesia', 'argumentatively']
          >>> get_times(game)
          [[5, 3, 5, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[31, 36, 40, 43]]
          >>> game = time_per_word(p, ['overfrailty', 'affair', 'gelatinizability'])
          >>> get_words(game)
          ['overfrailty', 'affair', 'gelatinizability']
          >>> get_times(game)
          [[5, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[17, 22, 27], [1, 5, 9]]
          >>> game = time_per_word(p, ['toys', 'uranophane'])
          >>> get_words(game)
          ['toys', 'uranophane']
          >>> get_times(game)
          [[5, 5], [4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 24, 26, 30, 35], [44, 49, 54, 55, 59], [50, 55, 57, 61, 63]]
          >>> game = time_per_word(p, ['impercipient', 'ali', 'indult', 'palmitic'])
          >>> get_words(game)
          ['impercipient', 'ali', 'indult', 'palmitic']
          >>> get_times(game)
          [[1, 2, 4, 5], [5, 5, 1, 4], [5, 2, 4, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[90, 95, 97, 99, 100, 104], [32, 35, 39, 44, 47, 48]]
          >>> game = time_per_word(p, ['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly'])
          >>> get_words(game)
          ['rubberneck', 'telangiectasy', 'unratable', 'dissolvableness', 'redheadedly']
          >>> get_times(game)
          [[5, 2, 2, 1, 4], [3, 4, 5, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 38, 40, 42]]
          >>> game = time_per_word(p, ['nocturia', 'cataphyllum', 'alroot'])
          >>> get_words(game)
          ['nocturia', 'cataphyllum', 'alroot']
          >>> get_times(game)
          [[1, 2, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26], [32, 37]]
          >>> game = time_per_word(p, ['undissenting'])
          >>> get_words(game)
          ['undissenting']
          >>> get_times(game)
          [[4], [5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 84, 88, 93, 98, 101], [97, 99, 103, 104, 107, 111]]
          >>> game = time_per_word(p, ['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic'])
          >>> get_words(game)
          ['accresce', 'during', 'unreproachableness', 'incomputable', 'sulphosuccinic']
          >>> get_times(game)
          [[1, 4, 5, 5, 3], [2, 4, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[53, 57, 59, 62, 67, 68], [17, 19, 23, 28, 29, 33], [46, 48, 51, 56, 60, 65]]
          >>> game = time_per_word(p, ['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia'])
          >>> get_words(game)
          ['unembraced', 'counterprotection', 'karyolysis', 'contuse', 'esophagomalacia']
          >>> get_times(game)
          [[4, 2, 3, 5, 1], [2, 4, 5, 1, 4], [2, 3, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 28, 31], [58, 63, 66], [28, 31, 34]]
          >>> game = time_per_word(p, ['resay', 'benjy'])
          >>> get_words(game)
          ['resay', 'benjy']
          >>> get_times(game)
          [[5, 3], [5, 3], [3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[88, 90, 92, 94], [19, 23, 28, 32], [71, 74, 78, 80]]
          >>> game = time_per_word(p, ['pantomime', 'fumatory', 'driftpiece'])
          >>> get_words(game)
          ['pantomime', 'fumatory', 'driftpiece']
          >>> get_times(game)
          [[2, 2, 2], [4, 5, 4], [3, 4, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[67, 71, 74, 76, 79], [61, 66, 70, 75, 80]]
          >>> game = time_per_word(p, ['uncurl', 'lobulose', 'parapsychical', 'revengement'])
          >>> get_words(game)
          ['uncurl', 'lobulose', 'parapsychical', 'revengement']
          >>> get_times(game)
          [[4, 3, 2, 3], [5, 4, 5, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[85, 89], [68, 71], [35, 38]]
          >>> game = time_per_word(p, ['lintwhite'])
          >>> get_words(game)
          ['lintwhite']
          >>> get_times(game)
          [[4], [3], [3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 57]]
          >>> game = time_per_word(p, ['myristicaceous'])
          >>> get_words(game)
          ['myristicaceous']
          >>> get_times(game)
          [[2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 60, 64, 66, 71, 75], [6, 7, 9, 14, 19, 23]]
          >>> game = time_per_word(p, ['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably'])
          >>> get_words(game)
          ['swearingly', 'pimple', 'unbundled', 'bencite', 'unfrustrably']
          >>> get_times(game)
          [[5, 4, 2, 5, 4], [1, 2, 5, 5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 28], [35, 38, 39, 43]]
          >>> game = time_per_word(p, ['unpapal', 'saiga', 'unbungling'])
          >>> get_words(game)
          ['unpapal', 'saiga', 'unbungling']
          >>> get_times(game)
          [[4, 1, 1], [3, 1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[83, 88], [60, 63]]
          >>> game = time_per_word(p, ['rhymemaking'])
          >>> get_words(game)
          ['rhymemaking']
          >>> get_times(game)
          [[5], [3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[20, 24]]
          >>> game = time_per_word(p, ['uninterlocked'])
          >>> get_words(game)
          ['uninterlocked']
          >>> get_times(game)
          [[4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12, 15, 18, 22, 24, 26, 27], [71, 75, 79, 83, 84, 86, 91]]
          >>> game = time_per_word(p, ['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton'])
          >>> get_words(game)
          ['moly', 'boldness', 'uraniid', 'inherently', 'diphenol', 'dermoskeleton']
          >>> get_times(game)
          [[3, 3, 4, 2, 2, 1], [4, 4, 4, 1, 2, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[98]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[82, 85, 88, 92, 97, 99, 100], [86, 91, 96, 98, 99, 104, 105], [74, 78, 80, 84, 88, 92, 95]]
          >>> game = time_per_word(p, ['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship'])
          >>> get_words(game)
          ['probationism', 'pargeboard', 'liquidly', 'nongentile', 'metrification', 'unseamanship']
          >>> get_times(game)
          [[3, 3, 4, 5, 2, 1], [5, 5, 2, 1, 5, 1], [4, 2, 4, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 53, 57, 61, 64]]
          >>> game = time_per_word(p, ['purloiner', 'cinnabarine', 'orlop', 'ovolo'])
          >>> get_words(game)
          ['purloiner', 'cinnabarine', 'orlop', 'ovolo']
          >>> get_times(game)
          [[2, 4, 4, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[84, 88, 91, 92, 94]]
          >>> game = time_per_word(p, ['undersheriffship', 'remonetize', 'crustation', 'syntypicism'])
          >>> get_words(game)
          ['undersheriffship', 'remonetize', 'crustation', 'syntypicism']
          >>> get_times(game)
          [[4, 3, 1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[95, 99, 104, 106]]
          >>> game = time_per_word(p, ['physiological', 'truantly', 'photomezzotype'])
          >>> get_words(game)
          ['physiological', 'truantly', 'photomezzotype']
          >>> get_times(game)
          [[4, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[75, 79, 82, 85, 88, 89], [93, 94, 95, 99, 102, 107], [60, 64, 65, 68, 69, 70]]
          >>> game = time_per_word(p, ['zymin', 'bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal'])
          >>> get_words(game)
          ['zymin', 'bloodstroke', 'dioestrous', 'heterochthonous', 'supraseptal']
          >>> get_times(game)
          [[4, 3, 3, 3, 1], [1, 1, 4, 3, 5], [4, 1, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 58, 62, 66, 67, 70, 72], [50, 53, 55, 60, 62, 64, 65]]
          >>> game = time_per_word(p, ['actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp'])
          >>> get_words(game)
          ['actiniochrome', 'reassimilation', 'bandicoot', 'nettlefoot', 'macarism', 'usurp']
          >>> get_times(game)
          [[3, 4, 4, 1, 3, 2], [3, 2, 5, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[68], [91]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[12, 17, 22], [69, 71, 76], [5, 8, 9]]
          >>> game = time_per_word(p, ['teems', 'haematosepsis'])
          >>> get_words(game)
          ['teems', 'haematosepsis']
          >>> get_times(game)
          [[5, 5], [2, 5], [3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[94, 96, 101, 106, 110, 115, 120], [52, 55, 60, 65, 69, 72, 75]]
          >>> game = time_per_word(p, ['labroid', 'prophasis', 'uncomplimented', 'subside', 'pseudandry', 'saltcat'])
          >>> get_words(game)
          ['labroid', 'prophasis', 'uncomplimented', 'subside', 'pseudandry', 'saltcat']
          >>> get_times(game)
          [[2, 5, 5, 4, 5, 5], [3, 5, 5, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[69, 72, 76, 80, 83, 87]]
          >>> game = time_per_word(p, ['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness'])
          >>> get_words(game)
          ['coconscious', 'diploglossate', 'fatalistic', 'ow', 'disquietedness']
          >>> get_times(game)
          [[3, 4, 4, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 42], [61, 62]]
          >>> game = time_per_word(p, ['thunderousness'])
          >>> get_words(game)
          ['thunderousness']
          >>> get_times(game)
          [[5], [1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 11, 16, 21, 22, 26], [6, 11, 16, 17, 19, 22]]
          >>> game = time_per_word(p, ['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird'])
          >>> get_words(game)
          ['heavenish', 'dysmetria', 'cl', 'posthexaplaric', 'dinglebird']
          >>> get_times(game)
          [[2, 5, 5, 1, 4], [5, 5, 1, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[55, 59, 60, 65, 67, 71], [37, 39, 43, 44, 45, 48]]
          >>> game = time_per_word(p, ['lands', 'rippable', 'hectical', 'profanism', 'pachysalpingitis'])
          >>> get_words(game)
          ['lands', 'rippable', 'hectical', 'profanism', 'pachysalpingitis']
          >>> get_times(game)
          [[4, 1, 5, 2, 4], [2, 4, 1, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[87, 92, 95, 96, 99, 103], [22, 24, 26, 31, 35, 36]]
          >>> game = time_per_word(p, ['scleranth', 'perdricide', 'renably', 'sorn', 'glutting'])
          >>> get_words(game)
          ['scleranth', 'perdricide', 'renably', 'sorn', 'glutting']
          >>> get_times(game)
          [[5, 3, 1, 3, 4], [2, 2, 5, 4, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[37, 41, 43, 45, 46, 51, 54], [72, 73, 76, 79, 81, 83, 84]]
          >>> game = time_per_word(p, ['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous'])
          >>> get_words(game)
          ['cardiectomy', 'mien', 'wellness', 'antitobacconist', 'zoosporangiophore', 'sarcogenous']
          >>> get_times(game)
          [[4, 2, 2, 1, 5, 3], [1, 3, 3, 2, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[21, 23, 28, 33], [35, 38, 43, 46], [25, 26, 29, 30]]
          >>> game = time_per_word(p, ['unidealistic', 'pretermitter', 'automatist'])
          >>> get_words(game)
          ['unidealistic', 'pretermitter', 'automatist']
          >>> get_times(game)
          [[2, 5, 5], [3, 5, 3], [1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 61], [0, 1]]
          >>> game = time_per_word(p, ['prefacer'])
          >>> get_words(game)
          ['prefacer']
          >>> get_times(game)
          [[4], [1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[33, 38, 42, 47, 51, 52], [87, 90, 95, 96, 99, 103], [40, 41, 44, 47, 52, 57]]
          >>> game = time_per_word(p, ['toxic', 'sphaeristerium', 'sexualization', 'tugurium', 'epineurium'])
          >>> get_words(game)
          ['toxic', 'sphaeristerium', 'sexualization', 'tugurium', 'epineurium']
          >>> get_times(game)
          [[5, 4, 5, 4, 1], [3, 5, 1, 3, 4], [1, 3, 3, 5, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[34, 39, 41, 46], [42, 46, 49, 52], [65, 66, 70, 74]]
          >>> game = time_per_word(p, ['appositionally', 'earthly', 'orchiocatabasis'])
          >>> get_words(game)
          ['appositionally', 'earthly', 'orchiocatabasis']
          >>> get_times(game)
          [[5, 2, 5], [4, 3, 3], [1, 4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 15], [58, 63, 65]]
          >>> game = time_per_word(p, ['americium', 'polariscopy'])
          >>> get_words(game)
          ['americium', 'polariscopy']
          >>> get_times(game)
          [[2, 2], [5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[17, 18, 22, 25, 30]]
          >>> game = time_per_word(p, ['acrocephaly', 'brushed', 'removedness', 'peenge'])
          >>> get_words(game)
          ['acrocephaly', 'brushed', 'removedness', 'peenge']
          >>> get_times(game)
          [[1, 4, 3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 52, 53, 56, 57]]
          >>> game = time_per_word(p, ['humicubation', 'hyperdulic', 'crimple', 'soother'])
          >>> get_words(game)
          ['humicubation', 'hyperdulic', 'crimple', 'soother']
          >>> get_times(game)
          [[1, 1, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[6, 7, 8, 10, 15, 18, 21], [1, 3, 5, 8, 11, 14, 15]]
          >>> game = time_per_word(p, ['abstractedly', 'parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind'])
          >>> get_words(game)
          ['abstractedly', 'parapsidal', 'unattendance', 'expirable', 'wheelwright', 'rind']
          >>> get_times(game)
          [[1, 1, 2, 5, 3, 3], [2, 2, 3, 3, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79, 83, 84, 88, 91], [90, 93, 97, 100, 101]]
          >>> game = time_per_word(p, ['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology'])
          >>> get_words(game)
          ['oliguresis', 'plethoretical', 'plantlike', 'electrotechnology']
          >>> get_times(game)
          [[4, 1, 4, 3], [3, 4, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 17, 21], [91, 93, 94, 99]]
          >>> game = time_per_word(p, ['hubber', 'patrology', 'spermatophore'])
          >>> get_words(game)
          ['hubber', 'patrology', 'spermatophore']
          >>> get_times(game)
          [[4, 4, 4], [2, 1, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[28, 33, 37], [24, 29, 33], [23, 28, 32]]
          >>> game = time_per_word(p, ['miskindle', 'deathbed'])
          >>> get_words(game)
          ['miskindle', 'deathbed']
          >>> get_times(game)
          [[5, 4], [5, 4], [5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 10, 13, 17, 20, 21, 25], [56, 57, 62, 63, 67, 69, 74], [97, 102, 106, 107, 108, 111, 115]]
          >>> game = time_per_word(p, ['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic'])
          >>> get_words(game)
          ['nummi', 'undisparaged', 'polarly', 'baldachino', 'strumae', 'posttoxic']
          >>> get_times(game)
          [[1, 3, 4, 3, 1, 4], [1, 5, 1, 4, 2, 5], [5, 4, 1, 1, 3, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[84, 89, 92, 97, 98, 101, 105], [72, 74, 76, 78, 83, 86, 89], [96, 101, 102, 105, 108, 112, 113]]
          >>> game = time_per_word(p, ['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly'])
          >>> get_words(game)
          ['wraprascal', 'renominate', 'quondam', 'gullibility', 'staysail', 'unfleshly']
          >>> get_times(game)
          [[5, 3, 5, 1, 3, 4], [2, 2, 2, 5, 3, 3], [5, 1, 3, 3, 4, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[40, 43, 45, 46]]
          >>> game = time_per_word(p, ['microclimatological', 'acquaintancy', 'tarsoplasty'])
          >>> get_words(game)
          ['microclimatological', 'acquaintancy', 'tarsoplasty']
          >>> get_times(game)
          [[3, 2, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[74], [94], [69]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[], [], []]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[71, 76, 80, 85, 86, 90, 95], [97, 101, 104, 108, 112, 114, 116], [53, 55, 60, 62, 64, 69, 72]]
          >>> game = time_per_word(p, ['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness'])
          >>> get_words(game)
          ['impanate', 'undisinfected', 'unnapkined', 'stockwright', 'nonconcern', 'clandestineness']
          >>> get_times(game)
          [[5, 4, 5, 1, 4, 5], [4, 3, 4, 4, 2, 2], [2, 5, 2, 2, 5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 13, 17, 20, 24, 27, 31], [31, 35, 36, 39, 43, 45, 48]]
          >>> game = time_per_word(p, ['agamogenesis', 'gmbh', 'toothy', 'achromatism', 'uintathere', 'horrorsome'])
          >>> get_words(game)
          ['agamogenesis', 'gmbh', 'toothy', 'achromatism', 'uintathere', 'horrorsome']
          >>> get_times(game)
          [[2, 4, 3, 4, 3, 4], [4, 1, 3, 4, 2, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[19]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[26, 29]]
          >>> game = time_per_word(p, ['unstoried'])
          >>> get_words(game)
          ['unstoried']
          >>> get_times(game)
          [[3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[57, 62, 66, 67, 71]]
          >>> game = time_per_word(p, ['tomblet', 'wapp', 'matrix', 'pitfall'])
          >>> get_words(game)
          ['tomblet', 'wapp', 'matrix', 'pitfall']
          >>> get_times(game)
          [[5, 4, 1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[78, 82, 87, 88, 92, 97]]
          >>> game = time_per_word(p, ['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave'])
          >>> get_words(game)
          ['angiocholecystitis', 'yoven', 'lovably', 'sheepmonger', 'molave']
          >>> get_times(game)
          [[4, 5, 1, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[1, 3, 6, 10, 13, 16]]
          >>> game = time_per_word(p, ['virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose'])
          >>> get_words(game)
          ['virify', 'ferrohydrocyanic', 'wambly', 'hydrotechnic', 'capillose']
          >>> get_times(game)
          [[2, 3, 4, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[23, 26, 28, 31, 36], [15, 20, 22, 27, 30], [81, 82, 87, 91, 96]]
          >>> game = time_per_word(p, ['aphesis', 'lactase', 'pleionian', 'guige'])
          >>> get_words(game)
          ['aphesis', 'lactase', 'pleionian', 'guige']
          >>> get_times(game)
          [[3, 2, 3, 5], [5, 2, 5, 3], [1, 5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[49, 51, 53, 57], [42, 46, 51, 52]]
          >>> game = time_per_word(p, ['overstalled', 'obstupefy', 'predeparture'])
          >>> get_words(game)
          ['overstalled', 'obstupefy', 'predeparture']
          >>> get_times(game)
          [[2, 2, 4], [4, 5, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[31, 34, 36, 40], [98, 100, 104, 106], [80, 85, 89, 94]]
          >>> game = time_per_word(p, ['operated', 'cithara', 'apparent'])
          >>> get_words(game)
          ['operated', 'cithara', 'apparent']
          >>> get_times(game)
          [[3, 2, 4], [2, 4, 2], [5, 4, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[0, 1, 5]]
          >>> game = time_per_word(p, ['translocate', 'contradictive'])
          >>> get_words(game)
          ['translocate', 'contradictive']
          >>> get_times(game)
          [[1, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[78, 79, 81]]
          >>> game = time_per_word(p, ['institute', 'agamid'])
          >>> get_words(game)
          ['institute', 'agamid']
          >>> get_times(game)
          [[1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[51, 56, 60]]
          >>> game = time_per_word(p, ['blastophthoric', 'subscience'])
          >>> get_words(game)
          ['blastophthoric', 'subscience']
          >>> get_times(game)
          [[5, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 13, 15, 20, 22]]
          >>> game = time_per_word(p, ['optotype', 'raise', 'placentitis', 'virtualism'])
          >>> get_words(game)
          ['optotype', 'raise', 'placentitis', 'virtualism']
          >>> get_times(game)
          [[4, 2, 5, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[9, 14, 15, 18, 19, 23, 27]]
          >>> game = time_per_word(p, ['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry'])
          >>> get_words(game)
          ['clanjamphrey', 'belord', 'vermeology', 'wrive', 'phellodermal', 'weaponry']
          >>> get_times(game)
          [[5, 1, 3, 1, 4, 4]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[79]]
          >>> game = time_per_word(p, [])
          >>> get_words(game)
          []
          >>> get_times(game)
          [[]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[43, 46, 49, 50], [58, 63, 67, 72], [8, 10, 11, 13]]
          >>> game = time_per_word(p, ['disensure', 'flashing', 'swarfer'])
          >>> get_words(game)
          ['disensure', 'flashing', 'swarfer']
          >>> get_times(game)
          [[3, 3, 1], [5, 4, 5], [2, 1, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[58, 61, 64, 65]]
          >>> game = time_per_word(p, ['semiography', 'phosphoaminolipide', 'unilocularity'])
          >>> get_words(game)
          ['semiography', 'phosphoaminolipide', 'unilocularity']
          >>> get_times(game)
          [[3, 3, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[93, 96, 101], [29, 34, 36], [36, 39, 41]]
          >>> game = time_per_word(p, ['coast', 'stageably'])
          >>> get_words(game)
          ['coast', 'stageably']
          >>> get_times(game)
          [[3, 5], [5, 2], [3, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[11, 16, 19], [70, 73, 75], [15, 18, 23]]
          >>> game = time_per_word(p, ['interacinous', 'boycottism'])
          >>> get_words(game)
          ['interacinous', 'boycottism']
          >>> get_times(game)
          [[5, 3], [3, 2], [3, 5]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[48, 53, 55, 57, 59, 60], [77, 82, 86, 89, 90, 91]]
          >>> game = time_per_word(p, ['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned'])
          >>> get_words(game)
          ['gormed', 'spry', 'agrobiological', 'zaphara', 'unlessoned']
          >>> get_times(game)
          [[5, 2, 2, 2, 1], [5, 4, 3, 1, 1]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[22, 26, 27, 30], [93, 94, 97, 102], [56, 57, 59, 61]]
          >>> game = time_per_word(p, ['motel', 'ten', 'kittendom'])
          >>> get_words(game)
          ['motel', 'ten', 'kittendom']
          >>> get_times(game)
          [[4, 1, 3], [1, 3, 5], [1, 2, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[97, 100, 105, 109, 113, 118, 123], [96, 97, 101, 105, 110, 112, 116], [20, 22, 26, 31, 34, 35, 38]]
          >>> game = time_per_word(p, ['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby'])
          >>> get_words(game)
          ['exhibitions', 'durational', 'templarlikeness', 'boghole', 'tersulphate', 'slubby']
          >>> get_times(game)
          [[3, 5, 4, 4, 5, 5], [1, 4, 4, 5, 2, 4], [2, 4, 5, 3, 1, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[97, 101, 104, 109, 111], [66, 68, 73, 76, 79]]
          >>> game = time_per_word(p, ['blackishly', 'fungous', 'script', 'rais'])
          >>> get_words(game)
          ['blackishly', 'fungous', 'script', 'rais']
          >>> get_times(game)
          [[4, 3, 5, 2], [2, 5, 3, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[71, 75, 76], [28, 33, 36]]
          >>> game = time_per_word(p, ['garruline', 'immusical'])
          >>> get_words(game)
          ['garruline', 'immusical']
          >>> get_times(game)
          [[4, 1], [5, 3]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[65, 67, 70], [68, 71, 73]]
          >>> game = time_per_word(p, ['ogam', 'wettish'])
          >>> get_words(game)
          ['ogam', 'wettish']
          >>> get_times(game)
          [[2, 3], [3, 2]]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> p = [[40, 41], [73, 76]]
          >>> game = time_per_word(p, ['autometric'])
          >>> get_words(game)
          ['autometric']
          >>> get_times(game)
          [[1], [3]]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(cats) # Make sure the abstraction barrier isn't crossed!
          >>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
          >>> words = ['This', 'is', 'fun']
          >>> game = cats.time_per_word(p, words)
          >>> cats.get_words(game)
          ['This', 'is', 'fun']
          >>> cats.get_times(game)
          [[3, 2, 1], [4, 2, 3]]
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
