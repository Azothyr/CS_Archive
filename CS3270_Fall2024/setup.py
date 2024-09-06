from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='phase02',
    version='0.1',
    packages=find_packages(),
    description='Phase 2 of the CS3270 project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zachary Peterson',
    author_email='10719862@uvu.edu',
    url='https://github.com/Azothyr/CS_Archive/tree/main/CS3270_Fall2024/phase02',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    install_requires=[
        'pandas',
        'PyQt5',
        'numpy',
        'scipy',
    ],
    include_package_data=True,
)

