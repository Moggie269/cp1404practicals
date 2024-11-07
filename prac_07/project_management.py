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
    load_default_projects(projects, 'projects')
    print(f'Loaded {len(projects)} projects from projects.txt')
    print(MENU)
    choice = input('>>> ').upper()
    while choice != 'Q':
        if choice == 'L':
            projects = []
            load_file = input('Select file to load from: ')
            load_default_projects(projects, load_file)
        elif choice == 'S':
            save_file = input('Select file to save to: ')
            save_default_projects(projects, save_file)
        elif choice == 'D':
            projects.sort()
            print('Incomplete projects:')
            display_projects(projects, False)
            print('Complete projects:')
            display_projects(projects, True)
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
    save_choice = input('Would you like to save to projects.txt? ').upper()
    if save_choice == 'Y':
        save_default_projects(projects, 'projects')
    print('Thank you for using custom-built project management software.')


def load_default_projects(projects, file):
    """Load projects from default file."""
    with open(file, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)


def save_default_projects(projects, file):
    """Save projects to default file."""
    with open(file, 'w') as out_file:
        out_file.write('Name	Start Date	Priority	Cost Estimate	Completion Percentage\n')
        for project in projects:
            out_file.write(project.__str__() + '\n')


def display_projects(projects, completeness):
    """Display projects."""
    for project in projects:
        if project.is_complete() is completeness:
            print(f'{project.name}, start: {project.start_date}, priority {project.priority}, '
                  f'estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%')


main()