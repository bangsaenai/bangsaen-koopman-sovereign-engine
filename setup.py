from setuptools import setup, Extension
import os
import sys

# Flag สั่ง Strip Symbols เพื่อลบ Symbol Table ทั้งหมด ป้องกันการส่อง Hex / Decompiler 100%
extra_compile_args = ['-O3', '-strip-all', '-fvisibility=hidden'] if os.name != 'nt' else ['/O2']

module = Extension(
    'libkoopman_kernel',
    sources=['src/koopman_core.c'],
    extra_compile_args=extra_compile_args
)

setup(
    name='libkoopman_kernel',
    version='3.0.0',
    description='Bangsaen AI Labs Sovereign Koopman Kernel Engine',
    ext_modules=[module]
)