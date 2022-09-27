import argparse
import tableauserverclient as TSC
import json


def main(args):
    print("\nproject_id ::", args.project_id)
    print("\ntype of project_id ::", type(args.project_id))
    temp1 = "{" + args.project_id + "}"
    print("\ntemp1 ::", temp1)
    print("\ntype temp1 ::", type(temp1))
    a = "{" +json.loads(temp1)+"}"
    print('\na ::', a)
    print('\ntype of a ::', type(a))
    
    # wb_list = []
    # for wb in args.workbook_files.split(","):
    #     temp_wb = wb.strip()
    #     if len(temp_wb) > 0:
    #         wb_list.append(temp_wb)
    # project_id = args.project_id.replace('"', "")

    # if len(wb_list) > 0:
    #     # Step 1: Sign in to server.
    #     tableau_auth = TSC.TableauAuth(args.username, args.password)
    #     server = TSC.Server(args.server_url)
    #     overwrite_true = TSC.Server.PublishMode.Overwrite

    #     with server.auth.sign_in(tableau_auth):
    #         # Step 2: Get all the projects on server, then look for the default one.
    #         all_projects, pagination_item = server.projects.get()
    #         project = next(
    #             (project for project in all_projects if project.name == args.project_name), None)

    #         # Step 3: If default project is found, form a new workbook item and publish.
    #         if project is not None:
    #             for wb_file in wb_list:
    #                 new_workbook = TSC.WorkbookItem(project_id)
    #                 new_workbook = server.workbooks.publish(
    #                     new_workbook, wb_file, overwrite_true)
    #                 print(f"\nWorkbook :: {wb_file} :: published")
    #         else:
    #             error = "The project could not be found."
    #             raise LookupError(error)
    # else:
    #     print("Workbook list is null")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--username', action='store',
                        type=str, required=True)
    parser.add_argument('--password', action='store',
                        type=str, required=True)
    parser.add_argument('--server_url', action='store',
                        type=str, required=True)
    parser.add_argument('--project_id', action='store',
                        type=str, required=True)
    parser.add_argument('--workbook_files', action='store',
                        type=str, required=True)
    args = parser.parse_args()
    main(args)
