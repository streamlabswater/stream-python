from setuptools import setup

setup(
    name='streamlabswater',
    version='1.0.0',
    packages=['streamlabswater'],
    keywords = ['streamlabs', 'streamlabswater', 'iot', 'water', 'sensor', 'smarthome', 'automation'],
    license='MIT',
    author='StreamLabs',
    author_email='support@streamlabswater.com',
    description='Python library for the StreamLabs developer API',
    install_requires=['requests'],
    python_requires='>=3.6',
)
