import datetime
import pytest
from unittest import mock
from app.main import outdated_products


class TestOutdatedProducts:
    @pytest.mark.parametrize(
        "input_products, expected_expired_products, mocked_today",
        [
            (
                [
                    {"name": "salmon", "expiration_date":
                        datetime.date(2022, 2, 10),
                        "price": 600},
                    {"name": "chicken", "expiration_date":
                        datetime.date(2022, 2, 5),
                        "price": 120},
                ],
                ["salmon", "chicken"],
                datetime.date(2022, 2, 20),
            ),
            (
                [
                    {"name": "chicken",
                        "expiration_date":
                        datetime.date(2022, 2, 5),
                        "price": 120},
                ],
                [],
                datetime.date(2022, 2, 5),
            ),
            (
                [],[], datetime.date(2022, 2, 5)
            )
        ]
    )
    @mock.patch("datetime.date")
    def test_given_products_and_date_return_expired_products(
            self,
            mock_date: mock.MagicMock,
            input_products: list[dict],
            expected_expired_products: list[str],
            mocked_today: datetime.date,
    ) -> None:
        mock_date.today.return_value = mocked_today
        result = outdated_products(input_products)
        assert result == expected_expired_products, \
            f"Expected: {expected_expired_products}, Got: {result}"

