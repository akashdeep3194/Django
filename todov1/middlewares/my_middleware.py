def test_middleware(get_response):
    def test_function(request):
        print("Before View")
        response = get_response(request)
        print("After View")
        return response
    return test_function