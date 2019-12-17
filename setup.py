import setuptools

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="alpha-orm",
    version="1.2.0",
    author="Claret Nnamocha",
    license='MIT',
    author_email="devclareo@gmail.com",
    description="A nice database orm written in python",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/alpha-orm/python-alpha-orm",
    packages=[
        'alphaorm',
        'alphaorm.drivers',
        'alphaorm.query_builders',
        'alphaorm.utilities',
        'alphaorm.generators'
    ],
    keywords=['database', 'orm', 'db', 'database-orm'],
    install_requires=[
        'pymysql',
        'six',
        'python-interface'
    ],
    classifiers=[
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3'
)
