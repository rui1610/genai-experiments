# GOLDEN PATH: coverage of product standard requirements

The `Golden Path` for SAP BTP delivers not only technical capabilities, but let's you build apps, that are compliant to the [SAP Product Standards](https://one.int.sap/company/management_systems/development_quality_management_system/product_standards)

These are the requirements of the SAP product standard  that the `Golden Path` already fullfils today:

|  ID | Requirement | Golden Path technology |
| --- | ----------- | ---------------------- | 
| [`acc253`](acc/prod_standard_overview.md) | Labels for Input and Output Fields |`CAP`: In most cases the requirement is fulfilled if Fiori Guidelines for labels are implemented.  |
| [`acc254`](acc/prod_standard_overview.md) | Screen Titles |`CAP`: In most cases the requirement is fulfilled if Fiori Guidelines for labels are implemented.  |
| [`acc255`](acc/prod_standard_overview.md) | Text Alternative for Non-Text Content |`CAP`: In most cases the requirement is fulfilled if Fiori Guidelines for labels are implemented.  |
| [`acc260`](acc/prod_standard_overview.md) | Text Resizing up to 200 percent |`CAP`: Fiori using Horizon themes supports text resizing up to 200% by supporting browser zoom function and responsive design  |
| [`acc261`](acc/prod_standard_overview.md) | Minimum Contrast |`CAP`: Fiori using Horizon themes have been optimized to conform with the color contrast considerations  |
| [`acc262`](acc/prod_standard_overview.md) | Color and Contrast Setting |`CAP`: Fiori using Horizon themes have been optimized to conform with the color contrast considerations  |
| [`acc267`](acc/prod_standard_overview.md) | Consistent Navigation |`CAP`: Fiori supports consistent navigation by the use of the Launchpad and the Shell Bar.  |
| [`acc268`](acc/prod_standard_overview.md) | Multiple Ways to Find Content |`CAP`: Fiori offers options for this principle, such as Global Search, App Search, navigation via the launchpad.  |
| [`acc269`](acc/prod_standard_overview.md) | Group Skipping |`CAP`: Fiori offers options for this principle, such as Global Search, App Search, navigation via the launchpad.  |
| [`acc270`](acc/prod_standard_overview.md) | Full Input Channel Support (Keyboard, Mouse, Touch) |`CAP`: SAP Fiori Design provides use-case-centric keyboard shortcuts and references to UI elements, which provide full and efficient keyboard support.  |
| [`acc271`](acc/prod_standard_overview.md) | Visible Focus |`CAP`  |
| [`acc281`](acc/prod_standard_overview.md) | Display Orientation |`CAP`: SAP Fiori is designed to take over the display orientation from the browser, and so does UI5.  |
| [`acc283`](acc/prod_standard_overview.md) | Text Spacing |`CAP`: SAP Fiori framework makes it possible to build applications that properly adapt to text spacing  |
| [`acc284`](acc/prod_standard_overview.md) | Content on Hover or Focus |`CAP`: Using Fiori  |
| [`glob17`](glob/prod_standard_overview.md) | Text Sorting |`CAP`: Supported by SAP Fiori  |
| [`glob94`](glob/prod_standard_overview.md) | Unicode Enablement |`CAP`  |
| [`glob179`](glob/prod_standard_overview.md) | Right-to-Left Layout and Bidirectional Text Support |`CAP`: Supported by SAP Fiori  |
| [`glob181`](glob/prod_standard_overview.md) | Development Tool Support for Internationalization |`CAP`: Still necessary? Obvious ...  |
| [`glob185`](glob/prod_standard_overview.md) | Currency Basics |`CAP`: Supported by SAP Fiori, CAP and HANA Cloud  |
| [`glob186`](glob/prod_standard_overview.md) | Time Zone Support |`CAP`: Supported by SAP Fiori, CAP and HANA Cloud  |
| [`glob187`](glob/prod_standard_overview.md) | Product Translatability |`CAP`: Supported by SAP Fiori  |
| [`glob189`](glob/prod_standard_overview.md) | Calendar Support |`CAP`: Supported by SAP Fiori  |
| [`glob190`](glob/prod_standard_overview.md) | User Settings Personalization |`CAP`: Supported by SAP Fiori  |
| [`glob192`](glob/prod_standard_overview.md) | Country and Region Handling |`CAP`: Supported by SAP Fiori  |
| [`glob193`](glob/prod_standard_overview.md) | Geographical Information: Display and Provisioning |`CAP`: Supported by SAP Fiori  |
| [`sec218`](sec/prod_standard_overview.md) | Internet Communication Filtering |`CAP`  |
| [`sec220`](sec/prod_standard_overview.md) | Cookie handling |`CAP`  |
| [`sec221`](sec/prod_standard_overview.md) | Session management |`CAP`  |
| [`sec223`](sec/prod_standard_overview.md) | Cross-site Request Forgery |`CAP`  |
| [`sec230`](sec/prod_standard_overview.md) | Identity Management, Authentication, SSO |`CAP`  |
| [`sec231`](sec/prod_standard_overview.md) | Username/Password authentication |`CAP`  |
| [`sec232`](sec/prod_standard_overview.md) | X.509 Certificate Authentication |`CAP`  |
| [`sec235`](sec/prod_standard_overview.md) | Memory corruption |`CAP`  |
| [`sec236`](sec/prod_standard_overview.md) | Information disclosure |`CAP`  |
| [`sec238`](sec/prod_standard_overview.md) | HTTP method handling |`CAP`  |
| [`sec239`](sec/prod_standard_overview.md) | Fail securely |`CAP`  |
| [`sec243`](sec/prod_standard_overview.md) | DLL Injection |`CAP`: using BTP runtimes  |
| [`sec278`](sec/prod_standard_overview.md) | URL Handling |`CAP`  |
| [`sec281`](sec/prod_standard_overview.md) | Secure UI Framework Usage |`CAP`  |
| [`sec283`](sec/prod_standard_overview.md) | Deserialization |`CAP`  |
| [`sec373`](sec/prod_standard_overview.md) | Strong data isolation with customer specific keys |`CAP`  |
| [`sec374`](sec/prod_standard_overview.md) | System-to-system communication |`CAP`  |
| [`sec375`](sec/prod_standard_overview.md) | Server Side Request Forgery (SSRF) |`CAP`  |
| [`sec378`](sec/prod_standard_overview.md) | Ensure secure multi-tenancy |`CAP`  |
| [`slc11`](slc/prod_standard_overview.md) | Applications shall store all permanent data in a standard persistence. |`CAP`: Using SAP HANA Cloud  |
| [`slc29`](slc/prod_standard_overview.md) | Productive Build Pipeline |`CAP`: Using SAP DwC or SAP CICD  |
| [`slc31`](slc/prod_standard_overview.md) | Follow the SAP Web Browser platforms standard. |`CAP`: Using SAP Fiori   |
| [`slc36`](slc/prod_standard_overview.md) | Use feature switches carefully and remove the switches as soon as possible. |`CAP`: Using SAP DwC or SAP CICD  |
| [`slc37`](slc/prod_standard_overview.md) | It shall be possible to remove an ABAP Add-on after it has been installed and used in a system. |`CAP`  |
| [`slc38`](slc/prod_standard_overview.md) | Usage of Automated Update Procedures for Cloud Systems |`CAP`: Using SAP DwC or SAP CICD  |
| [`ua060`](ua/prod_standard_overview.md) | Intuitive User Interface |`CAP`: Using Fiori  |
| [`uxc010`](uxc/prod_standard_overview.md) | Colors |`CAP`: Using SAP Fiori   |
| [`uxc011`](uxc/prod_standard_overview.md) | Theming Concept |`CAP`: Using SAP Fiori   |
| [`uxc012`](uxc/prod_standard_overview.md) | Typography |`CAP`: Using SAP Fiori   |
| [`uxc013`](uxc/prod_standard_overview.md) | Iconography |`CAP`: Using SAP Fiori   |
| [`uxc014`](uxc/prod_standard_overview.md) | Action Placement |`CAP`: Using SAP Fiori   |
| [`uxc015`](uxc/prod_standard_overview.md) | Terminology |`CAP`: Using SAP Fiori   |
| [`uxc016`](uxc/prod_standard_overview.md) | Shell bar |`CAP`: Using SAP Fiori   |
| [`uxc017`](uxc/prod_standard_overview.md) | Settings |`CAP`: Using SAP Fiori   |
| [`uxc019`](uxc/prod_standard_overview.md) | Icon Semantics |`CAP`: Using SAP Fiori   |
| [`uxc010`](uxc/prod_standard_overview.md) | Colors |`CAP`: Using SAP Fiori   |
| [`uxc011`](uxc/prod_standard_overview.md) | Theming Concept |`CAP`: Using SAP Fiori   |
| [`uxc012`](uxc/prod_standard_overview.md) | Typography |`CAP`: Using SAP Fiori   |
| [`uxc013`](uxc/prod_standard_overview.md) | Iconography |`CAP`: Using SAP Fiori   |
| [`uxc014`](uxc/prod_standard_overview.md) | Action Placement |`CAP`: Using SAP Fiori   |
| [`uxc015`](uxc/prod_standard_overview.md) | Terminology |`CAP`: Using SAP Fiori   |
| [`uxc016`](uxc/prod_standard_overview.md) | Shell bar |`CAP`: Using SAP Fiori   |
| [`uxc017`](uxc/prod_standard_overview.md) | Settings |`CAP`: Using SAP Fiori   |
| [`uxc019`](uxc/prod_standard_overview.md) | Icon Semantics |`CAP`: Using SAP Fiori   |


