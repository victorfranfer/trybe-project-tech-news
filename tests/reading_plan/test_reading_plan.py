from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.assets.news import NEWS
import pytest


def mock_news():
    return NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch("tech_news.analyzer.reading_plan.find_news", mock_news)

    result = ReadingPlanService.group_news_for_available_time(2)

    assert len(result["readable"]) == 6
    assert len(result["unreadable"]) == 4

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)
