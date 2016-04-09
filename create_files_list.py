import os
import re
import json
import sys

# write to a log file and console
def log(message, file_handle):
    file_handle.write(message + "\n")
    print(message)

# normalize the slashes in the paths, and remove case sensitivity for comparison on Windows
def prepare_paths(input_paths):
    paths = []
    for path in input_paths:
        paths.append(os.path.normcase(os.path.normpath(path)))
    return paths

def create_files_list_walk(search_path, excludes, log_path, manifest_path, include_regex=[], exclude_regex=[]):
    search_path = os.path.normcase(os.path.normpath(search_path))

    with open(log_path, 'a') as log_file, open(manifest_path, 'a') as manifest_file:
        log('searching: {0}'.format(search_path), log_file)
        files = os.listdir(search_path)
        for f in files:
            full_path = os.path.normcase(os.path.normpath(os.path.join(search_path, f)))
            log('{0}'.format(full_path), log_file)
            if full_path in excludes:
                log("excluded: " + full_path, log_file)
                continue

            if os.path.isdir(full_path):
                create_files_list_walk(full_path, excludes, log_path, manifest_path, include_regex, exclude_regex)
                continue

            if include_regex:
                skip_file = True
                for pattern in include_regex:
                    if re.match(pattern, full_path):
                        skip_file = False
                        log("including ({0}), it matches ({1})".format(full_path, pattern), log_file)
                        break
                if skip_file:
                    continue

            if exclude_regex:
                skip_file = False
                for pattern in exclude_regex:
                    if re.match(pattern, full_path):
                        skip_file = True
                        log("excluded ({0}): {1}".format(pattern, full_path), log_file)
                        break
                if skip_file:
                    continue

            manifest_file.write(full_path + "\n")

def create_files_list(config_path):
    with open(config_path, 'r') as config_file:
        json_config = json.loads(config_file.read())

    log_path = json_config['log']
    manifest_path = json_config['output']
    configs = json_config['dirs']

    # clear the log and manifest files
    with open(log_path, 'w'), open(manifest_path, 'w'):
        pass

    for config in configs:
        # convert the relative excluded paths to full paths
        excludes = []
        for rel_path in config['exclude']:
            excludes.append(os.path.normcase(os.path.normpath(os.path.join(config['dir'], rel_path))))

        excludes = prepare_paths(excludes)
        create_files_list_walk(config['dir'], excludes, log_path, manifest_path, config['include_regex'], config['exclude_regex'])

create_files_list(sys.argv[1])
