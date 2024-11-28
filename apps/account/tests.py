import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        email='test@example.com',
        password='testpassword'
    )

    assert user.email == 'test@example.com'
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_email_unique():
    User.objects.create(email='test@example.com', password='testpassword')
    with pytest.raises(Exception):
        User.objects.create(email='test@example.com', password='testpassword')
