from setuptools import setup, find_packages

setup(
    name='plotlyplus',
    version='0.1.0',
    author='Jiangang Hao',
    author_email='jgbrainstorm@gmail.com',
    description='Enhance pandas DataFrame with direct Plotly Express plotting functions, including safe versions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jgbrainstorm/plotlyplus',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pandas>=1.0.0',
        'plotly>=4.0.0'
    ],
    python_requires='>=3.6',
)
