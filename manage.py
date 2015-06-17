# exec(open("./api/restful/test.py").read())



# import runpy
# file_globals = runpy.run_path("./api/restful/test.py")

# import subprocess, sys
# subprocess.call(['/home/tonigor/py3/bin/python3.4', '/home/tonigor/pyb/pyb/api/restful/test.py'])
# print(sys.executable)
# pid = subprocess.Popen([sys.executable, '/home/tonigor/pyb/pyb/api/restful/test.py'])

def std_api_test():
    # import pyb.api.restful.stdapi
    exec(open("./pyb/api/restful/stdapi.py").read())

def launch_watcher():
    # import pyb.strategy.watcher
    exec(open("./pyb/strategy/watcher.py").read())

if __name__ == '__main__':
    import os, sys, subprocess
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    """ Going up one level : useless, i ve moved the files
    curr_dir = curr_dir.split('/')
    curr_dir.pop()
    curr_dir_up_one_lvl='/'.join(curr_dir)
    sys.path.append(curr_dir_up_one_lvl)
    """
    sys.path.append(curr_dir)

    # std_api_test()

    launch_watcher()