def get_installed_packages():
    # Run pip freeze command to get a list of installed packages
    output = subprocess.check_output(['pip3', 'freeze']).decode('utf-8')
    return output.split('\n')

def is_using_pkg(package_name):
    # Run pip show command to get information about the package
    output = subprocess.check_output(['pip3', 'show', package_name]).decode('utf-8')
    # Check if Wheel is mentioned in the output
    return re.search(r'Requires:.*?<insertname>', output) is not None

# Get list of installed packages
installed_packages = get_installed_packages()

# Check if each package is using a wheel
for package in installed_packages:
    if package:  # Skip empty lines
        package_name = package.split('==')[0]
        print(f"{package_name} is using <insertname>: {is_using_pkg(package_name)}")
