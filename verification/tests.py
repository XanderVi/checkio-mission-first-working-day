"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['2018-07-01', 14],
            "answer": '2018-07-16',
        },
        {
            "input": ['2018-02-19', 10],
            "answer": '2018-03-01',
        },
        {
            "input": ['2000-02-28', 5],
            "answer": '2000-03-06',
        },
        {
            "input": ['1999-12-20', 14],
            "answer": '2000-01-03',
        }
    ],
    "Extra": [
        {
            "input": ['2020-07-27', 11],
            "answer": '2020-08-07',
        },
        {
            "input": ['2024-02-19', 12],
            "answer": '2024-03-04',
        },
        {
            "input": ['2099-12-21', 11],
            "answer": '2100-01-01',
        },
        {
            "input": ['2016-11-14', 6],
            "answer": '2016-11-21',
        },

        {
            "input": ['2009-07-23', 11],
            "answer": '2009-08-03',
        }

    ]
}
