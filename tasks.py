import sys


if sys.argv[1] == 'train_spam':
    print('running train_spam')
    from tasks.train_spam import train_spam
    train_spam()
if sys.argv[1] == 'test':
    from test import run
    run()
else:
    print('no task found')
