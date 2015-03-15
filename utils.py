from fabric.colors import green, red


def notify(msg):
    bar = '+' + '-' * (len(msg) + 2) + '+'
    print(green(''))
    print(green(bar))
    print(green("| %s |" % msg))
    print(green(bar))
    print(green(''))


def error(msg):
    bar = '+' + '-' * (len(msg) + 2) + '+'
    print(red(''))
    print(red(bar))
    print(red("| %s |" % msg))
    print(red(bar))
    print(red(''))
