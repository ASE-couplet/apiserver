class ApiBaseException(Exception):
    status = 500
    message = 'error'


class BadRequest(ApiBaseException):
    status = 400
    message = 'bad request'


class NotFound(ApiBaseException):
    status = 404
    message = 'not found'
