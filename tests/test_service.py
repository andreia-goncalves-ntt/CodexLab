import unittest
from unittest.mock import patch

from app.service import list_tasks


TASKS = [
    {
        "id": 1,
        "title": "Write launch recap",
        "description": "Draft a short internal summary of the product launch.",
        "status": "open",
    },
    {
        "id": 2,
        "title": "Fix login redirect",
        "description": "Resolve the redirect loop after the OAuth callback.",
        "status": "done",
    },
    {
        "id": 3,
        "title": "Plan workshop agenda",
        "description": "Outline topics for the partner onboarding session.",
        "status": "open",
    },
]


class ListTasksTests(unittest.TestCase):
    @patch("app.service.load_tasks", return_value=TASKS)
    def test_returns_all_tasks_when_q_is_omitted(self, _load_tasks):
        self.assertEqual(list_tasks(), TASKS)

    @patch("app.service.load_tasks", return_value=TASKS)
    def test_matches_title_case_insensitively(self, _load_tasks):
        self.assertEqual(list_tasks(q="LAUNCH"), [TASKS[0]])

    @patch("app.service.load_tasks", return_value=TASKS)
    def test_matches_description_case_insensitively(self, _load_tasks):
        self.assertEqual(list_tasks(q="oauth"), [TASKS[1]])

    @patch("app.service.load_tasks", return_value=TASKS)
    def test_combines_status_and_q_filters(self, _load_tasks):
        self.assertEqual(list_tasks(status="open", q="plan"), [TASKS[2]])


if __name__ == "__main__":
    unittest.main()
