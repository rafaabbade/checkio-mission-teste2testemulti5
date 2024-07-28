"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
             {
        "input": [[3, 1, 2]],
        "answer": [[1, 3, 2], [1, 2, 3]]
    },
    {
        "input": [[4, 3, 2, 1]],
        "answer": [[1, 3, 2, 4], [1, 2, 3, 4]]
    },
    {
        "input": [[1, 2, 3]],
        "answer": [[1, 2, 3]]
    },
    {
        "input": [[5, 4, 3, 2, 1]],
        "answer": [[1, 4, 3, 2, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    },
    {
        "input": [[2, 3, 1, 5, 4]],
        "answer": [[1, 3, 2, 5, 4], [1, 2, 3, 5, 4], [1, 2, 3, 4, 5]]
    },
    {
        "input": [[6, 5, 4, 3, 2, 1]],
        "answer": [[1, 5, 4, 3, 2, 6], [1, 2, 4, 3, 5, 6], [1, 2, 3, 4, 5, 6]]
    }
    ]
}
