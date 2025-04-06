import os

def snake_to_title(name):
    return name.replace('_', ' ').title()

def create_module_structure(base_path, module_name):
    module_path = os.path.join(base_path, module_name)
    os.makedirs(module_path, exist_ok=True)

    # Define structure
    structure = {
        'models': ['__init__.py', 'model.py'],
        'views': ['view.xml'],
        'data': ['data.xml'],
        'report': ['report.xml'],
        'security': ['ir.model.access.csv', 'security.xml'],
        'wizards': ['__init__.py', 'wizard.py', 'wizard.xml'],
        'readme': ['DESCRIPTION.rst'],
    }

    # Create folders and files
    for folder, files in structure.items():
        folder_path = os.path.join(module_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                if file == '__init__.py':
                    if folder == 'models':
                        f.write("from . import model\n")
                    elif folder == 'wizards':
                        f.write("from . import wizard\n")
                    else:
                        f.write('')
                elif file == 'model.py' or file == 'wizard.py':
                    f.write(f"# {file} - Auto-generated Python file\n")
                elif file == 'ir.model.access.csv':
                    f.write("id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n")
                elif file == 'view.xml' or file == 'wizard.xml':
                    f.write(f"""<?xml version="1.0" encoding="UTF-8" ?>
<odoo>
    <record id="inherit_id" model="ir.ui.view">
        <field name="name">inherit_name</field>
        <field name="model">model.name</field>
        <field name="inherit_id" ref="model.inherited_view_name"/>
        <field name="arch" type="xml">
        <!-- View definitions go here -->
        </field>
    </record>
</odoo>
""")
                elif file == 'data.xml':
                    f.write("""<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <data noupdate="1">
        <record id="id_name" model="model.name">
            <field name="name">Name</field>
            <field name="company_id" eval="False" />
            <field name="active" eval="True" />
        </record>
    </data>
</odoo>
""")
                elif file == 'security.xml':
                    f.write("""<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <record id="group_group_name" model="res.groups">
        <field name="name">Group Name</field>
        <field name="category_id" ref="base.module_category_hidden" />
    </record>
</odoo>
""")
                elif file == 'report.xml':
                    f.write("""<?xml version="1.0" encoding="utf-8" ?>
<odoo>
    <!-- Report definitions go here -->
</odoo>
""")
                elif file == 'DESCRIPTION.rst':
                    f.write(f"""{snake_to_title(module_name)}
{'=' * len(module_name)}

This is an auto-generated module template.
""")

    # Root __init__.py
    with open(os.path.join(module_path, '__init__.py'), 'w') as f:
        f.write("from . import models\nfrom . import wizards\n")

    # LICENSE
    with open(os.path.join(module_path, 'LICENSE'), 'w') as f:
        f.write("""Odoo Proprietary License v1.0

This software and associated files (the "Software") may only be used (executed,
modified, executed after modifications) if you have purchased a valid license
from the authors, typically via Odoo Apps, or if you have received a written
agreement from the authors of the Software (see the COPYRIGHT file).

You may develop Odoo modules that use the Software as a library (typically
by depending on it, importing it and using its resources), but without copying
any source code or material from the Software. You may distribute those
modules under the license of your choice, provided that this license is
compatible with the terms of the Odoo Proprietary License (For example:
LGPL, MIT, or proprietary licenses similar to this one).

It is forbidden to publish, distribute, sublicense, or sell copies of the Software
or modified copies of the Software.

The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
""")

    # __manifest__.py
    with open(os.path.join(module_path, '__manifest__.py'), 'w') as f:
        f.write(f"""{{
    "name": "{snake_to_title(module_name)}",
    "summary": "Module for {snake_to_title(module_name)} features.",
    "version": "16.0.1.0.0",
    "category": "Customization",
    "author": "Ametras intelligence GmbH",
    "website": "https://www.ametras.com",
    "maintainer": "Ametras intelligence GmbH",
    "depends": ["base"],
    "data": [
        "data/data.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "report/report.xml",
        "wizards/wizard.xml",
        "views/view.xml"
    ],
    "license": "OPL-1",
}}
""")

    print(f"✅ Odoo module '{module_name}' created at: {module_path}")

if __name__ == "__main__":
    base_path = input("Enter the path to create the module in (e.g. /home/user/odoo/custom_addons): ").strip()
    module_name = input("Enter the module name (e.g. custom_common): ").strip()
    create_module_structure(base_path, module_name)
