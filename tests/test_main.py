import pytest

from main import execute_challenge


def test_challenge():
    df = execute_challenge()
    elements_count(df)
    content_validation(df)


def elements_count(df):
    count = df.count()
    assert count == 10, 'Expected 10 elements'
    with pytest.raises(AssertionError):
        assert count == 5, 'Error expected and handled'

def id_assertion(val, list):
    assert val in list


def content_validation(df):
    one = df.filter('flag == 1')
    one.foreach(lambda x: id_assertion(x['id'], [1, 3, 4, 5, 9]))
