from tools import req
import pytest

rq = req.REQ()


def test_ng_tc1_product_empty_payload():
    """

    :return:
    """
    print("\nTest case description...")

    input_data = {}
    info = rq.post("products", input_data)

    response_code = info[0]
    assert response_code == 400

    response_body = info[1]
    assert 'errors' in response_body.keys(), "Test case 1: Wrong error key"

    exp_err_msg = "No product data specified to create product"
    act_err_msg = response_body['errors'][0]['message']

    assert exp_err_msg == act_err_msg, "Wrong error message"

    exp_err_code = "woocommerce_api_missing_product_data"
    act_err_code = response_body['errors'][0]['code']

    assert exp_err_code == act_err_code, "Wrong error code"

    print ("TC1: PASS")


def test_ng_tc2_product_missing_title_key_in_payload():
    """

    :return:
    """
    print("\nTest case description...")

    input_data = {}
    product = {}
    product['regular_price'] = '19.99'
    product['type'] = 'simple'

    input_data['products'] = product
    info = rq.post('products', input_data)

    response_code = info[0]
    assert response_code == 400, "TC2: Wrong response code"

    response_body = info[1]
    assert 'errors' in response_body.keys(), "Test case 1: Wrong error key"

    exp_err_msg = "No product data specified to create product"
    act_err_msg = response_body['errors'][0]['message']

    assert exp_err_msg == act_err_msg, "Wrong error message"

    exp_err_code = "woocommerce_api_missing_product_data"
    act_err_code = response_body['errors'][0]['code']

    assert exp_err_code == act_err_code, "Wrong error code"

    print "TC2: PASS"


def test_ng_tc3_product_empty_string_for_title_in_payload():
    """

    :return:
    """

    print("\nTest case description...")

    input_data = {}
    product = {}
    product['regular_price'] = '19.99'
    product['type'] = 'simple'
    product['title'] = ''

    input_data['products'] = product
    info = rq.post('products', input_data)

    tc = 'ng, products, > empty title string'
    expected_message = "No product data specified to create product"
    expected_error_code = "woocommerce_api_missing_product_data"

    verify_ng_test_response(info, tc, expected_message, expected_error_code)


# Verification function - Better to put in separate functions
def verify_ng_test_response(response_list, test_case, exp_err_msg, exp_err_code):
    """

    :return:
    """

    # Verify response code
    response_code = response_list[0]
    assert response_code == 400, "%s: Wrong response code" % test_case

    # Verify response contains 'errors' key
    response_body = response_list[1]
    assert 'errors' in response_body.keys(), "%s: Wrong error key" % test_case

    # Verify the content of the error message
    act_err_msg = response_body['errors'][0]['message']
    assert exp_err_msg == act_err_msg, "%s: Wrong error message. Expected: %s, Actual: %s" % (test_case, exp_err_msg, act_err_msg)

    # Verify the error code in the response
    act_err_code = response_body['errors'][0]['code']

    assert exp_err_code == act_err_code, "Wrong error code"

    print "Test %s Pass" % test_case


# test_ng_tc1_product_empty_payload()
# test_ng_tc2_product_missing_title_in_payload()
# test_ng_tc3_product_empty_string_for_title_in_payload()
