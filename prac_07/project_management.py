"""
CP1404/CP5632 Practical - Project Management.
Estimate time: 30 minutes
Actual time:
"""
import datetime
from project import Project
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
        "- (U)pdate project\n- (Q)uit")


def main():
    """Display menu."""
    print('Welcome to Pythonic Project Management')
    projects = []
    load_default_projects(projects)
    print(f'Loaded {len(projects)} projects from projects.txt')
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            pass
        elif choice == 'S':
            pass
        elif choice == 'D':
            pass
        elif choice == 'F':
            pass
        elif choice == 'A':
            pass
        elif choice == 'U':
            pass
        else:
            print('Invalid choice')
        print(MENU)
        choice = input('>>> ').upper()

    print('Thank you for using custom-built project management software.')


def load_default_projects(projects):
    """Load projects from default file."""
    with open('projects', 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)


main()