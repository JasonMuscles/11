from wjs_01_测试模块1 import say_hello
from wjs_02_测试模块2 import say_hello

# 如果两个模块存在同名的函数，那么厚度凹入的模块函数
# 会覆盖掉先导入的函数，但是可以通过 as 别名进行解决
say_hello()
say_hello()
