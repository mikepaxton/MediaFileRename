import os

mediaFolder = "/Volumes/secondary/Media Conversion/Completed"
for directname, directnames, files in os.walk(mediaFolder):
    for f in files:
        # Split the file into the filename and the extension, saving
        # as separate variables
        filename, ext = os.path.splitext(str(f))
        if "." in filename:
            # If a '.' is in the name, rename, appending the suffix
            # to the new file
            new_name = filename.replace(".", "")
            os.rename(
                os.path.join(directname, f),
                os.path.join(directname, new_name + ext))