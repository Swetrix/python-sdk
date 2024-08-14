from setuptools import setup, find_packages

setup(
    name='swetrix-python',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests',
        'python-dotenv'
    ],
    description='A Python library for server-side tracking on Swetrix',
    author='Yehor Dremliuha',
    author_email='yehor@swetrix.com',
    url='https://github.com/yourusername/swetrix-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
