
Creating a Pooch Project
        
        General Instructions

        - Create a package called '<project name>'
                + create a datasets.py file
                + setup the code
        - on the root the project create a folder called datasets
                + add all file/sub-directories here
        - once done open python terminal and do the following:
                import pooch
                registry = pooch.make_registry(r"C:\SVN\spatial_pooch\data", "registery.txt", True)
        
        - Move that file to the package directory
        
        - Publish everything to github
        
Updating/Adding Data the registry:


        1. Run the following:
                import pooch
                registry = pooch.make_registry(r"<data path>", "registery.txt", True)
        2. Update the registery.txt in the github repo
