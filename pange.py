with open("Conclusion.txt", "w") as f:
    f.write("status is reassigned in=", len(status_Reassigned), "Buds", "which is",
            ((len(status_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("severity is reassigned in=", len(severity_Reassigned), "Buds", "which is",
            ((len(severity_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("version is reassigned in=", len(version_Reassigned), "Buds", "which is",
            ((len(version_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("product is reassigned in=", product_Reassigned, "Buds", "which is",
            ((len(product_Reassigned)/ len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("os is reassigned in=", len(os_Reassigned), "Buds", "which is",
            ((len(os_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("priority is reassigned in=", len(priority_Reassigned), "Buds", "which is",
            ((len(priority_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("component is reassigned in=", len(component_Reassigned), "Buds", "which is",
            ((len(component_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
    f.write("assignee is reassigned in=", len(assignee_Reassigned), "Buds", "which is",
            ((len(assignee_Reassigned) / len(Total_Bugs_Considered)) * 100), "% of Total Bug IDs\n")
