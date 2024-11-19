from setuptools import setup, find_packages

setup(
    name="substring_replacer",  # Name of your package
    version="1.0.0",
    packages=find_packages(),
    py_modules=["substring_replace_script"],  # Python files included
    install_requires=['argparse', 'setuptools'],  # Dependencies (if any)
    entry_points={
        'console_scripts': [
            'substring_replace=substring_replace_script:main',  # Referance what to run
        ],
    },
    author="Busai Kornel",
    author_email="kornel.busai@gmail.com",
    description="Script that removes substring from all file names within a directory.",
    url="https://github.com/Kornelbusai/substring_replace_tui",  # GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
