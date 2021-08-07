test = {
  'name': 'smallest-int-having',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_having LIMIT 48;
          2021/07/28 3:32:58 PM MDT|5
          2021/07/29 9:00:50 AM MDT|13
          2021/07/28 3:06:02 PM MDT|14
          2021/07/28 2:37:15 PM MDT|15
          2021/07/29 12:05:49 PM MDT|19
          2021/07/28 6:40:39 PM MDT|20
          2021/07/29 1:34:09 PM MDT|21
          2021/07/29 1:24:54 AM MDT|27
          2021/07/28 9:47:09 PM MDT|28
          2021/07/28 6:12:24 PM MDT|29
          2021/07/29 7:09:34 AM MDT|39
          2021/07/28 2:38:34 PM MDT|40
          2021/07/29 4:07:02 PM MDT|41
          2021/07/28 3:01:58 PM MDT|43
          2021/07/28 5:10:33 PM MDT|44
          2021/07/28 4:09:04 PM MDT|49
          2021/07/29 1:34:01 PM MDT|52
          2021/07/28 3:04:04 PM MDT|54
          2021/07/28 10:02:08 PM MDT|57
          2021/07/29 4:45:55 AM MDT|59
          2021/07/28 2:46:12 PM MDT|76
          2021/07/29 12:18:03 AM MDT|174
          2021/07/28 2:40:15 PM MDT|323
          2021/07/28 3:30:55 PM MDT|414
          2021/07/29 4:29:33 PM MDT|886
          2021/07/29 2:11:09 PM MDT|1322
          2021/07/29 3:41:19 PM MDT|177013
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
