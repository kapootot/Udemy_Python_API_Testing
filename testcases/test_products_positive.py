from tools import req
from tools import dbconnect


def test_create_a_product():
    """

    :return:
    """
    global product_id
    global title
    global price

    title = 'TEST1 TITLE'
    price = '9.99'

    input_data = {
                    'product': {
                        'title': title,
                        'type': 'simple',
                        'regular_price': price
                    }
    }

    info = rq.post('products', input_data)

    response_code = info[0]
    response_body = info[1]

    assert response_code == 201, "The status code is not as " \
                                 "expected. Expected: 201, actual: {}".format(response_code)

    rs_title = response_body['product']['title']
    rs_price = response_body['product']['regular_price']
    product_id = response_body['product']['id']

    print "id is: %s" % product_id

    assert rs_title == title, "Title is incorrect. Expected: {} Actual: {}".format(title, rs_title)
    assert rs_price == price, "Price is incorrect. Expected: {} Actual: {}".format(price, rs_price)

    print "\nTest PASS"


def test_verify_product_created_in_db():
    """

    :return:
    """

    # Get info from db
    sql = '''SELECT p.post_title, p.post_type, pm.meta_value FROM aw_posts p JOIN aw_postmeta pm
             ON p.id=pm.post_id WHERE p.id = %s AND pm.meta_key = '_regular_price' ''' % product_id

    qrs = qry.select('wp515', sql)

    db_title = qrs[0][0]
    db_type = qrs[0][1]
    db_regular_price = qrs[0][2]

    assert db_title == title

    assert db_type == "product"

    assert db_regular_price == price

    print "test_verify_product_created_in_db - PASS"

rq = req.REQ()
qry = dbconnect.DBConnect()
test_create_a_product()
test_verify_product_created_in_db()


