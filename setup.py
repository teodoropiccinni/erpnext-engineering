from setuptools import setup, find_packages

setup(
    name='engineering',
    version='0.0.1',
    description='Custom ERPNext module for managing Engineering flows',
    author='Teodoro PICCINNI',
    author_email='studio@teodoropiccinni.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
