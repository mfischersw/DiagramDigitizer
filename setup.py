from setuptools import setup, find_packages



setup(
    name='diagramdigitizer',
    version='1.0.0',
    description='DiagramDigitizer',
    long_description='DiagramDigitizer',
    author='Michael Fischer',
    author_email='mfischer.sw@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    entry_points={  # Optional
        'console_scripts': [
            'diagramdigitizer=diagramdigitizer:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/mfischersw/DiagramDigitizer/',
    }
)
