from setuptools import setup

setup(
    name="yamlip",
    version="0.0.1",
    url="http://github.com/jjmurre/yamlip",
    license='MIT',
    author="Jan Murre",
    author_email="jan.murre@catalyz.nl",
    description="A yaml interpolation tool",
    long_description="A yaml interpolation tool",
    py_modules=['intp', "attrdict"],
    install_requires=["PyYAML", "click"],
    entry_points={
        "console_scripts": ['yamlip=yamlip:yamlip'],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
