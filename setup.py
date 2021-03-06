from setuptools import setup


setup(
    name='slack-email-digest',
    version='0.1',
    author='Claudiu Saftoiu',
    author_email='csaftoiu@gmail.com',
    description='Export Slack history as a rich HTML email message',
    url='https://github.com/csaftoiu/slack-email-digest',

    install_requires=[
        'slacker(>=0.9.24)',
        'schema(>=0.6.2)',
        'jinja2(>=2.8)',
        'pytz(>=2016.6.1)',
        'tzlocal(>=1.2.2)',
        'emoji(>=0.3.9)',
        'pyshorteners(>=0.6.0)',
        'docoptcfg(>=1.0.2)',
        'clint(>=0.5.1)',
        'python-postmark(>=0.4.3)',
    ],

    packages=[],
    scripts=['scripts/slack-email-digest.py'],
)
