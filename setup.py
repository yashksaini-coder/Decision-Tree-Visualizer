from setuptools import setup, find_packages

setup(
    name="d-treevis",
    version="1.0.0",
    description="A library to visualize sklearn Decision Tree Classifiers.",
    author="yashksaini-coder",
    author_email="ys3853428@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy>=2.0.0",
        "matplotlib>=3.9.0",
        "Jinja2>=3.1.4",
        "scikit-learn>=1.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
