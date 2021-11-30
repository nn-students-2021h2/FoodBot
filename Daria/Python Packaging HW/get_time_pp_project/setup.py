from setuptools import setup

setup(
    name='get_time_pp_package',
    version='0.1',
    description='description',
    url='http://github.com/name/package_name',
    author='Daria Malikova',
    author_email='email@example.com',
    license='MIT',
    packages=['get_time_pp_package'],
    install_requires=[
        'requests==2.26.0',
        'get_time_package==0.1'
    ],
    entry_points={
        'console_scripts': [
            'get_time=get_time_pp_package.get_time_pp_module:main'
        ]
    }
)
