import fileinput
import os

if __name__ == '__main__':
    dir = os.path.dirname(os.path.abspath(__file__)) + '\\kit\\'
    print('Project initials (xx): ')
    initials = input()

    print('Creating project ' + initials + '...')
    os.rename('xx', initials)
    print('Root dir renamed to ' + initials)
    os.rename('xx_conf', initials + '_conf')
    print('Root conf dir renamed to ' + initials + '_conf')
    with fileinput.FileInput(('.gitignore', initials + '_conf\\.bowerrc'), inplace=True) as file:
        for line in file:
            print(line.replace('xx', initials), end='')
    print('.gitignore, .bowerrc set up')

    os.system('rm xx_env -rf')
    os.system('virtualenv ' + initials + '_env')
    os.system(initials + '_env\\Scripts\\pip install django djangorestframework')
    os.system(initials + '_env\\Scripts\\pip freeze >' + initials + '_conf\\requirements.txt')
    print('Installed packages:')
    os.system(initials + '_env\\Scripts\\pip freeze')
    print('List saved to requirements.txt')
    print('All done...')
    input()
