from markdown_pdf import MarkdownPdf, Section


def markdown2pdf():
    try:
        pdf = MarkdownPdf()
        with open("modified_resume.md", "r") as file:
            markdown_content = file.read()
        pdf.add_section(
            Section(markdown_content[3:-3]),
            user_css= "mystyle.css",
        )
        pdf.save("your_resume.pdf")
        return 1
    except Exception as e:
        print(e)
        return 0
