import setuptools

setuptools.setup(
    name="sylseq_paper",
    version="0.0.1",
    author="Jessie R. Liu",
    description="Code to recreate figure analyses for Liu 2025 sequencing paper.",
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib==3.5.1',
        'matplotlib_venn==0.11.7',
        'mne==0.20.7',
        'numpy==1.23.5',
        'pandas==1.3.5',
        'scikit_learn==1.2.1',
        'scipy==1.8.0',
        'seaborn==0.12.2',
        'statannot==0.2.3',
        'statsmodels==0.13.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8"
    ]
)
