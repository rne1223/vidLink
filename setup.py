from setuptools import setup

setup(
        name='vidLink',
        version='1.0',
        py_modules=['vidLink'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            vidLink=vidLink:cli
        ''',
)
