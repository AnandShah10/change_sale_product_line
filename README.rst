=======================
Custom Odoo Sale Module
=======================

Overview
========

This Odoo module customizes the display of product information in sale order lines. Specifically, it modifies the descriptions to display only the product name and adjusts the `product_tmpl_id` field to show the `default_code` of the product if it exists, otherwise, it shows the product name.

Key Features
============

- Customizes the sale order line description to display only the product name.
- Modifies the `product_tmpl_id` field to display the `default_code` if it exists, otherwise the product name.
- Uses Odoo's `_compute_display_name` compute method to achieve the above customizations.

Installation
============

1. Download the module from the repository.
2. Place the module folder in your Odoo add-ons directory.
3. Update the module list by going to `Apps` -> `Update Apps List`.
4. Search for "Custom Sale Module" and click on `Install`.

Configuration
=============

No additional configuration is required. Once installed, the module will automatically apply the custom display settings to the sale order lines.

Usage
=====

1. Navigate to `Sales` -> `Orders` -> `Quotations`.
2. Create a new quotation or edit an existing one.
3. Add products to the sale order lines.
4. Observe that the description field only shows the product name.
5. Check the `product_tmpl_id` field to see the `default_code` if available; otherwise, it shows the product name.


Contributing
============

1. Fork the repository.
2. Create a new branch (e.g., `feature/custom-display`).
3. Commit your changes.
4. Push the branch to your fork.
5. Create a pull request.

Support
=======

For support or questions, please open an issue in the repository or contact us at shahanand1072004@gmail.com.

License
=======

This module is licensed under the GPL-3 License.

Authors
=======

- Anand Shah.
