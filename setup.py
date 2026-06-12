from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as file_obj:
        requirements = [req.replace("\n", "") for req in file_obj.readlines()]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='student_performance_project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)