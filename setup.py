from setuptools import setup, find_packages

setup(
    ### Metadata
    name="substring_replacer",  # Name of package
    version="1.0.0",  # Version of package
    packages=find_packages(),
    py_modules=["substring_replace_script"],  # Python files included
    install_requires=['argparse', 'setuptools'],  # Dependencies 
    entry_points={
        'console_scripts': [
            'substring-replace=substring_replace_script:main',
        ],
    },
    author="Busai Kornél",
    author_email="kornel.busai@gmail.com",
    description="Script that removes substring from all file names within a directory.",
    url="https://github.com/Kornelbusai/substring_replace_tui",  # GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license_files = 'MIT'
)
