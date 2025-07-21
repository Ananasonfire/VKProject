def test_user_segment_workflow(client):
    # create segment
    r = client.post('/segments', json={'name': 'CLOUD_DISCOUNT_30'})
    sid = r.json()['id']

    # assign users manually
    r = client.post(f'/segments/{sid}/users', json={'user_ids': [1,2,3]})
    assert set(r.json()) == {1,2,3}

    # get user segments
    r = client.get('/users/2/segments')
    assert any(seg['id']==sid for seg in r.json()['segments'])