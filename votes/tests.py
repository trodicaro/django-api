from django.test import TestCase
from django.utils import timezone

from .models import Vote
from .serializers import VoteSerializer

# Create your tests here.

class QuestionModelTests(TestCase):
  def test_it_serializes(self):
    time = timezone.now()
    # print(time)
    vote = Vote.objects.create(
      subject = 'New vote',
      ayes = 1,
      nays = 0,
      vote_taken = time)
    serialized_vote = VoteSerializer(vote)
    serialized = (serialized_vote.data)
    # print(serialized)
    assert vote.id == serialized['id']
    assert vote.subject == serialized['subject']
    assert vote.ayes == serialized['ayes']
    assert vote.nays == serialized['nays']
    # assert vote.vote_taken == str(time)
