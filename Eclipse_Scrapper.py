import time
start = time.time()
import requests
import lxml.html as lh
from fake_useragent import UserAgent
ua = UserAgent()
hdr = {'User-Agent':str(ua.chrome)}
import pandas as pd
Total_Bugs_Considered=[]
status_Reassigned=[]
severity_Reassigned=[]
version_Reassigned=[]
product_Reassigned=[]
os_Reassigned=[]
priority_Reassigned=[]
component_Reassigned=[]
assignee_Reassigned=[]
status_NotReassigned=[]
severity_NotReassigned=[]
version_NotReassigned=[]
product_NotReassigned=[]
os_NotReassigned=[]
priority_NotReassigned=[]
component_NotReassigned=[]
assignee_NotReassigned=[]
for BugId in range(214000,353001): #[214094, 214195, 215424, 215518, 215858]:
    #BugId=215518
    url = 'https://bugs.eclipse.org/bugs/show_activity.cgi?id=' + str(BugId)
    # Create a handle, page, to handle the contents of the website
    page = requests.get(url, headers=hdr)
    # Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    # Create empty list
    col = []
    Status_seen = False
    Resolution_seen = False
    Considered_Bug = False
    tr_elements.reverse()
    for j in range(0, len(tr_elements)):

        for t in tr_elements[j]:
            name = (str(t.text_content().replace(" ", "")).replace("\n", ""))
            col.append(((str(name).lower())))
        if "status" in col:
            ##print(col)
            if col[col.index("status") + 2].lower() == "resolved" or "verified" or "closed":
                ##print(col[col.index("status") + 2].lower() )
                Status_seen= True
                if (Resolution_seen):
                    Considered_Bug = True
                    tr_elements.reverse()
                    break
        if "resolution" in col:
            if col[col.index("resolution") + 2].lower() == "fixed":
                ##print("Resolution=",col[col.index("resolution") + 2].lower())
                Resolution_seen = True
                if (Status_seen):
                    Considered_Bug = True
                    tr_elements.reverse()
                    break
        col=[]
    if Considered_Bug:
        Field_list = {"status_NotReassigned":status_NotReassigned,"severity_NotReassigned":severity_NotReassigned,"version_NotReassigned":version_NotReassigned,"product_NotReassigned":product_NotReassigned,"os_NotReassigned":os_NotReassigned,"priority_NotReassigned":priority_NotReassigned,"component_NotReassigned":component_NotReassigned,"assignee_NotReassigned":assignee_NotReassigned}
        Status_done = False
        Severity_done = False
        Version_done = False
        Product_done = False
        Os_done = False
        Priority_done = False
        Component_done = False
        Assignee_done = False
        Status_count=0

        print(BugId,"is considered")
        Total_Bugs_Considered.append(BugId)
        for j in range(1, len(tr_elements)):
            for t in tr_elements[j]:
                # i+=1
                # #print(t)
                name = (str(t.text_content().replace(" ", "")).replace("\n", ""))

                # #print(name,type(name),name.isalnum())
                col.append(((str(name).lower()).replace(" ", "")).replace("\n", ""))
            # #print(col)

            if "status" in col and not(Status_done):

                if (col[col.index("status") + 1].lower() == "resolved" or "fixed"):
                    Status_count = j+1
                    if col[col.index("status") + 2] == "reopened":
                        Status_done =True
                        #print("Write in status Reassigned", BugId)
                        #status_row += updating_to_xlsx("Status.xlsx", status_row, 1, BugId, status_flag)
                        status_Reassigned.append(BugId)

                        del Field_list["status_NotReassigned"]

                elif (col[col.index("status") + 2] == "reopened") and j==Status_count:
                    Status_done = True
                    ##print("Write in status Reassigned", BugId)
                    #status_row += updating_to_xlsx("Status.xlsx", status_row, 1, BugId,status_flag)
                    status_Reassigned.append(BugId)
                    del Field_list["status_NotReassigned"]

            elif "severity" in col and not(Severity_done):
                if (not (col[col.index("severity") + 1].isspace()) and (col[col.index("severity") + 1].isspace()) != "--"):
                    #print("col[col.index('severity') + 1]=",type(col[col.index("severity") + 1]))
                    ##print("Write in severity Reassigned", BugId)
                    severity_Reassigned.append(BugId)
                    Severity_done =  True
                    #severity_row += updating_to_xlsx("Severity.xlsx", severity_row, 1, BugId)
                    del Field_list["severity_NotReassigned"]


            elif "version" in col and not(Version_done):
                if (not (col[col.index("version") + 1].isspace()) and (col[col.index("version") + 1].isspace()) != "--"):
                    ##print("Write in version Reassigned", BugId)
                    version_Reassigned.append(BugId)
                    Version_done = True
                    #version_row += updating_to_xlsx("Version.xlsx", version_row, 1, BugId)
                    del Field_list["version_NotReassigned"]
            elif "product" in col and not(Product_done):
                if (not (col[col.index("product") + 1].isspace()) and (col[col.index("product") + 1].isspace()) != "--"):
                    ##print("Write in product Reassigned", BugId)
                    product_Reassigned.append(BugId)
                    Product_done = True
                    #product_row += updating_to_xlsx("Product.xlsx", product_row, 1, BugId)
                    del Field_list["product_NotReassigned"]
            elif "os" in col and not(Os_done):
                if (not (col[col.index("os") + 1].isspace()) and (col[col.index("os") + 1].isspace()) != "--"):
                    ##print("Write in os Reassigned", BugId)
                    os_Reassigned.append(BugId)
                    Os_done = True
                   # os_row += updating_to_xlsx("Os.xlsx", os_row, 1, BugId)
                    del Field_list["os_NotReassigned"]
            elif "priority" in col and not(Priority_done):
                if (not (col[col.index("priority") + 1].isspace()) and (col[col.index("priority") + 1].isspace()) != "--"):
                    ##print("Write in priority Reassigned", BugId)
                    priority_Reassigned.append(BugId)
                    Priority_done = True
                    #priority_row += updating_to_xlsx("Priority.xlsx", priority_row, 1, BugId)
                    del Field_list["priority_NotReassigned"]

            elif "component" in col and not(Component_done):
                if (not (col[col.index("component") + 1].isspace()) and (col[col.index("component") + 1].isspace()) != "--"):
                    ##print("Write in component Reassigned", BugId)
                    component_Reassigned.append(BugId)
                    Component_done = True
                    #component_row += updating_to_xlsx("Component.xlsx", component_row, 1, BugId)
                    del Field_list["component_NotReassigned"]

            elif "assignee" in col and not(Assignee_done):
                if (not (col[col.index("assignee") + 1].isspace()) and (col[col.index("assignee") + 1].isspace()) != "--"):
                    ##print("Write in assignee Reassigned", BugId)
                    assignee_Reassigned.append(BugId)
                    Assignee_done = True
                    # assignee_row += updating_to_xlsx("Assignee.xlsx", assignee_row, 1, BugId)
                    del Field_list["assignee_NotReassigned"]

            col = []
        #print(Field_list)
        ##print(status_Reassigned)
        for left in Field_list:
            #print(left,"Write in NotReassigned",BugId)
            Field_list[left].append(BugId)
def DF_to_EXCEL(df,File_Name):

    writer = pd.ExcelWriter(File_Name+'.xlsx')
    df.to_excel(writer, sheet_name='Sheet')
    writer.save()
df_Status=pd.DataFrame({"Reassigned":pd.Series(status_Reassigned),"Not-Reassigned":pd.Series(status_NotReassigned)})
DF_to_EXCEL(df_Status,"Status")
df_Severity=pd.DataFrame({'Reassigned':pd.Series(severity_Reassigned),'Not-Reassigned':pd.Series(severity_NotReassigned)})
DF_to_EXCEL(df_Severity,"Severity")
df_Version=pd.DataFrame({'Reassigned':pd.Series(version_Reassigned),'Not-Reassigned':pd.Series(version_NotReassigned)})
DF_to_EXCEL(df_Version,"Version")
df_Product=pd.DataFrame({'Reassigned':pd.Series(product_Reassigned),'Not-Reassigned':pd.Series(product_NotReassigned)})
DF_to_EXCEL(df_Product,"Product")
df_Os=pd.DataFrame({'Reassigned':pd.Series(os_Reassigned),'Not-Reassigned':pd.Series(os_NotReassigned)})
DF_to_EXCEL(df_Os,"Os")
df_Priority=pd.DataFrame({'Reassigned':pd.Series(priority_Reassigned),'Not-Reassigned':pd.Series(priority_NotReassigned)})
DF_to_EXCEL(df_Priority,"Priority")
df_Component=pd.DataFrame({'Reassigned':pd.Series(component_Reassigned),'Not-Reassigned':pd.Series(component_NotReassigned)})
DF_to_EXCEL(df_Component,"Component")
df_Assignee=pd.DataFrame({'Reassigned':pd.Series(assignee_Reassigned),'Not-Reassigned':pd.Series(assignee_NotReassigned)})
DF_to_EXCEL(df_Assignee,"Assignee")
end = time.time()
print("Script took ", end - start)
#print("Field_list=",Field_list)
with open("Conclusion.txt", "w") as f:
    f.write("Script took " + str(end - start) + "\n")
    f.write("status is reassigned in="+str(len(status_Reassigned))+ " Bugs"+ " which is "+
            str((len(status_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("severity is reassigned in="+ len(severity_Reassigned)+ "Bugs"+ "which is"+
            str((len(severity_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("version is reassigned in="+ len(version_Reassigned)+ "Bugs"+ "which is"+
            str((len(version_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("product is reassigned in="+ product_Reassigned+ "Bugs"+ "which is"+
            str((len(product_Reassigned)/ len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("os is reassigned in="+ len(os_Reassigned)+ "Bugs"+ "which is"+
            str((len(os_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("priority is reassigned in="+ len(priority_Reassigned)+ "Bugs"+ "which is"+
            str((len(priority_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("component is reassigned in="+ len(component_Reassigned)+ "Bugs"+ "which is"+
            str((len(component_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
    f.write("assignee is reassigned in="+ len(assignee_Reassigned)+ "Bugs"+ "which is"+
            str((len(assignee_Reassigned) / len(Total_Bugs_Considered)) * 100)+ "% of Total Bug IDs\n")
