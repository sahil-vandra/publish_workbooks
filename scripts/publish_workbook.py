import os
import json
import argparse
import tableauserverclient as TSC


def signin():
    tableau_auth = TSC.TableauAuth(args.username, args.password)
    server = TSC.Server(args.server_url, use_server_version=True)
    server.auth.sign_in(tableau_auth)
    return server


def switchSite(server, site_id):
    site = server.sites.get_by_id(site_id)
    server.auth.switch_site(site)


def getProject(server, project_path, file_path):
    all_projects, pagination_item = server.projects.get()
    project = next(
        (project for project in all_projects if project.name == project_path), None)
    if project.id is not None:
        return project.id
    else:
        error = f"The project for {file_path} workbook could not be found."
        print(
            f"{data['file_path']} workbook is not published.")
        raise LookupError(error)
        exit(1)


def publishWB(server, file_path, name, project_id, show_tabs, hidden_views):
    wb_path = os.path.dirname(os.path.realpath(__file__)).rsplit(
        '/', 1)[0] + "/workbooks/" + file_path

    new_workbook = TSC.WorkbookItem(
        name=name, project_id=project_id, show_tabs=show_tabs)
    new_workbook = server.workbooks.publish(
        new_workbook, wb_path, 'Overwrite', hidden_views=hidden_views)


def main(args):
    project_data_json = json.loads(args.project_data)
    try:
        # Sign in to server.
        server = signin()

        for data in project_data_json:
            switchSite(server, data['site_id'])

            if data['project_path'] is None:
                error = f"The project project_path field is Null in JSON Template."
                print(
                    f"{data['file_path']} workbook is not published.")
                raise LookupError(error)
                exit(1)
            else:
                # Step 2: Get all the projects on server, then look for the required one.
                project_id = getProject(
                    server, data['project_path'], data['file_path'])

                # Step 3: Form a new workbook item and publish.
                publishWB(server, data['file_path'], data['name'], project_id,
                          data['show_tabs'], data['hidden_views'])

                # wb_path = os.path.dirname(os.path.realpath(__file__)).rsplit(
                #     '/', 1)[0] + "/workbooks/" + data['file_path']

                # new_workbook = TSC.WorkbookItem(
                #     name=data['name'], project_id=project_id, show_tabs=data['show_tabs'])
                # new_workbook = server.workbooks.publish(
                #     new_workbook, wb_path, 'Overwrite', hidden_views=data['hidden_views'])

                # if data['tags'] is not None:
                #     new_workbook.tags = set(data['tags'])
                #     new_workbook = server.workbooks.update(
                #         new_workbook)

                print(
                    f"\nWorkbook :: {data['file_path']} :: published in {data['project_path']} project")

                server.auth.sign_out()

    except Exception as e:
        print("Workbook not published.\n", e)
        exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument('--username', action='store',
                        type=str, required=True)
    parser.add_argument('--password', action='store',
                        type=str, required=True)
    parser.add_argument('--server_url', action='store',
                        type=str, required=True)
    parser.add_argument('--project_data', action='store',
                        type=str, required=True)

    args = parser.parse_args()
    main(args)
