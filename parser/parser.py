import argparse
import json
import os
import re
from collections import defaultdict


def is_dir_or_file(path_arg):
    if os.path.isdir(path_arg) or os.path.isfile(path_arg):
        return path_arg
    raise argparse.ArgumentTypeError(f"Wrong path argument: {path_arg}")


def get_log_files(path_to_logs):
    if os.path.isfile(path_to_logs):
        return path_to_logs


def parse_json(log):
    ip = defaultdict(int)
    methods = defaultdict(int)
    client_errs = defaultdict(int)
    times = defaultdict(int)
    server_errs = defaultdict(int)

    regexp = re.compile(
        r"^(?P<ip>[\d.]+)"  # IP
        r" - \S+ "  # skip
        r"\[.+?\] "  # time
        r"\"(?P<method>\S+) [^ ]+ .+?\" "  # method + path + HTTP
        r"(?P<status>\d+) "  # status
        r"\S+ "  # size
        r"\"(?P<url>.*?)\" "  # url
        r"\".*\" "  # agent
        r"(?P<time_r>\d+)$"  # time
    )

    reqs_count = 0
    with open(log, 'r') as file:
        for index, line in enumerate(file):
            line = line.strip()
            m = regexp.search(line)
            if not m:
                continue
            g = m.groupdict()
            ip[g['ip']] += 1
            methods[g['method']] += 1

            g_time = int(g['time_r'])
            g_str = ' '.join((g['ip'], g['method'], g['url']))
            g_str_status = g_str + " " + g['status']

            if times[g_str] < g_time:
                times[g_str] = g_time

            g_status = g['status']
            if g_status.startswith('4'):
                client_errs[g_str_status] += 1
            if g_status.startswith('5'):
                server_errs[g_str_status] += 1

            reqs_count += 1

    top_10_ip = dict(sorted(ip.items(), key=lambda d: d[1], reverse=True)[:10])
    top_10_methods = dict(sorted(methods.items(), key=lambda d: d[1], reverse=True))
    client_err = dict(sorted(client_errs.items(), key=lambda d: d[1], reverse=True)[:10])
    server_err = dict(sorted(server_errs.items(), key=lambda d: d[1], reverse=True)[:10])
    top_times = dict(sorted(times.items(), key=lambda d: d[1], reverse=True)[:10])
    dict_stat = {
        "total_requests": reqs_count,
        "top_10_ip": top_10_ip,
        "methods": top_10_methods,
        "top_10_long_reqs": top_times,
        "top_10_client_errors": client_err,
        "top_10_server_errors": server_err
    }
    return json.dumps(dict_stat, indent=4)


def parse_json_to_file(json, filename):
    with open(filename, 'w') as file:
        file.write(json)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Process access.log and returns some stats in json-format.")
    parser.add_argument('-p', '--path', action='store', type=is_dir_or_file,
                        help='Path to log file or dir. If dir passed all log files will be processed.', required=True)

    args = parser.parse_args()
    log = get_log_files(args.path)
    json = parse_json(log)
    parse_json_to_file(json, "parse_log.json")
