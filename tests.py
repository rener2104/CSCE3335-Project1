import pytest
from tam_sorter.algorithm import SORT_TAM_SERVER, SWAP_SERVER


@pytest.mark.parametrize("input_sequence, expected_output", [
    (['M', 'T', 'A', 'M', 'A', 'T', 'A'], ['T', 'T', 'A', 'A', 'A', 'M', 'M']),
    (['T', 'A', 'M', 'M', 'A', 'T'], ['T', 'T', 'A', 'A', 'M', 'M']),
    ([], [])
])
def test_SORT_TAM_server(input_sequence, expected_output):
    assert SORT_TAM_SERVER(input_sequence) == expected_output

@pytest.mark.parametrize("arr, i, j, expected_output",[
    (['T','A','M'],0,2,['M','A','T']),
    (['M','A','T'],1,2,['M','T','A']),
    (['A', 'T', 'M'], 0, 1, ['T', 'A', 'M']),
    ])
def test_SWAP_server(arr, i, j, expected_output):
    SWAP_SERVER(arr,i,j)
    assert arr == expected_output