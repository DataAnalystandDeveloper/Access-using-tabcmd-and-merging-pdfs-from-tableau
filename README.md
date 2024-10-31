# Tableau PDF Export, Merge, and Page Numbering Automation

This project automates exporting views from Tableau, merging non-blank PDF files, and adding page numbers to the final merged PDF. It uses Python along with several libraries (`subprocess`, `PyPDF2`, `glob2`, `fitz` from `PyMuPDF`, and `os`) to streamline the process.

## Features

- **Export Views from Tableau**: Export Tableau views as PDFs using the `tabcmd` command-line utility.
- **Merge PDFs**: Combine exported PDFs into a single PDF file, excluding any blank pages.
- **Add Page Numbers**: Append page numbers to the final merged PDF.
- **Additional Customization**: Easily add other functions or features as needed.

