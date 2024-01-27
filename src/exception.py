import sys
# Adjust the import based on your actual logger location
from logger import logging

def error_message_details(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    #_, _, exc_tb = error_details
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error, error_details=error_details)

    def __str__(self):
        return self.error_message

# Uncomment the following section if you want to test the CustomException
# if __name__ == '__main__':
#     logging.info("Logging has started ")
#
#     try:
#         a = 1 / 0
#
#     except Exception as e:
#         logging.info('divided by 0')
#         raise CustomException(e, sys)
