import datetime
from django.urls import reverse

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Who is the best course director", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


POLL_INDEX = "polls:index"


def create_question(question_text: str, days: int) -> Question:
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse(POLL_INDEX))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        created_question: Question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse(POLL_INDEX))
        self.assertQuerysetEqual(response.context["latest_question_list"], [created_question])

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse(POLL_INDEX))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
