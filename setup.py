from setuptools import setup


setup(
    name='cldfbench_ecoclimate',
    py_modules=['cldfbench_ecoclimate'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-ecoclimate=cldfbench_ecoclimate:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
