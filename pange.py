import time
start = time.time()
status_Reassigned=[3,5,6]
Total_Bugs_Considered=[1,2,3,4,5]
end = time.time()
print("Script took ",end - start)
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

#print("Field_list="+Field_list)

for BugId in range(506000 - 655001):
    url = 'https://bugzilla.gnome.org/show_activity.cgi?id=' + str(BugId)


