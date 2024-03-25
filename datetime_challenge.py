def normalize_and_find_range(dates):
    pass


def test_normalize_and_find_range():
    input_dates = [
        "2024-03-20",
        "14/03/2024",
        "March 14, 2024",
        "2024-03-18",
        "01/04/2024",
        "February 28, 2024"
    ]
    expected_normalized = ['2024-03-20', '2024-03-14',
                           '2024-03-14', '2024-03-18', '2024-04-01', '2024-02-28']
    expected_range = ('2024-02-28', '2024-04-01')

    normalized_dates, date_range = normalize_and_find_range(input_dates)

    # Check if the lists match, disregarding order
    assert set(normalized_dates) == set(
        expected_normalized), "Normalized dates do not match expected output."

    # Check if the date range matches
    assert date_range == expected_range, "Date range does not match expected output."

    print("All tests passed!")


# You'll need to implement the normalize_and_find_range function to pass these tests.
test_normalize_and_find_range()
