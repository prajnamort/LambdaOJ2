import os
from importlib.machinery import SourceFileLoader

from django.core.exceptions import ValidationError


def get_compare_func(compare_file_name):
    compare = SourceFileLoader('compare', compare_file_name).load_module()
    return compare.compare_func


def validate_compare_file(value):
    with open('/tmp/tmp_compare_file.py', 'wb') as fc,\
         open('/tmp/tmp_input_sample.txt', 'w') as f1,\
         open('/tmp/tmp_output_sample.txt', 'w') as f2:
        fc.write(value.file.read())
        f1.write('1\n')
        f2.write('1\n')
    def _cleanup():
        try:
            os.remove(fc.name)
            os.remove(f1.name)
            os.remove(f2.name)
        except:
            pass
    try:
        compare_func = get_compare_func(fc.name)
        result = compare_func(f1.name, f2.name)
        assert isinstance(result, bool), 'Compare 函数返回值不是 bool 类型'
    except Exception as e:
        _cleanup()
        message = str(e) or 'Compare 函数文件错误，请检查语法和逻辑'
        raise ValidationError(message)
    else:
        _cleanup()
