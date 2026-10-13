
import sys
import platform
import math

print("=== Python Environment Test ===")
print(f"Version  : {platform.python_version()}")
print(f"Platform : {platform.system()} {platform.release()}")
print(f"Binary   : {sys.executable}")

# Basic calculation check
test_val = 144
sqrt_val = math.isqrt(test_val)
print(f"Math check: sqrt({test_val}) = {sqrt_val}")

print("Installation is verified and functioning.")
