import os
import shutil
import subprocess
import xml.etree.ElementTree as ET

from PyQt5.QtWidgets import (QApplication, QFileDialog, QLabel, QLineEdit,
                             QMainWindow, QPushButton)


class InstallerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.zip_file_path = None
        self.app_icon_path = None
        self.company_logo_path = None
        self.license_path = None
        self.readme_path = None
        # self.output_path = os.path.join("/","Users", "jyot", "Desktop")

    def initUI(self):
        self.setWindowTitle("Python Installer Generator")
        self.setGeometry(100, 100, 700, 700)

        self.upload_button = QPushButton("Upload Zip File", self)
        self.upload_button.setGeometry(20, 20, 160, 30)
        self.upload_button.clicked.connect(self.upload_zip)

        self.mainFile_name_label = QLabel("Main Python File Name:", self)
        self.mainFile_name_label.setGeometry(330, 20, 100, 30)
        self.mainFile_name_input = QLineEdit(self)
        self.mainFile_name_input.setGeometry(450, 20, 160, 25)

        self.upload_button = QPushButton("Upload Company Logo", self)
        self.upload_button.setGeometry(20, 60, 160, 30)
        self.upload_button.clicked.connect(self.select_company_logo)

        self.upload_button = QPushButton("Upload App Icon", self)
        self.upload_button.setGeometry(20, 100, 160, 30)
        self.upload_button.clicked.connect(self.select_app_icon)

        self.app_name_label = QLabel("App Name:", self)
        self.app_name_label.setGeometry(20, 140, 100, 30)
        self.app_name_input = QLineEdit(self)
        self.app_name_input.setGeometry(120, 140, 160, 30)

        self.version_label = QLabel("Version:", self)
        self.version_label.setGeometry(20, 180, 100, 30)
        self.version_input = QLineEdit(self)
        self.version_input.setGeometry(120, 180, 160, 30)
        
        self.identifier_label = QLabel("App-Identifier:", self)
        self.identifier_label.setGeometry(20, 220, 100, 30)
        self.identifier_input = QLineEdit(self)
        self.identifier_input.setGeometry(120, 220, 160, 30)
    
        self.minimum_os_label = QLabel("Minimum OS:", self)
        self.minimum_os_label.setGeometry(20, 260, 100, 30)
        self.minimum_os_input = QLineEdit(self)
        self.minimum_os_input.setGeometry(120, 260, 160, 30)

        self.copyright_label = QLabel("Copyright:", self)
        self.copyright_label.setGeometry(20, 300, 100, 30)
        self.copyright_input = QLineEdit(self)
        self.copyright_input.setGeometry(120, 300, 160, 30)

        self.upload_button = QPushButton("Upload License", self)
        self.upload_button.setGeometry(20, 340, 160, 30)
        self.upload_button.clicked.connect(self.select_license_file)

        self.upload_button = QPushButton("Upload Readme", self)
        self.upload_button.setGeometry(20, 380, 160, 30)
        self.upload_button.clicked.connect(self.select_readme_file)

        self.upload_button = QPushButton("Select Output Directory", self)
        self.upload_button.setGeometry(20, 420, 200, 30)
        self.upload_button.clicked.connect(self.select_output_path)

        self.package_button = QPushButton("Create Installer", self)
        self.package_button.setGeometry(20, 500, 160, 30)
        self.package_button.setEnabled(False)
        self.package_button.clicked.connect(self.installer_macos)

    def upload_zip(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.zip_file_path, _ = QFileDialog.getOpenFileName(self, "Select Zip file", "", "Zip Files (*.zip)", options=options)

        if self.zip_file_path:
            self.package_button.setEnabled(True)
            print("Selected Zip file:", self.zip_file_path)
    
    def select_app_icon(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.app_icon_path, _ = QFileDialog.getOpenFileName(self, "Select App Icon", "", "Icon Files (*.ico *.icns)", options=options)

        if self.app_icon_path:
            print("Selected App Icon:", self.app_icon_path)

    def select_company_logo(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.company_logo_path, _ = QFileDialog.getOpenFileName(self, "Select Company Logo", "", "Image Files (*.png *.jpg *.jpeg *.gif *.bmp)", options=options)

        if self.company_logo_path:
            print("Selected Company Logo:", self.company_logo_path)
    
    def select_license_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.license_path, _ = QFileDialog.getOpenFileName(self, "Select License", "", "Text Files (*.txt *.rtf);;All Files (*)", options=options)

        if self.license_path:
            print("Selected License:", self.license_path)
    
    def select_readme_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.readme_path, _ = QFileDialog.getOpenFileName(self, "Select Readme", "", "HTML Files (*.html *.htm);;Text Files (*.txt);;All Files (*)", options=options)

        if self.readme_path:
            print("Selected Readme:", self.readme_path)

    
    def select_output_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        self.selected_output_path = QFileDialog.getExistingDirectory(self, "Select output Directory", options=options)

        if self.selected_output_path:
            print("Selected Output path:", self.selected_output_path)


    def installer_macos(self):
        input_path = self.zip_file_path
        main_file = self.mainFile_name_input.text()
        app_name = self.app_name_input.text()
        app_version = self.version_input.text()
        app_identifier = self.identifier_input.text()
        app_icon_path = self.app_icon_path  # (icns format)
        company_logo_path = self.company_logo_path 
        license_file_path = self.license_path
        readme_file_path = self.readme_path
        output_path = self.selected_output_path
        minimum_os = self.minimum_os_input.text()
        copyright_name = self.copyright_input.text()

        # temp_dir = tempfile.mkdtemp()
        # subprocess.run(f"pyinstaller {py_path}")
        # Create an application bundle
        # app_bundle_path = os.path.join(temp_dir, f"{app_name}.app")  # Replace with your app name
        # Copy the company logo file to the application resources (for macOS)
        # resources_path = os.path.join(app_bundle_path, "Contents", "Resources")
        # os.makedirs(resources_path, exist_ok=True)
        # shutil.copy(company_logo_path, resources_path)


        command = [
            "pyinstaller", "--onefile", "--windowed",
            "--name", f"{app_name}",
            f"--osx-bundle-identifier={app_identifier}",
            f"--icon={app_icon_path}",
            f"{main_file}"
        ]
        print(command)
        subprocess.run(command, cwd=input_path, check=True)

        # to create folder with name of app
        dist_path = os.path.join(output_path, app_name)
        os.makedirs(dist_path, exist_ok=True)

        shutil.copy(license_file_path, dist_path)
        shutil.copy(readme_file_path, dist_path)

        source_app_path = os.path.join(input_path,"dist",f"{app_name}.app")
        dist_full_path = os.path.join(dist_path, os.path.basename(source_app_path))
        shutil.copytree(source_app_path, dist_full_path)

 
        dist_NameComponent_plist_path = os.path.join(dist_path, "NameComponent.plist")
        dist_NameComponent_pkg_path = os.path.join(dist_path, "NameComponent.pkg")
        dist_distribution_plist_path = os.path.join(dist_path, "distribution.plist")
        dist_distribution_pkg_path = os.path.join(dist_path, f"{app_name}.pkg")
        install_location_path = os.path.join("/", "Applications", f"{app_name}.app")

        command1 = [
            "pkgbuild",
            "--analyze",
            "--root", dist_full_path,
            dist_NameComponent_plist_path
        ]
        print(command1)
        subprocess.run(command1, check=True)
        
        
        command2 = [
            "pkgbuild",
            "--root", dist_full_path,
            "--identifier", app_identifier,
            "--version", app_version,
            "--min-os-version", minimum_os,
            "--install-location", install_location_path,
            "--component-plist", dist_NameComponent_plist_path,
            dist_NameComponent_pkg_path
        ]
        print(command2)
        subprocess.run(command2, check=True)

        command3 = [
            "productbuild",
            "--synthesize",
            "--package", dist_NameComponent_pkg_path,
            dist_distribution_plist_path
        ]
        print(command3)
        subprocess.run(command3, check=True)

        xml_file_path = dist_distribution_plist_path

        # Load the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        title_element = ET.Element('title')
        title_element.text = f"{app_name}"
        root.append(title_element)

        readme_element = ET.Element('readme')
        readme_element.set('file', f"{readme_file_path}")
        root.append(readme_element)

        license_element = ET.Element('license')
        license_element.set('file', f"{license_file_path}")
        root.append(license_element)

        background_element = ET.Element('background')
        background_element.set('file', f"{company_logo_path}")
        background_element.set('alignment', 'bottomleft')
        root.append(background_element)

        tree.write(xml_file_path)

        command4 = [
            "productbuild",
            "--distribution", dist_distribution_plist_path,
            "--resources", dist_path,
            "--package-path", dist_NameComponent_pkg_path,
            dist_distribution_pkg_path
        ]
        print(command4)
        try:
            subprocess.run(command4, check=True)
            print("Package build completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

def main():
    app = QApplication([])
    window = InstallerApp()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
