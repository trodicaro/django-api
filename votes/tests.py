from django.test import TestCase
from django.utils import timezone

from .models import Vote
from .serializers import VoteSerializer

# Create your tests here.

class QuestionModelTests(TestCase):
  def test_it_serializes(self):
    vote = Vote.objects.create(
      subject = 'New vote',
      ayes = 1,
      nays = 0)
    serialized_vote = VoteSerializer(vote)
    serialized = (serialized_vote.data)
    assert vote.id == serialized['id']
    assert vote.subject == serialized['subject']
    assert vote.ayes == serialized['ayes']
    assert vote.nays == serialized['nays']
