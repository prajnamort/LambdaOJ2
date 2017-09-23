import os
from importlib.machinery import SourceFileLoader

from django.core.exceptions import ValidationError


def get_compare_func(compare_file_name):
    compare = SourceFileLoader('compare', compare_file_name).load_module()
    return compare.compare_func


def validate_compare_file(value):
    with open('/tmp/tmp_compare_file.py', 'wb') as fc:
        fc.write(value.file.read())

    def _cleanup():
        try:
            os.remove(fc.name)
        except:
            pass

    try:
        get_compare_func(fc.name)
    except Exception as e:
        _cleanup()
        message = str(e) or 'Compare 函数文件错误，请检查语法和逻辑'
        raise ValidationError(message)
    else:
        _cleanup()
