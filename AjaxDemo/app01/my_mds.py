from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class IpValid(MiddlewareMixin):
    def process_request(self, request):
        """

        :param request:
        :return: 默认返回None,当返回一个响应体时，则实现了拦截,原路返回
        """
        print("MD1 process_request")
        visit_ip = request.META.get("REMOTE_ADDR")
        if visit_ip in ["127.0.0.2", ""]:
            return HttpResponse("IP Illegal")

    def process_response(self, request, response):
        print("MD1 process_response")
        print("MD1 response:", response)

        return response


class Hi(MiddlewareMixin):
    def process_request(self, request):
        print("MD2 process_request")

    def process_response(self, request, response):
        print("MD2 process_response")
        print("MD2 response:", response.content)

        response.content = b"<h1>welcome to Lyon</h1>" + response.content

        return response