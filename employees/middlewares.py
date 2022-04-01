from urllib import response


def my_middleware(get_response):
    print("One Time Initialization")
    def my_function(request):
        print("This is before view")
        response=get_response(request)
        print("This is after view")
        return response
    return my_function

"""Class based middleware"""
'''class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One Time Initialization")

        def __call__(self,request):
            print("This is before view")
            response=self.get_response(request)
            print("This is after view")
            return response '''
    