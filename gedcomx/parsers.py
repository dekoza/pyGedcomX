# flake8: noqa
import re

import lark

date_pattern = re.compile(
    # against specs core, but respects examples from specs
    r"""
    ^
    (
        (?P<approx>A?)
        (?P<year>[\+-]\d{4})
        (
            -
            (?P<month>\d{2})
            (
                -
                (?P<day>\d{2})
                (
                    T
                    (?P<hour>\d{2})
                    (
                        :
                        (?P<minute>\d{2})
                        (
                            :
                            (?P<second>\d{1,2})
                        )?
                    )?
                    (?P<tz>
                        [\+-]\d{2}
                        (:\d{2})?
                        | Z
                    )?
                )?
            )?
        )?
    )?
    $""",
    re.X,
)
duration_pattern = re.compile(
    # This pattern is broader than original specification.
    # Values not conforming to specs (for example "1000 seconds")
    # should be recalculated during parsing (using pendulum)
    # and returned in canonical form.
    r"""
    ^
    P
    (?P<years>\d+Y)?
    (?P<months>\d+M)?
    (?P<days>\d+D)?
    (
        T
        (?P<hours>\d+H)?
        (?P<minutes>\d+M)?
        (?P<seconds>\d+S)?
    )?
    $
    """,
    re.X,
)

grammar = r"""

start: date_format

date_format: SIMPLE_DATE
           | approx
           | closed_date_range
           | open_date_range
           | recurring

SIMPLE_DATE: /[\+-]\d{4}(-\d{2}(-\d{2}(T\d{2}(:\d{2}(:\d{1,2})?)?([\+-]\d{2}(:\d{2})?|Z)?)?)?)?/

DURATION: /P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?/

closed_date_range: SIMPLE_DATE "/" SIMPLE_DATE
                  | SIMPLE_DATE "/" DURATION
open_date_range: SIMPLE_DATE "/"
               | "/" SIMPLE_DATE

approx: "A" (SIMPLE_DATE|closed_date_range|open_date_range)

recurring: "R/" closed_date_range
         | "R" COUNT "/" closed_date_range

COUNT: DIGIT+

%import common.DIGIT
"""

date_preparser = lark.Lark(grammar)
