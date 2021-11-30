from unixtime_packages.my_namespace.get_unixtime_package.unixtime import get_time

from datetime import datetime



def print_time_pretty(unixtime):
    formated_time = datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    print(formated_time)

def main():
    unixtime = get_time()
    print_time_pretty(unixtime)

if __name__ == '__main__':
    main()
