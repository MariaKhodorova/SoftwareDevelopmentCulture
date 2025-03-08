from setuptools import setup, find_packages

setup(
    name='PyPi Practice',
    version='1.0',  # Версия вашего пакета
    packages=find_packages(),  # Автоматически находит все пакеты в проекте
    install_requires=[],
    author='Yulia Kravtsova',
    author_email='yuvwwa@gmail.com',
    description='Практическое задание PyPi в аудиторийй',
    #long_description=open('README.rst').read(),
    #long_description_content_type='text/x-rst',
    url='https://github.com/MariaKhodorova/SoftwareDevelopmentCulture.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
