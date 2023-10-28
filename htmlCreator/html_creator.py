import webbrowser
import os

def create_html():

    # Prompt for the paragraph
    paragraph = input("Enter your paragraph: ")

    # Determine the current working directory
    current_directory = os.getcwd()


    # Open so that the file will close
    with open("index.html", "w") as page:
        page.write(
            f"""
            <!DOCTYPE html>
        
            <html lang="en">
                <head>  
                    <meta charset="UTF-8">
                    <link rel="stylesheet" href="stylesheet.css">  
                    <title></title>
                </head>

                <body>
                    <p>{paragraph}</p>
                </body>
            </html>
            """
        )


    # Open so that the file will close
    with open("stylesheet.css", "w") as css:
        css.write(
            """
            body {
                background-color: darkgrey;
                text-align: center;
            }

            p {
                font-family: Arial, Helvetica, sans-serif;
                font-size: 100px;
                font-weight: 600;
                background-image: linear-gradient(to right, #3b6340, #0f00e7);
                color: transparent;
                background-clip: text;
                -webkit-background-clip: text;
            }
        """
        )

    file_url = f"file://{current_directory}/index.html"

    # Open the index file using the url, default browser, tab
    webbrowser.open(file_url, 2, True)


create_html()