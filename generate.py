import os
import shutil

templateExtensions = ['.template', '.example', '.sample', '.placeholder']

def generateFromTemplates():
    currentDir = os.getcwd()
    for root, dirs, files in os.walk(currentDir):
        for file in files:
            fileName, extension = os.path.splitext(file)
            if extension in templateExtensions:
                srcPath = os.path.join(root, file)
                destPath = os.path.join(root, fileName)
                if not os.path.exists(destPath):
                    shutil.copy(srcPath, destPath)
                    print(f'Copied {srcPath} to {destPath}')

generateFromTemplates()