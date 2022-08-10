import pytest
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ads_list(client):
    ads_factory = AdFactory.create_batch(5)

    response = client.get('/ad/')

    ads = []
    for ad in ads_factory:
        ads.append(
            {
                'id': ad.id,
                'name': ad.name,
                'author': ad.author_id,
                'price': ad.price,
                'description': ad.description,
                'is_published': ad.is_published,
                'category': ad.category_id,
                'image': ad.image.url if ad.image else None,
            }
        )
    expected_response = {
        "results": ads,
        "next": None,
        "previous": None,
        "count": 5,
    }

    assert response.status_code == 200
    assert response.json() == expected_response
