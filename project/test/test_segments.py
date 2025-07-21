def test_crud_flow(client):
    # create
    r = client.post('/segments', json={'name': 'MAIL_GPT'})
    assert r.status_code == 201
    sid = r.json()['id']

    # duplicate
    r2 = client.post('/segments', json={'name': 'MAIL_GPT'})
    assert r2.status_code == 409

    # list
    r = client.get('/segments')
    assert any(s['id']==sid for s in r.json())

    # update
    r = client.put(f'/segments/{sid}', json={'name': 'VOICE'})
    assert r.json()['name'] == 'VOICE'

    # delete
    r = client.delete(f'/segments/{sid}')
    assert r.status_code == 204
    r = client.get('/segments')
    assert not any(s['id']==sid for s in r.json())